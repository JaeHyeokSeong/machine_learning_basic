# 경사 하강법 (Gradient Descent)

import matplotlib.pylab as plt
import pandas as pd
from sklearn.model_selection import train_test_split
# SGD : Stochastic Gradient Descent (확률적 경사 하강법)
from sklearn.linear_model import SGDRegressor

dataset = pd.read_csv("LinearRegressionData.csv")

# 독립 변수
X = dataset.iloc[:, :-1].values
# 종속 변수
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 확률적 경사 하강법을 위한 객체 생성
# max_iter : 훈련 세트 반복 횟수 (Epoch 횟수)
# eta0 : 학습률 (learning rate)

# 지수 표기법
# 1e-3 : 0.001 (10^-3)
# 1e-4 : 0.0001 (10^-4)
# 1e+3 : 1000 (10^3)
# 1e+4 : 10000 (10^4)
# sr = SGDRegressor(max_iter=1000, eta0=1e-4, verbose=1)
sr = SGDRegressor()
sr.fit(X_train, y_train)

# data 시각화
# 산점도 그래프
plt.scatter(X_train, y_train, color="blue")
# 선 그래프
plt.plot(X_train, sr.predict(X_train), color="green")
# title
plt.title("Score by Hours (train data, SGD)")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

# 훈력 세트를 통한 모델 평가
score = sr.score(X_train, y_train)
print(score)
