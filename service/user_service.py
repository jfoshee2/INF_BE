import bcrypt

from db_access import db_users

s = bcrypt.gensalt()  # global variable to store password hashes


def create_user(user_name, password):
    return db_users.create_user(user_name, bcrypt.hashpw(password, s))


def login_user(user_name, password):
    pass


def get_time_frame(user_id):
    pass

