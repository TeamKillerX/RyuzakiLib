from deprecation import deprecated
from ntgcalls import InputMode

from .audio_parameters import AudioParameters
from .audio_stream import AudioStream


@deprecated(
    deprecated_in='1.0.0.dev1',
    details='Use pytgcalls.types.AudioStream instead.',
)
class InputAudioStream(AudioStream):
    def __init__(
        self,
        path: str,
        parameters: AudioParameters = AudioParameters(),
        header_enabled: bool = False,
    ):
        super().__init__(InputMode.File, path, parameters)
        self.header_enabled = header_enabled
