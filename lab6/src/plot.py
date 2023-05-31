import matplotlib.pyplot as plt

def plot_result(y, x, f, method):
    fig = plt.figure()
    fig.suptitle('differentiation result', fontsize=20)
    ax = fig.add_subplot(111)
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.plot(x, y, marker="o", label=f"{method} differentiation result") #marker circle
    plt.plot(x, f, marker=".", label="input function") #marker point
    # for i,j in zip(x, [round(i, 3) for i in y]):
    #     ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
    #     ax.annotate('(%s,' %i, xy=(i,j))
    plt.legend()
    plt.show()
    ax.grid()
    pass
