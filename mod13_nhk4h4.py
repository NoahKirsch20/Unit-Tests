import unittest
import datetime

#Wasn't sure if I had to ask for user input then validate or do just validation.
#So I went with what I was comfortable doing in asking for the user input first.

class symbol(unittest.TestCase):

    def setUp(self):
        self.chartChoice = ""
        self.startDate = ""
        self.endDate = ""
        
    #Chart Type
    def test_chart(self):
        print("1. Bar Chart")
        print("2. Line Chart")
        #Ask for chart choice
        self.chartChoice = input("What chart type do you wants?: ")
        if chartChoice == '1':
            print("Bar Chart chosen.")
            pass
        elif chartChoice == '2':
            print("Line Chart chosen.")
            pass
        else:
            print("Invalid")
        
    #Symbol
    def test_symbol(self):
        #Ask for Stock Symbol
        self.symbol = input("Stock Symbols: ")
        if len(symbol) > 0 & len(symbol) < 8:
            pass
        else:
            print("Too long or too short of a stock symbol.")
                                 
    #Time Series
    def test_time(self):
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")

        self.timeSeries = int(input("What time series would you like?: "))

        timeSeries_Dict = { 1: "Time Series (60min)", 2: "Time Series (Daily)",
                            3: "Time Series (Weekly)", 4: "Time Series (Monthly)" }
        
        if timeSeries == '1':
            print("Intraday chosen.")
            pass
        elif timeSeries == '2':
            print("Daily chosen.")
            pass
        elif timeseries == '3':
            print("Weekly chosen.")
            pass
        elif timeSeries == '4':
            print("Monthly chosen.")
            pass
        else:
            print("Invalid")

    #Start Date
    def test_start(self):
        self.startDate = input("Start Date (YYYY-MM-DD): ")
        #Have startDate checked for correct format.
        start = datetime.date(startDate, "%Y-%m-%d")
        print(start)
        pass
   
    #End Date
    def test_end(self):
        self.endDate = input("End Date (YYYY-MM-DD): ")
        #Have endDate checked for correct format.
        end = datetime.date(endDate, "%Y-%m-%d")
        print(end)
        pass

if __name__ == "__main__":
    unittest.main()
