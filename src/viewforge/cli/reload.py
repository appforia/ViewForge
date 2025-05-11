import sys
import time
import importlib
import traceback
import importlib.util
from pathlib import Path
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from viewforge.core.app import App
from viewforge.ui.elements.text import Text

def load_app_entry(source):
    if source.endswith(".py"):
        spec = importlib.util.spec_from_file_location("reloaded_module", source)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        module = importlib.import_module(source)
    return module

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, source):
        self.source = source

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"🔄  File modified: {event.src_path}")
            try:
                module = load_app_entry(self.source)
                app = App.current()
                if app:
                    print("✅  UI reloaded.")
                    app._components = module.build()
                    app.reload()
            except Exception as e:
                print("❌  Reload error:", e)
                traceback.print_exc()
                app = App.current()
                if app:
                    app._components = [Text("Reload error. Check console.")]
                    app.reload()

def run_reload():
    if len(sys.argv) >= 2:
        source = sys.argv[1]
    else:
        default_main = Path("main.py")
        if default_main.exists():
            print("📂  No module specified — using 'main.py' in current directory")
            source = str(default_main)
        else:
            print("❌  No module specified and no 'main.py' found")
            sys.exit(1)

    try:
        module = load_app_entry(source)
        components = module.build()
    except Exception as e:
        print(f"⚠️ Failed to load app: {e}")
        components = [Text(f"Error loading {source}")]

    app = App()

    def start_watcher():
        observer = Observer()
        print(f"[DEBUG] Watching directory: {Path.cwd()}")
        observer.schedule(ReloadHandler(source), path=str(Path.cwd()), recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    threading.Thread(target=start_watcher, daemon=True).start()
    app.run(components, True)
