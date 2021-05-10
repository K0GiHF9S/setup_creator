
import ctypes
from msl.loadlib import Server32
from pathlib import Path


class Cpp32(Server32):
    def __init__(self, host, port, **kwargs):
        super(Cpp32, self).__init__(
            str(Path(__file__).parent / 'UNLHA32'), 'windll', host, port)

    def test(self):
        s = ctypes.c_char_p(r'a -d1 -jso1 -jf0 -+1 e:\\test\\sample.lzh e:\\test\\ test '.encode('utf-8'))
        return self.lib.Unlha(None, s, None, ctypes.c_int8(0))
