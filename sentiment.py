from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np
comment = []
songname="Hey Kong"
with open(songname+".txt", mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    # print(rows)
    for row in rows:
        if row not in comment:
            comment.append(row.strip('\n'))
    # print(comment)


def snowanalysis(self):
    sentimentslist = []
    for li in self:
        print(li)
        s = SnowNLP(li)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.xlabel("The comments distribution")
    plt.show()
    print(sentimentslist)

    for i in range(len(sentimentslist)):
        if (sentimentslist[i] > 0.5):
            sentimentslist[i] = 1
        else:
            sentimentslist[i] = -1
    print(sentimentslist)
    info = []
    a = 0
    b = 0
    for x in range(0, len(sentimentslist)):
        if (sentimentslist[x] == 1):
            a = a + 1
        else:
            b = b + 1
    info.append(b)
    info.append(a)
    print(info)
    info2 = ['negative', 'positive']
    plt.bar(info2, info, tick_label=info2, color='#2FC25B')
    plt.xlabel("comments analyst")
    plt.show()


snowanalysis(comment)
