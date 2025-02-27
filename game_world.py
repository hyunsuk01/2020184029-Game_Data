import pickle
import server

world = [[] for _ in range(4)]
collision_pairs = {}

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in world:
        layer.clear()
    collision_pairs.clear()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)


def save():
    game_data = [world, collision_pairs] # 게임 월드 정보와 충돌 관련 정보를 묶은 리스트
    with open('game.save','wb') as f:
        pickle.dump(game_data, f)

def load():
    global world, collision_pairs
    with open('game.save', 'rb') as f:
        game_data = pickle.load(f)
        world, collision_pairs = game_data

def all_objects(): #게임 내 모든 객체들을 리스트로 넘겨준다.
    world_objects = []
    for layer in world:
        for o in layer:
            world_objects.append(o)
    return world_objects