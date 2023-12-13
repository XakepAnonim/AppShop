# from fastapi import APIRouter
#
# from auth.base_config import fastapi_users, auth_backend
#
# router = APIRouter(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth",
#     tags=["Auth"],
# )