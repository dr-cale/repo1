# Business logic, please delete example
from starlette.responses import JSONResponse
from app.database.daos import ExampleQuery
from app.api.models import QueryModel
import trino

class Basic:
    def __init__(self):
        self.c = ExampleQuery()

    def get_data(self, uid):
        return self.c.get_record(id='id')

    def get_all_tables():
        try:
            conn = trino.dbapi.connect(
                host='dev-solverai.thingsolver.com',
                port=8081,
                user='DraganChe',
                catalog='hive',
                schema='che',
                http_scheme='http',
                verify=False
            )
            cur = conn.cursor()
            cur.execute('show tables')
            rows = cur.fetchall()
            return JSONResponse(
                    status_code=200,
                    content={
                        'Result': rows
                    }
                )
        except Exception as e:
            return JSONResponse(
                    status_code=404,
                    content={
                        'Result': str(e)
                    }
                )

    def get_specific_table(querymodel: QueryModel):
        try:
            conn = trino.dbapi.connect(
                host='dev-solverai.thingsolver.com',
                port=8081,
                user='DraganChe',
                catalog=querymodel.trinoCatalog,
                schema=querymodel.trinoSchema,
                http_scheme='http',
                verify=False
            )
            cur = conn.cursor()
            if querymodel.firstname == None:
                querymodel.firstname = ''
            cur.execute(f'select * from {querymodel.table} where "firstname" like \'%{querymodel.firstname}%\'')
            rows = cur.fetchall()
            if len(rows) == 0:
                return JSONResponse(
                    status_code=404,
                    content={
                        'Result': 'The query returned no matches.'
                    }
                )
            return JSONResponse(
                    status_code=200,
                    content={
                        'Result': rows
                    }
                )
        except Exception as e:
            return JSONResponse(
                    status_code=404,
                    content={
                        'Result': str(e)
                    }
                )

