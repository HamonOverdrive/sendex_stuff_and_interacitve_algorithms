import matplotlib.pyplot as plt

def graph_operation(x, y):
    print('function that graphs {} and {}'.format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3]
y1 = [2, 3 , 1]

graph_me = [x1, y1]

graph_operation(*graph_me)