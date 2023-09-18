# Tema L29 Python
# 1. Implementati o clasa MediaPlayer cu o singura metoda “reda” care primeste ca parametru un
# Video si apeleaza pe acest video metodele “playVideo”, “playAudio”. Implementati clasa Video
# care are 2 metode “playVideo” si “playAudio”. Fiecare metoda va face un print cu un text care
# descrie imaginea, respectiv sunetul. Implementati o clasa Audio care are o singura metoda
# numita “play” care face un print ce descrie sunetul. Implementati adaptorul necesar (o clasa
# care este si Audio si Video) astfel incat sa puteti creea un obiect de tip Audio dar care se
# comporta ca un video pe care il puteti trimite metodei “reda” din MediaPlayer

class MediaPlayer:
    def reda(self, video):
        video.playVideo()
        video.playAudio()

class Video:
    def playVideo(self):
        print("Redare video: imaginea este afișată.")

    def playAudio(self):
        print("Redare video: sunetul este redat.")

class Audio:
    def play(self):
        print("Redare audio: sunetul este redat.")

class AudioToVideoAdapter:
    def __init__(self, audio):
        self.audio = audio

    def playVideo(self):
        self.audio.play()

    def playAudio(self):
        self.audio.play()

media_player = MediaPlayer()

video = Video()
media_player.reda(video)


audio = Audio()
audio_adapter = AudioToVideoAdapter(audio)
media_player.reda(audio_adapter)