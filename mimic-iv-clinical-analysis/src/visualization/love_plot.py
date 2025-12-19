import matplotlib.pyplot as plt

def plot_love(df_before, df_after, covariates):
    """Plot Love plot for covariate balance before and after PSM."""
    plt.figure(figsize=(8, 6))
    for cov in covariates:
        plt.plot([0, 1], [df_before[cov].mean(), df_after[cov].mean()], marker='o', label=cov)
    plt.xticks([0, 1], ['Before', 'After'])
    plt.ylabel('Mean Covariate Value')
    plt.title('Love Plot: Covariate Balance')
    plt.legend()
    plt.show()
