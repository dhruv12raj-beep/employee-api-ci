from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fastapi"}


@app.get("/home")
def home():
    return {"message": "Welcome to home"}
