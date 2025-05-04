from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Simulated training data: [stamina, dist_to_treasure, dist_to_hideout, knight_nearby (1/0)]
X = np.array([
    [90, 2, 5, 0],  # go for treasure
    [40, 2, 1, 1],  # return to hideout
    [10, 5, 1, 0],  # rest
    [70, 1, 4, 1],  # avoid knight
    [95, 1, 5, 0],  # go for treasure
    [15, 4, 2, 1],  # rest
    [30, 1, 1, 1],  # return
])

# Labels: 0 = rest, 1 = go to treasure, 2 = return to hideout, 3 = avoid knight
y = np.array([1, 2, 0, 3, 1, 0, 2])

model = DecisionTreeClassifier()
model.fit(X, y)

# Decision function to use in-game
def decide_action(stamina, dist_to_treasure, dist_to_hideout, knight_nearby):
    input_data = np.array([[stamina, dist_to_treasure, dist_to_hideout, knight_nearby]])
    return model.predict(input_data)[0]
