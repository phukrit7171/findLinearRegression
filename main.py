# Import numpy
import numpy as np
# Define the input and output variables
x = np.array(list(map(float, input("input x : ").split())))
y = np.array(list(map(float, input("input y : ").split())))
# Perform linear regression with polyfit
coeffs = np.polyfit(x, y, deg=1)
# Print the coefficients
print(coeffs)