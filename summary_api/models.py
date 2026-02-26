from sqlalchemy import Column, Integer, String, Text, Float, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class InterviewSummary(Base):
    __tablename__ = "interview_summary"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, unique=True, nullable=False)
    domain = Column(String, nullable=False)
    projects = Column(Text)
    strengths = Column(Text)
    weaknesses = Column(Text)
    final_score = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())