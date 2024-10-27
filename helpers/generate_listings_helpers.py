from pydantic import BaseModel, Field, NonNegativeInt

class ListingOutput(BaseModel):
    neighborhood: str = Field(description="The neighborhood for the listing")
    price: NonNegativeInt = Field(description="The price of the unit")
    bedrooms: NonNegativeInt = Field(description="The number of bedrooms in the unit")
    bathrooms: float = Field(description="The number of bathrooms in the unit")
    house_size: NonNegativeInt = Field(description="The size of the unit in sq. ft.")
    property_description: str = Field(description="The description of the property")
    neighborhood_description: str = Field(
        description="The description of the neighborhood"
    )