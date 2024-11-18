## Implementation
The implementation of the delete service is as follows:

I have use **FastAPI** to implement my solution to simulate a database I have used a Python dict.

The `delete_tour_task` is the task which is run asynchronously to delete the tour:
- The function wait 10sec before deleting the specified tour.

The `delete_tour` function is the main function which is called when the delete request is made.
- If the specified tour is not found in the database, it will return a 404 error.
- If the specified tour is found, it will start the `delete_tour_task` asynchronously and return a 200 status code.

The `get_tour` function is used to get the list of tours form the 'database'.  

### Testing
- We can see by performing a DELETE request to the `/delete/{tour_id}` endpoint, and then a GET request to the `/tours` endpoint, that the specified tour has not been deleted instantly, but after 10 seconds.

- To run the server use `fastapi dev main.py` will being in the virtual env `source .env/bin/activate`

- This functionality be tested using a **curl** command
`curl -X "DELETE" http://localhost:8000/tour/{tour_id}` will running the server on port **8000**

- Run `curl http://localhost:8000/tours` to get the list of the tours
