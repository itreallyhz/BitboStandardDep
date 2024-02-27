from pydantic import BaseModel, constr, EmailStr

class UserSchema(BaseModel):
    first_name: constr(min_length=3, max_length=50)
    last_name: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=3, max_length=50)
    user_type: constr(min_length=4, max_length=20)

class AddResidentSchema(BaseModel):
    first_name: constr(min_length=3, max_length=50)
    last_name: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=3, max_length=50)



