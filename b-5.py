def main():
    # データをスペース区切りで入力してもらう
    data = input("データを入力してください（スペース区切り）: ")
    numbers = [int(x) for x in data.split()]  # 入力を整数のリストに変換
    # 合計値
    total = calculate_sum(numbers)
    print(f"合計値: {total}")
    # 最大値
    max_value = calculate_max(numbers)
    print(f"最大値: {max_value}")
    # 最小値
    min_value = calculate_min(numbers)
    print(f"最小値: {min_value}")
    # 平均値
    avg = calculate_mean(numbers)
    print(f"平均値: {avg}")


# 合計値を計算する関数
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 最大値を計算する関数
def calculate_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


# 最小値を計算する関数
def calculate_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


# 平均値を計算する関数
def calculate_mean(numbers):
    total = calculate_sum(numbers)  # 合計値を再利用
    count = len(numbers)
    return total / count


# メイン関数の呼び出し
if __name__ == "__main__":
    main()
