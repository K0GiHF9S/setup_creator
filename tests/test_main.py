import pytest
from setup_creator.__main__ import parse_args
from pathlib import Path

def test_version():
    with pytest.raises(SystemExit) as e:
        parse_args('-v'.split())
    assert e.value.code == 0


def test_help():
    with pytest.raises(SystemExit) as e:
        parse_args('-h'.split())
    assert e.value.code == 0


def test_no_setting():
    with pytest.raises(SystemExit) as e:
        parse_args('-s dummy.toml'.split())
    assert e.value.code == 2


def test_setting(shared_datadir : Path):
    parse_args(f'-s {shared_datadir / "test.toml"}'.split())
