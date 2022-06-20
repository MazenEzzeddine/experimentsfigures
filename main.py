# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import matplotlib.pyplot as plt
import csv

from numpy import double


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(1)
            elif math.floor(double(row[0])) < 97:
                replicas.append(2)
            elif math.floor(double(row[0])) < 174:
                replicas.append(3)
            elif math.floor(double(row[0])) < 240:
                replicas.append(2)
            elif math.floor(double(row[0])) < 272:
                replicas.append(3)
            elif math.floor(double(row[0])) < 333:
                replicas.append(4)
            elif math.floor(double(row[0])) < 366:
                replicas.append(3)
            elif math.floor(double(row[0])) < 409:
                replicas.append(2)
            elif math.floor(double(row[0])) < 439:
                replicas.append(3)
            elif math.floor(double(row[0])) < 525:
                replicas.append(4)
            elif math.floor(double(row[0])) < 556:
                replicas.append(3)
            elif math.floor(double(row[0])) < 586:
                replicas.append(2)
            else:
                replicas.append(1)

    for r in range(len(replicas)):
        print(replicas[r])
    print(len(replicas))
    print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t, replicas, '--r',  label='replicas')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    ax2.spines['left'].set_color('blue')
    ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Microservice replicas')

    plt.title('Workload and corresponding microservices instances')
    ax1.legend()
    ax2.legend(loc=1)

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
