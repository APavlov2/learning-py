from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    fullname: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes=True

    def toJSON(self):
        return self.model_dump(exclude={'id'})