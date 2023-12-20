import pandas as pd

# 讀取 CSV 檔案
csv_data = pd.read_csv("111年偏鄉學校.csv", sep=",", encoding='big5')

# 將 DataFrame 寫入 JSON 檔案
csv_data.to_json("school.json", orient="index", force_ascii=False, indent=2)
