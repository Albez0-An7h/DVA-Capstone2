import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, col):
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()
