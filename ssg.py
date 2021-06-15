import typer
from ssg.site import Site

def main(self, source="content", dest="dist"):
    config = {"source:" source, "dest": dest}
    for key, value in config.items():
        Site(**config)