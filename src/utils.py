import functools
from grpc import insecure_channel


def build_ch(stub, channel_fn=insecure_channel, host='127.0.0.1', port=40401):
    channel = channel_fn(f'{host}:{port}')
    return stub(channel)


def create_ch_builder(stub):
    return functools.partial(build_ch, stub=stub)
