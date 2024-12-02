import unittest
import grpc
import logging
from server import start_server
import flight_booking_pb2 as pb2
import flight_booking_pb2_grpc as pb2_grpc

logging.basicConfig(level=logging.INFO)

class TestFlightBookingService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server
        cls.server = start_server()
        cls.channel = grpc.insecure_channel("localhost:50051")
        cls.stub = pb2_grpc.FlightBookingServiceStub(cls.channel)

    @classmethod
    def tearDownClass(cls):
        # Stop the server
        cls.server.stop(0)
        cls.channel.close()
        
    def test_flight_booking_scenario(self):
        logging.info("Step 1: Initial state - no bookings")
        booking_list = self.stub.ListBookings(pb2.Empty())
        self.assertEqual(len(booking_list.bookings), 0, "Initial state should be empty")

        logging.info("Step 2: Add a booking")
        response = self.stub.AddBooking(
            pb2.Booking(
                passenger_name="John Doe",
                departure_airport="JFK",
                arrival_airport="LAX",
                departure_date="2024-12-15",
                arrival_date="2024-12-16",
            )
        )
        self.assertIn("Booking added", response.message)

        logging.info("Step 3: Check state after adding")
        booking_list = self.stub.ListBookings(pb2.Empty())
        self.assertEqual(len(booking_list.bookings), 1, "There should be one booking")

        booking = booking_list.bookings[0]
        self.assertEqual(booking.passenger_name, "John Doe")
        self.assertEqual(booking.departure_airport, "JFK")
        self.assertEqual(booking.arrival_airport, "LAX")

        logging.info("Step 4: Update the booking")
        updated_response = self.stub.UpdateBooking(
            pb2.Booking(
                id=booking.id,
                passenger_name="Jane Doe",
                departure_airport="JFK",
                arrival_airport="LAX",
                departure_date="2024-12-15",
                arrival_date="2024-12-16",
            )
        )
        self.assertIn("updated", updated_response.message)

        logging.info("Step 5: Check state after update")
        booking_list = self.stub.ListBookings(pb2.Empty())
        self.assertEqual(len(booking_list.bookings), 1)
        self.assertEqual(booking_list.bookings[0].passenger_name, "Jane Doe")

        logging.info("Step 6: Remove the booking")
        remove_response = self.stub.RemoveBooking(
            pb2.BookingId(id=booking.id)
        )
        self.assertIn("removed", remove_response.message)

        logging.info("Step 7: Check state after removal")
        booking_list = self.stub.ListBookings(pb2.Empty())
        self.assertEqual(len(booking_list.bookings), 0, "There should be no bookings")


if __name__ == "__main__":
    unittest.main()
