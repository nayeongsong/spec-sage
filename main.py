from fastapi import FastAPI

app = FastAPI(title="Spec Sage", description="FastAPI project for performance testing agent")


@app.get("/")
def read_root():
    return {"message": "Hello from spec-sage!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
