class Customer:
    def __init__(self, first_name, family_name, age):
        """初期化メソッド"""
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        """フルネームを返す"""
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        """年齢に応じた入場料を計算する"""
        if self.age < 20:
            return 1000  # こども料金
        elif self.age < 65:
            return 1500  # おとな料金
        else:
            return 1200  # シニア料金

    def info_csv(self):
        """顧客情報をCSV形式で返す"""
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


# 顧客オブジェクトの作成
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# 動作確認
print(ken.full_name())  # "Ken Tanaka"
print(tom.full_name())  # "Tom Ford"
print(ieyasu.full_name())  # "Ieyasu Tokugawa"

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# 以降で各問のコードを追加していく

# C-1. フルネームを取得できる

print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

# C-2. 年齢という概念の追加

print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
# 料金の計算ルール
# こども料金(20歳未満): 1000円
# おとな料金(20歳以上65歳未満): 1500円
# シニア料金(65歳以上): 1200円

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(ken.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
