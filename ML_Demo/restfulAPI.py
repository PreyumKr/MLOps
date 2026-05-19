from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
from typing import List, Optional, Dict
from fastapi.openapi.utils import get_openapi

app = FastAPI()

def custom_openapi():
    # Cache the schema so it doesn't regenerate on every request
    if app.openapi_schema:
        return app.openapi_schema
    
    # Generate the default schema
    openapi_schema = get_openapi(
        title="Custom API Title",
        version="2.0.0",
        description="This is a custom description",
        routes=app.routes,
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Assign the custom function to the app
app.openapi = custom_openapi


# Placeholder database
items_db = [
    {"id": 1, "name": "Laptop", "description": "High-end gaming laptop"}
]

class ItemResponse(BaseModel):
    id: int
    name: str
    links: Dict[str, str]

# 1. GET Request: Returns 200 OK by default
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, request: Request):
    item = next((i for i in items_db if i["id"] == item_id), None)
    if item is None:
        # Rule: Return 404 if resource doesn't exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    base_url = str(request.base_url).rstrip("/")
    return {
        "id": item["id"],
        "name": item["name"],
        "links": {
            "self": f"{base_url}/items/{item_id}",
            "all_items": f"{base_url}/items"
        }
    }

# 2. POST Request: Explicitly returns 201 Created
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    new_id = len(items_db) + 1
    items_db.append({"id": new_id, "name": name})
    return {"message": "Created successfully", "id": new_id}

# 3. DELETE Request: Returns 204 No Content
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    global items_db
    if not any(i["id"] == item_id for i in items_db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    items_db = [i for i in items_db if i["id"] != item_id]
    return None # 204 means no content is returned