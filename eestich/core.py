import glob
import os
import re
from typing import Dict, List

import rasterio
from osgeo import gdal
from rasterio.merge import merge


def get_filename(root: str, extension: str = None) -> List[str]:
    extension = f"*.tif" if extension is None else f"*.{extension}"
    pattern = os.path.join(root, extension)
    return glob.glob(pattern)


def get_rows(paths: List[str], pattern: str = None):
    pattern = '(\d+)' if pattern is None else pattern
    basenames = [os.path.basename(_) for _ in paths]

    for filename in basenames:
        row = re.findall(pattern, filename)[-2]
        