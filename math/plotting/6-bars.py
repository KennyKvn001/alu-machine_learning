#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

persons = ["Farrah", "Fred", "Felicia"]
x = np.arange(len(persons))

plt.bar(x, apples, width=0.5, color="red", label="Apples")
plt.bar(x, bananas, width=0.5, bottom=apples, color="yellow", label="Bananas")
plt.bar(
    x, oranges, width=0.5, bottom=apples + bananas, color="#ff8000", label="Oranges"
)
plt.bar(
    x,
    peaches,
    width=0.5,
    bottom=apples + bananas + oranges,
    color="#ffe5b4",
    label="Peaches",
)

plt.ylabel("Quantity of Fruit", fontsize="small")
plt.title("Number of Fruit per Person", fontsize="small")
plt.xticks(x, persons)
plt.yticks(np.arange(0, 81, 10))
plt.legend(loc="upper right", fontsize="small")

plt.show()
