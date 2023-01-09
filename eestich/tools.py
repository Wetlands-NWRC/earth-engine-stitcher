from . import core

from abc import ABC


class Tool(ABC):
    pass


class TiffStitcher(Tool):
    def __init__(self, src: str, dest: str) -> None:
        super().__init__()
        self.src = src
        self.dest = dest
    # TODO add props for setting re pattern and scratch ws 
    
    def run(self) -> None:
        fn = core.get_filename(self.src)
        bn = core.get_basenames(fn)
        rows = core.get_rows(basenames=bn, pattern=None)
        fn_row = core.files_by_row(
            indexs=rows,
            basenames=bn,
            root=self.src
        )

        core.build_ras_by_row(
            cfg=fn_row,
            dest=None,
        )

        core.build_mosaic(
            dump="./dump",
            outname=self.dest
        )
        return None