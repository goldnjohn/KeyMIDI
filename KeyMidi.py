# Numpad_MIDI

# version 0.0.1

# A simple program that uses PC Numpad and sends MIDI Notes. It can be useful to switch tracks with ease 

# Dependencies pynput and rtmidi libraries

import pynput
import rtmidi

global switch

def sec_A_On(ke):
    global switch
    print('{0} pressed'.format(ke)) # printing whatever key is pressed
    if ke == pynput.keyboard.Key.right: #First Test
        midiout.send_message([0x90, 60, 112])
    if hasattr(ke, 'vk') and ke.vk ==106 :  # Numpad *  Changing Sec_A to Sec_B
        if switch == 2:
            return False
        else:
            switch = 1
            b()
    if hasattr(ke, 'vk') and ke.vk ==109 :  # Numpad -  Changing Sec_A to Sec_C
        if switch == 3:
            return False
        else:
            switch = 1
            c()
    if hasattr(ke, 'vk') and ke.vk ==107 :  # Numpad +  Changing Sec_A to Sec_D
        if switch == 4:
            return False
        else:
            switch = 1
            d()
    if hasattr(ke, 'vk') and ke.vk == 96 :  # Numpad 0
        midiout.send_message([0x90, 12, 1])  # (Note-on,C-0,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 97 :  # Numpad 1
        midiout.send_message([0x90, 13, 1])  # (Note-on,C#-0,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 98 :  # Numpad 2
        midiout.send_message([0x90, 14, 1])  # (Note-on,D-0,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 99 :  # Numpad 3
        midiout.send_message([0x90, 15, 1])  # (Note-on,D#-0,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x90, 16, 1])  # (Note-on,E-0,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x90, 17, 1])  # (Note-on,F-0,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x90, 18, 1])  # (Note-on,F#-0,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x90, 19, 1])  # (Note-on,G-0,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x90, 20, 1])  # (Note-on,G#-0,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x90, 21, 1])  # (Note-on,A-0,Volume 1)
 
def sec_A_Off(ke):
    print('{0} release'.format(ke)) # printing whatever key is pressed
    if ke == pynput.keyboard.Key.right: # First Test
        midiout.send_message([0x80, 60, 0])
    if ke == pynput.keyboard.Key.esc: # Emergency Exit
        return False
    if hasattr(ke, 'vk') and ke.vk == 96 : # Numpad 0
        midiout.send_message([0x80, 12, 0])  # (Note-off,C-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 97 : # Numpad 1
        midiout.send_message([0x80, 13, 0])  # (Note-off,C#-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 98 : # Numpad 2
        midiout.send_message([0x80, 14, 0])  # (Note-off,D-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 99 : # Numpad 3
        midiout.send_message([0x80, 15, 0])  # (Note-off,D#-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x80, 16, 0])  # (Note-off,E-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x80, 17, 0])  # (Note-off,F-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x80, 18, 0])  # (Note-off,F#-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x80, 19, 0])  # (Note-off,G-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x80, 20, 0])  # (Note-off,G#-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x80, 21, 0])  # (Note-off,A-0,Volume 0)

def sec_B_On(ke):
    global switch
    print('{0} pressed'.format(ke)) # printing whatever key is pressed
    if hasattr(ke, 'vk') and ke.vk ==111 :  # Numpad /  Changing Sec_B to Sec_A
        if switch == 1:
            return False
        else:
            switch = 2
            a()
    if hasattr(ke, 'vk') and ke.vk ==109 :  # Numpad -  Changing Sec_B to Sec_C
        if switch == 3:
            return False
        else:
            switch = 2
            c()
    if hasattr(ke, 'vk') and ke.vk ==107 :  # Numpad +  Changing Sec_B to Sec_D
        if switch == 4:
            return False
        else:
            switch = 2
            d()
    if hasattr(ke, 'vk') and ke.vk == 96 :  # Numpad 0
        midiout.send_message([0x90, 22, 1])  # (Note-on,A#-0,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 97 :  # Numpad 1
        midiout.send_message([0x90, 23, 1])  # (Note-on,B-0,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 98 :  # Numpad 2
        midiout.send_message([0x90, 24, 1])  # (Note-on,C-1,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 99 :  # Numpad 3
        midiout.send_message([0x90, 25, 1])  # (Note-on,C#-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x90, 26, 1])  # (Note-on,D-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x90, 27, 1])  # (Note-on,D#-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x90, 28, 1])  # (Note-on,E-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x90, 29, 1])  # (Note-on,F-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x90, 30, 1])  # (Note-on,F#-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x90, 31, 1])  # (Note-on,G-1,Volume 1)
 
