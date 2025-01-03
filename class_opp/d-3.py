# 課題D-3: 正方形オブジェクト
import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)

    def diagonal(self):
        return round(math.sqrt(2) * self.side, 2)


# テストコード
square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12
square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
