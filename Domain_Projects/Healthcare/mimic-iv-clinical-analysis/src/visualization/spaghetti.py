import matplotlib.pyplot as plt
import numpy as np

def plot_spaghetti(df, group_col, value_col, time_col):
    """Plot spaghetti plot with confidence intervals for vital sign trajectories."""
    groups = df[group_col].unique()
    for group in groups:
        group_df = df[df[group_col] == group]
        plt.plot(group_df[time_col], group_df[value_col], label=f'{group}')
        mean = group_df[value_col].mean()
        std = group_df[value_col].std()
        plt.fill_between(group_df[time_col], mean-std, mean+std, alpha=0.2)
    plt.legend()
    plt.title('Vital Sign Trajectories')
    plt.show()
