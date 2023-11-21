### Spamwatch
• Example usage
```python
from RyuzakiLib.spamwatch.clients import SibylBan

clients = SibylBan()

message = await clients.add_ban(user_id=client.me.id, reason="scammer", is_banned=True)
await message.reply_text(message)

# Part 2 
showing = await clients.get_ban(user_id=client.me.id, banlist=True)
print(showing)

# Part 3 
results = await clients.get_all_banlist()
print(results)
```
• Can't Unbanned: ask support [@xtdevs](https://t.me/xtdevs)
