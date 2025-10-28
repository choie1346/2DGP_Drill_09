world = []

# world object 추가
def add_object(o):
    world.append(o)

# world object update
def update():
    for o in world:
        o.update()

def render():
    for o in world:
        o.draw()

