"""
Create a FastAPI application that integrates with OpenAI's API to process User query.
This application will read the Query from a User, search the vector for matched chunk,
and retrieve the matched details from the Vector Database


- Create an API endpoint to submit user query.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel
import logging
from QueryProcessor import process_user_query

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Request model
class QueryRequest(BaseModel):
    query: str

@app.post("/ask/")
async def user_query(request: QueryRequest):
    """
    Endpoint to submit a user query.
    """
    logging.info("Received Query:", request.query)
    evaluation = process_user_query(request.query)
    print("Evaluation result:", evaluation)
    return evaluation