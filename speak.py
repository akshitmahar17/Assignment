from win32com.client import Dispatch

def speak(str):
    s = Dispatch("sapi.spvoice")
    s.speak(str)

if __name__ == '__main__':
    speak("A python program with artificial intelligence")