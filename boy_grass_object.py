from pico2d import *

# Game object class here
class Grass:
    def __init__(self): # 생성자. self는 자신을 가리키는 더미 변수, 항상 써야 함 !!
        self.image = load_image('grass.png') # 객체(나)의 속성 만들어 주기
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running, grass
    running = True
    grass = Grass()

def update_world():
    grass.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
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
