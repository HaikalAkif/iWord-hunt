#import
from pydub import AudioSegment
from pydub.playback import play
import multiprocessing

class MusicUtil:
    def __init__(self, music_path):
        self.music_path = music_path
        self.music_process = None

    def play_music(self):
        song = AudioSegment.from_mp3(self.music_path)
        play(song)

    def start_playback(self):
        self.music_process = multiprocessing.Process(target = self.play_music)
        self.music_process.start()

    def stop_playback(self):
        self.music_process.kill()
