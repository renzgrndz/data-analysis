import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("Input list must contain exactly 9 elements.")
    
    # Convert list into a 3x3 matrix
    list = np.array(list).reshape(3, 3)
    
    # Print matrix for debugging
    print("Matrix:\n", list)

    # Calculate mean, variance, std dev, max, min, and sum
    calculations = {
        'mean': {
            'overall': np.mean(list),
            'rows': np.mean(list, axis=1).tolist(),
            'columns': np.mean(list, axis=0).tolist()
        },
        'variance': {
            'overall': np.var(list),
            'rows': np.var(list, axis=1).tolist(),
            'columns': np.var(list, axis=0).tolist()
        },
        'std_dev': {
            'overall': np.std(list),
            'rows': np.std(list, axis=1).tolist(),
            'columns': np.std(list, axis=0).tolist()
        },
        'max': {
            'overall': np.max(list),
            'rows': np.max(list, axis=1).tolist(),
            'columns': np.max(list, axis=0).tolist()
        },
        'min': {
            'overall': np.min(list),
            'rows': np.min(list, axis=1).tolist(),
            'columns': np.min(list, axis=0).tolist()
        },
        'sum': {
            'overall': np.sum(list),
            'rows': np.sum(list, axis=1).tolist(),
            'columns': np.sum(list, axis=0).tolist()
        },
    }

    # Print calculations for debugging
    print("Calculations:\n", calculations)

    return calculations
