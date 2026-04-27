from fastapi import FastAPI, HTTPException, Path, Query

server = FastAPI()

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
        
arr = [1,5,2,3,8,4,9]
@server.get("/sort")
def sort_data(order: str = Query('asc', description="Order of Sorting")):
    if order == 'asc':
        return {'message': f"{sorted(arr, reverse=False)}"}
    elif order == 'desc':
        return {'message': f"{sorted(arr, reverse=True)}"}
    else:
        raise HTTPException(status_code=400, detail="Invalid sorting order")