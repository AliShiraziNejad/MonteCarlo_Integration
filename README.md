Examples:
_________________________
def function(point):
    x1, x2, x3, x4 = point
    return np.exp(-(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2))

limits = [[-5, 5], [-5, 5], [-5, 5], [-5, 5]]
_________________________
def function(point):
    x1 = point
    return np.exp(-(x1 ** 2))

limits = [[-5, 5]]
_________________________
def function(point):
    x, y = point
    mu_x, mu_y = 0, 0
    sigma_x, sigma_y = 1, 1

    normalization = 1 / (2 * np.pi * sigma_x * sigma_y)
    exponent = -((x - mu_x) ** 2 / (2 * sigma_x ** 2) + (y - mu_y) ** 2 / (2 * sigma_y ** 2))

    return normalization * np.exp(exponent)

limits = [[-5, 5], [-5, 5]]
_________________________
def function(point):
    x = point

    result = x * np.sin(x ** 2)

    return result

limits = [[-2, 15]]
