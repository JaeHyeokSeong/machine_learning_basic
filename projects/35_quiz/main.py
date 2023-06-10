import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("QuizData.csv")
total = dataset.iloc[:, :-1].values
reception = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(total, reception, test_size=0.25, random_state=0)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

plt.scatter(X_train, y_train, color="blue")
plt.plot(X_train, lr_model.predict(X_train), color="green")
plt.title("wedding reception (train)")
plt.xlabel("total")
plt.ylabel("reception")
plt.show()

plt.scatter(X_test, y_test, color="blue")
plt.plot(X_train, lr_model.predict(X_train), color="green")
plt.title("wedding reception (test)")
plt.xlabel("total")
plt.ylabel("reception")
plt.show()

train_set_score = lr_model.score(X_train, y_train)
test_set_score = lr_model.score(X_test, y_test)
print(f"train set score : {train_set_score}")
print(f"test set score : {test_set_score}")

total_reception = 300
expected_reception = int(np.round(lr_model.predict([[total_reception]])))
print(f"결혼식 참석 인원 {total_reception} 명에 대한 예상 식수 인원은 {expected_reception} 명 입니다.")
