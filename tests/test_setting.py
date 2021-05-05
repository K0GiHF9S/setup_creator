from setup_creator.setting import Setting


def test_setting():
    setting = Setting('test.toml')
    print(setting)
    # assert setting.a == 1
