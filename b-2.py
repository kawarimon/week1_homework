# ユーザーから行数と列数を入力
row = int(input("行数を入力してください: "))
col = int(input("列数を入力してください: "))
# 指定された行数と列数の掛け算表を作成
for x_num in range(1, row + 1):  # 行を繰り返す
    for y_num in range(1, col + 1):  # 列を繰り返す
        result = x_num * y_num  # 掛け算結果を計算
        print(result, end=" ")
    print()  # 改行


# 実行結果
# 行数を入力してください: 4
# 列数を入力してください: 6
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
