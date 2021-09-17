# KeyMIDI
A python Script which allows to use Numpad as MIDI Pad<br>

# Releases
Download KeyMIDI.py file from [here](https://github.com/goldnjohn/KeyMIDI/blob/main/KeyMidi.py)

# Features
* Numpad can be transformed into a MIDI pad
* It allows upto 40 keys (10x4) range from `C0` to `D#3` that you can assign to anything in your DAW
* Numpad is divided into 4 Sections

<img alt="shot" src="./Assets/Numpad.jpg" width="300" height="400">
* Keys in the section are as follows
 
 <img alt="shot" src="./Assets/Numpad1.png" width="300" height="400">       <img alt="shot" src="./Assets/Numpad2.png" width="300" height="400"> <br>
 
 <img alt="shot" src="./Assets/Numpad3.png" width="300" height="400">       <img alt="shot" src="./Assets/Numpad4.png" width="300" height="400">
    
# Usage
* Install `pynput` and `rtmidi` libraries through pip3 
* Download LoopMIDI application from [here](http://www.tobias-erichsen.de/wp-content/uploads/2020/01/loopMIDISetup_1_0_16_27.zip)
* Create a virtual port inside loopMIDI
* Run `KeyMIDI.exe` 
* Enter virtual port number of loopMIDI when asked

# Dependencies
* pynput
* rtmidi

# Issues
Optimized for fast switching between keys but between section might have some latency (to be fixed in future updates)

