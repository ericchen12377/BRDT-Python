import Risk
import Cost
import numpy as np
class Optimal:
    def __init__(self, name, pi):
        ''' Constructor for this class. '''
        # assign the name of distribution
        self.name = name
        self.pi = pi
        

    def Optimal_Sample_Size(self, c, R, thres_CR):
        self.c = c
        self.R = R
        self.thres_CR = thres_CR
        print('Compute optimal sample size for ' + self.name + ' RDT')
        self.n = self.c + 1
        self.CR = Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Consumer_Risk()
        while self.CR > self.thres_CR:
            self.n += 1
            self.CR = Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Consumer_Risk()
        return self.n

    # def Optimal_Cost(self, cost_fix, cost_var, sales_volume, cost_warranty, cost_reliability_growth):
    #     self.cost_fix = cost_fix
    #     self.cost_var = cost_var
    #     self.sales_volume = sales_volume
    #     self.cost_warranty = cost_warranty
    #     self.cost_reliability_growth = cost_reliability_growth
    #     print('Compute optimal cost for ' + self.name + ' RDT')
    #     nRc_vec = np.array([(x, y, z) for x in self.n for y in self.R for z in self.c])
    #     cost_vec = np.array([Cost.Cost(self.name, n = nRc[0], c = nRc[2], pi = self.pi, R = nRc[1], cost_fix = self.cost_fix, cost_var = self.cost_var, sales_volume = self.sales_volume, cost_warranty = self.cost_warranty, cost_reliability_growth = self.cost_reliability_growth).Cost_Expected() for nRc in nRc_vec])
    #     CR_vec = np.array([Consumer_Risk.Consumer_Risk(self.name, n = nRc[0], c = nRc[2], pi = self.pi, R = nRc[1]).Binom_Consumer_Risk() for nRc in nRc_vec])

    #     CR_ind = np.where(CR_vec <= self.thres_CR)
    #     cost_ind = np.where(cost_vec == min(cost_vec[CR_ind]))
    #     return nRc_vec[cost_ind]
    
    

if __name__ == '__main__':
    import Prior
    pi = Prior.Prior(name = 'Beta', size = 1000, par = [1, 1], random_state = 1234).Prior_MCsim()
    p = Optimal(name = 'Binomial', pi = pi)
    print(p.Optimal_Sample_Size(c = 2, R = 0.8, thres_CR = 0.05))

