from concurrent import futures
import grpc
from google.protobuf import empty_pb2
from grpc_reflection.v1alpha import reflection


import payment_pb2
import payment_pb2_grpc
import card_pb2
import card_pb2_grpc
    


class PaymentService(payment_pb2_grpc.PaymentServiceServicer):
    def __init__(self):
        self.payments = []

    def ListPayments(self, request, context):
        return payment_pb2.PaymentList(payments=self.payments)

    def AddPayment(self, request, context):
        # Validate card using Card Validation Service
        with grpc.insecure_channel('localhost:50080') as channel:
            card_stub = card_pb2_grpc.CardServiceStub(channel)
            validation_request = card_pb2.Card(
                cardNumber=request.creditCardNumber,
                cardOwner=request.creditCardOwner
            )
            validation_response = card_stub.validateCard(validation_request)
            if not validation_response.value:
                return payment_pb2.PaymentResponse(status="Invalid Card")

        # Add payment to in-memory storage
        new_payment = payment_pb2.Payment(
            creditCardNumber=request.creditCardNumber,
            creditCardOwner=request.creditCardOwner,
            orderId=request.orderId
        )
        self.payments.append(new_payment)
        return payment_pb2.PaymentResponse(status="Payment Added")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    SERVICES_NAMES = (
        payment_pb2.DESCRIPTOR.services_by_name['PaymentService'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICES_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Payment Service started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
