import uvicorn
from fastapi import FastAPI

from src.wikipedia import wikipedia_app

app = FastAPI()


@app.get("/health", status_code=200)
def health_check():
    return {}


app.include_router(wikipedia_app)

if __name__ == "__main__":
    uvicorn.run("app:app", port=5069, reload=True, access_log=False)
