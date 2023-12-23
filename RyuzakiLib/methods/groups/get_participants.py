from typing import List
from typing import Optional
from typing import Union

from ...scaffold import Scaffold
from ...types.groups.group_call_participant import GroupCallParticipant


class GetParticipants(Scaffold):
    async def get_participants(
        self,
        chat_id: Union[int, str],
    ) -> Optional[List[GroupCallParticipant]]:

        chat_id = await self._resolve_chat_id(chat_id)
        await self.get_call(chat_id)

        return await self._app.get_group_call_participants(
            chat_id,
        )
