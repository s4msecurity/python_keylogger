import pynput.keyboard as Keyboard

ky = ""

def numpad(num):
    switch = {
        96 : "0",
        97 : "1",
        98 : "2",
        99 : "3",
        100 : "4",
        101 : "5",
        102 : "6",
        103 : "7",
        104 : "8",
        105 : "9"
    }
    return switch.get(num, "")

def scase (sc):
    switch = {
        Keyboard.Key.space : " ",
        Keyboard.Key.ctrl_l : " ctr_1 ",
        Keyboard.Key.alt_l : " alt_1 ",
        Keyboard.Key.ctrl_r : " ctr_r ",
        Keyboard.Key.shift : " shift ",
        Keyboard.Key.shift_r : " shift_r ",
        Keyboard.Key.caps_lock : " caps_lock ",
        Keyboard.Key.tab : " tab ",
        Keyboard.Key.esc : " esc ",
        Keyboard.Key.enter : "\n"
    }
    return switch.get(sc, "_")

def on_press(key):
    global ky
    try:
        if hasattr(key, 'vk') and 96 <= key.vk <= 105:
            ky = ky + numpad(key.vk)
        else:
            ky = ky + f'{key.char}'
    except AttributeError:    
        ky =  ky + scase(key)
    print(ky)

def on_release(key):
    if key == Keyboard.Key.esc:
        return False
 
with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()