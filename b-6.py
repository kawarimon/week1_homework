import random  # サイコロの乱数生成に使用


def main():
    # ユーザー入力を取得
    n = int(input("サイコロの面の数は?: "))  # N面サイコロの面数
    m = int(input("何回振りますか?: "))  # 振る回数
    # サイコロを振る
    results = roll_dice(n, m)
    print(results)  # 結果を表示


# サイコロを振る関数
def roll_dice(n, m):
    rolls = []
    for _ in range(m):  # M回振る
        roll = random.randint(1, n)  # 1からNの乱数を生成
        rolls.append(roll)  # 結果をリストに追加
    return rolls


# メイン関数の呼び出し
if __name__ == "__main__":
    main()
