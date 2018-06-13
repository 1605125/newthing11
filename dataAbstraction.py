class Bank:
    def setRateOfInterest(self):
        # self.rate = 16.50
        raise NotImplementedError("only subclasses  subclasses can i ")

    def getRateOfInterest(self):
        return self.rate


class HDFC(Bank):

    def setRateOfInterest(self):
        self.rate = 16.50

    def getRateOfInterest(self):
        return self.rate


hdfc = HDFC()
hdfc.setRateOfInterest()
print(hdfc.getRateOfInterest())
