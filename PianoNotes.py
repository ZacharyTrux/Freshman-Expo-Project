import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(13)

notesList = ["C4", "C#4/Db4", "D4", "D#/Eb4", "E4", "F4", "F#4/Gb4", "G4", "G#4/Ab4", "A4", "A#4/Bb4", "B4", "C5"]
keys_dict = {num_keys: notesList[num_keys] for num_keys in range(0, 13)}
channelDict = {}

for i in range(0, 13):
    channelDict[i] = pygame.mixer.Channel(i)


# print(channelDict)

while True:
    # for i in range(0, 13):
    #     print(f"Channel: {i} = {channelDict[i]}")
    for i in range(0, 13):
        if channelDict[i].get_busy() == False:
            noteToPlay = keys_dict[i]
            noteToPlay = noteToPlay.replace("/", '')
            note = pygame.mixer.Sound(f"notes/{noteToPlay}.wav")
            channelDict[i].play(note)