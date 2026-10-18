import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X_arr = np.array(X, dtype=float)
    y_arr = np.array(y, dtype=float)
    
    XtX = X_arr.T @ X_arr
    Xty = X_arr.T @ y_arr
    
    theta = np.linalg.inv(XtX) @ Xty
    
    theta_rounded = [round(float(val), 4) for val in theta]
    
    return theta_rounded