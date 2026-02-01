import logging
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "healthy"}

@app.get("/api/message")
def message():
    logger.info("Message endpoint hit")
    return {"message": "Hello from backend"}
