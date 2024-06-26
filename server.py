from fastapi import FastAPI
from src.sagemaker.resources import get_sagemaker_endpoint
from src.sagemaker.query_endpoint import make_query_request
from src.schemas.query import Query
from src.config import get_config_for_endpoint
import uvicorn
app = FastAPI()


@app.get("/endpoint/{endpoint_name}")
def get_endpoint(endpoint_name: str):
    return get_sagemaker_endpoint(endpoint_name)


@app.post("/endpoint/{endpoint_name}/query")
def query_endpoint(endpoint_name: str, query: Query):
    config = get_config_for_endpoint(endpoint_name)
    if query.context is None:
        query.context = ''
    return make_query_request(endpoint_name, query, config)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
