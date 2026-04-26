import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, col):
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()


def plot_pie_chart(df, col):
    df[col].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title(f'Pie chart of {col}')
    plt.show()
