# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import repl_pb2 as repl__pb2


class ReplStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Run = channel.unary_unary(
            '/coop.rchain.node.model.Repl/Run',
            request_serializer=repl__pb2.CmdRequest.SerializeToString,
            response_deserializer=repl__pb2.ReplResponse.FromString,
        )
        self.Eval = channel.unary_unary(
            '/coop.rchain.node.model.Repl/Eval',
            request_serializer=repl__pb2.EvalRequest.SerializeToString,
            response_deserializer=repl__pb2.ReplResponse.FromString,
        )


class ReplServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Run(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Eval(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReplServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Run':
        grpc.unary_unary_rpc_method_handler(
            servicer.Run,
            request_deserializer=repl__pb2.CmdRequest.FromString,
            response_serializer=repl__pb2.ReplResponse.SerializeToString,
        ),
        'Eval':
        grpc.unary_unary_rpc_method_handler(
            servicer.Eval,
            request_deserializer=repl__pb2.EvalRequest.FromString,
            response_serializer=repl__pb2.ReplResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'coop.rchain.node.model.Repl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))
