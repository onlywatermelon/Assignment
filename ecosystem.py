import random

class Eco:
    def __init__(self,river_length=-1,fishes=-1,bears=-1,steps=-1,river=[]):
        self.river_length = river_length
        self.fishes = fishes
        self.bears = bears
        self.steps = steps
        self.river = river
    
    def get_Int(self,kind:str):
        while True:
            number_of_kind = input('Please enter the {} :'.format(kind))
            if number_of_kind.isdigit():
                return int(number_of_kind)
                break
            else:
                print('Please enter the postive integer without any notation!')

    def get_river_length(self):
        river_length = self.get_Int('river length')
        self.river_length = river_length
    
    def get_fishes(self):
        while True:
            fishes = self.get_Int('number of fishes')
            if self.river_length >= fishes:
                self.fishes = fishes 
                break
            else:
                print('Number of fishes must be smaller than river\'s length.')
    
    def get_bears(self):
        while True:
            bears = self.get_Int('number of bears')
            if self.river_length >= (self.fishes+bears):
                self.bears = bears 
                break
            else:
                print('Number of fishes must be smaller than river\'s length minus number of fishes.')

    def get_steps(self):
        steps = self.get_Int('number of steps')
        self.steps = steps

    def set_river(self):
        river = ['F']*self.fishes + ['B']*self.bears +['N']*(self.river_length-self.fishes-self.bears)
        random.shuffle(river)
        self.river = river
        print('River', self.river)

    def get_move(self,place):
        if place == 1:
            return random.choice([0,1])
        elif place == (len(self.river)-1):
            return random.choice([-1,0])
        else:
            return random.choice([-1,0,1])

    def simulation(self):
        new = []
        for i in range(self.steps):
            none_list = []
            lst = iter(range(len(self.river)))
            for j in lst:
                if self.river[j] == 'F':
                    move = self.get_move(j)
                    if move != 0:
                        if self.river[j+move] == 'N':
                            self.river[j], self.river[j+move] = 'N', 'F'
                            if move == 1:
                                lst.__next__()
                        elif self.river[j+move] == 'B':
                            self.river[j] = 'N'
                        else:
                            new.append('F')
                
                if self.river[j] == 'B':
                    move = self.get_move(j)
                    if move != 0:
                        if self.river[j+move] in ['N', 'F']:
                            self.river[j], self.river[j+move] = 'N', 'B'
                            if move == 1:
                                lst.__next__()
                        elif self.river[j+move] == 'B':
                            new.append('B')

            if len(new) > 0:
                for k in new:
                    none_list = [index for (index,value) in enumerate(self.river) if value == 'N']
                    try:
                        random_choice_none = random.choice(none_list)
                        self.river[random_choice_none] = k
                        new.remove(k)
                    except:
                        pass
                    try:
                        none_list.remove(random_choice_none)
                    except:
                        pass
                
            print('Step', i+1, self.river)
            if len(set(self.river)) == 1:
                break

    def main(self):
        self.get_river_length()
        self.get_fishes()
        self.get_bears()
        self.set_river()
        self.get_steps()
        self.simulation()

if __name__ == "__main__":
    eco = Eco()
    eco.main()
