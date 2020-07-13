import numpy as np

class Indicator:
    def __init__(self, name):

        ''' Constructor for this class. '''
        """
        :type name: str 
        :rtype: int
        """
        self.name = name # assign the name of distribution

    def Binary_Indicator(self, prob, R):
        """
        :type pi: float 
        :type R: float
        :rtype: int
        """
        self.prob = prob
        self.R = R
        #print('Generate binary indicator for ' + self.name + ' RDT')
        if self.name == 'Binomial':
            return np.where(self.prob <= 1 - self.R, 1, 0)
        else:
            print('Not available!') 
            return []

if __name__ == '__main__':
    p = Indicator(name = 'Binomial')
    print(p.Binary_Indicator(prob = 0.1, R = 0.8))