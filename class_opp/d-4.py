# 課題D-4: カウンターその1


class MyCounterV1:
    def __init__(self, value=0):
        self.value = value

    def count_up(self):
        self.value += 1


# テストコード
counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0
counter1.count_up()
print(counter1.value)  # 1
counter1.count_up()
print(counter1.value)  # 2
counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7
counter2.count_up()
print(counter2.value)  # 8
counter2.count_up()
print(counter2.value)  # 9
