from functools import cmp_to_key

# medium 

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.name
        
    def comparator(a, b):
        name1, score1 = a.name, a.score
        name2, score2 = b.name, b.score

        if score1 < score2 :
            return 1 
        elif score1 > score2 :
            return -1
        elif name1 < name2:
            return -1
        elif name1 > name2:
            return 1
        else:
            return 0


n = int(input())