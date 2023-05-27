# Multiple Linear Regression (다중 선형 회귀)
# 원-핫 인코딩

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("MultipleLinearRegressionData.csv")

# 독립 변수
# dataset.iloc[row, column]
X = dataset.iloc[:, :-1].values
# 종속 변수
y = dataset.iloc[:, -1].values

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(drop="first"), [2])], remainder="passthrough")
X = ct.fit_transform(X)

# data set 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 다중 선형 회귀 (학습 시키기)
reg = LinearRegression()
reg.fit(X_train, y_train)

# 예측값 그리고 실제값 비교하기 (테스트 세트을 이용해서)
y_predict = reg.predict(X_test)

# 계수값 그리고 y 절편값 확인하기
m = reg.coef_
y_intercept = reg.intercept_

# 방정식 출력
print(f"y = {y_intercept} ", end="")
for m_ in m:
    print(f"+ {m_}x ", end="")
print()

# model 평가
score = reg.score(X_train, y_train)
print(score)
score = reg.score(X_test, y_test)
print(score)
