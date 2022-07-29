#Explaination: https://en.wikipedia.org/wiki/Quarterback#:~:text=The%20quarterback%20(commonly%20abbreviated%20%22QB,directly%20behind%20the%20offensive%20line.
class QuarterBack:
    def __init__(self, yrds, tds, cmps, atts, ints, wins):
        self.wins = wins

        # Calculate quarterback passer rating (NCAA)
        self.rating = ((8.4*yrds) + (330*tds) + (100*cmps) - (200 * ints))/atts
        
    #less than or equal compare function for this class
    def __le__(self, other):
        if (self.rating <= other.rating) or (self.wins <= other.wins):
            return True
        return False

    #greater than function comparision for this class
    def __gt__(self, other):
        if self.wins> other.wins and self.rating>other.rating:
            return True
        return False
        # Complete the method...
    
    #The syntax for less than and greater than compare function can be use for any class

peyton = QuarterBack(yrds=4700, atts=679, cmps=450, tds=33, ints=17, wins=10)
eli = QuarterBack(yrds=4002, atts=539, cmps=339, tds=31, ints=25, wins=9)
tom= QuarterBack(yrds=4806, atts=578, cmps=398, tds=50, ints=8, wins=16)
if peyton > eli and peyton > tom :
    print('Peyton is the better QB')
elif eli> tom and eli> peyton:
    print('Eli is the better QB')
elif tom> eli and tom> peyton:
    print('Tom is the better QB')
else:
    print('It is not clear who the better QB is...')
