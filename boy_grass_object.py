from pico2d import *
from random import *

# Game object class here
class Grass:
    def __init__(self): # 생성자. self는 자신을 가리키는 더미 변수, 항상 써야 함 !!
        self.image = load_image('grass.png') # 객체(나)의 속성 만들어 주기
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
    # boy = Boy()
    team = [Boy() for i in range(11)]
    world += team

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
