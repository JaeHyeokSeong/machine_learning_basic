# Polynomial Regression 다항 회귀
# 공부 시간에 따른 시험 점수 (우등생)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv("PolynomialRegressionData.csv")

# feature
X = dataset.iloc[:, :-1].values
# target
y = dataset.iloc[:, -1].values

# 단순 선형 회귀 (Simple Linear Regression) 을 사용해서 그래프 그리기
reg = LinearRegression()
reg.fit(X, y)

# data 시각화
plt.scatter(X, y, color="blue")
plt.plot(X, reg.predict(X), color="green")
plt.title("Score by hours (honour student)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

# model 평가 (1 에 가까울 수록 좋은 점수)
print(f"Linear Regression Score : {reg.score(X, y)}")

# 다항 회귀 (Polynomial Regression) 을 사용해서 그래프 그리기
poly_reg = PolynomialFeatures(degree=4)
# degree=2 기준 x 를 [x^0, x^1, x^2] 로 변환 해준다
# ex) x = 0.2 이면 [1, 0.2, 0.04] 로 반환 된다
X_poly = poly_reg.fit_transform(X)

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

# data 시각화
plt.scatter(X, y, color="blue")
plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color="green")
plt.title("Score by hours (honour student)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

# 곡선 부드럽게 만들기
X_range = np.arange(min(X), max(X), 0.1)

plt.scatter(X, y, color="blue")
plt.plot(X_range, lin_reg.predict(poly_reg.fit_transform(X_range.reshape(-1, 1))), color="green")
plt.title("Score by hours (honour student)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

print(f"Polynomial Regression Score : {lin_reg.score(poly_reg.fit_transform(X), y)}")

# 공부 시간에 따른 시험 성적 예측
# Linear Regression 을 사용하였을때의 예측값
print(f"2 hours expected score {reg.predict([[2]])} by Linear regression")
# Polynomial Regression 을 사용하였을때의 예측값
print(f"2 hours expected score {lin_reg.predict(poly_reg.fit_transform([[2]]))} by Polynomial Regression")
