import pickle

class NPC:
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name

with open('npc.pickle', 'rb') as f:
    group = pickle.load(f)

for o in group:
    print(o.name, o.x, o.y)