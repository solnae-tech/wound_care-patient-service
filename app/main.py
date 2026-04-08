from fastapi import FastAPI
from db.database import Base, engine
from api.profile_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()   

app.include_router(router)