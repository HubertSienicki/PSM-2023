import numpy as np
import matplotlib.pyplot as plt

eq = lambda arr: np.array([10 * (arr[1] - arr[0]), -arr[0] * arr[2] + 25 * arr[0] - arr[1], arr[0] * arr[1] - 8 / 3 * arr[2]])

def calc(f, initial, dt, start, end, method):
    time = np.arange(start, end, dt)
    res = np.zeros((len(time), len(initial)))
    res[0] = initial

    for i in range(1, len(time)):
        if method == 'euler':
            res[i] = res[i - 1] + dt * f(res[i - 1])
        elif method == 'midpoint':
            k1 = dt * f(res[i - 1])
            k2 = dt * f(res[i - 1] + 0.5 * k1)
            res[i] = res[i - 1] + k2
        elif method == 'rk4':
            k1 = dt * f(res[i - 1])
            k2 = dt * f(res[i - 1] + 0.5 * k1)
            k3 = dt * f(res[i - 1] + 0.5 * k2)
            k4 = dt * f(res[i - 1] + k3)
            res[i] = res[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return time, res

initial = np.array([1, 1, 1])
t_start = 0
t_end = 100

methods = ['euler', 'midpoint', 'rk4']
outputs = [calc(eq, initial, 0.03, t_start, t_end, method) for method in methods]

fig, axs = plt.subplots(3, figsize=(8, 18))

for i, method in enumerate(methods):
    axs[i].plot(outputs[i][1][:, 0], outputs[i][1][:, 2], label=method.capitalize(), alpha=0.7)
    axs[i].set(xlabel='x', ylabel='z', title=method.capitalize())
    axs[i].grid()

plt.legend()
plt.show()
