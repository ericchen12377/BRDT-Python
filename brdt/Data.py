import Risk
import Cost
import Optimal
import numpy as np
import pandas as pd
class Data:
    def __init__(self, name, pi, cost_fix, cost_var, sales_volume, cost_warranty, cost_reliability_growth):
        ''' Constructor for this class. '''
        # assign the name of distribution
        self.name = name
        self.pi = pi
        self.cost_fix = cost_fix
        self.cost_var = cost_var
        self.sales_volume = sales_volume
        self.cost_warranty = cost_warranty
        self.cost_reliability_growth = cost_reliability_growth
        
    def All_Data(self, n_list, c_list, R_list):
        self.n_list = n_list
        self.c_list = c_list
        self.R_list = R_list
        res = pd.DataFrame()
        print('Generate all test plans data for ' + self.name + ' RDT')
        ncR_list = np.array([(n, c, R) for n in self.n_list for c in self.c_list for R in self.R_list])
        CR_list = []
        #PR_list = []
        AP_list = []
        RDT_list = []
        RG_list = []
        RG_exp_list = []
        WS_list = []
        WS_exp_list = []
        WS_failureprob_list = []
        cost_list = []
        for i in range(len(ncR_list)):
            self.n = ncR_list[i][0]
            self.c = ncR_list[i][1]
            self.R = ncR_list[i][2]
            CR_list.append(Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Consumer_Risk())
            #PR_list.append(Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Producer_Risk())
            AP_list.append(Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Acceptance_Prob())
            RDT_list.append(Cost.Cost(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).RDT(self.cost_fix, self.cost_var))
            RG_list.append(Cost.Cost(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Reliability_Growth(self.cost_reliability_growth))
            RG_exp_list.append(RG_list[i] * (1 - AP_list[i]))
            WS = Cost.Cost(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Warranty(self.sales_volume, self. cost_warranty)
            WS_list.append(WS[0])
            WS_failureprob_list.append(WS[1])
            WS_exp_list.append(WS_list[i] * AP_list[i])
            cost_list.append(RDT_list[i] + RG_exp_list[i] + WS_exp_list[i])

        res['n'] = ncR_list[:, 0]
        res['c'] = ncR_list[:, 1]
        res['R'] = ncR_list[:, 2]
        res['CR'] = CR_list
        #res['PR'] = PR_list
        res['AP'] = AP_list
        res['RDT_Cost'] = RDT_list
        res['Reliabiltiy_Growth_Cost'] = RG_list
        res['Reliabiltiy_Growth_Cost_exp'] = RG_exp_list
        res['Warranty_Services_Cost'] = WS_list
        res['Warranty_Services_Failure_Probability'] = WS_failureprob_list
        res['Warranty_Services_Cost_exp'] = WS_exp_list

        return res
    

    def Optimal_Data(self, c_list, R_list, thres_CR):
        self.c_list = c_list
        self.R_list = R_list
        self.thres_CR = thres_CR
        res = pd.DataFrame()
        print('Generate optimal test plans data for ' + self.name + ' RDT')
        cR_list = np.array([(c, R) for c in self.c_list for R in self.R_list])
        CR_list = []
        #PR_list = []
        AP_list = []
        RDT_list = []
        RG_list = []
        RG_exp_list = []
        WS_list = []
        WS_exp_list = []
        WS_failureprob_list = []
        cost_list = []
        n_optimal_list = []
        for i in range(len(cR_list)):
            self.c = cR_list[i][0]
            self.R = cR_list[i][1]
            self.n = Optimal.Optimal(self.name, self.pi).Optimal_Sample_Size(self.c, self.R, self.thres_CR)
            n_optimal_list.append(self.n)
            CR_list.append(Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Consumer_Risk())
            #PR_list.append(Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Producer_Risk())
            AP_list.append(Risk.Risk(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Acceptance_Prob())
            RDT_list.append(Cost.Cost(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).RDT(self.cost_fix, self.cost_var))
            RG_list.append(Cost.Cost(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Reliability_Growth(self.cost_reliability_growth))
            RG_exp_list.append(RG_list[i] * (1 - AP_list[i]))
            WS = Cost.Cost(self.name, n = self.n, c = self.c, pi = self.pi, R = self.R).Warranty(self.sales_volume, self. cost_warranty)
            WS_list.append(WS[0])
            WS_failureprob_list.append(WS[1])
            WS_exp_list.append(WS_list[i] * AP_list[i])
            cost_list.append(RDT_list[i] + RG_exp_list[i] + WS_exp_list[i])

        res['n'] = n_optimal_list
        res['c'] = cR_list[:, 0]
        res['R'] = cR_list[:, 1]
        res['CR'] = CR_list
        #res['PR'] = PR_list
        res['AP'] = AP_list
        res['RDT_Cost'] = RDT_list
        res['Reliabiltiy_Growth_Cost'] = RG_list
        res['Reliabiltiy_Growth_Cost_exp'] = RG_exp_list
        res['Warranty_Services_Cost'] = WS_list
        res['Warranty_Services_Failure_Probability'] = WS_failureprob_list
        res['Warranty_Services_Cost_exp'] = WS_exp_list

        return res



if __name__ == '__main__':
    import Prior
    pi = Prior.Prior(name = 'Beta', size = 1000, par = [1, 1], random_state = 1234).Prior_MCsim()
    p = Data(name = 'Binomial', pi = pi, cost_fix = 0.5, cost_var = 1, \
        sales_volume = 1, cost_warranty = 0.8, cost_reliability_growth = 10)
    #print(p.All_Data(n_list = [0,1,2,3,4], c_list = [0,1,2], R_list = [0.5, 0.6, 0.7]).head())
    print(p.Optimal_Data(c_list = [0,1,2], R_list = [0.5, 0.6, 0.7], thres_CR = 0.05))

