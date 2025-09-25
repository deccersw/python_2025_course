import logging

logging.basicConfig(
    level=logging.INFO,
    # - указываем уровень информации, начиная с которого,
    # будут записываться информация"""
    filename='week03/app.log',
    # если не указывать файл, вывод будет производиться в консольку
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
)

logging.info("Программа запущена")
logging.warning("Предупреждение")
logging.error("Ошибка")

x, y = 4, 0
logging.info(f"The values of x and y are {x} and {y}")
try:
    result = x / y
    logging.info(f"x/y successful with result: {x/y}.")
except ZeroDivisionError:
    logging.error("Ошибка деления на ноль")
