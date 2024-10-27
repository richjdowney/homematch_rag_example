# Define the metadata extraction function.
def metadata_func(record: dict, metadata: dict) -> dict:

    metadata["neighborhood"] = record.get("neighborhood")
    metadata["price"] = record.get("price")
    metadata["bedrooms"] = record.get("bedrooms")
    metadata["bathrooms"] = record.get("bathrooms")
    metadata["house_size"] = record.get("house_size")
    metadata["property_description"] = record.get("property_description")
    metadata["neighborhood_description"] = record.get("neighborhood_description")

    return metadata