import logging
from typing import Optional, Union

from ntgcalls import FileError

from ...exceptions import ClientNotStarted, NoMTProtoClientSet, NotInGroupCallError
from ...scaffold import Scaffold
from ...to_async import ToAsync
from ...types import ChangedStream
from ...types.input_stream.stream import Stream
from ..utilities.stream_params import StreamParams

py_logger = logging.getLogger("ryuzakilib")


class ChangeStream(Scaffold):
    async def change_stream(
        self,
        chat_id: Union[int, str],
        stream: Optional[Stream] = None,
    ):
        if self._app is None:
            raise NoMTProtoClientSet()

        if not self._is_running:
            raise ClientNotStarted()

        chat_id = await self._resolve_chat_id(chat_id)
        try:
            await ToAsync(
                self._binding.change_stream,
                chat_id,
                await StreamParams.get_stream_params(stream),
            )
        except FileError:
            raise FileNotFoundError()
        except Exception:
            raise NotInGroupCallError()

        await self._on_event_update.propagate(
            "RAW_UPDATE_HANDLER",
            self,
            ChangedStream(chat_id),
        )
