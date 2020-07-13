import numpy as np
from scipy.stats import binom
import Indicator as Indicator


class Risk:
    def __init__(self, name, n, c, pi, R):
        ''' Constructor for this class. '''
        self.name = name # assign the name of distribution
        self.n = n
        self.c = c
        self.pi = pi
        self.R = R
        self.Ind = Indicator.Indicator(self.name)

    def Consumer_Risk(self):
        print('Compute consumer risk for ' + self.name + ' RDT')
        sum1 = sum([self.Ind.Binary_Indicator(i, self.R) for i in self.pi] * binom.cdf(k = self.c, n = self.n, p = self.pi))
        sum2 = sum(binom.cdf(k = self.c, n = self.n, p = self.pi))
        return 1 - sum1 / sum2
    
    def Producer_Risk(self):
        print('Compute producer risk for ' + self.name + ' RDT')
        sum1 = sum([self.Ind.Binary_Indicator(i, self.R) for i in self.pi] * (1 - binom.cdf(k = self.c, n = self.n, p = self.pi)))
        sum2 = sum(1 - binom.cdf(k = self.c, n = self.n, p = self.pi))
        return sum1 / sum2

    def Acceptance_Prob(self):
        print('Compute acceptance probability for ' + self.name + ' RDT')
        return sum(binom.cdf(k = self.c, n = self.n, p = self.pi)) / len(self.pi)




if __name__ == '__main__':
    import Prior
    pi = Prior.Prior(name = 'Beta', size = 1000, par = [1, 1], random_state = 1234).Prior_MCsim()
    p = Risk(name = 'Binomial', n = 10, c = 2, pi = pi, R = 0.5)
    print(p.Consumer_Risk())
    print(p.Producer_Risk())
    print(p.Acceptance_Prob())
