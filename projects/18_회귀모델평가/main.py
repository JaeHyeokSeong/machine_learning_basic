# 18 회귀 모델 평가 실습

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

dataset = pd.read_csv("MultipleLinearRegressionData.csv")

# 독립 변수
# dataset.iloc[row, column]
X = dataset.iloc[:, :-1].values
# 종속 변수
y = dataset.iloc[:, -1].values

# 표에서 place column 이 숫자가 아닌 문자로 작성 되어져 있다. 이를 기계에게 학습 시키기 위해서는
# 문자를 숫자로 변영 시켜줘야 한다
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(drop="first"), [2])], remainder="passthrough")
X = ct.fit_transform(X)

# data set 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 다중 선형 회귀 (학습 시키기)
reg = LinearRegression()
reg.fit(X_train, y_train)

# X_test 입력에 대한 예측값 predict
y_predict = reg.predict(X_test)

# MAE (Mean Absolute Error) : (실제 값과 예측 값) 차이의 절대값
# MSE (Mean Squared Error) : (실제 값과 예측 값) 차이의 제곱
# RMSE (Root Mean Squared Error) : (실제 값과 예측 값) 차이의 제곱의 루트
# R^2 : 결정 계수

# R^2 는 1에 가까울 수록, 나머지는 0에 가까울수록 좋은 모델임

mark = mean_absolute_error(y_test, y_predict)
print(f"MAE (Mean Absolute Error) : {mark}")

mark = mean_squared_error(y_test, y_predict)
print(f"MSE (Mean Squared Error) : {mark}")

mark = mean_squared_error(y_test, y_predict, squared=False)
print(f"RMSE (Root Mean Squared Error) : {mark}")

mark = r2_score(y_test, y_predict)
print(f"R^2 (결정 계수) : {mark}")
