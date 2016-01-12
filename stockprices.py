#Finds lowest buy price from the price list
def buyPrice(priceList):
    priceList = [float(i) for i in priceList]
    priceList.sort()
    return str(priceList[0])

#Find the highest acceptable sell price from the price list
def sellPrice(priceList):
    buyIndex = priceList.index(buyPrice(priceList))
    sellPrice = buyPrice(priceList)
    return max(priceList[buyIndex + 2:])
        
stockPrices = open('stockprices.txt','r')
priceList = []
for line in stockPrices:
    priceList = line.split()

print 'Buy: ', buyPrice(priceList), '\n', 'Sell: ', sellPrice(priceList)