from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Features: [stamina, dist_to_hunter, hunter_stealth (0/1), hunter_wealth, is_adjacent (0/1)]
X = np.array([
    [100, 3, 0, 30, 0],  # patrol
    [95, 1, 0, 50, 1],   # detain
    [80, 2, 0, 40, 0],   # chase
    [50, 1, 1, 20, 1],   # detain
    [20, 2, 0, 0, 0],    # rest
    [10, 5, 1, 0, 0],    # rest
    [70, 1, 1, 10, 1],   # detain
    [90, 4, 0, 0, 0],    # patrol
    [60, 2, 0, 5, 0],    # chase
    [30, 1, 1, 0, 1],    # detain
    [100, 5, 0, 0, 0],   # patrol
    [85, 3, 1, 25, 0],   # chase
    [100, 1, 0, 60, 1],  # detain
    [95, 0, 1, 50, 1],   # detain
    [40, 4, 0, 10, 0],   # rest
    [100, 3, 0, 0, 0],   # patrol
])

y = np.array([
    1, 3, 2, 3, 0, 0, 3, 1, 2, 3, 1, 2, 3, 3, 0, 1
])

model = DecisionTreeClassifier()
model.fit(X, y)

def decide_knight_action(stamina, dist_to_hunter, hunter_stealth, hunter_wealth, is_adjacent):
    input_data = np.array([[stamina, dist_to_hunter, hunter_stealth, hunter_wealth, is_adjacent]])
    return model.predict(input_data)[0]  # 0=rest, 1=patrol, 2=chase, 3=detain, 4=return
