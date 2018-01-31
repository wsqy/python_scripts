import time


class MyTimer():
    def __init__(self):
        self.prompt = "还没开始计时哦，可以调用start()方法开始计时"
        self.starttime = 0
        self.stoptime = 0
        self.unit = ["年", "月", "天", "小时", "分钟", "秒"]
        self.lasted = []
    # 开始计时

    def start(self):
        self.starttime = time.localtime()
        self.prompt = "提示：请先调用stop()方法停止计时！"
        print("计时开始。。。")
    # 计时结束

    def stop(self):
        if isinstance(self.starttime, int):
            print("还没开始计时哦，可以调用start()方法开始计时")
        else:
            self.stoptime = time.localtime()
            self._calc()
            print("计时结束。。。。。")

    # 内部方法 计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.stoptime[index] - self.starttime[index])
            # print(self.lasted)
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + str(self.unit[index])

        self.starttime = 0
        self.stoptime = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self):
        pass


if __name__ == "__main__":
    a = MyTimer()
    input()
    a.start()
    a.stop()
