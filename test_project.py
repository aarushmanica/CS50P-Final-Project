def test_register():
    assert register_user("Aarush", "test_password") == True


def test_login():
    assert login() == True


def test_if_main_screen_exists():
    assert main() == True