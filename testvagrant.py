dic=[{'name':'leatherwallet','unitprice':1100,'gst':18,'quant':1},
     {'name':'umbrella','unitprice':900,'gst':12,'quant':4},
     {'name':'cig','unitprice':200,'gst':28,'quant':3},
     {'name':'honey','unitprice':100,'gst':0,'quant':2}]

gst=[]
s=[]

count=0
for i in range(0,4):
    s.append(dic[i]['unitprice']*dic[i]['quant'])
    if dic[i]['gst']!=0:
        gst.append(s[i]*dic[i]['gst']/100)
    else:
        gst.append(0)
max=gst[3]
for i in range(1,4):
    if gst[i]<max:
        max=gst[i]
        count=i
print("max gst product:", dic[count],'GST Amt.=',gst[0])
sum=0
for i in range(4):
    sum+=gst[i]+s[i]
print('total amt to be paid:', s[0])
