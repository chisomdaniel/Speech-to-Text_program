import speech_recognition as sr
'''A voice to text program. accepts users audio input and
display the translated text from the audio.

This program allows you to use an audio file,
or provide a live input from your laptop mic.

If you want to use a different audio file,
save the name in the appropriate variable `audio_file`,
and ensure the audio file format is of type `.wav` and
it is saved to the same file locaton as this python program

To use the live input option,
Wait for the '[speak now...]' prompt before speaking.
Say 'quit' to end the program.
'''

print("Do you want to use the default audio file,\nor you want to provide live input with your mic?\n")
ans = input("[Enter 1 for audio file or 2 for live input]: ")
try:
    ans = int(ans)
except:
    print("You did not select a valid option, please try again")
    exit()

if ans not in [1, 2]:
    print("You did not select a valid option, please try again")
    exit()

r = sr.Recognizer()

print('Getting Ready...\n')
print('Good day Master! give me a sec to set up...')

audio_file = 'speech_to_text_audio.wav'
error_count = 0
run = True
while run:

    if ans == 1:
        mic = sr.AudioFile(audio_file)
    else:
        mic = sr.Microphone()

    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            if ans == 1:
                audio = r.record(source)
                result = r.recognize_google(audio, show_all=True)
                text = result['alternative'][0]['transcript']
                print("[Here's your result]:")
                print(text)
                break
            else:
                print("[speak now...]")
                audio = r.listen(source)

        result = r.recognize_google(audio, show_all=True)

        text = result['alternative'][0]['transcript']  # display only the most likely transcription
        if text.lower() == 'quit':
            run = False
        else:
            print(text)
            error_count = 0
        print("<say something else or say 'quit' to end>")
    except sr.RequestError:  # if there is no internet connection
        print("I am having issues connecting to the internet.\nPlease ensure your device is well connected to the internet")
        run = False
    except:  # if not voice can be detected by the microphone
        if ans == 2:
            print("<I didn't quite get what you said, please come again>")
            error_count += 1
            if error_count == 5:  # Quit the program if unable to identify user's voice 5 times in a row
                print("Please ensure your microphone is connected properly and functional.")
                run = False
