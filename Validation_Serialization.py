from pydantic import BaseModel, field_validator
from datetime import datetime

class UserCreate(BaseModel):
    age: int
    @property
    def birth_year(self) -> int:
        return datetime.now().year - self.age
    @field_validator('age')
    def validate_age(cls, v):
        if not 13 <= v <= 120:
            raise ValueError("Invalid age")
        return v

# FASTAPI ENDPOINT
@app.post("/users")
def create_user(user: UserCreate):
    db.save(birth_year=user.birth_year)                  # Computed, never sent by client
