from sqlalchemy.orm import Session
from schema import schemas
from db import models


def get_profile_service(db: Session, user_id: int):
    return db.query(models.UserProfiles).filter_by(user_id=user_id).first()


def update_profile_service(db: Session, user_id: int, data: schemas.ProfileUpdate):
    profile = get_profile_service(db, user_id)
    if not profile:
        raise ValueError(f"Profile for user {user_id} not found.")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)
    return profile


def delete_profile_service(db: Session, user_id: int):
    profile = get_profile_service(db, user_id)
    if not profile:
        raise ValueError(f"Profile for user {user_id} not found.")

    db.delete(profile)
    db.commit()
    return profile