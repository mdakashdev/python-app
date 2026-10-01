from fastapi import APIRouter



router = APIRouter(
    prefix="/api/department",
    tags=["Department"]
)

@router.get("/list")
def get_list():
    return {
        "message": "test"
    }
