# Import Library 
import numpy as np
import matplotlib.pyplot as plt

def linear_regression():
    x = np.array(list(map(float, input("input x : ").split())))
    y = np.array(list(map(float, input("input y : ").split())))
    # Perform linear regression with polyfit
    coeffs = np.polyfit(x, y, deg=1)
    try:
        # plot garph
        plt.scatter(x, y)
        plt.plot(x, coeffs[0] * x + coeffs[1], color='red')
        plt.show()
    except:
        print("Your device not support GUI or don't have matplotlib")
    # Print the coefficients
    print(coeffs)
linear_regression()