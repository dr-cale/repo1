# Database access object
# Here we work with db object but business logic should be in services.py
from app.database.db import ExampleDB
from app.api.models import QueryModel
from starlette.responses import JSONResponse


class ExampleQuery:
    def __init__(self):
        self.c = ExampleDB('localhost').connect()

    def get_record(self, id):
        pass

    def get_fields_in_record(self,id):
        pass

    def query(self, id):
        pass

