# world[0] : 배경(가장 밑)
# world[1] : 캐릭터(가장 위)
world = [[], []]

# world object 추가
def add_object(o, depth = 1):
    world[depth].append(o)

# world object update
def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print('월드에 존재하지 않은 객체를 삭제하려고 합니다.')
