from Grabscreen import grab_screen
import cv2
import time
import pytesseract
from directkeys import PressKey,ReleaseKey, W, A, S, D,F3, C, MouseMoveTo, LSHIFT, Q, E
import pygetwindow as gw
import pyautogui
import pydirectinput


t_time = 0.09


def straight():
    PressKey(W)
    time.sleep(1)
    ReleaseKey(A)
    ReleaseKey(D)


def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)


def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)


def move_forward():
    PressKey(LSHIFT)
    PressKey(W)
    time.sleep(0.5)
    ReleaseKey(W)
    ReleaseKey(LSHIFT)


def move_left(length):
    PressKey(LSHIFT)
    PressKey(A)
    time.sleep(length)
    ReleaseKey(A)
    ReleaseKey(LSHIFT)


def move_right(length):
    PressKey(LSHIFT)
    PressKey(D)
    time.sleep(length)
    ReleaseKey(D)
    ReleaseKey(LSHIFT)


def get_ingredient_coords(ingredient):
    if( ingredient =='nether_wart'):
        coords = pyautogui.locateOnScreen('./images/nether_wart_ingredient.png', region=(0,0,800,640))
    elif ingredient == 'ingredient1':
        coords = pyautogui.locateOnScreen('./images/sugar_ingredient.png', region=(0, 0, 800, 640))
    elif ingredient == 'ingredient2':
        coords = pyautogui.locateOnScreen('./images/glowstone_ingredient.png', region=(0, 0, 800, 640))
    elif ingredient == 'ingredient3':
        coords = pyautogui.locateOnScreen('./images/gunpowder_ingredient.png', region=(0, 0, 800, 640))
    else:
        coords = None
    if coords == None :
        print("No ", ingredient)
    else:
        x, y, a, b = coords
        print("Ingredient ", ingredient," stack location : ", x, y, a, b)
        return coords
    return -1


def get_ingredients():
    try:
        nw_coords  = get_ingredient_coords('nether_wart')
        i1_coords = get_ingredient_coords('ingredient1')
        i2_coords = get_ingredient_coords('ingredient2')
        i3_coords = get_ingredient_coords('ingredient3')
        return nw_coords, i1_coords, i2_coords, i3_coords
    except:
        print('Missing ingredients!')
        return -1, -1, -1, -1


def prepare_window():
    minecraft_window = gw.getWindowsWithTitle('Minecraft* 1.15.2 - Multiplayer (3rd-party)')[0]
    #minecraft_window = gw.getWindowsWithTitle('Minecraft 1.16.1 - Singleplayer')[0]
    minecraft_window.resizeTo(800, 640)
    minecraft_window.moveTo(0, 0)


def reset_mouse():
    pyautogui.moveTo(700,540)


def add_ingredient(coords):
    # add ingredient
    PressKey(LSHIFT)
    pyautogui.moveTo(coords)
    pyautogui.moveRel(coords[2]/2, coords[3]/2)
    pyautogui.rightClick()
    ReleaseKey(LSHIFT)
    reset_mouse()
    print("Added ingredient")


def drop_potions():
    pyautogui.moveTo(350, 286)
    PressKey(Q)
    time.sleep(0.1)
    ReleaseKey(Q)
    pyautogui.moveTo(398, 300)
    PressKey(Q)
    time.sleep(0.1)
    ReleaseKey(Q)
    pyautogui.moveTo(444, 292)
    PressKey(Q)
    time.sleep(0.1)
    ReleaseKey(Q)
    reset_mouse()


def is_ingredient_coords_ok(coords):
    region = (coords[0], coords[1], coords[0] + coords[2], coords[1] + coords[3])
    print('region:', region)
    empty = pyautogui.locateOnScreen('./images/empty_slot.png', region=region)
    if empty:
        print("empty:", empty)
        return False
    return True


def exit_bs():
    PressKey(E)
    time.sleep(0.1)
    ReleaseKey(E)


def serve_brewing_stand(i_coords, first):
    if i_coords == -1:
        print("No ingredients!")
        return False # find new ingredients
    if first:
        bottles = pyautogui.locateOnScreen('./images/three_water_bottles.png', region=(0, 0, 800, 640))
    else:
        bottles = True
    if bottles:
        ready_to_brew = pyautogui.locateOnScreen('./images/empty_brewing_slot.png', region=(0, 0, 800, 640))
        if ready_to_brew:
            print("Bottles are present!")
            add_ingredient(i_coords)


def serve_brewing_stand_old():
    nw_coords, ingredient1, ingredient2, ingredient3 = get_ingredients()
    if nw_coords == -1 or ingredient1 == -1 or ingredient2 == -1:
        print("No ingredients!")
        return
    bottles = pyautogui.locateOnScreen('./images/three_water_bottles.png', region=(0, 0, 800, 640))
    #here loop
    bottles_error = 0
    while bottles_error < 60:
        bottles = pyautogui.locateOnScreen('./images/three_water_bottles.png', region=(0,0,800,640))
        if bottles != None:
            print("Bottles are present!")
            #check ingredient coords
            if is_ingredient_coords_ok(nw_coords, ingredient1, ingredient2, ingredient3):
                print("Empty ingredient. Find new!")
                nw_coords, ingredient1, ingredient2, ingredient3 = get_ingredients()
                if nw_coords == -1 or ingredient1 == -1 or ingredient2 == -1:
                    print("No ingredients!")
                    return
            else:
                print("Ingredient still there!")

            add_ingredient(nw_coords)
            add_ingredient(ingredient1)
            add_ingredient(ingredient2)
            if ingredient3 != -1 and ingredient3 is not None:
                add_ingredient(ingredient3)
            print("ready to drop potions")
            drop_potions()
            time.sleep(1)
            PressKey(E)
            time.sleep(0.1)
            ReleaseKey(E)
            pyautogui.rightClick()
            reset_mouse()
            time.sleep(0.5)
        else:
            bottles_error += 1
            time.sleep(5)
            PressKey(E)
            time.sleep(0.1)
            ReleaseKey(E)
            pyautogui.rightClick()
            reset_mouse()
            time.sleep(0.5)
            print("Bottles not present!")

