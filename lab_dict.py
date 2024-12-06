import pickle
from tokenize import group


class NPC:
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name

npc1 = NPC(100, 200, 'jeni')
# print(type(npc1.__dict__))
# print(npc1.__dict__)
# # npc1.x = 200 동일
# # npc1.__dict__.update({'x':200})
npc2 = NPC(500, 100, 'zwi')

group = [npc1, npc2] # 하나로 묶고.
with open('npc.pickle', 'wb') as f:
    pickle.dump(group, f)
