from pydantic import BaseModel, EmailStr, Field


class UserSignup(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ResumeData(BaseModel):
    user_id: str
    fullName: str
    position: str
    email: EmailStr
    mobile: str
    location: str
    linkedIn: str
    github: str
    profile: str
    experience: str
    skills: str
    certificate: str
