from concurrent import futures
import grpc
from google.protobuf import empty_pb2
from grpc_reflection.v1alpha import reflection

import card_pb2
import card_pb2_grpc

class CardService(card_pb2_grpc.CardServiceServicer):
    def validateCard(self, request, context):
        # Dummy card validation
        if request.cardNumber == "1234-1234-1234-1234" and request.cardOwner == "CardOwner":
            return card_pb2.BoolValue(value=True)
        return card_pb2.BoolValue(value=False)
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    card_pb2_grpc.add_CardServiceServicer_to_server(CardService(), server)
    server.add_insecure_port('0.0.0.0:50080')
    SERVICE_NAMES = (
        card_pb2.DESCRIPTOR.services_by_name['CardService'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    print("Card Service started on port 50080")
    server.wait_for_termination()
    
    
if __name__ == "__main__":
    serve()