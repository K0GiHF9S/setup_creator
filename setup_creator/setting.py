from dataclasses import dataclass
from dataclasses import InitVar
from typing import Optional
from typing import Union
from pathlib import Path


@dataclass(frozen=True)
class GitSetting:
    name: str
    repo: str
    tag: str


FILETYPE = Union[str, Path]


@dataclass
class Setting:
    filename: InitVar[FILETYPE]
    gits: Optional[list[GitSetting]] = None

    def __post_init__(self, filename: FILETYPE):
        import toml
        data = toml.load(filename)
        if isinstance(data.get('git'), list):
            self.gits = [GitSetting(**d) for d in data['git']]
        # object.__setattr__(self, 'surface', node.surface)
