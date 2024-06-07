import logging as lg
import time as tm

lg.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", level=lg.DEBUG, filename="logs.txt")
logger = lg.getLogger("Testlogger")

logger.debug("Este es un mensaje para debug")
logger.info("Info only")
logger.warning("WARNING DUDE!")

tm.sleep(5)

logger.info("First message")
tm.sleep(1)
logger.info("Start of building list")

list_aux = [1, 2, 3, 4, 5]
logger.info("List created")

tm.sleep(3)

for number in list_aux:
    logger.info(f"Printing numbers on list -> {number}")

tm.sleep(3)
logger.info("Finishing program")
