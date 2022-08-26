import chunk
import speech_recognition as sr
import os
import re
from pydub import AudioSegment
from pydub.silence import split_on_silence


def silencebasedconversion(path):
    """Split audio file into chunk based on silence
    Args:
        path (str): Path to audio file. Format should be .wav only
    """
    audio = AudioSegment.from_wav(path)

    chunk_save_path = "sample_audio/audio_chunks"
    recognised_text_file = "sample_audio/recognized.txt"
    fh = open(recognised_text_file, "w+")
    
    # split on silences longer than 1000ms (1 sec)
    min_silence_len=1000
    # anything under -16 dBFS is considered silence
    silence_thresh=-17
    # keep 200 ms of leading/trailing silence
    keep_silence=200
    
    if len(audio)>90000:
        # Split audio into chunks if audio length is greater than 9000ms
        chunks = split_on_silence(audio, min_silence_len = min_silence_len, silence_thresh = silence_thresh, keep_silence=keep_silence)
    else:
        chunks = [audio]

    if not os.path.exists(chunk_save_path):
        os.mkdir(chunk_save_path)

    # os.chdir(chunk_save_path)
    i = 0
    for ck in chunks:
        chunksilent = AudioSegment.silent(duration = 10)
        audio_chunk = chunksilent + ck + chunksilent
        print("saving chunk{0}.wav".format(i))
        filename = "{1}/chunk{0}.wav".format(i, chunk_save_path)
        audio_chunk.export(filename, format ="wav")
        print("Processing chunk "+str(i))
        file = filename
        r = sr.Recognizer()
        with sr.AudioFile(file) as source:
            r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)
            try:
                rec = r.recognize_google(audio_listened)
                fh.write(rec+". ")
                fh.flush()
            except sr.UnknownValueError:
                print("Audio is not understandable")
            except sr.RequestError as e:
                print("Could not request results. check the internet connection")

        i += 1

    fh.close()

def search_text(search_keyword) -> int:
    """Search for given keyword and return number of occurance of the word. O is none (character case is ignored)
    Args:
        search_keyword (str): string word to search inside audio transcript.
    """

    transcript_file_path = "sample_audio/recognized.txt"

    occurances = 0
    with open(transcript_file_path, "r")  as f:
        text = f.read()
        
        result = re.findall(f"({search_keyword})", text)
        occurances = len(result)

    print(f"Yeah!! Keyword found.....\nKeyword: {search_keyword}, No. of occurances: {occurances}")
    return occurances

if __name__ == '__main__':                          
    print('Please provide the audio file path')
    # file_path = input()
    keyword = "Ajay"
    sound=AudioSegment.from_mp3("sample_audio/test_audio.mp3")
    sound.export("sample_audio/transcript.wav",format="wav")
    AUDIO_FILE="sample_audio/transcript.wav"
    silencebasedconversion(AUDIO_FILE)
    search_text(keyword)
