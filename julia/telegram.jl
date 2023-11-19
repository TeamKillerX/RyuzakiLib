const BOT_ID = "your_bot_id"
const TOKEN = "your_token"

function bot_token_acces(bot_id::String, token::String)::String
    url = "https://api.telegram.org/bot" * bot_id * token * "/sendMessage"
    return url
end

function send_message(user_id::String, text::String)::String
    urls = bot_token_acces(BOT_ID, TOKEN)
    payload = "{\"chat_id\": \"" * user_id * "\", \"text\": \"" * text * "\", \"disable_web_page_preview\": true, \"disable_notification\": false, \"reply_to_message_id\": null}"
    response = ""
    curl = curl_easy_init()
    if curl != C_NULL
        headers = C_NULL
        headers = curl_slist_append(headers, "accept: application/json")
        headers = curl_slist_append(headers, "User-Agent: Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)")
        headers = curl_slist_append(headers, "content-type: application/json")
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers)
        curl_easy_setopt(curl, CURLOPT_URL, urls)
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload)
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback)
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response)
        res = curl_easy_perform(curl)
        curl_easy_cleanup(curl)
    end
    return response
end

user_id = "your_user_id"
text = "Hello, World!"
result = send_message(user_id, text)
println(result)
