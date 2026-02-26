# Summary Storage System

**Author:** Vasudha Ajay Tayade  
**Module:** Summary Storage System  
**Task:** Store final structured interview summary in database format  

---

## **Project Overview**

This project is a simple backend system to store structured interview summaries in a PostgreSQL database.  
It uses **FastAPI** for the API and **SQLAlchemy** for database modeling.  

**Features:**
- Store interview summaries with session ID, domain, projects, strengths, weaknesses, and final score
- Automatic timestamp for each entry
- Minimal and clean API design for easy usage
- Tested and verified with PostgreSQL via pgAdmin

---

## **Database Schema**

**Table:** `interview_summary`

| Column       | Type        | Notes                     |
|------------- |------------ |-------------------------- |
| id           | Integer     | Primary key, auto-increment |
| session_id   | String      | Unique session identifier  |
| domain       | String      | Interview domain           |
| projects     | String      | Projects worked on         |
| strengths    | String      | Candidate strengths        |
| weaknesses   | String      | Candidate weaknesses       |
| final_score  | Float       | Final score (0–10)         |
| created_at   | Timestamp   | Auto-generated timestamp   |

---

## **Setup Instructions**

1. **Clone the repository:**
```bash
git clone <your_repo_url>
cd summary_api
