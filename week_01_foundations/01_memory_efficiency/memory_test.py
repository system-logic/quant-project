import numpy as np

# Размер массива
N = 1_000_000

# Создаём массивы с разными типами данных
dtypes = [np.float64, np.float32, np.int16, np.uint8]

for dtype in dtypes:
    arr = np.ones(N, dtype=dtype)  # или np.arange(N, dtype=dtype)
    print(f"dtype: {dtype.__name__:>8} | nbytes: {arr.nbytes:>10,} bytes ({arr.nbytes / 1024**2:.2f} MB)")