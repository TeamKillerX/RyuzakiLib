import random
from .anime import *
from .waifu import *
from .browsers import Browsers
from .cache import Cache
from .groups import AlreadyJoined
from .groups import ErrorDuringJoin
from .groups import GroupCall
from .groups import GroupCallParticipant
from .groups import JoinedGroupCallParticipant
from .groups import JoinedVoiceChat
from .groups import LeftGroupCallParticipant
from .groups import LeftVoiceChat
from .groups import MutedCall
from .groups import NotInGroupCall
from .groups import UpdatedGroupCallParticipant
from .groups import UpgradeNeeded
from .input_stream import AudioImagePiped
from .input_stream import AudioParameters
from .input_stream import AudioPiped
from .input_stream import AudioQuality
from .input_stream import AudioVideoPiped
from .input_stream import CaptureAudioDevice
from .input_stream import CaptureAVDesktop
from .input_stream import CaptureAVDeviceDesktop
from .input_stream import CaptureVideoDesktop
from .input_stream import InputAudioStream
from .input_stream import InputStream
from .input_stream import InputVideoStream
from .input_stream import VideoParameters
from .input_stream import VideoPiped
from .input_stream import VideoQuality
from .input_stream.quality import HighQualityAudio
from .input_stream.quality import HighQualityVideo
from .input_stream.quality import LowQualityAudio
from .input_stream.quality import LowQualityVideo
from .input_stream.quality import MediumQualityAudio
from .input_stream.quality import MediumQualityVideo
from .stream import ChangedStream
from .stream import MutedStream
from .stream import PausedStream
from .stream import ResumedStream
from .stream import StreamAudioEnded
from .stream import StreamDeleted
from .stream import StreamVideoEnded
from .stream import UnMutedStream
from .update import Update

from .translated_object import TranslatedObject
from .base_translator import BaseTranslator

DEFAULT_TRANSLATION_ENDPOINT: str = "https://translate.google.com/translate_a/single"
DEFAULT_TTS_ENDPOINT: str = "https://translate.google.com/translate_tts"

class Device:
    DEVICES: tuple = (
        "Linux; U; Android 10; Pixel 4",
        "Linux; U; Android 10; Pixel 4 XL",
        "Linux; U; Android 10; Pixel 4a",
        "Linux; U; Android 10; Pixel 4a XL",
        "Linux; U; Android 11; Pixel 4",
        "Linux; U; Android 11; Pixel 4 XL",
        "Linux; U; Android 11; Pixel 4a",
        "Linux; U; Android 11; Pixel 4a XL",
        "Linux; U; Android 11; Pixel 5",
        "Linux; U; Android 11; Pixel 5a",
        "Linux; U; Android 12; Pixel 4",
        "Linux; U; Android 12; Pixel 4 XL",
        "Linux; U; Android 12; Pixel 4a",
        "Linux; U; Android 12; Pixel 4a XL",
        "Linux; U; Android 12; Pixel 5",
        "Linux; U; Android 12; Pixel 5a",
        "Linux; U; Android 12; Pixel 6",
        "Linux; U; Android 12; Pixel 6 Pro",
    )

    __i = 0

    @classmethod
    def shift(cls) -> str:
        cls.__i += 1
        cls.__i %= len(cls.DEVICES)
        return cls.DEVICES[cls.__i]

def get_base_headers() -> dict:
    return {
        "User-Agent": "GoogleTranslate/6.28.0.05.421483610 ({device})".format(
            device=Device.shift(),
        )
    }

__all__ = [
    "AlreadyJoined",
    "AudioParameters",
    "AudioImagePiped",
    "AudioPiped",
    "AudioQuality",
    "AudioVideoPiped",
    "Browsers",
    "Cache",
    "ChangedStream",
    "ErrorDuringJoin",
    "GroupCall",
    "GroupCallParticipant",
    "HighQualityAudio",
    "HighQualityVideo",
    "InputAudioStream",
    "InputStream",
    "InputVideoStream",
    "JoinedGroupCallParticipant",
    "JoinedVoiceChat",
    "LowQualityAudio",
    "LowQualityVideo",
    "LeftGroupCallParticipant",
    "LeftVoiceChat",
    "MutedStream",
    "MediumQualityAudio",
    "MediumQualityVideo",
    "NotInGroupCall",
    "PausedStream",
    "ResumedStream",
    "StreamAudioEnded",
    "StreamDeleted",
    "StreamVideoEnded",
    "UnMutedStream",
    "UpdatedGroupCallParticipant",
    "Update",
    "CaptureAudioDevice",
    "CaptureAVDesktop",
    "CaptureAVDeviceDesktop",
    "CaptureVideoDesktop",
    "VideoParameters",
    "VideoPiped",
    "VideoQuality",
    "UpgradeNeeded",
    "MutedCall"
]
