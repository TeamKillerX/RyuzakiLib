import subprocess
from typing import List, Union


async def ufw_insert_deny_from(ip: str):
    block_command = ["sudo", "ufw", "insert", "1", "deny", "from", ip, "to", "any"]
    return subprocess.run(block_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

async def ufw_reload():
    return subprocess.run(["sudo", "ufw", "reload"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

async def ufw_delete_deny_from(ip: str):
    unblock_command = ["sudo", "ufw", "delete", "deny", "from", ip, "to", "any"]
    return subprocess.run(unblock_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

async def ufw_allow_from(ip: str):
    allow_command = ["sudo", "ufw", "allow", "from", ip, "to", "any"]
    return subprocess.run(allow_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

async def command_run(command: List[Union[str, any]]):
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
