prices=[10,20,80,40,50,98]
print(prices)
avgprc=sum(prices)/len(prices)
print("avarage",avgprc)
avg_prc=[price for price in prices if price > avgprc]
print(avg_prc)
