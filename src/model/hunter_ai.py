from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Better balanced training data:
# [stamina, dist_to_treasure, dist_to_hideout, knight_nearby (1/0)]
X = np.array([
    [95, 1, 5, 0],  # go to treasure
    [90, 2, 4, 0],  # go to treasure
    [80, 1, 6, 1],  # go to treasure
    [70, 2, 3, 1],  # go to treasure
    [60, 4, 2, 1],  # return to hideout
    [50, 3, 1, 1],  # return to hideout
    [40, 2, 1, 0],  # return to hideout
    [30, 2, 2, 0],  # return to hideout
    [20, 3, 1, 0],  # rest
    [10, 5, 1, 0],  # rest
    [15, 1, 2, 1],  # rest
    [85, 1, 6, 1],  # go to treasure
    [45, 3, 2, 0],  # return to hideout
    [25, 2, 2, 1],  # avoid knight
    [35, 3, 3, 1],  # avoid knight
    [90, 1, 4, 1],  # go to treasure
    [70, 1, 3, 0],  # go to treasure
    [15, 2, 1, 1],  # rest
    [55, 2, 4, 1],  # return
    [65, 1, 4, 1],  # go to treasure
])

y = np.array([
    1, 1, 1, 1,
    2, 2, 2, 2,
    0, 0, 0,
    1, 2, 3, 3,
    1, 1, 0, 2, 1
])

model = DecisionTreeClassifier()
model.fit(X, y)

def decide_action(stamina, dist_to_treasure, dist_to_hideout, knight_nearby):
    input_data = np.array([[stamina, dist_to_treasure, dist_to_hideout, knight_nearby]])
    return model.predict(input_data)[0]
