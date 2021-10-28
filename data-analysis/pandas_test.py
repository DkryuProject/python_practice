import pandas as pd

# 리스트로 생성하기
data1 = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df1 = pd.DataFrame(data1, columns=['학번', '이름', '점수'])

print(df1)

# 딕셔너리로 생성하기
data2 = { 
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
}

df2 = pd.DataFrame(data2)
print(df2)