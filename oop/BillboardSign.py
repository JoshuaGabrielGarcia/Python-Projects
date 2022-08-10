class BillSign:
    def __init__(self, lngt):
        self.lngt = lngt

    def __gt__(self, other):
        for i in range(len(other.lngt)+1):
            result = other.lngt[:i] + ">" + self.lngt
            result += ">" + other.lngt[i:]
            print(result)


jeans = BillSign("Jeans")
legs = BillSign("Leggings")

jeans>legs