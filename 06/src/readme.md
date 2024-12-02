
For starting the server manually:

```bash
python server.py
```

For testing :
```bash
python -m unittest testing.py -v
```

Result :
```
test_flight_booking_scenario (testing.TestFlightBookingService.test_flight_booking_scenario) ...
INFO:root:Step 1: Initial state - no bookings
INFO:root:Step 2: Add a booking
INFO:root:Step 3: Check state after adding
INFO:root:Step 4: Update the booking
INFO:root:Step 5: Check state after update
INFO:root:Step 6: Remove the booking
INFO:root:Step 7: Check state after removal
ok

----------------------------------------------------------------------
Ran 1 test in 0.038s

OK
```