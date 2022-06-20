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

def secondworkload():
    # Use a breakpoint in the code line below to debug your script.
    time = []

    m = 15


    p0=[]
    p1=[]
    p2=[]
    p3=[]
    p4=[]

    for t in range(1,120):
        time.append(t)
        p0.append(15)
        p1.append(15)
        p2.append(15)
        p3.append(15)
        p4.append(15)



    for t in range(121, 121+45):
        time.append(t)
        p0.append(m)
        p1.append(m)
        p2.append(15)
        p3.append(15)
        p4.append(15)
        m= m+1

    for t in range(121+45, 121+45+75):
        time.append(t)
        p0.append(m)
        p1.append(m)
        p2.append(15)
        p3.append(15)
        p4.append(15)
    m=15
    for t in range( 121+45+75, 121+45+75 + 45):
        time.append(t)
        p0.append(60)
        p1.append(60)
        p2.append(m)
        p3.append(15)
        p4.append(15)
        m=m+1
    for t in range(121 + 45 + 75 + 45, 121 + 45 + 75 + 45 + 75):
        time.append(t)
        p0.append(60)
        p1.append(60)
        p2.append(m)
        p3.append(15)
        p4.append(15)
    m=15
    for t in range(121 + 45 + 75 + 45+75, 121 + 45 + 75 + 45 + 75 + 45):
        time.append(t)
        p0.append(60)
        p1.append(60)
        p2.append(60)
        p3.append(m)
        p4.append(15)
        m=m+1
    for t in range(121 + 45 + 75 + 45 + 75+45, 121 + 45 + 75 + 45 + 75 + 45+75):
        time.append(t)
        p0.append(60)
        p1.append(60)
        p2.append(60)
        p3.append(m)
        p4.append(15)
    for t in range(121 + 45 + 75 + 45 + 75+45 + 75, 121 + 45 + 75 + 45 + 75 + 45+75 + 120):
        time.append(t)
        p0.append(15)
        p1.append(15)
        p2.append(15)
        p3.append(15)
        p4.append(15)




    fig, ax1 = plt.subplots()

    ax1.plot(time, p0, color='blue', label='P0')
    ax1.plot(time, p1, color='red', label='P1')
    ax1.plot(time, p2, color='green', label='P2')
    ax1.plot(time, p3, color='yellow', label='p3')
    ax1.plot(time, p4, color='brown', label='p4')
    plt.legend()

    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secondworkload()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
