# 404 Beat Catalog API

A RESTful music beat catalog API built with **Python**, **FastAPI**, **SQLite**, **SQLAlchemy**, and **Pydantic**.

This project manages music beat metadata such as title, BPM, genre, and ID. It supports creating, reading, updating, deleting, and filtering beats through API endpoints.

## Features

- Get all beats
- Get a beat by ID
- Filter beats by genre
- Filter beats by BPM
- Add new beats
- Update existing beats
- Delete beats
- SQLite database persistence
- Pydantic data validation
- HTTP error handling with `HTTPException`
- Interactive API testing with FastAPI Swagger docs

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

## Project Purpose

The purpose of this project is to practice backend API development using Python and FastAPI. It simulates a music catalog backend that could be used for a beat store, producer dashboard, music library, or audio-related application.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Confirms the API is running |
| GET | `/beats` | Returns all beats |
| GET | `/beats/{beat_id}` | Returns a beat by ID |
| GET | `/beats/genre/{genre}` | Returns beats by genre |
| GET | `/beats/bpm/{bpm}` | Returns beats by BPM |
| POST | `/beats` | Adds a new beat |
| PUT | `/beats/{beat_id}` | Updates an existing beat |
| DELETE | `/beats/{beat_id}` | Deletes a beat |

## Example Beat Data

```json
{
  "title": "Corruption",
  "bpm": 142,
  "genre": "Malware Trap"
}
