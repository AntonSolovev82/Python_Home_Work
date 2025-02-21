import pytest
from users import UserTable


@pytest.fixture()
def users():
    user_table = UserTable()
    yield user_table

def test_create_user(users, email, subject):
    user_id = users.create_user('new_user@yandex.ru', 3)
    rows = users.get_user_list()
    for user in rows:
        if user[0] == user_id:
            print('user = ', user, user[1])
            assert user[1] == 'new_user@yandex.ru'
            assert user[2] == 3

    users.update_user(user_id, 'not_already_new_user@yandex.ru', 2)
    rows = users.get_user_list()
    for user in rows:
        if user[0] == user_id:
            assert user[1] == 'not_already_new_user@yandex.ru'
            assert user[2] == 2

    users.delete_user(user_id)
    rows = users.get_user_list()
    is_find = False
    for user in rows:
        if user[0] == user_id:
            is_find = True
            break
        assert is_find is False