import glob
import os
import re
from typing import Dict, List,Set

import rasterio
from osgeo import gdal
from rasterio.merge import merge


def get_filename(root: str, extension: str = None) -> List[str]:
    extension = f"*.tif" if extension is None else f"*.{extension}"
    pattern = os.path.join(root, extension)
    return glob.glob(pattern)

def get_basenames(paths: List[str]) -> List[str]:
    return [os.path.basename(_) for _ in paths]

def get_rows(basenames: List[str], pattern: str = None) -> Set:
    pattern = '(\d+)' if pattern is None else pattern
    return set([re.findall(pattern, filename)[-2] for filename in basenames])

def files_by_row(indexs: Set[str], basenames: List[str]) -> Dict[str, str]:
    
    cfg = {idx: [] for idx in indexs}
    
    for name in basenames:
        for idx in  indexs:
            row = re.findall('(\d+)', name)[-2]
            if idx == row:
                cfg.get(row).append(name)
    return cfg

def raster_factory(buffer: list, filename: str) -> None:
    src = buffer[-1]
        
    mosaic, out_trans = merge(buffer)
    
    out_meta = src.meta.copy()
    
    out_meta.update({
        'driver': "GTiff",
        'height': mosaic.shape[1],
        'width': mosaic.shape[2],
        'transform': out_trans,
        'crs': "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"
    })
    with rasterio.open(filename, 'w', **out_meta) as rast:
        rast.write(mosaic)
        rast.close()
    
    [_.close() for _ in buffer]
    buffer = None
    return None

def build_ras_by_row(cfg: Dict[str, List[str]], dest: str = None) -> None:
    dest = "./dump" if dest is None else dest
    
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for row, paths in cfg.items():
        
        buffer = [rasterio.open(_)for _ in paths]
        tifname = f'dump-{row}.tif'
        filename = os.path.join(dest, tifname)
        raster_factory(
            buffer=buffer,
            filename=filename
        )
        tifname, filename = None, None
    return None

def build_mosaic(dump: str, outname: str) -> None:
    
    inputs = [os.path.join(dump, tail) for tail in os.listdir(dump)]
    buffer = [rasterio.open(_) for _ in inputs]
    
    raster_factory(buffer=buffer, filename=outname)
    return None