def sec_B_Off(ke):
    print('{0} release'.format(ke)) # printing whatever key is pressed
    if ke == pynput.keyboard.Key.esc: # Emergency Exit
        return False
    if hasattr(ke, 'vk') and ke.vk == 96 : # Numpad 0
        midiout.send_message([0x80, 22, 0])  # (Note-off,A#-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 97 : # Numpad 1
        midiout.send_message([0x80, 23, 0])  # (Note-off,B-0,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 98 : # Numpad 2
        midiout.send_message([0x80, 24, 0])  # (Note-off,C-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 99 : # Numpad 3
        midiout.send_message([0x80, 25, 0])  # (Note-off,C#-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x80, 26, 0])  # (Note-off,D-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x80, 27, 0])  # (Note-off,D#-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x80, 28, 0])  # (Note-off,E-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x80, 29, 0])  # (Note-off,F-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x80, 30, 0])  # (Note-off,F#-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x80, 31, 0])  # (Note-off,G-1,Volume 0)

def sec_C_On(ke):
    global switch
    print('{0} pressed'.format(ke)) # printing whatever key is pressed
    if hasattr(ke, 'vk') and ke.vk ==111 :  # Numpad /  Changing Sec_C to Sec_A
        if switch == 1:
            return False
        else:
            switch = 3
            a()
    if hasattr(ke, 'vk') and ke.vk ==106 :  # Numpad *  Changing Sec_C to Sec_B
        if switch == 2:
            return False
        else:
            switch = 3
            b()
    if hasattr(ke, 'vk') and ke.vk ==107 :  # Numpad +  Changing Sec_C to Sec_D
        if switch == 4:
            return False
        else:
            switch = 3
            d()
    if hasattr(ke, 'vk') and ke.vk == 96 :  # Numpad 0
        midiout.send_message([0x90, 32, 1])  # (Note-on,G#-1,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 97 :  # Numpad 1
        midiout.send_message([0x90, 33, 1])  # (Note-on,A-1,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 98 :  # Numpad 2
        midiout.send_message([0x90, 34, 1])  # (Note-on,A#-1,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 99 :  # Numpad 3
        midiout.send_message([0x90, 35, 1])  # (Note-on,B-1,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x90, 36, 1])  # (Note-on,C-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x90, 37, 1])  # (Note-on,C#-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x90, 38, 1])  # (Note-on,D-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x90, 39, 1])  # (Note-on,D#-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x90, 40, 1])  # (Note-on,E-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x90, 41, 1])  # (Note-on,F-2,Volume 1)
 
def sec_C_Off(ke):
    print('{0} release'.format(ke)) # printing whatever key is pressed
    if ke == pynput.keyboard.Key.esc: # Emergency Exit
        return False
    if hasattr(ke, 'vk') and ke.vk == 96 : # Numpad 0
        midiout.send_message([0x80, 32, 0])  # (Note-off,G#-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 97 : # Numpad 1
        midiout.send_message([0x80, 33, 0])  # (Note-off,A-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 98 : # Numpad 2
        midiout.send_message([0x80, 34, 0])  # (Note-off,A#-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 99 : # Numpad 3
        midiout.send_message([0x80, 35, 0])  # (Note-off,B-1,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x80, 36, 0])  # (Note-off,C-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x80, 37, 0])  # (Note-off,C#-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x80, 38, 0])  # (Note-off,D-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x80, 39, 0])  # (Note-off,D#-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x80, 40, 0])  # (Note-off,E-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x80, 41, 0])  # (Note-off,F-2,Volume 0)

