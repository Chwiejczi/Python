import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s -%(name)s -%(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/cinema.log"), logging.StreamHandler()],
)

logging.getLogger().handlers[0].setLevel(logging.DEBUG)
logging.getLogger().handlers[1].setLevel(logging.INFO)
