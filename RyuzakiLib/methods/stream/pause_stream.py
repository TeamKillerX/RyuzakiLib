from typing import Union

from ntgcalls import ConnectionError

from ...exceptions import ClientNotStarted
from ...exceptions import NoMTProtoClientSet
from ...exceptions import NotInGroupCallError
from ...scaffold import Scaffold
from ...to_async import ToAsync
from ...types import PausedStream


class PauseStream(Scaffold):
    async def pause_stream(
        self,
        chat_id: Union[int, str],
    ):
        if self._app is None:
            raise NoMTProtoClientSet()

        if not self._is_running:
            raise ClientNotStarted()

        chat_id = await self._resolve_chat_id(chat_id)
        try:
            status = await ToAsync(
                self._binding.pause,
                chat_id,
            )
            await self._on_event_update.propagate(
                'RAW_UPDATE_HANDLER',
                self,
                PausedStream(chat_id),
            )
            return status
        except ConnectionError:
            raise NotInGroupCallError()
