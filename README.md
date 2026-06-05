# 404 Beat Catalog API

A RESTful music beat catalog API built with **Python**, **FastAPI**, **SQLite**, **SQLAlchemy**, and **Pydantic**.

This project manages music beat metadata such as title, BPM, genre, and ID. It supports creating, reading, updating, deleting, and filtering beats through API endpoints.

## Features

* Get all beats
* Get a beat by ID
* Filter beats by genre
* Filter beats by BPM
* Add new beats
* Update existing beats
* Delete beats
* SQLite database persistence
* Pydantic data validation
* HTTP error handling with `HTTPException`
* Interactive API testing with FastAPI Swagger docs

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* Uvicorn

## Project Purpose

The purpose of this project is to practice backend API development using Python and FastAPI. It simulates a music catalog backend that could be used for a beat store, producer dashboard, music library, or audio-related application.

## API Endpoints

| Method | Endpoint               | Description                 |
| ------ | ---------------------- | --------------------------- |
| GET    | `/`                    | Confirms the API is running |
| GET    | `/beats`               | Returns all beats           |
| GET    | `/beats/{beat_id}`     | Returns a beat by ID        |
| GET    | `/beats/genre/{genre}` | Returns beats by genre      |
| GET    | `/beats/bpm/{bpm}`     | Returns beats by BPM        |
| POST   | `/beats`               | Adds a new beat             |
| PUT    | `/beats/{beat_id}`     | Updates an existing beat    |
| DELETE | `/beats/{beat_id}`     | Deletes a beat              |

## Example Beat Data

```json
{
  "title": "Corruption",
  "bpm": 142,
  "genre": "Malware Trap"
}
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/EmmanRay567/404-Beat-Catalog-API.git
```

### 2. Move into the project folder

```bash
cd 404-Beat-Catalog-API
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
py -m uvicorn MusicBeatsAPI:app --reload
```

### 5. Open the API in your browser

Home route:

```text
http://127.0.0.1:8000/
```

Interactive API docs:

```text
http://127.0.0.1:8000/docs
```

Use the `/docs` page to test the GET, POST, PUT, and DELETE endpoints.


## What I Learned

While building this project, I practiced:

* Creating REST API endpoints with FastAPI
* Using SQLite for database persistence
* Creating SQLAlchemy database models
* Validating request data with Pydantic
* Implementing CRUD operations
* Returning proper HTTP errors
* Structuring backend logic around real-world API patterns

## Future Improvements

* Add user authentication
* Add search by title
* Add pagination for large beat catalogs
* Add price and license fields
* Add upload support for beat audio files
* Deploy the API online
* Connect the API to a frontend dashboard

## Author

Created by **Emmanuel Ray / 404RayDot**

GitHub: [EmmanRay567](https://github.com/EmmanRay567)
