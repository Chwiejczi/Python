import importlib
import time
from os import getcwd

import czas

current_path = getcwd()
print(f"aktualna scieżka: {current_path}")
print(f"aktualny czas nr 1:{czas.aktualny_czas}")
time.sleep(20)
print(f"aktualny czas nr 2:{czas.aktualny_czas}")
importlib.reload(czas)
print(f"aktualny czas nr 3:{czas.aktualny_czas}")
