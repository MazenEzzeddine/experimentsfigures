# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def lagunaware():
    # Use a breakpoint in the code line below to debug your script.
    x = []
    y = [0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
20,
79,
234,
133,
159,
190,
185,
124,
5,
212,
223,
0,
0,
35,
204,
91,
107,
75,
214,
6,
4,
49,
0,
73,
120,
81,
198,
589,
341,
533,
168,
179,
194,
131,
44,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0]

    y1 = [
        0,
         0,
         20,
         79,
         234,
         133,
         159,
         190,
         185,
         124,
         5,
         212,
         223,
         0,
         0,
         35,
         204,
         91,
         107,
         75,
         214,
         6,
         4,
         49,
         0,
         73,
         120,
         81,
         198,
         589,
         341,
         533,
         168,
         179,
         194,
         131,
         44,
         0,
         0,
    0]

    # with open('lag.csv', 'r') as csvfile:
    #     lines = csv.reader(csvfile)
    #     i = 1
    #     for row in lines:
    #         if i == 1:
    #              i = i+1
    #         else:
    #              x.append(row[0])
    #              y.append((row[1]))



    y2= [0,
        0,
        0,
        116,
        103,
        403,
        458,
        670,
        758,
        776,
        922,
        1103,
        1191,
        1341,
        1480,
        1227,
        1579,
        1379,
        633,
        326,
        186,
        153,
        170,
        131,
        120,
        141,
        185,
        546,
        1217,
        1463,
        1441,
        1216,
        851,
        932,
        672,
        330,
        24,
        0,
        0,
        0
    ]




    t=0
    k = []
    intt = []
    inttunaware= []

    for i in  range(len(y1)):
        k.append(t)
        intt.append(float(y1[i]))
        inttunaware.append(float(y2[i]))
        t=t+15






    plt.plot(k, intt,
             label="autoscaling with load aware assignment")

    plt.plot(k, inttunaware,
             label="autoscaling with load unaware assignment")

    plt.xticks()
    plt.xlabel('time')
    plt.ylabel('events lag')
    plt.title('Events lag  autoscaling ')
    #plt.grid()
    plt.legend()
    plt.show()
# Press the green button in the gutter to run the script.


def lagunawaresimple():
    # Use a breakpoint in the code line below to debug your script.
    x = []
    y1 = [
0,
193,
70,
59,
45,
20,
49,
70,
55,
57,
62,
117,
130,
155,
151,
151,
151,
157,
280,
313,
184,
185,
198,
202,
145,
0,
0,
0,
20,
70,
57,
70,
60,
16,
69,
19,
51,
66,
55,
0,
]



    # with open('lag.csv', 'r') as csvfile:
    #     lines = csv.reader(csvfile)
    #     i = 1
    #     for row in lines:
    #         if i == 1:
    #              i = i+1
    #         else:
    #              x.append(row[0])
    #              y.append((row[1]))



    y2= [
0,
214,
70,
70,
70,
70,
70,
70,
70,
84,
202,
370,
817,
1407,
1887,
2514,
3039,
3679,
4391,
4944,
4798,
4764,
5164,
5464,
5864,
6164,
6564,
6564,
5529,
4488,
3427,
2266,
1358,
570,
165,
67,
47,
71,
68,
63,
52,
         0

    ]




    t=0
    k = []
    intt = []
    inttunaware= []

    for i in  range(len(y1)):
        k.append(t)
        intt.append(float(y1[i]))
        inttunaware.append(float(y2[i]))
        t=t+15






    plt.plot(k, intt,
             label="autoscaling with load aware assignment")

    plt.plot(k, inttunaware,
             label="autoscaling with load unaware assignment")

    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events lag')
    plt.title('Events lag during autoscaling')
    #plt.grid()
    plt.legend()
    plt.show()

def lag30oldworkload():
    # Use a breakpoint in the code line below to debug your script.
    x = []
    y1 = [0,0,


        0,
        0,
        68,
        234,
        844,
        1859,
        229,
        260,
        180,
        166,
        123,
        35,
        20,
        0,
        89,
        111,
        516,
        1245,
        1394,
        1508,
        1110,
        293,
        0,
        132,
        56,
        199,
        316,
        739,
        1258,
        1772,
        2109,
        2080,
        1120,
        752,
        191,
        33,
        0,
    0



    ]



    # with open('lag.csv', 'r') as csvfile:
    #     lines = csv.reader(csvfile)
    #     i = 1
    #     for row in lines:
    #         if i == 1:
    #              i = i+1
    #         else:
    #              x.append(row[0])
    #              y.append((row[1]))



    y2= [
0,
214,
70,
70,
70,
70,
70,
70,
70,
84,
202,
370,
817,
1407,
1887,
2514,
3039,
3679,
4391,
4944,
4798,
4764,
5164,
5464,
5864,
6164,
6564,
6564,
5529,
4488,
3427,
2266,
1358,
570,
165,
67,
47,
71,
68,
63,
52,
         0

    ]




    t=0
    k = []
    intt = []
    inttunaware= []

    for i in  range(len(y1)):
        k.append(t)
        intt.append(float(y1[i]))
        #inttunaware.append(float(y2[i]))
        t=t+15






    plt.plot(k, intt,
             label="Events lag (30 seconds decision interval)")



    plt.xticks()
    plt.xlabel('Time (sec)')
    plt.ylabel('Events lag')
    plt.title(' ')
    #plt.grid()
    plt.legend()
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #lagunawaresimple()
    lag30oldworkload()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
