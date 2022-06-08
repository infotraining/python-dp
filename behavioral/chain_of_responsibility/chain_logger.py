from copyreg import constructor
from distutils.debug import DEBUG
from distutils.log import INFO
import logging
from typing import List


class QueueHandler(logging.Handler):
    def __init__(self, q: List[str]):
        super().__init__()
        self._q = q

    def emit(self, record):
        self._q.append(self.format(record))


class EvenFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record: logging.LogRecord):
        no = record.msg.split(maxsplit=1)[0]
        return int(no) % 2 == 0


class ExclamationMarkFormatter(logging.Formatter):

    def __init__(self):
        super().__init__()

    def format(self, record):
        return super().format(record) + "!!!"    


class BetterTimeFormatter(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None, style='%', validate=True):
        super().__init__(fmt, datefmt, style, validate)

    def formatTime(self, record, datefmt) -> str:
        return "<<" + super().formatTime(record, datefmt) + ">>"

if __name__ == "__main__":

    ########################
    # parent logger
    log_a = logging.getLogger('A')

    # stream handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # formatter - Strategy
    formatter = BetterTimeFormatter(
        '-- %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #formatter = ExclamationMarkFormatter()
    ch.setFormatter(formatter)

    # add ch handler to logger
    log_a.addHandler(ch)

    # file handler
    fh = logging.FileHandler('data.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    log_a.addHandler(fh)

    # 'application' code
    log_a.debug('1 - debug message')
    log_a.info('2 - info message')
    log_a.warning('3 - warn message')
    log_a.error('4 - error message')
    log_a.critical('5 - critical message')

    ###########################
    # child logger

    log_ab = logging.getLogger('A.B')
    log_ab.setLevel(logging.DEBUG)

    assert log_a.getChild('B') is log_ab

    q_logs = []
    qh = QueueHandler(q_logs)
    qh.setLevel(logging.DEBUG)
    qh.addFilter(EvenFilter())
    log_ab.addHandler(qh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '  ++ %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log_ab.addHandler(ch)

    # 'application' code
    log_ab.debug('6 - debug message')
    log_ab.info('7 - info message')
    log_ab.warning('8 - warn message')
    log_ab.error('9 - error message')
    log_ab.critical('10 - critical message')
    log_ab.debug('11 - debug message')
    log_ab.info('12 - info message')
    log_ab.warning('13 - warn message')
    log_ab.error('14 - error message')
    log_ab.critical('15 - critical message')

    print('*' * 80)

    print(q_logs)
