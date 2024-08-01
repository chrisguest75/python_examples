from datetime import datetime

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zipcode: str

    def __init__(self, street: str, city: str, zipcode: str):
        super().__init__(street=street, city=city, zipcode=zipcode)


class Meeting(BaseModel):
    when: datetime
    where: Address
    why: str = 'No idea'



