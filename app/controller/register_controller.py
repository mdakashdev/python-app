from app.schemas.auth import RegisterRequest

def store(data: RegisterRequest):
    return {
        "message": "successfully registration11",
        "data": data
    }