import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
#Simulateing random walk 1000 times to get better result
all_walks = []
for T in range(1000) :
    walk = [0]
    for x in range(100) :
        step = walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        walk.append(step)
    all_walks.append(walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

end = np_aw_t[-1,:]
plt.hist(end)
plt.show()
