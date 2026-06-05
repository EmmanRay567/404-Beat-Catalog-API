# this is a simple API for managing music beats using FastAPI. It includes endpoints to retrieve a list of beats and a home endpoint to confirm that the API is running.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import uvicorn

app = FastAPI()

DataBaseURL = "sqlite:///./beats.db"

engine = create_engine(DataBaseURL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Beats(Base):
    __tablename__ = "beats"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    bpm = Column(Integer)
    genre = Column(String)

class BeatCreate(BaseModel):
    title: str
    bpm: int
    genre: str

Base.metadata.create_all(bind=engine)

#this sets the home endpoint that returns a message saying th API is running if someone were to access it.
#this hslps test and make sure that the api works and that the user can access it.
@app.get("/")
def home():
    return {"message": "The APi is running "}

#this means that if someone goes to the beats API endpoint, it will give back or return the list of beats that were created
@app.get("/beats")
def get_beats():
    db = SessionLocal()
    beats = db.query(Beats).all()
    db.close()

    return beats

# this means that if someone goes to the beats genre API endpoint, it will give back a list of beats matching that specific genre.
@app.get("/beats/genre/{genre}")
def get_beats_by_genre(genre: str):
    db = SessionLocal()

    genre_beats = db.query(Beats).filter(Beats.genre.ilike(genre)).all()

    db.close()

    return genre_beats

# this means that if someone goes to the beats bpm API endpoint, it will give back a list of beats matching that specific bpm.
@app.get("/beats/bpm/{bpm}")
def get_beats_by_bpm(bpm: int):
    db = SessionLocal()

    bpm_beats = db.query(Beats).filter(Beats.bpm == bpm).all()

    db.close()

    return bpm_beats

#if someone goes to the beats id API endpoint, it will give back the beat matching that specific beat identiification.
#if that beat is not found, then it will tell the user the beat cannot bee found.
@app.get("/beats/{beat_id}")
def get_beat(beat_id: int):
    db = SessionLocal()

    beat = db.query(Beats).filter(Beats.id == beat_id).first()

    db.close()

    if beat:
        return beat

    raise HTTPException(status_code=404, detail="Beat not found")

@app.put("/beats/{beat_id}")
def update_beat(beat_id: int, beat: BeatCreate):
    db = SessionLocal()
    existing_beat = db.query(Beats).filter(Beats.id == beat_id).first()
    if existing_beat:
        existing_beat.title = beat.title
        existing_beat.bpm = beat.bpm
        existing_beat.genre = beat.genre
        db.commit()
        db.refresh(existing_beat)
        db.close()
        return {
            "message": "Beat updated",
            "beat": existing_beat
        }
    db.close()
    raise HTTPException(status_code=404, detail="Beat not found")

#this allows the user to create new beats using the app.post. the user is able to send a beat as a dictionary, and the API will assign it an ID and add it to the list of beats.
#the new beat is then returned to the user.

@app.post("/beats", status_code=201)
def AddBeats(beat: BeatCreate):
    db = SessionLocal()

    new_beat = Beats(
        title=beat.title,
        bpm=beat.bpm,
        genre=beat.genre
    )

    db.add(new_beat)
    db.commit()
    db.refresh(new_beat)

    db.close()

    return {
        "message": "Beat added",
        "beat": new_beat
    }

@app.delete("/beats/{beat_id}")
def delete_beat(beat_id: int):
    db = SessionLocal()

    beat = db.query(Beats).filter(Beats.id == beat_id).first()

    if beat:
        db.delete(beat)
        db.commit()
        db.close()

        return {"message": "Beat deleted"}

    db.close()

    raise HTTPException(status_code=404, detail="Beat not found")

if __name__ == "__main__":
    uvicorn.run("MusicBeatsAPI:app", host="127.0.0.1", port=8000, reload=True)
