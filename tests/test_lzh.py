from setup_creator.lzh import cpp64


def test_lzh():
    client = cpp64.Cpp64()
    assert client.test() == 0
    client.shutdown_server32()
