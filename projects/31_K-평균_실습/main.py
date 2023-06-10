import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

dataset = pd.read_csv("KMeansData.csv")

# 비지도 학습에서는 종속변수가 없다 왜냐하면 비지도 학습이기 때문에 정답이 없기 때문이다.
# 따라서 X를 기준으로 하여서 비슷한 성격을 가진 요소들끼리 그룹을 만들어지는 기법을 clustering
# 이라고 한다.
X = dataset.iloc[:, :].values

# data 시각화
# 산점도 그래프 그리기
plt.scatter(X[:, 0], X[:, -1], color="blue")
plt.title("Score by Hours")
plt.xlabel("hour")
plt.ylabel("score")
plt.show()

# 위의 그래프에서 볼수 있다시피 hour feature는 범위가 0~10 이고, score feature는
# 0~100 사이의 범위를 가지고 있다, 즉 다시 말해서 두 features 들의 범위가 다르다는 소리이다.
# 따라서 모델을 학습시킬때 feature들 간의 크기가 다른다면 이를 통합 시켜줘야지만 올바른 모델을
# 얻을 수 가 있다.

# Feature Scaling 하기
sc = StandardScaler()
X = sc.fit_transform(X)
print(X)

# 산점도 그래프 다시 그려보기
plt.scatter(X[:, 0], X[:, -1], color="green")
plt.title("Score by Hours (After Scaling)")
plt.xlabel("hour")
plt.ylabel("score")
plt.show()

# 최적의 K 값 찾기 with (엘보우 방식 Elbow Method)
inertia_list = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", n_init=1)
    kmeans.fit(X)
    # 각 노드들로 부터 클러스터의 중심(centroid) 까지의 제곱의 합 : kmeans.inertia_
    inertia_list.append(kmeans.inertia_)

# 각 노드들로 부터 클러스터의 중심까지의 제곱의 합 데이터를 시각화 하기
plt.plot(range(1, 11), inertia_list)
plt.title("Elbow Method")
plt.xlabel("n_clusters")
plt.ylabel("inertia")
plt.show()

# 최적의 k 값은 4임을 위에서 생성된 그래프를 통해서 알수 있음. 이때 k를 선정할때 기울기가 완만하게
# 떨어지는 k 값을 잡아주면 된다
k = 4
kmeans = KMeans(n_clusters=k, init="k-means++", n_init=1)
kmeans.fit(X)
y_means = kmeans.predict(X)
print(y_means)

# y_means data 시각화 하기
centers = kmeans.cluster_centers_
print(centers)

for cluster in range(k):
    plt.scatter(X[y_means == cluster, 0], X[y_means == cluster, 1], edgecolors="black")
    plt.scatter(centers[cluster, 0], centers[cluster, 1], s=200, edgecolors="black", color="yellow", marker="s")
    plt.text(centers[cluster, 0], centers[cluster, 1], cluster, va="center", ha="center")
plt.title("Score by Hours")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()

# 데이터 시각화 (스케일링 원복)
X_org = sc.inverse_transform(X)
centers_org = sc.inverse_transform(centers)

for cluster in range(k):
    plt.scatter(X_org[y_means == cluster, 0], X_org[y_means == cluster, 1], edgecolors="black")
    plt.scatter(centers_org[cluster, 0], centers_org[cluster, 1], s=200, edgecolors="black", color="yellow", marker="s")
    plt.text(centers_org[cluster, 0], centers_org[cluster, 1], cluster, va="center", ha="center")

plt.title("Score by Hours")
plt.xlabel("hours")
plt.ylabel("score")
plt.show()