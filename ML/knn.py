import matplotlib.pyplot as plt

x = [15, 18, 12, 8, 21, 45, 24, 19, 23, 8, 5]
y = [12, 6, 3, 18, 12, 19, 28, 54, 11, 17, 15]
classes = [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0]

plt.scatter(x, y, c=classes)
#plt.show()

from sklearn.neighbors import KNeighborsClassifier

data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(data, classes)

new_x = 48
new_y = 21
new_point = [(new_x, new_y)]

predicted = knn.predict(new_point)
plt.scatter(x+[new_x], y+[new_y], c=classes+[predicted[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new,class = {predicted[0]}")
plt.show()