def get_ingredient(i_type):
    if i_type == 0:
        ingredient = 'nether_wart'
    elif i_type == 1:
        ingredient = 'ingredient1'
    elif i_type == 2:
        ingredient = 'ingredient2'
    elif i_type == 3:
        ingredient = 'ingredient3'
    else:
        ingredient = 'unknown'
    try:
        return get_ingredient_coords(ingredient)
    except:
        print('Missing ingredient ', ingredient ,'!')
        return -1



def open_stand():
    #pyautogui.rightClick()
    pydirectinput.rightClick()
    time.sleep(0.1)
    #reset_mouse()
    stand_image = pyautogui.locateOnScreen('./images/brewing_stand_label.png', region=(0, 40, 800, 640))
    if stand_image is not None:
        print("Brewing stand found!")
        reset_mouse()
        return True
    else:
        print("Brewing stand not found!")
        return False

#brewing ready
def ready():
    if pyautogui.locateOnScreen('./images/empty_brewing_slot.png', region=(0, 40, 800, 640)):
        return True
    return False

def alternate_bs(nw_with_drop):
    #prepare ingredients
    open_stand()
    nw_coords, ingredient1, ingredient2, ingredient3 = get_ingredients()
    exit_bs()
    coords = [nw_coords, ingredient1, ingredient2, ingredient3]
    if nw_coords == -1 or ingredient1 == -1 or ingredient2 == -1 or ingredient3 == -1:
        print("No ingredients!")
        return
    for k in range(11):
        error = 0
        for j, coord in enumerate(coords):
            if j == 0 and nw_with_drop:
                continue
            i = 1
            while i < 6:
                while not open_stand() and error < 30:
                    error += 1
                    if i % 5 == 0:
                        pydirectinput.moveRel(-3, 0)
                    else:
                        pydirectinput.moveRel(3, 0)
                    print("trying to find brewing stand...")
                while not ready() and error < 30:
                    print("waiting to finish brewing!")
                    time.sleep(2)
                if error >= 30:
                    return
                if j == 0:
                    first = True
                else:
                    first = False
                reset_mouse()
                print(coord)
                serve_brewing_stand(coord, first)
                exit_bs()
                time.sleep(0.1)
                if i % 5 == 0:
                    print(i)
                    pydirectinput.moveTo(399, 334)
                    pydirectinput.moveTo(401, 334)
                    pydirectinput.moveRel(-390, 0)
                    pydirectinput.moveRel(-130, 0)
                    print("moved 780")
                else:
                    pydirectinput.moveTo(401, 334)
                    pydirectinput.moveTo(399, 334)
                    pydirectinput.moveRel(130, 0)
                #time.sleep(0.1)
                i+=1
        print("ready to drop potions")
        i = 1
        while i < 6:
            open_stand()
            while not ready():
                print("waiting to finish brewing!")
                time.sleep(1)
            drop_potions()
            add_ingredient(nw_coords)
            nw_with_drop = True
            exit_bs()
            time.sleep(0.1)
            if i % 5 == 0:
                pydirectinput.moveTo(399, 334)
                pydirectinput.moveTo(401, 334)
                pydirectinput.moveRel(-390, 0)
                pydirectinput.moveRel(-130, 0)
                #reset screen
                reset_pos = pyautogui.locateOnScreen('./images/reseting_screen_5.png', region=(0, 40, 800, 640), confidence=0.6)
                if reset_pos:
                    print("reseting screen!")
                    print(reset_pos)
                    #pydirectinput.moveTo(reset_pos[0]+135, reset_pos[1]+256)
                    pydirectinput.moveTo(reset_pos[0] + 77, reset_pos[1] + 249)
            else:
                pydirectinput.moveTo(401, 334)
                pydirectinput.moveTo(399, 334)
                pydirectinput.moveRel(130, 0)
            time.sleep(0.2)
            i += 1
    return nw_with_drop

def fill_water():
    time.sleep(4)
    for i in range(9):
        bottles = pyautogui.locateOnScreen('./images/empty_bottle.png', region=(0, 40, 800, 640), confidence=0.9)
        if bottles:
            pydirectinput.mouseDown(button='right')
            bottles_reg = (bottles[0], bottles[1], bottles[0] + bottles[2], bottles[1] + bottles[3])
            while True:
                water_bottle = pyautogui.locateOnScreen('./images/filled_bottle.png', region=bottles_reg, confidence=0.68)
                if water_bottle:
                    print('filled')
                    break
        pydirectinput.mouseUp(button='right')

def main():
    #pyautogui.mouseInfo()
    prepare_window()
    last_time = time.time()
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)
    print(pyautogui.position())
    paused = False
    for i in range(1):
        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(0, 40, 800, 640))
            print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)c
            #cv2.imshow('window', screen)
            #text = pytesseract.image_to_string(img)
            nw_with_drop = True
            for j in range(8):
                nw_with_drop = alternate_bs(nw_with_drop)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                ccv2.destroyAllWindows()
                break
    return 0





main()


