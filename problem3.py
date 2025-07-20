import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hello, i am sarvesh. I am a python developer. I am learning python from python ultimate course by code with harry.")
engine.runAndWait()