def sec_D_On(ke):
    global switch
    print('{0} pressed'.format(ke)) # printing whatever key is pressed
    if hasattr(ke, 'vk') and ke.vk ==111 :  # Numpad /  Changing Sec_D to Sec_A
        if switch == 1:
            return False
        else:
            switch = 4
            a()
    if hasattr(ke, 'vk') and ke.vk ==106 :  # Numpad *  Changing Sec_D to Sec_B
        if switch == 2:
            return False
        else:
            switch = 4
            b()
    if hasattr(ke, 'vk') and ke.vk ==109 :  # Numpad -  Changing Sec_D to Sec_C
        if switch == 3:
            return False
        else:
            switch = 4
            c()
    if hasattr(ke, 'vk') and ke.vk == 96 :  # Numpad 0
        midiout.send_message([0x90, 42, 1])  # (Note-on,F#-2,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 97 :  # Numpad 1
        midiout.send_message([0x90, 43, 1])  # (Note-on,G-2,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 98 :  # Numpad 2
        midiout.send_message([0x90, 44, 1])  # (Note-on,G#-2,Volume 1) 
    if hasattr(ke, 'vk') and ke.vk == 99 :  # Numpad 3
        midiout.send_message([0x90, 45, 1])  # (Note-on,A-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x90, 46, 1])  # (Note-on,A#-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x90, 47, 1])  # (Note-on,B-2,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x90, 48, 1])  # (Note-on,C-3,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x90, 49, 1])  # (Note-on,C#-3,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x90, 50, 1])  # (Note-on,D-3,Volume 1)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x90, 51, 1])  # (Note-on,D#-3,Volume 1)
 
def sec_D_Off(ke):
    print('{0} release'.format(ke)) # printing whatever key is pressed
    if ke == pynput.keyboard.Key.esc: # Emergency Exit
        return False   
    if hasattr(ke, 'vk') and ke.vk == 96 : # Numpad 0
        midiout.send_message([0x80, 42, 0])  # (Note-off,F#-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 97 : # Numpad 1
        midiout.send_message([0x80, 43, 0])  # (Note-off,G-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 98 : # Numpad 2
        midiout.send_message([0x80, 44, 0])  # (Note-off,G#-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 99 : # Numpad 3
        midiout.send_message([0x80, 45, 0])  # (Note-off,A-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 100 : # Numpad 4
        midiout.send_message([0x80, 46, 0])  # (Note-off,A#-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 101 : # Numpad 5
        midiout.send_message([0x80, 47, 0])  # (Note-off,B-2,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 102 : # Numpad 6
        midiout.send_message([0x80, 48, 0])  # (Note-off,C-3,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 103 : # Numpad 7
        midiout.send_message([0x80, 49, 0])  # (Note-off,C#-3,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 104 : # Numpad 8
        midiout.send_message([0x80, 50, 0])  # (Note-off,D-3,Volume 0)
    if hasattr(ke, 'vk') and ke.vk == 105 : # Numpad 9
        midiout.send_message([0x80, 51, 0])  # (Note-off,D#-3,Volume 0)
def a():
    sec_A = pynput.keyboard.Listener(on_press=sec_A_On,on_release=sec_A_Off)
    sec_A.start()
    sec_A.join()
def b():
    sec_B = pynput.keyboard.Listener(on_press=sec_B_On,on_release=sec_B_Off)
    sec_B.start()
    sec_B.join()
def c():
    sec_C = pynput.keyboard.Listener(on_press=sec_C_On,on_release=sec_C_Off)
    sec_C.start()
    sec_C.join()
def d():
    sec_D = pynput.keyboard.Listener(on_press=sec_D_On,on_release=sec_D_Off)
    sec_D.start()
    sec_D.join()

switch = 1
# opening port
midiout = rtmidi.MidiOut()
midiout.open_port(1)
a()    