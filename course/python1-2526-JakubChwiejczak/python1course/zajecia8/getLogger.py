import logging
from datetime import datetime
from pathlib import Path


def get_logger(name: str, level: int = logging.INFO, log_dir: Path = Path("logs")) -> logging.Logger:
    """Tworzy skonfigurowany logger z handlerami do konsoli i pliku."""

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d")
    file_handler = logging.FileHandler(log_dir / f"app_{timestamp}.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger