import math

# nokta tanımlama
points = [(1, 2), (4, 6), (5, 8), (9, 1), (3, 3)]

# fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# mesafe hesabı
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# min mesafe bulunması
min_distance = min(distances)

# sonuc
print("Hesaplanan Mesafeler: ", distances)
print("Minimum Mesafe: ", min_distance)
