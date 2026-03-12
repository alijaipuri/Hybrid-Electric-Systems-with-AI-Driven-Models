import matplotlib.pyplot as plt
import numpy as np

scores = np.random.randn(100).cumsum()

plt.plot(scores)
plt.title("RL Performance")
plt.xlabel("Episode")
plt.ylabel("Score")
plt.show()
