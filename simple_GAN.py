import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
def real_f(x):
    return x*x
plt.plot(np.linspace(-1,1,100), real_f(np.linspace(-1,1,100)))
plt.ylabel('x2')
plt.xlabel('x')
plt.show()

def generate_real_samle(n=100):
    '''
    функция сэпмлирует данные из реального распределения
    :param n:
    :return:
    '''
    x = np.random.rand(n)-0.5
    y = real_f(x)
    return np.vstack((x,y)).T
real_data = generate_real_samle(n=100)
plt.scatter(real_data[:,0], real_data[:,1])
plt.show()