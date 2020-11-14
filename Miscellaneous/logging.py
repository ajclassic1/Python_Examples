import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
LOGGING = logging.getLogger(__name__)

names = {1: ["Alan"], 2: ["Melanie"], 3: ["Johnson"]}
LOGGING.info(names)
