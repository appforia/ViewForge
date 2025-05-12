import os
import tempfile

def viewforge_runtime_dir() -> str:
    """
    Returns a writable cross-platform temp folder for ViewForge runtime assets.
    On Windows: C:/Users/you/AppData/Local/Temp/viewforge
    On Linux/macOS: /tmp/viewforge
    """
    base = tempfile.gettempdir()
    path = os.path.join(base, "viewforge")
    os.makedirs(path, exist_ok=True)
    return path
