from os import path
from pathlib import Path


class Site:

    def __init__(self, source, dest):
        source = Path(source)
        dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exists_okay=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if path is self.directory:
                self.create_dir(path)