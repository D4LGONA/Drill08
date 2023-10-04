from pico2d import *
from random import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = randint(100, 700), 90
        self.frame = randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        if randint(0, 1) == 1: # 큰 공
            self.image = load_image('ball41x41.png')
        else: # 작은 공
            self.image = load_image('ball21x21.png')
        self.speed = randint(5, 20)
        self.x, self.y = randint(0, 800), 599

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running, grass, team, world
    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(11)]
    balls = [Ball() for i in range(20)]
    world += team
    world += balls

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world() # game logic
    render_world() # draw game world
    delay(0.05)

# finalization code

close_canvas()
