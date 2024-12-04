def main():
    # 気温データを辞書として保持
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]
    # 問題1: 全国の平均気温を計算
    national_avg = calculate_national_avg(weather_information)
    print(f"全国の平均気温: {national_avg:.1f}℃")
    # 問題2: 大阪府の全ての駅名をカンマ区切りで出力
    osaka_stations = get_osaka_stations(weather_information)
    print(f"大阪府の駅: {', '.join(osaka_stations)}")
    # 問題3: 福岡県の平均気温を計算
    fukuoka_avg = calculate_fukuoka_avg(weather_information)
    print(f"福岡県の平均気温: {fukuoka_avg:.1f}℃")


# 全国の平均気温を計算
def calculate_national_avg(data):
    total_temp = sum(item["temperature"] for item in data)
    count = len(data)
    return total_temp / count


# 大阪府の全ての駅名を取得
def get_osaka_stations(data):
    return [item["station"] for item in data if item["prefecture"] == "大阪府"]


# 福岡県の平均気温を計算
def calculate_fukuoka_avg(data):
    fukuoka_data = [item["temperature"] for item in data if item["prefecture"] == "福岡県"]
    total_temp = sum(fukuoka_data)
    count = len(fukuoka_data)
    return total_temp / count


# メイン関数の呼び出し
if __name__ == "__main__":
    main()
