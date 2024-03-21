from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first_api():
    version = "1.0.0"
    module = "Housekeeping"
    return {"version": version, "module": module}