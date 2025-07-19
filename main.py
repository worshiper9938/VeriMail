from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email_checker import check_email

app = FastAPI()

class EmailRequest(BaseModel):
    email: EmailStr

@app.post("/validate-email")
def validate_email(req: EmailRequest):
    try:
        result = check_email(req.email)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
