import matplotlib.pyplot as plt

x = list(range(1, 9))
nums = [10, 540, 3623, 4045, 1380, 318, 68, 16]


plt.bar(x, nums, color = 'green')
plt.xlabel('guesses')
plt.ylabel('frequency')
plt.savefig('exemple/graph.jpg')