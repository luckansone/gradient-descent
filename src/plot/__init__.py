from plot.grid_compute import compute_j_grid, compute_j
from plot.plots_2d import cost_function_plot_2d, loss_plot_2d, data_plot_2d, execution_time_plot_2d
from plot.plots_2d import data_plot_clf_2d, data_plot_clf_1d
from plot.plots_3d import data_plot_3d, cost_function_plot_3d, data_plot_clf_3d


def plot_regression_all(h, properties, weights_history, loss_history, y_pred_history):
    cost_function_plot_2d(h, properties, weights_history)
    cost_function_plot_3d(h, properties, weights_history, loss_history)
    loss_plot_2d(loss_history)
    data_plot_2d(h, y_pred_history)
    data_plot_3d(h, y_pred_history)


def plot_classification_all(h, properties, weights_history, loss_history, y_pred_history):
    cost_function_plot_2d(h, properties, weights_history)
    cost_function_plot_3d(h, properties, weights_history, loss_history)
    loss_plot_2d(loss_history)
    data_plot_clf_1d(h, y_pred_history)
    data_plot_clf_2d(h, y_pred_history)
    data_plot_clf_3d(h, y_pred_history)
