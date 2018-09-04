import functools
import toolz

from google.protobuf.empty_pb2 import Empty
from google.protobuf.message import Message
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer

from .generated.CasperMessage_pb2 import DataWithBlockInfo
from .generated.RhoTypes_pb2 import Channel, Var, Par, Expr

expr_to_obj_mapping = {'g_string': str}


def expr_to_obj(expr):
    type_, value = toolz.first(expr.items())
    return expr_to_obj_mapping[type_](value)


@functools.singledispatch
def expr_from_obj(_):
    raise ValueError(f'unknown type {type(_)}')


@expr_from_obj.register(str)
def _(s):
    return from_dict({'g_string': s}, Expr)


@functools.singledispatch
def to_dict(other):
    return other


@to_dict.register(RepeatedCompositeFieldContainer)
def _(container):
    return [to_dict(e) for e in container]


@to_dict.register(Message)
def _(message):
    exprs = getattr(message, 'exprs', None)
    if exprs is not None:
        return [expr_to_obj(expr) for expr in to_dict(exprs)]
    return {f[0].name: to_dict(f[1]) for f in message.ListFields()}


def from_dict(d, klass):
    proto = klass()
    for key, value in d.items():
        setattr(proto, key, value)
    return proto


def to_channel(objs):
    par = Par()
    par.exprs.extend([expr_from_obj(obj) for obj in objs])
    channel = Channel()
    channel.quote.CopyFrom(par)
    return channel
