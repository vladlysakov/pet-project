import os

from pet_project.common.constants import DatabaseVariables


class DatabaseConfig:
    engine = os.getenv(DatabaseVariables.ENGINE, DatabaseVariables.DEFAULT_ENGINE)
    name = os.getenv(DatabaseVariables.TABLE, DatabaseVariables.DEFAULT_TABLE_NAME)
    user = os.getenv(DatabaseVariables.USER, DatabaseVariables.DEFAULT_USER)
    password = os.getenv(DatabaseVariables.PASSWORD, DatabaseVariables.DEFAULT_PASSWORD)
    host = os.getenv(DatabaseVariables.HOST, DatabaseVariables.DEFAULT_HOST)
    port = os.getenv(DatabaseVariables.PORT, DatabaseVariables.DEFAULT_PORT)

    user_model = os.getenv(DatabaseVariables.AUTH_USER_MODEL, DatabaseVariables.DEFAULT_AUTH_USER_MODEL)
