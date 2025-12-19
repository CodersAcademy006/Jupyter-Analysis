import matplotlib.pyplot as plt
import seaborn as sns

def plot_missingness_heatmap(df):
    """Plot missingness heatmap for vital signs."""
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title('Missingness Heatmap')
    plt.show()
