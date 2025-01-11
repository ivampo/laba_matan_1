import numpy as np
import matplotlib.pyplot as plt


def metod_dichotomy(func, a, b, eps):
    delta = eps/2 # я посчитал что представленный алгоритм в файле неверный т.к
    # длина отрезка на k-ой итерации равна (b - a - eps)/ 2^k + eps > eps. алгоритм никогда бы не закончился
    iterations = []
    dist_iterations = []
    iterations.append((a + b) / 2)
    dist_iterations.append(b - a)
    while b - a > eps: # округляю иначе питон никогда не выдаст false
        if func((a + b - delta) / 2) <= func((a + b + delta) / 2):
            b = (a + b + delta) / 2
        else:
            a = (a + b - delta) / 2
        dist_iterations.append(b - a)
        iterations.append((a + b) / 2)
    return [(a + b) / 2, iterations, dist_iterations]

def grafik(func, a, b, iterations, dist_iterations):
    x = np.linspace(a, b, int((b - a) * 100))
    y = func(x)
    plt.subplot(2, 1, 1)
    plt.plot(x, y, label='f(x) = x^3 - 3x^2 + 4', color='blue')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Линия x=0
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Линия y=0
    if iterations:
        points_y = func(np.array(iterations))
        plt.scatter(iterations, points_y, color='red', label='Точки', zorder=5)
    plt.title('График функции f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.savefig('function_plot.png', dpi=300, bbox_inches='tight')

    plt.subplot(2, 1, 2)
    x = list(range(1, len(dist_iterations) + 1))
    y = dist_iterations
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Линия через точки')
    plt.title('зависимость длины отрезка от итерации')
    plt.xlabel('итерация')
    plt.ylabel('длина отрезка')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig('function_plot_dist.png', dpi=300, bbox_inches='tight')
    plt.show()

def find_all_roots(func, a, b, step=0.1, eps=0.0000000001):
    def find_root(func, a, b, eps):
        while abs(a - b) > eps:
            c = (a + b) / 2
            if abs(func(c)) < eps:
                return c
            if func(a) * func(c) < 0:
                b = c
            else:
                a = c
        return (a + b) / 2
    roots = []
    x = a
    while x < b:
        next_x = min(x + step, b)
        if func(x) * func(next_x) < 0:
            root = find_root(func, x, next_x, eps)
            if not any(abs(root - r) < eps for r in roots):
                roots.append(root)
        x = next_x
    return roots

def func(x):
    return abs(1 / x - 2)


a, b = 0.25 , 2
s = metod_dichotomy(func, a, b, 0.001)
grafik(func, a, b, s[1], s[2])
