import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from FrameWorks.MVC.Models.Footwear import Footwear
from FrameWorks.MVC.Models.FootwearRequest import FootwearRequest
from FrameWorks.MVC.Models.FootwearResponce import FootwearResponse
from FrameWorks.MVC.Repository import Repository
from FrameWorks.MVC.Service import Service
from FrameWorks.MVC.Controller import Controller

app = FastAPI(
    Title="Footwear API",
    description="API for managing footwear items",
    version="1.0.0"
)
controller = Controller(Service(Repository()))

print("server is running...")

@app.get("/")
async def select():
    return JSONResponse( [item.__dict__ for item in controller.readAll()])

@app.post("/create")
async def create(footwear: FootwearRequest):
    print(controller.create(footwear).__dict__)
    return JSONResponse({"status": "200"})

@app.put("/update/{footwear_id}")
async def update(footwear_id: int, footwear: FootwearRequest):
    updated_footwear = controller.update(footwear_id, footwear)
    if updated_footwear is not None:
        return JSONResponse(updated_footwear.__dict__)
    else:
        return JSONResponse({"error": "Footwear not found"}, status_code=404)

@app.delete("/delete/{footwear_id}")
async def delete(footwear_id: int):
    success = controller.delete(footwear_id)
    if success:
        return JSONResponse({"status": "200"})
    else:
        return JSONResponse({"error": "Footwear not found"}, status_code=404)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
