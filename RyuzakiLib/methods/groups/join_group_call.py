import logging
from typing import Optional
from typing import Union

from ntgcalls import ConnectionError
from ntgcalls import FileError
from ntgcalls import InvalidParams

from ...exceptions import AlreadyJoinedError
from ...exceptions import ClientNotStarted
from ...exceptions import NoActiveGroupCall
from ...exceptions import NoMTProtoClientSet
from ...exceptions import TelegramServerError
from ...exceptions import UnMuteNeeded
from ...mtproto import BridgedClient
from ...scaffold import Scaffold
from ...to_async import ToAsync
from ...types import JoinedVoiceChat
from ...types.input_stream.stream import Stream
from ..utilities.stream_params import StreamParams

py_logger = logging.getLogger('pytgcalls')


class JoinGroupCall(Scaffold):
    async def join_group_call(
        self,
        chat_id: Union[int, str],
        stream: Optional[Stream] = None,
        invite_hash: str = None,
        join_as=None,
    ):
        if join_as is None:
            join_as = self._cache_local_peer

        chat_id = await self._resolve_chat_id(chat_id)
        self._cache_user_peer.put(chat_id, join_as)

        if self._app is None:
            raise NoMTProtoClientSet()

        if not self._is_running:
            raise ClientNotStarted()

        chat_call = await self._app.get_full_chat(
            chat_id,
        )
        if chat_call is None:
            raise NoActiveGroupCall()

        media_description = await StreamParams.get_stream_params(
            stream,
        )

        try:
            call_params: str = await ToAsync(
                self._binding.create_call,
                chat_id,
                media_description,
            )

            result_params = await self._app.join_group_call(
                chat_id,
                call_params,
                invite_hash,
                media_description.video is None,
                self._cache_user_peer.get(chat_id),
            )

            await ToAsync(
                self._binding.connect,
                chat_id,
                result_params,
            )

            participants = await self._app.get_group_call_participants(
                chat_id,
            )

            for x in participants:
                if x.user_id == BridgedClient.chat_id(
                        self._cache_local_peer,
                ):
                    self._need_unmute[chat_id] = x.muted_by_admin

            await self._on_event_update.propagate(
                'RAW_UPDATE_HANDLER',
                self,
                JoinedVoiceChat(chat_id),
            )
        except FileError:
            raise FileNotFoundError()
        except ConnectionError:
            raise AlreadyJoinedError()
        except InvalidParams:
            raise UnMuteNeeded()
        except Exception:
            raise TelegramServerError()
