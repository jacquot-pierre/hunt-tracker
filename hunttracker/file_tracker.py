import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HuntAttributesEventHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()

    def on_modified(self, event):
        super().on_modified(event)
        logging.info("File modified: %s", event.src_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "F:\\devel\\hunt-tracker\\hunttracker"
    event_handler = HuntAttributesEventHandler()
    observer = Observer()
    
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join() 

