from scipy.stats import beta

class Prior:
    def __init__(self, name, size, par):
        ''' Constructor for this class. '''
        """
        :type name: str 
        :type size: int
        :type par: list
        :rtype: list
        """
        
        self.name = name # assign the name of distribution ["Beta", "Dirichlet"]
        self.size = size
        self.par = par
 
 
    def Prior_MCsim(self):
        print('Generate Monte Carlo Simulation for ' + self.name + ' distribution')
        if self.name == 'Beta':
            return beta.rvs(a = self.par[0], b = self.par[1], size = self.size)
        else : 
            print("Not Available")

if __name__ == '__main__':
    p = Prior('Beta', 10, [1, 1])
    print(p.Prior_MCsim())
