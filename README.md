# Student Management API

## Project Overview
This project is a simple REST API for managing student records, including student IDs, names, and scores.

It is built with Python and Flask and uses SQLite for data storage.

Git is used for version control.

## Tech Stack
- Python
- Flask
- SQLite
- Git

## Features
- Retrieve all student records.
- Retrieve a specific student by ID.
- Add a new student record.
- Handle invalid requests and database errors.

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/<int:student_id>` | Retrieve a student by ID |
| POST | `/students` | Add a new student |

## Installation & Usage

### Requirements

- Python 3.14
- Git

### Setup (Windows PowerShell)

1. Clone the repository and navigate to the project directory.

2. Create a virtual environment.

   ```powershell
   python -m venv .venv
   ```
3. Activate the virtual environment.
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies.
   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Initialize the database.
   ```powershell
   python init_db.py
   ```

6. Start the Flask server.
   ```powershell
   python app.py
   ```

7. Open another PowerShell terminal and test the API.
   ```powershell
   curl.exe -i http://127.0.0.1:5000/students
   ```

### Alternative: Run Without Activating the Virtual Environment

If PowerShell blocks `Activate.ps1`, you can use the virtual environment's Python executable directly.

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Initialize the database:

```powershell
.\.venv\Scripts\python.exe init_db.py
```

Start the Flask server:

```powershell
.\.venv\Scripts\python.exe app.py
```

## Error Handling
| Status Code | Description |
|---|---|
| 400 | Invalid request or missing required fields |
| 404 | Student not found |
| 500 | Internal server error |