# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import card_pb2 as card__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in card_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CardServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.validateCard = channel.unary_unary(
                '/card.CardService/validateCard',
                request_serializer=card__pb2.Card.SerializeToString,
                response_deserializer=card__pb2.BoolValue.FromString,
                _registered_method=True)


class CardServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def validateCard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CardServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'validateCard': grpc.unary_unary_rpc_method_handler(
                    servicer.validateCard,
                    request_deserializer=card__pb2.Card.FromString,
                    response_serializer=card__pb2.BoolValue.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'card.CardService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('card.CardService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CardService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def validateCard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/card.CardService/validateCard',
            card__pb2.Card.SerializeToString,
            card__pb2.BoolValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)