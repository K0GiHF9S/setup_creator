from dataclasses import dataclass
from dataclasses import InitVar
from typing import Optional


@dataclass(frozen=True)
class GitSetting:
    name: str
    repo: str
    tag: str


@dataclass
class Setting:
    filename: InitVar[str]
    gits: Optional[list[GitSetting]] = None

    def __post_init__(self, filename: str):
        import toml
        data = toml.load(filename)
        if isinstance(data.get('git'), list):
            self.gits = [GitSetting(**d) for d in data['git']]
        # object.__setattr__(self, 'surface', node.surface)
        pass
