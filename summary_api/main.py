from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/store-summary")
def store_summary(summary: schemas.SummaryCreate, db: Session = Depends(get_db)):
    
    db_summary = models.InterviewSummary(
        session_id=summary.session_id,
        domain=summary.domain,
        projects=summary.projects,
        strengths=summary.strengths,
        weaknesses=summary.weaknesses,
        final_score=summary.final_score
    )

    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)

    return {"message": "Summary stored successfully"}