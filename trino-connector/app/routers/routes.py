# Endpoints, you can create multiple files if is necessary and include them into main.py

from fastapi import APIRouter

from app.api.services import Basic
from app.api.models import QueryModel

############################
##### ---- ROUTES ---- #####
############################

appl = APIRouter()

# curl -K GET localhost:8000/fetch_all
@appl.get("/fetch_all")
def root():
    return Basic.get_all_tables()

# curl -K GET localhost:8000/fetch_specific?table=users3&firstname=an
@appl.post("/fetch_specific")
def root(querymodel: QueryModel):
    return Basic.get_specific_table(querymodel)

##################################
##### ---- EXEC METHODS ---- #####
##################################
