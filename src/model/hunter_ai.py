from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Enhanced dataset with more examples and new feature:
# [stamina, dist_to_treasure, dist_to_hideout, knight_nearby (1/0), is_carrying (1/0)]
X = np.array([
    [95, 1, 5, 0, 0], [90, 2, 4, 0, 0], [80, 1, 6, 1, 0], [70, 2, 3, 1, 0],
    [60, 4, 2, 1, 1], [50, 3, 1, 1, 1], [40, 2, 1, 0, 1], [30, 2, 2, 0, 1],
    [20, 3, 1, 0, 0], [10, 5, 1, 0, 0], [15, 1, 2, 1, 0],
    [85, 1, 6, 1, 0], [45, 3, 2, 0, 1], [25, 2, 2, 1, 0], [35, 3, 3, 1, 0],
    [90, 1, 4, 1, 0], [70, 1, 3, 0, 0], [15, 2, 1, 1, 0],
    [55, 2, 4, 1, 1], [65, 1, 4, 1, 0],
    [95, 1, 5, 0, 1], [80, 3, 2, 0, 1], [75, 2, 1, 0, 1],
    [25, 4, 2, 1, 1], [15, 1, 1, 1, 1], [85, 1, 5, 0, 1],
    [45, 1, 1, 0, 1], [35, 1, 1, 0, 1], [65, 1, 1, 0, 1],
    [90, 2, 3, 1, 0], [40, 4, 1, 0, 0], [55, 2, 3, 1, 0],
    [20, 3, 4, 1, 0], [30, 3, 3, 1, 0], [70, 2, 4, 0, 0],
    [80, 1, 2, 0, 0], [60, 1, 2, 1, 1], [50, 2, 3, 1, 1],
    [25, 2, 2, 1, 1], [10, 1, 1, 1, 1]
])

y = np.array([
    1, 1, 1, 1,
    2, 2, 2, 2,
    0, 0, 0,
    1, 2, 3, 3,
    1, 1, 0,
    2, 1,
    2, 2, 2,
    0, 0, 2,
    2, 2, 2,
    1, 2, 2,
    0, 3, 1,
    1, 2, 2,
    3, 0
])

model = DecisionTreeClassifier()
model.fit(X, y)

def decide_action(stamina, dist_to_treasure, dist_to_hideout, knight_nearby, is_carrying):
    input_data = np.array([[stamina, dist_to_treasure, dist_to_hideout, knight_nearby, is_carrying]])
    return model.predict(input_data)[0]