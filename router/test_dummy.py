from fastapi import APIRouter, HTTPException, status
from typing import Dict

router = APIRouter(prefix="/test", tags=["TEST"])

@router.get("/{error_code}")
def get_test(error_code: int) -> Dict:
    """
    Simulates different error status codes for testing purposes.
    """
    if error_code == 200:
        return {"data": "Success (Simulated)"}
    elif error_code == 201:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Created (Simulated)")
    elif error_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request (Simulated)")
    elif error_code == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized (Simulated)")
    elif error_code == 403:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden (Simulated)")
    elif error_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found (Simulated)")
    elif error_code == 405:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method Not Allowed (Simulated)")
    elif error_code == 409:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflict (Simulated)")
    elif error_code == 422:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable Entity (Simulated)")
    elif error_code == 500:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error (Simulated)")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Unknown Error Code: {error_code}")
    

@router.post("/{error_code}")
def get_test(error_code: int) -> Dict:
    """
    Simulates different error status codes for testing purposes.
    """
    if error_code == 200:
        return {"data": "Success (Simulated)"}
    elif error_code == 201:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Created (Simulated)")
    elif error_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request (Simulated)")
    elif error_code == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized (Simulated)")
    elif error_code == 403:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden (Simulated)")
    elif error_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found (Simulated)")
    elif error_code == 405:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method Not Allowed (Simulated)")
    elif error_code == 409:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflict (Simulated)")
    elif error_code == 422:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable Entity (Simulated)")
    elif error_code == 500:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error (Simulated)")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Unknown Error Code: {error_code}")
    

@router.put("/{error_code}")
def get_test(error_code: int) -> Dict:
    """
    Simulates different error status codes for testing purposes.
    """
    if error_code == 200:
        return {"data": "Success (Simulated)"}
    elif error_code == 201:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Created (Simulated)")
    elif error_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request (Simulated)")
    elif error_code == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized (Simulated)")
    elif error_code == 403:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden (Simulated)")
    elif error_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found (Simulated)")
    elif error_code == 405:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method Not Allowed (Simulated)")
    elif error_code == 409:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflict (Simulated)")
    elif error_code == 422:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable Entity (Simulated)")
    elif error_code == 500:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error (Simulated)")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Unknown Error Code: {error_code}")
    

@router.delete("/{error_code}")
def get_test(error_code: int) -> Dict:
    """
    Simulates different error status codes for testing purposes.
    """
    if error_code == 200:
        return {"data": "Success (Simulated)"}
    elif error_code == 201:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Created (Simulated)")
    elif error_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request (Simulated)")
    elif error_code == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized (Simulated)")
    elif error_code == 403:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden (Simulated)")
    elif error_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found (Simulated)")
    elif error_code == 405:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method Not Allowed (Simulated)")
    elif error_code == 409:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflict (Simulated)")
    elif error_code == 422:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Unprocessable Entity (Simulated)")
    elif error_code == 500:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error (Simulated)")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Unknown Error Code: {error_code}")