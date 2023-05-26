# linear regression, 선형 회귀 (지도 학습)

# 공부 시간에 따른 시험 점수

import matplotlib.pyplot as plt  # 데이터 시각화를 위해서 사용
import pandas as pd  # 데이터를 편안하게 가공하기 위해서 사용
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("LinearRegressionData.csv")

# 독립 변수 (원인)
# dataset.iloc[row, column]
X = dataset.iloc[:, :-1].values

# 종속 변수 (결과)
Y = dataset.iloc[:, -1].values

# linear regression 을 위한 객체 생성
reg = LinearRegression()
# 독립 변수 그리고 종속 변수을 사용해서 학습시켜서 모델을 만듬
reg.fit(X, Y)

# X 에 대한 예측 값
y_pred = reg.predict(X)
print(y_pred)

# 산점도 그래프
plt.scatter(X, Y, color="blue")
# 선 그래프
plt.plot(X, y_pred, color="green")
plt.title("Score by Hours")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

print(f"\n9시간 공부했을 때 예상 점수 : {reg.predict([[9]])}")

# linear regression graph 기울기 (m)
m = reg.coef_
y_intercept = reg.intercept_
print(m, y_intercept)
# 수식 : y = mx + b
print(f"y = {m}x + {y_intercept}")
