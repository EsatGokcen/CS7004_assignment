from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Features: [stamina, dist_to_hunter, hunter_wealth]
X = np.array([
    [100, 5, 0],  # patrol
    [90, 3, 10],  # patrol
    [80, 2, 20],  # chase
    [70, 1, 50],  # chase
    [60, 1, 30],  # chase
    [50, 3, 5],   # patrol
    [40, 2, 0],   # chase
    [30, 3, 0],   # patrol
    [20, 2, 0],   # retreat
    [10, 1, 0],   # retreat
    [90, 2, 50],  # chase
    [85, 4, 10],  # patrol
    [65, 1, 25],  # chase
    [25, 3, 10],  # retreat
    [100, 4, 0],  # patrol
    [95, 2, 15],  # chase
    [75, 1, 30],  # chase
    [35, 2, 0],   # chase
    [15, 4, 0],   # retreat
    [60, 3, 0],   # patrol
    [70, 2, 40],  # chase
    [80, 1, 45],  # chase
    [90, 3, 0],   # patrol
    [55, 2, 5],   # chase
    [45, 3, 5],   # patrol
])

y = np.array([
    1, 1, 2, 2, 2, 1, 2, 1, 0, 0,
    2, 1, 2, 0, 1, 2, 2, 2, 0, 1,
    2, 2, 1, 2, 1
])

model = DecisionTreeClassifier()
model.fit(X, y)

def decide_knight_action(stamina, dist_to_hunter, hunter_wealth):
    input_data = np.array([[stamina, dist_to_hunter, hunter_wealth]])
    return model.predict(input_data)[0]  # 0=retreat, 1=patrol, 2=chase