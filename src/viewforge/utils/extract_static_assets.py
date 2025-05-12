import os
import shutil
from importlib.resources import as_file, files
from pathlib import Path
from typing import Optional


def extract_static_assets(destination: Optional[str] = None) -> str:
    """
    Copies Vite assets from embedded package to the given destination.
    Returns the path used.
    """
    if destination is None:
        from viewforge.utils.tempdir import viewforge_runtime_dir
        destination = os.path.join(viewforge_runtime_dir(), "assets")

    package = "viewforge.plugins.shoelace.sldist.assets"
    asset_folder = files(package)
    os.makedirs(destination, exist_ok=True)

    for asset in asset_folder.iterdir():
        dest_file = Path(destination) / asset.name
        with as_file(asset) as asset_path:
            if dest_file.exists() and dest_file.stat().st_size == asset_path.stat().st_size:
                continue
            shutil.copyfile(asset_path, dest_file)

    return destination
