import numpy as np
import MCI


def function(point):
    x1, x2, x3, x4 = point
    return np.exp(-(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2))


limits = [[-5, 5], [-5, 5], [-5, 5], [-5, 5]]
n_sims = 2 ** 20

result_QMC = MCI.monte_carlo_integration_qmc(function, limits, n_sims)
print("QMC Monte Carlo Integration Result:", result_QMC)
