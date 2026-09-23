import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    arr = np.asarray(arr)

    # Validate array dimensions
    if arr.ndim not in (1, 2):
        raise ValueError(f"Input array must be 1D or 2D, got {arr.ndim}D array.")

    match norm_type:
        case 'l1':
            return float(np.sum(np.abs(arr)))
        case 'l2':
            return float(np.sqrt(np.sum(np.square(arr))))
        case 'linf':
            return float(np.max(np.abs(arr)))
        case 'frobenius':
            if arr.ndim != 2:
                raise ValueError("Frobenius norm requires a 2D array (matrix).")
            return float(np.sqrt(np.sum(np.square(arr))))
        case _:
            raise ValueError(
                f"Unsupported norm_type: {norm_type!r}. "
                "Must be one of 'l1', 'l2', 'linf', or 'frobenius'."
            )