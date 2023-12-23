from ..py_object import PyObject
from .audio_quality import AudioQuality


class AudioParameters(PyObject):
    def __init__(
        self,
        bitrate: int = 48000,
        channels: int = 1,
    ):
        max_bit, max_chan = max(AudioQuality, key=lambda x: x.value[0]).value
        self.bitrate: int = min(bitrate, max_bit)
        self.channels: int = min(channels, max_chan)

    @staticmethod
    def from_quality(quality: AudioQuality):
        return AudioParameters(*quality.value)
