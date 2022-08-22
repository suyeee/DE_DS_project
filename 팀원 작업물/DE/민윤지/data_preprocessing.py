import os
import pandas as pd
import numpy as np

# 여러 csv 파일 불러온 후, 합치기
nums = range(1,4)

train_data = pd.DataFrame()
for num in nums:
  path = '/content/drive/MyDrive/mc_final_project/train_data_500(%d).csv'%num
  data = pd.read_csv(path)
  train_data = pd.concat([train_data, data])

# 필요컬럼 추리기file_name = 'sample_data.xlsx'
result = train_data[['시간','지점명','기온','강수량','풍속','풍향','습도']]
result

# 엑셀파일로 저장
file_name = 'train_data.xlsx'
result.to_excel(file_name)
