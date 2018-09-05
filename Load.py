class Load:
    
    def __init__(self,annualInterestRate=2.5,
        numberOfYear=1,loadAmout=1000,borrower=" "):
        self.__annualInterestRate=annualInterestRate
        self.__numberOfYear=numberOfYear
        self.__loadAmount=loadAmout
        self.__borrower=borrower
#  读取私有数据        
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def getNumberOfYear(self):
        return self.__numberOfYear
    
    def getLoadAmount(self):
        return self.__loadAmount
    
    def getBorrower(self):
        return self.__borrower
    
# 设置私有数据
    def setAnnualInterestRate(self,annualInterestRate):
        self.__annualInterestRate=annualInterestRate

    def setNumberOfYear(self,numberOfYear):
        self.__numberOfYear=numberOfYear

    def setLoadAmount(self,loadAmount):
        self.__loadAmount=loadAmount

    def setBorrower(self,borrower):
        self.__borrower=borrower

    #  一些方法
    def getMonthlyPayment(self):
        monthlyInterestRate=self.__annualInterestRate/1200
        monthlyPayment=\
            self.__loadAmount*monthlyInterestRate/(1-(1/(1+monthlyInterestRate)**(self.__numberOfYear*12)))
        return monthlyPayment
    
    def getTotalPayment(self):
        totalPayment=self.getMonthlyPayment()*\
            self.__numberOfYear*12
        return totalPayment
        


