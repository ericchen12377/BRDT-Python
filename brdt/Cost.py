import numpy as np
import Risk
from scipy.stats import binom

class Cost:
    def __init__(self, name, n, c, pi, R):
        ''' Constructor for this class. '''
        
        # assign the name of distribution
        self.name = name 
        self.n = n
        self.c = c
        self.pi = pi
        self.R = R
        self.AP = Risk.Risk(self.name, self.n, self.c, self.pi, self.R).Acceptance_Prob()

    def RDT(self, cost_fix, cost_var):
        self.cost_fix = cost_fix
        self.cost_var = cost_var
        print('Compute RDT cost for ' + self.name + ' RDT')
        return self.cost_fix + self.cost_var * self.n
    
    def Warranty(self, sales_volume, cost_warranty):
        self.sales_volume = sales_volume
        self.cost_warranty = cost_warranty
        print('Compute warranty cost for ' + self.name + ' RDT')
        failureprob = sum(binom.cdf(k = self.c, n = self.n, p = self.pi) * self.pi) / sum(binom.cdf(k = self.c, n = self.n, p = self.pi))
        return self.cost_warranty * failureprob * self.sales_volume, failureprob

    def Reliability_Growth(self, cost_reliability_growth):
        self.cost_reliability_growth = cost_reliability_growth
        print('Compute reliability growth cost for ' + self.name + ' RDT')
        return self.cost_reliability_growth

    def Expected(self):
        if self.name == 'Binomial':
            return self.RDT(self.cost_fix, self.cost_var) + self.Reliability_Growth(self.cost_reliability_growth) * (1 - self.AP) + \
            self.Warranty(self.sales_volume, self.cost_warranty)[0] * self.AP


if __name__ == '__main__':
    import Prior
    pi = Prior.Prior(name = 'Beta', size = 1000, par = [1, 1], random_state = 1234).Prior_MCsim()
    p = Cost(name = 'Binomial', n = 10, c = 2, pi = pi, R = 0.5)
    print(p.RDT(cost_fix = 1, cost_var = 1))
    print(p.Warranty(sales_volume = 1, cost_warranty = 0.8))
    print(p.Reliability_Growth(cost_reliability_growth = 10))
    print(p.Expected())

