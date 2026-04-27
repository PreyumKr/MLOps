from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import List, Optional, Annotated

class Address(BaseModel):
    city: str
    state: str
    country: str

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    hobbies: List[str]
    address: Address
    status: Optional[str] = None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value : EmailStr):
        valid_domain = ['idfc.com', 'iitgn.ac.in']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain")
        return value
    
    @field_validator('name', mode='before')
    @classmethod
    def capitalise_name(cls, value: str):
        return value.capitalize()

    @model_validator(mode='after')
    def validate_model(self):
        if self.age > 100:
            raise ValueError("The patient is very old")
        return self

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.is_adult)
    print(patient.email)
    print(patient.address.city)
    print("Inserted")

address1 = Address(city='Ahmedabad', state='Gujarat', country='India')

patient_info = {'name': 'Preyum Kumar', 'age': 19, 'hobbies': ['Cycling', 'Running'], 'status': "Hulu", 'email': "preyum@idfc.com", 'address': address1}

patient1 = Patient(**patient_info)

print(patient1.model_dump())
print(type(patient1.model_dump()))
print(patient1.model_dump_json())
print(type(patient1.model_dump_json()))

insert_patient_data(patient1)