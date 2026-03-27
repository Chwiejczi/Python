import time
from pathlib import Path


class FileLock:
    def __init__(self, filepath, timeout):
        self.filepath = Path(filepath)
        self.timeout = timeout
        self.lockFile = Path(str(filepath) + ".loc")

    def __enter__(self):
        # if os.path.exists(self.filepath):
        #   time.sleep(10)
        #  if os.path.exists(self.filepath):
        #     raise TimeoutError(f"Nie można uzyskać blokady pliku {self.filepath} - timeout")
        # self.lock=Path.touch(self.filepath)
        start = time.time()
        while self.lockFile.exists():
            if time.time() - start > 10:
                raise TimeoutError(
                    "Nie można uzyskać blokady pliku {self.filepath} - timeout"
                )
            time.sleep(1)
        self.lockFile.touch()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # if exc_type:
        #     print(f"Wystąpił wyjątek: {exc_value}")
        if self.lockFile.exists():
            self.lockFile.unlink()
        return False  # dlatego ze wyjatek obsluzymy w eneter
