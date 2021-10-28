# 넘파이(Numpy)는 수치 데이터를 다루는 파이썬 패키지
import numpy as np

#리스트를 가지고 1차원 배열 생성
# a = np.array([1, 2, 3, 4, 5])
# print(type(a))
# print(a)

# b = np.array([[10, 20, 30], [ 60, 70, 80]]) 
# print(b)

# 모든값이 0인 2x3 배열 생성
# a = np.zeros((2,3)) .
# print(a)

# 모든값이 1인 2x3 배열 생성.
# a = np.ones((2,3)) 
# print(a)

# 모든 값이 특정 상수인 배열 생성. 이 경우에는 7.
# a = np.full((2,2), 7) 
# print(a)

# 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성.
# a = np.eye(3)
# print(a)

# 임의의 값으로 채워진 배열 생성
# a = np.random.random((2,2)) 
# print(a)

# 0부터 10까지
# a = np.arange(10)
# print(a)

# 1부터 9까지 +2씩 적용되는 범위
# a = np.arange(1, 10, 2)
# print(a)

# 0부터 n-1 까지의 숫자를 생성 reshape()를 통해 배열을 생성
# a = np.array(np.arange(30)).reshape((5,6))
# print(a)

# slice 처리
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = a[0:2, 0:2]
# print(b)

# indexing
# a = np.array([[1,2], [4,5], [7,8]])
# b = a[[2, 1],[1, 0]] # a[[row2, row1],[col1, col0]]을 의미함.
# print(b)

# 연산
# x = np.array([1,2,3])
# y = np.array([4,5,6])

# b = x + y # 각 요소에 대해서 더함
# # b = np.add(x, y)와 동일함
# print(b)

# 행렬곱
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.dot(a, b)
print(c)