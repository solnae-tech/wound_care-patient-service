from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from schema.schemas import ProfileUpdate, ProfileOut
from services.profile_service import get_profile_service, update_profile_service, delete_profile_service

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.get("/{user_id}", response_model=ProfileOut)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    profile = get_profile_service(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"Profile for user {user_id} not found.")
    return profile


@router.patch("/{user_id}", response_model=ProfileOut)
def update_profile(user_id: int, data: ProfileUpdate, db: Session = Depends(get_db)):
    try:
        return update_profile_service(db, user_id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_profile_service(db, user_id)
        return None
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))