# FastAPI MongoDB Integration

This project demonstrates a basic FastAPI application integrated with MongoDB. It includes an endpoint to register users by passing details via Postman and saving the data in MongoDB.

---

## Features
- FastAPI-based RESTful API.
- MongoDB integration for data storage using `motor` (an async MongoDB driver).
- User signup functionality with validation.

---

## Requirements

- Python 3.7+
- MongoDB (local or cloud-hosted, such as MongoDB Atlas)
- Dependencies:
  - `fastapi`
  - `uvicorn`
  - `motor`
  - `pydantic`

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies
```bash
pip install fastapi uvicorn motor pydantic
```

### 3. MongoDB Configuration
- **Local MongoDB**: Ensure MongoDB is running on your machine at `mongodb://localhost:27017` (default URI).
- **Remote MongoDB**: Replace the `MONGO_DETAILS` variable in the code with your MongoDB connection string:
  ```python
  MONGO_DETAILS = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
  ```

---

## Usage

### 1. Start the FastAPI Server
Run the application with `uvicorn`:
```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000/`.

### 2. Test the API using Postman
#### Endpoint: `/signup/`
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/signup/`
- **Headers**:
  - `Content-Type`: `application/json`
- **Body (JSON)**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "mypassword123"
  }
  ```
- **Expected Response**:
  ```json
  {
    "message": "User registered successfully",
    "user_id": "<MongoDB ObjectId>"
  }
  ```

### 3. Verify MongoDB Data
- Check the database (`test_database`) and the `users` collection for the inserted data.

---

## Project Structure
```
.
├── main.py        # FastAPI application code
├── requirements.txt # Dependencies for the project
└── README.md      # Project documentation
```

---

## Notes
- Passwords are stored as plain text in this example for simplicity. For production, always hash passwords before storing them (e.g., using `bcrypt`).
- Use proper environment variables for sensitive data like database connection strings.

---

## License
This project is open-source and available under the MIT License.

