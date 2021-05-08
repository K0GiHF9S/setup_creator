from setup_creator.setting import Setting
from pathlib import Path


def test_setting(shared_datadir: Path):
    setting = Setting(shared_datadir / "test.toml")
    print(setting)
