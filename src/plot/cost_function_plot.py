import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def compute_j_grid(h, theta0_grid, theta1_grid, cost_function, C=1, regularization=None):
    if regularization is None:
        penalty = lambda x: (x * 0).sum()
    elif regularization == 'L1':
        penalty = lambda x: C*np.abs(x)[:, 1:].sum() / len(h.y)
    elif regularization == 'L2':
        penalty = lambda x: C * np.square(x)[:, 1:].sum() / (len(h.y)*2)

    grid = []
    for theta0 in theta0_grid:
        row = []
        for theta1 in theta1_grid:
            w = np.array([[theta0], [theta1]])
            y_pred = h.hypothesis(w=w)
            elem = cost_function.get_loss(y_pred, h.y) + penalty(w)
            row.append(elem)
        grid.append(row)
    return np.array(grid)


def cost_function_plot_2d(h, properties, loss_history, weights_history):
    if h.X.shape[1] != 2 and len(weights_history) > 2:
        return

    x = h.X[:, 1]
    y = list(map(lambda x: x[0], h.y))

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,6.15))

    theta = [np.array([i[0][0], i[1][0]]) for i in weights_history]

    theta0 = [i[0] for i in weights_history]
    theta1 = [i[1] for i in weights_history]

    thetha0_min = np.min(theta0) - 3*np.std(theta0)
    thetha0_max = np.max(theta0) + 3*np.std(theta0)

    thetha1_min = np.min(theta1) - 3*np.std(theta1)
    thetha1_max = np.max(theta1) + 3*np.std(theta1)

    theta0_grid = np.linspace(thetha0_min, thetha0_max, 101)
    theta1_grid = np.linspace(thetha1_min, thetha1_max, 101)

    J_grid = compute_j_grid(h, theta0_grid, theta1_grid, properties.cost_function, C=properties.reg_coef, regularization=properties.regularization)

    X, Y = np.meshgrid(theta0_grid, theta1_grid)
    contours = ax.contour(X, Y, J_grid, 30)

    ax.clabel(contours)
    for j in range(2,len(theta)):
        ax.annotate('', xy=theta[j], xytext=theta[j-1],
                    arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                    va='center', ha='center')

    ax.set_xlabel(r'$w_0$')
    ax.set_ylabel(r'$w_1$')
    ax.set_title('Cost function')

    plt.show()
    st.pyplot()