# 5 - RESTful - Conditional GET
## Implementation

The service is implemented using FastAPI. To simulate a database, a Python dict is used.

The `get_tours` function is used to get the list of tours from the 'database'. It implement conditional get through If None Match and If Modified Since headers.

### Run the application

To enter the virtual env:
```bash
source .env/bin/activate
```

To run the FastAPI server:
```bash
fastapi dev main.py
```

### Test the application

We can test the application using **curl** commands

- Classic GET **without** conditions :
    ```bash
    curl http://localhost:8000/tours -i
    ```
    =>
    ```
    HTTP/1.1 200 OK
    date: Mon, 18 Nov 2024 14:31:59 GMT
    server: uvicorn
    content-length: 157
    content-type: application/json
    last-modified: Monday, 18 November 2024 15:26:09
    etag: a8499c657b701103d6fbb01235f40b5a

    [{"id":1,"name":"Skiing in the Alps","customers":[]},{"id":2,"name":"Hiking in the Andes","customers":[]},{"id":3,"name":"Surfing in Hawaii","customers":[]}]
    ```

- GET request with **If-None-Match** condition :
    ```bash
    curl -X GET http://127.0.0.1:8000/tours -H "If-None-Match: a8499c657b701103d6fbb01235f40b5a" -i
    ```
    =>
    ```
    HTTP/1.1 304 Not Modified
    date: Mon, 18 Nov 2024 14:34:28 GMT
    server: uvicorn
    content-type: application/json
    ```

- GET request with bad **If-None-Match** condition Etag:
    ```bash
    curl -X GET http://127.0.0.1:8000/tours -H "If-None-Match: b8499c657b701103d6fbb01235f40b5a" -i
    ```
    =>
    ```
    HTTP/1.1 200 OK
    date: Mon, 18 Nov 2024 14:35:59 GMT
    server: uvicorn
    content-length: 157
    content-type: application/json
    last-modified: Monday, 18 November 2024 15:26:09
    etag: a8499c657b701103d6fbb01235f40b5a

    [{"id":1,"name":"Skiing in the Alps","customers":[]},{"id":2,"name":"Hiking in the Andes","customers":[]},{"id":3,"name":"Surfing in Hawaii","customers":[]}]
    ```

- GET request with **IF-None-Match** weak Etag :
    ```bash
    curl -X GET http://127.0.0.1:8000/tours -H "If-None-Match: W/\"d5fec08841b226de29bad96cb7d402e0\"" -i
    ```
    =>
    ```
    HTTP/1.1 304 Not Modified
    date: Mon, 18 Nov 2024 14:47:43 GMT
    server: uvicorn
    content-type: application/json
    ```

- GET request with **If-Modified-Since** condition :
    ```bash
    curl -X GET http://127.0.0.1:8000/tours -H "If-Modified-Since: Wed, 14 Nov 2024 14:00:00 GMT" -i
    ```
    =>
    ```
    HTTP/1.1 200 OK
    date: Mon, 18 Nov 2024 14:45:22 GMT
    server: uvicorn
    content-length: 157
    content-type: application/json
    last-modified: Monday, 18 November 2024 15:44:41
    etag: a8499c657b701103d6fbb01235f40b5a

    [{"id":1,"name":"Skiing in the Alps","customers":[]},{"id":2,"name":"Hiking in the Andes","customers":[]},{"id":3,"name":"Surfing in Hawaii","customers":[]}]
    ```
