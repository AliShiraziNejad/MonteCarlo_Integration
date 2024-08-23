import numpy as np
from scipy.stats.qmc import Sobol
import time

def monte_carlo_integration(func, bounds, num_samples):
    start_time = time.time()

    dim = len(bounds)
    volume = np.prod([bound[1] - bound[0] for bound in bounds])

    points = np.random.uniform(0, 1, (num_samples, dim))
    for i in range(dim):
        points[:, i] = bounds[i][0] + (bounds[i][1] - bounds[i][0]) * points[:, i]

    values = np.apply_along_axis(func, 1, points)
    total = np.sum(values)

    time_random = time.time() - start_time
    print(f"Monte Carlo Integration run time: {time_random}")

    return total / num_samples * volume


def monte_carlo_integration_qmc(func, bounds, num_samples):
    start_time = time.time()

    dim = len(bounds)  # determine number of dimensions
    sampler = Sobol(d=dim, scramble=True)  # initializes a Sobol sequence sampler for dim dimensions

    # generates num_samples Sobol sequence points, which are uniformly distributed in the unit cube [0,1]^dim
    sample_points = sampler.random(num_samples)

    # scales the Sobol sequence points from the unit cube [0,1] to the integration bounds
    for i in range(dim):
        sample_points[:, i] = bounds[i][0] + (bounds[i][1] - bounds[i][0]) * sample_points[:, i]

    # Vectorized function evaluation
    func_values = func(sample_points.T)

    # calculates the volume of the integration domain, which is the product of the lengths of each dimension's bounds
    volume = np.prod([bound[1] - bound[0] for bound in bounds])

    # computes the estimated integral by multiplying the mean of the function values by the volume of the domain
    integral = np.mean(func_values) * volume

    time_random = time.time() - start_time
    print(f"QMC Monte Carlo Integration run time: {time_random:.6f} seconds")

    return integral
