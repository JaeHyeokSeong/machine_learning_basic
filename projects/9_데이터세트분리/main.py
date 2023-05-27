import matplotlib.pylab as plt
import pandas as pd
# 훈련 세트 그리고 테스트 세트를 분리하기 위해서 아래를 import 함
from sklearn.model_selection import train_test_split
# 지도학습에서 선형회귀를 이용해서 model을 만들기 위한 import
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("LinearRegressionData.csv")

# dataset.iloc[row, column]
# 독립 변수 가져오기
X = dataset.iloc[:, :-1].values
# 종속 변수 가져오기
y = dataset.iloc[:, -1].values

# 훈련 세트 : X_train, y_train
# 테스트 세트 : X_test, y_test
# test_size=0.2 의미는 훈련 세트 비중을 80% 그리고 테스트 세트 비중을 20%로 사용한다는 의미
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# print(X, len(X))
#
# print(X_train, len(X_train))
#
# print(X_test, len(X_test))

# print(y, len(y))
#
# print(y_train, len(y_train))
#
# print(y_test, len(y_test))

# 분리된 데이터를 통한 모델링
reg = LinearRegression()
# model 만들기
# 훈련 세트를 사용해서 학습 시키기
reg.fit(X_train, y_train)

# data 시각화 (훈련 세트)
# 산점도 그래프
plt.scatter(X_train, y_train, color="blue")
# 선 그래프
plt.plot(X_train, reg.predict(X_train), color="green")
# title
plt.title("Score by Hours (train data)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

# data 시각화 (테스터 세트)
plt.scatter(X_test, y_test, color="blue")
plt.plot(X_train, reg.predict(X_train), color="green")
plt.title("Score by Hours (test data)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

# 학습 시킨 직선 그래프의 길울기 및 y 절편값 보기
m = reg.coef_
y_intercept = reg.intercept_

print(f"y = {m}x + {y_intercept}")

# model 평가
# 테스트 세트를 통한 모델 평가
score = reg.score(X_test, y_test)
print(score)  # (0 ~ 1) 사이

# 훈련 세트를 통한 모델 평가
score = reg.score(X_train, y_train)
print(score)
