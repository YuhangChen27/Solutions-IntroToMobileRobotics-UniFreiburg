import math
from re import X
import numpy as np
import matplotlib.pyplot as plt

class SolutionExercise00(object):
    def __init__(self):
        pass

    @staticmethod
    def function_f(x: np.ndarray):
        return np.sin(x) * np.cos(x)

    def plottting(self, interval, save_dir=None):
        assert isinstance(interval, tuple)
        fig = plt.figure()
        ax = fig.add_subplot()

        x = np.linspace(interval[0], interval[1], 1000)
        ax.plot(x, self.function_f(x))

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        if save_dir is not None:
            plt.savefig(save_dir)

        plt.show()

    def random_generate(self, seed=None, save_dir=None):
        if seed is not None:
            np.random.seed(seed)

        normal_x = np.random.normal(loc=5, scale=2, size=100000)
        uniform_x = np.random.uniform(low=0, high=10, size=100000)

        print('Random normal distribution', 'Mean:', np.mean(normal_x), 'Standard deviation:', np.std(normal_x))
        print('Random uniform distribution', 'Mean:', np.mean(uniform_x), 'Standard deviation:', np.std(uniform_x))

        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)

        ax1.hist(normal_x, 50, density=True)
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_title('Normal distribution of mean 5 std 2')

        ax2.hist(uniform_x, 50, density=True)
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        ax2.set_title('Uniform distribution from 0 to 10')

        plt.tight_layout()

        if save_dir is not None:
            plt.savefig(save_dir)
            
        plt.show()


if __name__ == "__main__":
    sol = SolutionExercise00()
    sol.plottting((-2*math.pi, 2*math.pi), 'function_plot.png')
    sol.random_generate(seed=49)
