from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.config import config
from app.database import connect_to_mongo, close_mongo_connection
from app.logger import setup_logger

from api.routes_auth import router as auth_router
from api.routes_upload import router as upload_router
from api.routes_query import router as query_router
from api.routes_monitoring import router as monitoring_router

logger = setup_logger()

app = FastAPI(
title="Advanced RAG-Enabled Transformer Embedding System",
description="Intelligent Knowledge Discovery from Excel Datasets",
version="1.0.0"
)

app.add_middleware(
CORSMiddleware,
allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# ---------------- Startup ----------------

@app.on_event("startup")
async def startup_event():
logger.info("Starting RAG System...")
await connect_to_mongo()
logger.info("RAG System started successfully")

# ---------------- Shutdown ----------------

@app.on_event("shutdown")
async def shutdown_event():
logger.info("Shutting down RAG System...")
await close_mongo_connection()
logger.info("RAG System shut down")

# ---------------- Root Endpoint ----------------

@app.get("/")
async def home():
return {
"message": "Advanced RAG-Enabled Transformer Embedding System",
"version": "1.0.0",
"docs": "/docs",
"health": "/api/health"
}

# ---------------- API Endpoint ----------------

@app.get("/api")
async def root():
return {
"message": "Advanced RAG API running",
"version": "1.0.0",
"status": "operational"
}

# ---------------- Health Check ----------------

@app.get("/api/health")
async def health_check():
return {"status": "healthy"}

# ---------------- Routers ----------------

app.include_router(auth_router, prefix="/api")
app.include_router(upload_router, prefix="/api")
app.include_router(query_router, prefix="/api")
app.include_router(monitoring_router, prefix="/api")

# ---------------- Run Server ----------------

if **name** == "**main**":
import uvicorn
uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
