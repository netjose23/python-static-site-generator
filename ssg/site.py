from pathlib import Path


class Site:

    def __init__(self, source, dest):
        source = Path(self)
        dest = Path(self)

    def create_dir(self, path):
        directory = Path(self.dest / path.relative_to(self.source))
        path.relative_to(self.source)
        mkdir = (parents=True, exists_okay=True)