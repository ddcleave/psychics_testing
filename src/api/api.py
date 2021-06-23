from src.api.routers import homepage, new_test, expected_number
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(homepage.router, tags=["homepage"])
api_router.include_router(new_test.router, tags=["new_test"])
api_router.include_router(expected_number.router, tags=["expected"])
