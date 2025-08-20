from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file detected: {event.src_path}")

def watch_folder(path):
    observer = Observer()
    observer.schedule(FolderHandler(), path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()