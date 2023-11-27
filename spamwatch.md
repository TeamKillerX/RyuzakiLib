### Spamwatch
• Example usage
```python
from RyuzakiLib.spamwatch.clients import SibylBan

clients = SibylBan("your_api_key_here")

message = clients.add_ban(user_id=client.me.id, reason="scammer", is_banned=True)
await message.reply_text(message)

# Part 2
showing = clients.get_ban(user_id=client.me.id, banlist=True)
print(showing)

# Part 3
results = clients.get_all_banlist()
print(results)
```
