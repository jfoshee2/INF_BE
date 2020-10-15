from db_access import util


def create_user(user_name, pw_hash):
    util.insert_row("INSERT INTO USERS (USER_NAME, PW_HASH) VALUES (%s, %s)", user_name, pw_hash,)
