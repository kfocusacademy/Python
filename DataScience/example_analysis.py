"""Small example analysis using the Iris dataset.
Saves a scatter plot to DataScience/iris_scatter.png and prints basic info.
"""
import os

try:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')  # non-interactive backend suitable for servers
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
except Exception as e:
    print("Missing dependencies or import error:", e)
    print("Install required packages: pip install -r requirements.txt")
    raise

OUT_DIR = os.path.join(os.path.dirname(__file__))
PLOT_PATH = os.path.join(OUT_DIR, 'iris_scatter.png')


def main():
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    # Basic info
    print('Dataset target names:', iris.target_names)
    print('Data shape:', df.shape)
    print(df.head())

    # Scatter plot: sepal length vs sepal width colored by species
    plt.figure(figsize=(6, 4))
    species = df['target']
    x = df['sepal length (cm)']
    y = df['sepal width (cm)']
    scatter = plt.scatter(x, y, c=species, cmap='viridis', alpha=0.8)
    plt.xlabel('Sepal length (cm)')
    plt.ylabel('Sepal width (cm)')
    plt.title('Iris: Sepal length vs Sepal width')
    legend1 = plt.legend(*scatter.legend_elements(), title='species')
    plt.gca().add_artist(legend1)
    plt.tight_layout()

    plt.savefig(PLOT_PATH)
    print(f'Wrote plot to: {PLOT_PATH}')


if __name__ == '__main__':
    main()
