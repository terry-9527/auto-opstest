from datetime import datetime
import logging
from utils.handle_path import log_dir

class MyLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        super().__init__(name)
        self.setLevel(level)

        # 设置渠道的输出格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s [%(lineno)d行]: %(message)s'
        formatter = logging.Formatter(fmt)
        # 设置输出渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        # 输出渠道添加到日志器
        self.addHandler(handle1)
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

# now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# log_file = log_dir + "-" + now + ".log"
mylogger = MyLogger("ARS", file=r"F:\yunweixitong\outputs\log\my.log")

if __name__ == '__main__':
    mylogger = MyLogger("ARS", file = r"F:\yunweixitong\outputs\log\my.log")
    mylogger.info("this is a test by fide")