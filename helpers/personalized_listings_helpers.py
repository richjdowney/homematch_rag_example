import json
from pydantic import BaseModel, Field
from typing import List

class AttributeParser(BaseModel):

    min_house_size: int = Field(description="The minimum house size suggested by the user")
    max_budget: int = Field(description="The maximum budget specified by the user")
    min_bedrooms: int = Field(description="The minumum number of bedrooms specified by the user")
    min_bathrooms: int = Field(description="The minimum number of bathrooms specified by the user")
    neighborhoods: List[str] = Field(description="A list of neighborhoods the user is interested in")


def create_where_filter(parsed_output):
    """Create a where filter that matches the required syntax for Chroma from 
    the parse LLM output
    """
    bedrooms=parsed_output.min_bedrooms 
    bathrooms=parsed_output.min_bathrooms
    budget=parsed_output.max_budget
    house_size=parsed_output.min_house_size
    neighborhoods=parsed_output.neighborhoods

    if neighborhoods[0] != "":

        neighborhoods=json.dumps(neighborhoods)

        where_filter = f"""{{"$and": [
            {{"bedrooms": {{"$gte": {bedrooms}}}}}, 
            {{"bathrooms": {{"$gte": {bathrooms}}}}}, 
            {{"price": {{"$lte": {budget}}}}}, 
            {{"house_size": {{"$gte": {house_size}}}}}, 
            {{"neighborhood": {{"$in": {neighborhoods}}}}}
            ]}}
        """

    else: 
        where_filter = f"""{{"$and": [
            {{"bedrooms": {{"$gte": {bedrooms}}}}}, 
            {{"bathrooms": {{"$gte": {bathrooms}}}}}, 
            {{"price": {{"$lte": {budget}}}}}, 
            {{"house_size": {{"$gte": {house_size}}}}}
            ]}}
        """

    return where_filter