# Logistic Regression
# 공부 시간에 따른 자격증 시험 합격 가능성

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv("LogisticRegressionData.csv")
# 독립 변수
X = dataset.iloc[:, :-1].values
# 종속 변수
y = dataset.iloc[:, -1].values

# data train set 그리고 test set 으로 분리하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

# Logistic Regression (로지스틱회귀 모델을 사용하여서 학습시키기)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# 6시간 공부 하였을때 합격여부 예측해보기
result = classifier.predict([[6]])
probability = classifier.predict_proba([[6]])
print(f"6 hours study result : {result}, probability [Fail, Pass] : {probability}")

# 4시간 공부 하였을때 합격여부 예측해보기
result = classifier.predict([[4]])
probability = classifier.predict_proba([[4]])
print(f"4 hours study result : {result}, pass probability [Fail, Pass] : {probability}")

# model 평가하기
y_pred = classifier.predict(X_test)
print(f"예측값 : {y_pred}")
print(f"실제값 : {y_test}")
print(f"공부시간 : {X_test}")

print(f"score : {classifier.score(X_test, y_test)}")

# data 시각화 진행하기 (Train Set, Test Set)
X_range = np.arange(min(X), max(X), 0.1)
# p = 1 / (1 + e^-y) 이때 y = mx + b 이다
# p = 1 / (1 + np.exp(-(m * X_range + b)))
p = 1 / (1 + np.exp(-(classifier.coef_ * X_range + classifier.intercept_)))
p = np.reshape(p, -1)

plt.scatter(X_train, y_train, color="blue")
plt.scatter(X_test, y_test, color="orange")
plt.plot(X_range, p, color="green")
plt.plot(X_range, np.full(len(X_range), 0.5), color="red")
plt.title("Probability by Hours")
plt.xlabel("hours")
plt.ylabel("Pass Probability")
plt.show()

# 혼동 행렬 (Confusion Matrix)
cm = confusion_matrix(y_test, y_pred)

# [cm 출력 형태]
# True Negative    False Positive
# 불합격일거야 (예측)   합격일거야 (예측)
# 불합격     (실제)   불합격    (실제)

# False Negative   True Positive
# 불합격일거야 (예측)   합격일거야 (예측)
# 합격      (실제)   합격      (실제)

# |------|
# | 1  2 |   [cm 출력 형태에서 위치 1, 4 는 정확하게 예측한 수를 의미하는
# | 3  4 |   것 이고 위치 2, 3 은 부정확하게 예측한 것을 의미하는 것이다.]
# |------|

print(cm)