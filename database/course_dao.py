from sqlalchemy import create_engine, text
import pandas as pd
# import urllib.parse as url_parse
from urllib.parse import quote_plus

# Only 1 db and username,pw,db is same
# If different then we need parameterized constructor

#("<dialect>+<driver>://<username>:<password>@<server_url:port>/<database_name>")
class CreateMySQLEngineInstance:

    def __init__(self):
        # password = quote_plus("abdul@123")
        password = "root"
        self.engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/python_db")
    
    def get_engine(self):
        return self.engine
    
# CRUD (DAO) -> Logic (in form of functions)

def create_table():
    mysql_instance = CreateMySQLEngineInstance()
    engine = mysql_instance.get_engine()
    drop_query = text("drop table if exists course")
    create_table_query = text("""
    create table course
    (
        cid int primary key auto_increment,  
        name varchar(100) not null,
        description text not null,
        duration varchar(100) not null
    )
    """)

    with engine.connect() as connection:
        connection.execute(drop_query)
        connection.execute(create_table_query)

        print("Table created successfully")
    
def insert_course(course_name, course_duration, description):
    mysql_instance = CreateMySQLEngineInstance()

    engine = mysql_instance.get_engine()

    insert_query = text("insert into course(name, description, duration) values (:cname, :cdesc, :cdur)")

    with engine.connect() as connection:
        result = connection.execute(insert_query,{"cname":course_name,"cdur":course_duration, "cdesc":description})
        connection.commit()
        print(f"Insert successfully, Rows affected = {result.rowcount}")

def get_all_courses():
    mysql_instance = CreateMySQLEngineInstance()

    engine = mysql_instance.get_engine()


    query = "select * from course"

    # Table in form of dataframe

    df = pd.read_sql(query,engine)

    return df


def get_course_by_id(course_id):
    mysql_instance = CreateMySQLEngineInstance()

    engine = mysql_instance.get_engine()


    query = text(f"select * from course where cid = {course_id}")

    # Table in form of dataframe

    df = pd.read_sql(query,engine)

    return df

def delete_course(course_id):
    mysql_instance = CreateMySQLEngineInstance()

    engine = mysql_instance.get_engine()

    delete_query = text("delete from course where cid = :cou_id")

    with engine.connect() as connection:
        connection.execute(delete_query,{"cou_id":course_id})

        connection.commit()

        print(f"Course with id = {course_id} deleted successfully")


def update_course(course_id, updated_course_desc, updated_course_name, updated_course_duration):
    mysql_instance = CreateMySQLEngineInstance()

    engine = mysql_instance.get_engine()

    delete_query = text("update course set name = :cname, description = :cdesc, duration = :cdur where cid = :cou_id")

    with engine.connect() as connection:
        result = connection.execute(delete_query,{"cname":updated_course_name,"cdur":updated_course_duration, "cdesc":updated_course_desc,"cou_id":course_id})
        connection.commit()
        print(f"Updated successfully, Rows affected = {result.rowcount}")