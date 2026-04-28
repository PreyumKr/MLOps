from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi.responses import JSONResponse

server = FastAPI()

sett = {1,5,2,3,8,4,9}

class Item(BaseModel):
    number: Annotated[int, Field(..., gt=0, lt=100, description="Number should be between 0 and 100")]


@server.get("/")
def index():
    return {'message': 'Hello to FastAPI'}


@server.get("/about")
def about():
    return {'message': "Its a Dummy FastAPI Code to test implimentation of FastAPI"}


@server.get("/view/{id}")
def get_id_data(id: int = Path(..., description="It fetches the data from our list and shows dynamic data as per any given number")):
    if id in [1,2,3,4,5,6]:
        return {'message': '1 to 6'}
    elif id in [7,8,9,10]:
        return {'message': '7 to 10'}
    else:
        raise HTTPException(status_code=404, detail="Id Not Found")
        

@server.get("/sort")
def sort_data(order: str = Query('asc', description="Order of Sorting")):
    if order == 'asc':
        return {'message': f"{sorted(sett, reverse=False)}"}
    elif order == 'desc':
        return {'message': f"{sorted(sett, reverse=True)}"}
    else:
        raise HTTPException(status_code=400, detail="Invalid sorting order")
    

@server.post("/insert")
def insert_data(item: Item):
    if item.number in sett:
        raise HTTPException(status_code=400 ,detail="Data already exists in database")
    
    sett.add(item.number)
    return JSONResponse(status_code=201, content="{'message': 'Data Inserted'}")


@server.put("/edit/{cur_number}")
def edit_arr(cur_number: int = Path(..., description="The number currently in the set database"), new_number: Item = Query(..., description="New number to be added and not currently in the set dataabse")):
    if cur_number not in sett:
        raise HTTPException(status_code=404, detail="The number don't exist in the database")
    
    if new_number.number in sett:
        raise HTTPException(status_code=400, detail="The new number provided already exists in the database")
    
    sett.remove(cur_number)
    sett.add(new_number.number)

    return JSONResponse(status_code=201, content={'message':'The data got updated'})

@server.delete("/delete/{item}")
def delete_item(item: int):
    if item not in sett:
        raise HTTPException(status_code=404, detail="No such data found")
    
    sett.remove(item)
    return JSONResponse(status_code=201, content={"message": "Data deleted"})