import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def calculate_mean(data):
    return np.mean(data)

def calculate_median(data):
    return np.median(data)

def calculate_mode(data):
    return pd.Series(data).mode().iloc[0]

def calculate_variance(data):
    return np.var(data)

def calculate_std_dev(data):
    return np.std(data)

def main():
    data = [12, 15, 18, 20, 22, 25, 30]
    
    print("Dataset:", data)

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data)
    std_dev = calculate_std_dev(data)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)

    X = np.array(data).reshape(-1, 1)  
    y = np.array([1, 2, 3, 4, 5, 6, 7]) 

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    plt.scatter(X, y, color='blue', label='Data Points')
    plt.plot(X, predictions, color='red', label='Regression Line')
    plt.title('Linear Regression Example')
    plt.xlabel('Data Values')
    plt.ylabel('Predicted Values')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
