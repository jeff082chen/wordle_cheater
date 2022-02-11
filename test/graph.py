import matplotlib.pyplot as plt

x = list(range(1, 9))
nums = [10, 587, 3855, 4048, 1169, 228, 82, 21]


plt.bar(x, nums, color = 'blue')
plt.xlabel('guesses')
plt.ylabel('frequency')
plt.savefig('exemple/graph.jpg')