from fastapi import FastAPI
from query import generate_response

app = FastAPI()

@app.get("/query/{ip}")
def query_host(ip: str):
    response = generate_response(ip)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
