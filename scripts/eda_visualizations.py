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


def plot_boxplot(df, x_col, y_col):
    sns.boxplot(x=x_col, y=y_col, data=df)
    plt.title(f'Boxplot of {y_col} by {x_col}')
    plt.show()
