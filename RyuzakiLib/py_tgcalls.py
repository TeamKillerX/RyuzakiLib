import atexit
from typing import Any

from ntgcalls import NTgCalls

from .environment import Environment
from .handlers import HandlersHolder
from .methods import Methods
from .mtproto import MtProtoClient
from .scaffold import Scaffold
from .types import Cache
from .types.update_solver import UpdateSolver


class PyTgCalls(Methods, Scaffold):
    def __init__(
        self,
        app: Any,
        cache_duration: int = 120,
    ):
        super().__init__()
        self._app = MtProtoClient(
            cache_duration,
            app,
        )
        self._is_running = False
        self._env_checker = Environment(
            self._REQUIRED_PYROGRAM_VERSION,
            self._REQUIRED_TELETHON_VERSION,
            self._REQUIRED_HYDROGRAM_VERSION,
            self._app.client,
        )
        self._cache_user_peer = Cache()
        self._wait_result = UpdateSolver()
        self._on_event_update = HandlersHolder()
        self._binding = NTgCalls()

        def cleanup():
            if self._async_core is not None:
                self._async_core.cancel()

        atexit.register(cleanup)
