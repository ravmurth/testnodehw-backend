# testnodehw-backend

A backend project for testnodehw that provides a simple REST API.

## API Endpoints

### GET /hello/<name>

Returns a greeting message with the provided name.

Example:
```
GET /hello/World
```

Response:
```json
{
  "message": "Hello World"
}
```

### POST /hello

Accepts a JSON body with a "name" field and returns a greeting message.

Example:
```
POST /hello
Content-Type: application/json

{
  "name": "World"
}
```

Response:
```json
{
  "message": "Hello World"
}
```

## Setup and Running

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

The API will be available at http://localhost:5000
