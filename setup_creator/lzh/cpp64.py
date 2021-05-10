
from msl.loadlib import Client64
from pathlib import Path

class Cpp64(Client64):
    def __init__(self):
        super(Cpp64, self).__init__(module32='cpp32', append_sys_path=str(Path(__file__).parent))

    def test(self):
        return self.request32('test')
