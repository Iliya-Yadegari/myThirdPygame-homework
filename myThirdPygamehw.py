HEIGHT = 500
WIDTH = 500


#moving_switch = 'key'

zombie_obj = Actor('character_zombie_idle',(250,50))
alien_obj = Actor('alien',(250,450))
robot_obj = Actor('robot_win',(250,250))

robot_obj.moving_switch = 'key'

bg = 'bg'

def draw():
    screen.blit(bg,(0,0))
    robot_obj.draw()
    alien_obj.draw()
    zombie_obj.draw()

def update():
        pass


def robot_keyboard_mov():
    if keyboard.up:
        robot_obj.top -= 4
    if keyboard.down:
        robot_obj.bottom += 4
    if keyboard.left:
        robot_obj.left -= 4
    if keyboard.right:
        robot_obj.right += 4

def alien_keyboard_mov():
    if keyboard.up:
        robot_obj.top -= 4
    if keyboard.down:
        robot_obj.bottom += 4
    if keyboard.left:
        robot_obj.left -= 4
    if keyboard.right:
        robot_obj.right += 4

def zombie_keyboard_mov():
    if keyboard.up:
        robot_obj.top -= 4
    if keyboard.down:
        robot_obj.bottom += 4
    if keyboard.left:
        robot_obj.left -= 4
    if keyboard.right:
        robot_obj.right += 4

def on_mouse_down(pos,button):

    if robot_obj.collidepoint(pos) and button == mouse.LEFT:
        robot_obj.image = 'alien_hurt'
        robot_keyboard_mov()

    if alien_obj.collidepoint(pos) and button == mouse.LEFT:
        alien_obj.image = 'alien_hurt'
        alien_keyboard_mov()

    if zombie_obj.collidepoint(pos) and button == mouse.LEFT:
        zombie_obj.image = 'alien_hurt'
        zombie_keyboard_mov()
