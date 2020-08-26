import pandas as pd

dframe1 = pd.read_csv('HISTORICAL-DATA.csv')

dframe2 = pd.read_csv('NEWS.csv')

dframe = pd.merge(dframe1, dframe2, how = 'left', on = 'Date')
df = dframe.fillna(0)

lst1 = []
lst1 = df['Date'].tolist()

lst2 = []
lst2 = df['Close'].tolist()

lst3 = []
lst3 = df['Sentiment'].tolist()

l = len(lst1)

for i in range(l):
    wt = 0.05 * lst2[i]
    if lst3[i] > 0.5:
        lst2[i] = lst2[i] + wt * lst3[i]
    else:
        lst2[i] = lst2[i] - wt * lst3[i]

lst = []
for i in range(l):
    pkt = {}
    pkt['Close'] = lst2[i]
    pkt['Date'] = lst1[i]
    lst.append(pkt)
##print(lst)

fdata = pd.DataFrame(lst)

fdata.to_csv('DATA.csv', index = False)

