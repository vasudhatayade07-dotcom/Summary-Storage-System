from pydantic import BaseModel

class SummaryCreate(BaseModel):
    session_id: str
    domain: str
    projects: str
    strengths: str
    weaknesses: str
    final_score: float