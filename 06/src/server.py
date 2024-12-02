import grpc
from concurrent import futures
import flight_booking_pb2 as pb2
import flight_booking_pb2_grpc as pb2_grpc
import uuid


class FlightBookingService(pb2_grpc.FlightBookingServiceServicer):
    def __init__(self):
        # In-memory storage for bookings (Fake database)
        self.bookings = {}

    def ListBookings(self, request, context):
        return pb2.BookingList(bookings=list(self.bookings.values()))

    def AddBooking(self, request, context):
        booking_id = str(uuid.uuid4())
        booking = pb2.Booking(
            id=booking_id,
            passenger_name=request.passenger_name,
            passenger_email=request.passenger_email,
            departure_date=request.departure_date,
            arrival_date=request.arrival_date,
            departure_airport=request.departure_airport,
            arrival_airport=request.arrival_airport,
        )
        self.bookings[booking_id] = booking
        return pb2.BookingResponse(success=True, message=f"Booking added with ID: {booking_id}")

    def RemoveBooking(self, request, context):
        if request.id in self.bookings:
            del self.bookings[request.id]
            return pb2.BookingResponse(success=True, message="Booking removed successfully")
        return pb2.BookingResponse(success=False, message="Booking ID not found")

    def UpdateBooking(self, request, context):
        if request.id in self.bookings:
            self.bookings[request.id] = request
            return pb2.BookingResponse(success=True, message="Booking updated successfully")
        return pb2.BookingResponse(success=False, message="Booking ID not found")


def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_FlightBookingServiceServicer_to_server(FlightBookingService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    return server
    
if __name__ == "__main__":
    server=start_server()
    server.wait_for_termination()
    
