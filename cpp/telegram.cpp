#include <iostream>
#include <string>
#include <curl/curl.h>

std::string BOT_ID = "your_bot_id";
std::string TOKEN = "your_token";

std::string bot_token_acces(std::string bot_id, std::string token) {
    std::string url = "https://api.telegram.org/bot" + bot_id + token + "/sendMessage";
    return url;
}

std::string send_message(std::string user_id, std::string text) {
    std::string urls = bot_token_acces(BOT_ID, TOKEN);
    std::string payload = "{\"chat_id\": \"" + user_id + "\", \"text\": \"" + text + "\", \"disable_web_page_preview\": true, \"disable_notification\": false, \"reply_to_message_id\": null}";
    std::string response;

    CURL *curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if (curl) {
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "accept: application/json");
        headers = curl_slist_append(headers, "User-Agent: Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)");
        headers = curl_slist_append(headers, "content-type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_URL, urls.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();

    return response;
}

int main() {
    std::string user_id = "your_user_id";
    std::string text = "Hello, World!";
    std::string result = send_message(user_id, text);
    std::cout << result << std::endl;
    return 0;
}
