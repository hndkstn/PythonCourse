
import random

class Stock():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol

class MutualFund():
    def __init__(self, symbol):
        self.symbol = symbol

class Portfolio(object):
    def __init__(self):
        self.cash = 0
        self.mutualfunds = {}
        self.stock = {}
        self.transaction=[]

    def addCash(self, amt):
        self.amt=amt
        self.cash = self.cash + amt
        self.transaction.append("$" + str(amt) + " cash is added. Balance: $" + str(round(self.cash,1)))

    def withdrawCash(self, amt):
        self.amt=amt
        self.cash = self.cash - amt
        self.transaction.append("$" + str(amt) + " cash is withdrawn. Balance: $" + str(round(self.cash,1)))

        def buyStock(self, share, stock ):
        self.share = share
        self.symbol= stock.symbol
        self.price = stock.price
        self.cash = self.cash - self.price * self.share
        self.transaction.append(str(share) + " shares of " + str(self.symbol) + " stock is bought. Balance: $" + str(round(self.cash,1)))
        if stock.symbol in self.stock:
            self.stock[stock.symbol] = self.stock[stock.symbol] + share
        else:
            self.stock[stock.symbol] = share


    def sellStock(self, symbol , share ):
        self.share = share
        self.symbol = symbol
        self.first_price = self.price
        self.cash = self.cash + self.first_price * random.uniform(0.5, 1.5) * self.share
        self.transaction.append(str(share) + " shares of " + str(self.symbol) + " stock is sold. Balance: $" + str(round(self.cash,1)))
        if symbol in self.stock:
            self.stock[symbol] = self.stock[symbol] - share
        else:
            self.stock[symbol] = 0

    def buyMutualFund(self,share,mutualfunds):
        self.share = share
        self.symbol = mutualfunds.symbol
        self.cash = self.cash - self.share
        self.transaction.append(str(share) + " shares of " + str(self.symbol) + " mutualfund is bought. Balance: $" + str(round(self.cash,1)))
        if mutualfunds.symbol in self.mutualfunds:
            self.mutualfunds[mutualfunds.symbol] = self.mutualfunds[mutualfunds.symbol] + share
        else:
            self.mutualfunds[mutualfunds.symbol] = share

    def sellMutualFund(self,symbol,share):
        self.share = share
        self.symbol = symbol
        self.cash = self.cash + self.share * random.uniform(0.9, 1.2)
        self.transaction.append(str(share) + " shares of " + str(self.symbol) + " mutualfund is sold. Balance: $" + str(round(self.cash,1)))
        if symbol in self.mutualfunds:
            self.mutualfunds[symbol] = self.mutualfunds[symbol] - share
        else:
            self.mutualfunds[symbol] = share

    def history(self):
        print( " " + "\n ".join(self.transaction))

    def __str__(self):
        return "Cash balance: " + str(round(self.cash,2)) +"$" + "\n" + "Stock Balance: " + str(self.stock) + "\n" + "Mutual Fund Balance: " + str(
            self.mutualfunds)

    def __repr__(self):
        return self.__str__()

portfolio = Portfolio()  #Creates a new portfolio

portfolio.addCash(300.50)  #Adds cash to the portfolio

s = Stock(20, "HFH")  #Creates Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s)  #Buys 5 shares of stock s

mf1 = MutualFund("BRT")  #Create MF with symbol "BRT"
mf2 = MutualFund("GHT")  #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1)  #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2)  #Buys 2 shares of "GHT"

portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)

portfolio.history()
print(portfolio)
