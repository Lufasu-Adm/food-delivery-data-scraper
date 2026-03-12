from pydantic import BaseModel, Field, HttpUrl, field_validator
import logging

class RestaurantSchema(BaseModel):
    name: str = Field(..., min_length=1, description="Nama restoran tidak boleh kosong")
    rating: float = Field(default=0.0, ge=0.0, le=5.0, description="Rating harus antara 0.0 sampai 5.0")
    link: str = Field(..., description="Link URL restoran")

    @field_validator('name')
    def name_must_not_be_unknown(cls, v):
        if v.lower() == 'n/a' or not v.strip():
            raise ValueError('Nama restoran tidak valid')
        return v