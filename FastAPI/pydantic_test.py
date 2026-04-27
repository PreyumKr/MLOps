from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Annotated

class Patient(BaseModel):
    name: str
    # age: int = Field(gt=18, lt=120)
    age: Annotated[int, Field(gt=18, lt=120, title='Age of the Patient', description="Age should be greater than 18 and less than 120", examples=[18, 89, 55])]
    Email: Optional[EmailStr] = None
    hobbies: List[str]
    status: Optional[str] = None

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

patient_info = {'name': 'Preyum Kumar', 'age': 24, 'hobbies': ['Cycling', 'Running'], 'status': "Hulu"}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)