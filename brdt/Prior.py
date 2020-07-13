from scipy.stats import beta

class Prior:
    def __init__(self, name, size, par, random_state):
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
        self.random_state = random_state
 
 
    def Prior_MCsim(self):
        print('Generate ' + str(self.size) + " samples for " + self.name + ' distribution')
        if self.name == 'Beta':
            return beta.rvs(a = self.par[0], b = self.par[1], size = self.size, random_state = self.random_state)
        else : 
            print("Not Available")
            return []

if __name__ == '__main__':
    p = Prior(name = 'Beta', size = 1000, par = [1, 1], random_state = 1234)
    print(p.Prior_MCsim())
