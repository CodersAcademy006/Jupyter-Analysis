import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

def plot_calibration_curve(y_true, y_pred):
    """Plot calibration curve for predicted risk."""
    prob_true, prob_pred = calibration_curve(y_true, y_pred, n_bins=10)
    plt.plot(prob_pred, prob_true, marker='o')
    plt.plot([0, 1], [0, 1], linestyle='--')
    plt.xlabel('Predicted Risk')
    plt.ylabel('Actual Risk')
    plt.title('Calibration Curve')
    plt.show()
