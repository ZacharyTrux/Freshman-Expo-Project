from playsound import playsound
from pynput.keyboard import Key, Listener
from pynput import keyboard

## CONSTANTS ##
OCTAVE = 4
TRANSPOSE = 0

# Dictionary establishing the relationship between input its cooresponding output.
noteDict = {"q": f"C{OCTAVE}",  "2": f"Db{OCTAVE}", 
            "w": f"D{OCTAVE}",  "3": f"Eb{OCTAVE}",
            "e": f"E{OCTAVE}",  "r": f"F{OCTAVE}",
            "5": f"Gb{OCTAVE}", "t": f"G{OCTAVE}",
            "6": f"Ab{OCTAVE}", "y": f"A{OCTAVE}", 
            "7": f"Bb{OCTAVE}", "u": f"B{OCTAVE}", 
            "i": f"C{OCTAVE + 1}"}

noteDictKeyList = ["q", "2", "w", "3", "e", "r", "5", "t", "6", "y", "7", "u"]

# Dictionary establishing the frequencies of their respective notes.
frequencyDict = {f"C{OCTAVE}": 261.63, f"Db{OCTAVE}": 277.18, 
                 f"D{OCTAVE}": 293.66, f"Eb{OCTAVE}": 311.13, 
                 f"E{OCTAVE}": 329.63, f"F{OCTAVE}": 349.23, 
                 f"Gb{OCTAVE}": 369.99, f"G{OCTAVE}" : 392.00,
                 f"Ab{OCTAVE}": 415.30, f"A{OCTAVE}": 440.00, 
                 f"Bb{OCTAVE}": 466.16, f"B{OCTAVE}": 493.88,
                 f"C{OCTAVE + 1}": 523.25}

## FUNCTIONS ##
def on_press(key):
    global OCTAVE
    global noteDictValueList
    input = (str(key).replace("'", ""))

    if input == ",":
        if OCTAVE > 1:
            OCTAVE -= 1
        else:
            pass

        print(f"Octave +{OCTAVE}")

        noteDictValueList = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", f"C{OCTAVE + 1}"]

        dictValue = 0
        while dictValue < 10:
            for dictKey in noteDictKeyList:
                noteDict[dictKey] = noteDictValueList[dictValue] + f"{OCTAVE}"
                dictValue += 1

    elif input == ".":
        if OCTAVE < 7:
            OCTAVE += 1
        else:
            pass

        print(f"Octave +{OCTAVE}")
        
        noteDictValueList = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", f"C{OCTAVE + 1}"]

        dictValue = 0
        while dictValue < 10:
            for dictKey in noteDictKeyList:
                print(dictValue)
                noteDict[dictKey] = noteDictValueList[dictValue] + f"{OCTAVE}"
                dictValue += 1

    elif input == "/":
        print(noteDict)


    try:
        playsound(f'notes/{noteDict[input]}.wav', False)
    except:
        print("That's not a note!")

def on_release(key):
    #print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False
    
##### MAIN #####
# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()