def arrysort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x
x = np.array([2, 1, 4, 3, 5])
arrysort(x)

