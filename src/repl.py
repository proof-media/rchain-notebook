from .generated import repl_pb2_grpc
from .generated.repl_pb2 import CmdRequest, EvalRequest
from . import rho_types
from .utils import create_ch_builder

build_ch = create_ch_builder(repl_pb2_grpc.ReplStub)


def run(ch, line):
    cmd_request = rho_types.from_dict({'line': line}, CmdRequest)
    ret = ch.Run(cmd_request)
    return rho_types.to_dict(ret)


def eval(ch, program):
    eval_request = rho_types.from_dict({'program': program}, EvalRequest)
    ret = ch.Eval(eval_request)
    return rho_types.to_dict(ret)
