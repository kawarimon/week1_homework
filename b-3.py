# 行数と列数を入力してもらう
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
# 九九表を作成
for x_num in range(1, row + 1):  # 行のループ
    for y_num in range(1, col + 1):  # 列のループ
        result = x_num * y_num  # 掛け算の結果を計算
        # 結果を式と共に整形して出力（1桁、2桁、3桁も整列）
        print(f"{x_num} x {y_num} = {result:<3}", end=" | ")
    print()  # 行の最後に改行
