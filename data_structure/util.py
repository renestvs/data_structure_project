__author__ = 'rene_esteves'

import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [0,1,4,9,16]

def execution_times(x, y):
    plt.plot(x,y)

    plt.ylabel('Time (ms)')
    plt.xlabel("Input")

    plt.show()


