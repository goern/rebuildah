# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import release_engineering_pb2 as release__engineering__pb2


class ReleaseEngineeringStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCurrentRelease = channel.unary_unary(
            "/ninja.thoth_station.rebuildah.ReleaseEngineering/GetCurrentRelease",
            request_serializer=release__engineering__pb2.ContainerRepository.SerializeToString,
            response_deserializer=release__engineering__pb2.SemanticVersion.FromString,
        )
        self.PushEvent = channel.unary_unary(
            "/ninja.thoth_station.rebuildah.ReleaseEngineering/PushEvent",
            request_serializer=release__engineering__pb2.ContainerRepository.SerializeToString,
            response_deserializer=release__engineering__pb2.Empty.FromString,
        )


class ReleaseEngineeringServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCurrentRelease(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PushEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ReleaseEngineeringServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetCurrentRelease": grpc.unary_unary_rpc_method_handler(
            servicer.GetCurrentRelease,
            request_deserializer=release__engineering__pb2.ContainerRepository.FromString,
            response_serializer=release__engineering__pb2.SemanticVersion.SerializeToString,
        ),
        "PushEvent": grpc.unary_unary_rpc_method_handler(
            servicer.PushEvent,
            request_deserializer=release__engineering__pb2.ContainerRepository.FromString,
            response_serializer=release__engineering__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ninja.thoth_station.rebuildah.ReleaseEngineering", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ReleaseEngineering(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCurrentRelease(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ninja.thoth_station.rebuildah.ReleaseEngineering/GetCurrentRelease",
            release__engineering__pb2.ContainerRepository.SerializeToString,
            release__engineering__pb2.SemanticVersion.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def PushEvent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ninja.thoth_station.rebuildah.ReleaseEngineering/PushEvent",
            release__engineering__pb2.ContainerRepository.SerializeToString,
            release__engineering__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
