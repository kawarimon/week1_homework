# 課題D-6: カウンターその3
class MyCounterV3:
    def __init__(self, value=0, step=1):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step


# テストコード
counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1
counter1.count_up()
print(counter1.value)  # 3
counter1.count_up()
print(counter1.value)  # 5
counter1.count_down()
print(counter1.value)  # 3
counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3
counter2.count_down()
print(counter2.value)  # -1
counter2.count_down()
print(counter2.value)  # -5
