import pgzrun
import random
import recipes

TITLE = "BarMleczny"
WIDTH = 800
HEIGHT = 600

current_order = "None"
order_items = recipes.RECIPES[current_order]
taca = []
money = 0

counter = Actor('counter_1', (WIDTH//2-90, HEIGHT//2+140))
fence_gate = Actor('fence_gate_1', (WIDTH//2+312, HEIGHT//2+150))

btn_dough = Rect((50, 250), (120, 50))


def draw():
    screen.clear()
    screen.fill((40, 40, 40))

    counter.draw()
    fence_gate.draw()

    screen.draw.filled_rect(btn_dough, (70, 80, 100))
    screen.draw.text("Dough", (btn_dough.x + 25, btn_dough.y + 15), fontsize=20)

def on_mouse_down(pos):

    if btn_dough.collidepoint(pos):
        print("ciasto")

pgzrun.go()