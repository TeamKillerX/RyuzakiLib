from ...types.groups.group_call_participant import GroupCallParticipant
from ...types.update import Update


class LeftGroupCallParticipant(Update):
    def __init__(
        self,
        chat_id: int,
        participant: GroupCallParticipant,
    ):
        super().__init__(chat_id)
        self.participant = participant
