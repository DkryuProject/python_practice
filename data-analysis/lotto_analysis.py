from pymongo import MongoClient
import pandas as pd

#DB에서 로또 정보 읽어오기
client = MongoClient('localhost', 27017)

db = client["test"]
collections = db["lotto"]

lotto_list = collections.find({}, {"_id": False})

df = pd.DataFrame(lotto_list)

df_num = df[['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'bonus']]
#print(df_num)

# 최빈값 가져오기
pd.options.display.float_format = '{:,.5}'.format  # 깔끔하게 나오게 하기 위해
for i in range(1, 8):
    if i == 7:
      print(f'보너스 번호 최빈값 : {df_num.iloc[:,i-1].mode().values}')
    else:  
      print(f'{i} 번 번호 최빈값 : {df_num.iloc[:,i-1].mode().values}')

print(df_num.describe())
