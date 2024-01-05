import asyncio
import os
import subprocess
import sys

vars = [
    "API_ID",
    "API_HASH",
    "STRING_SESSION1",
    "BOT_TOKEN",
    "LOG_GROUP_ID",
    "SUDO_USERS",
    "MONGO_DB_URI",
    "OWNER_ID",
    "DURATION_LIMIT",
    "SUPPORT_CHANNEL",
    "ASSISTANT_PREFIX",
    "MUSIC_BOT_NAME",
]


def _check(z):
    new = []
    for var in vars:
        ent = os.environ.get(var + z)
        if not ent:
            return False, new
        new.append(ent)
    return True, new


for z in range(5):
    n = str(z + 1)
    if z == 0:
        z = ""
    fine, out = _check(str(z))
    if fine:
        subprocess.Popen(
            [sys.executable, "-m", "KillerXMusic", out[0], out[1], out[2], out[3], out[4], n],
            stdin=None,
            stderr=None,
            stdout=None,
            cwd=None,
        )

loop = asyncio.get_event_loop()

try:
    loop.run_forever()
except Exception as er:
    print(er)
finally:
    loop.close()
