from sqlalchemy import create_engine
from sqlalchemy.sql import text


class UserTable:
    def __init__(self):
        self.__scripts = {
            "select": "select * from users where user_id = :user_id",
            "insert": "insert into users (user_id, user_email, subject_id) select :user_id, :user_email, :subject_id",
            "update": "update users set user_email = :user_email, subject_id = :subject_id where user_id = :user_id",
            "delete": "delete from users where user_id = :user_id",
            "get_new_id": "select max(user_id) + 1 user_id from users",
            "select_all": "select * from users where user_id is not null"
        }
        db_connection_string = "postgresql://postgres:E2eqefd@localhost:5432/QA"
        self.db = create_engine(db_connection_string)

    def create_user(self, user_email, subject_id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            row = connection.execute(text(self.__scripts["get_new_id"])).fetchall()
            # rows = result.mappings().all()
            new_user_id = row[0][0]
            exec_params = {"user_id": new_user_id,
                           "user_email": f'{user_email}',
                           "subject_id": subject_id
                           }
            connection.execute(text(self.__scripts["insert"]), exec_params)
            transaction.commit()
            return new_user_id

    def get_user_list(self):
        with self.db.connect() as connection:
            return connection.execute(text(self.__scripts["select_all"])).fetchall()

    def update_user(self, user_id, user_email, subject_id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            exec_params = {"user_id": user_id,
                           "user_email": f'{user_email}',
                           "subject_id": subject_id
                           }
            connection.execute(text(self.__scripts["update"]), exec_params)
            transaction.commit()

    def delete_user(self, user_id):
        with self.db.connect() as connection:
            transaction = connection.begin()
            exec_params = {"user_id": user_id}
            connection.execute(text(self.__scripts["delete"]), exec_params)
            transaction.commit()