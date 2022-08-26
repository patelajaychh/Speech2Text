# Speech to Text App
This application accepts any mp3 file, transcibe in into text. User can also find a keyword if present in audio or not.


## Installation
Befor running this app make sure to run below commands - 
```bash
# On ubuntu 20.04LTS
sudo apt install portaudio19-dev python3-pyaudio 

# On ubuntu 18.05LTS
sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio 

sudo apt-get install -y  build-essential swig git libpulse-dev
```

After successfully running above commands, install requied python libraries - 

    pip3 install -r requirements.txt


After installing libraries, clone this repository and execute - 
```bash
cd <root>/Speech2Text
python3 stt_app.py
```



# REFERENCE
* https://pdf.co/blog/transcribe-speech-recordings-to-text-python 
* https://betterprogramming.pub/create-searchable-audio-using-python-78b5afc5122