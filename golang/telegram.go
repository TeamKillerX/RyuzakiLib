package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

const (
	BOT_ID = "your_bot_id"
	TOKEN  = "your_token"
)

func botTokenAccess(botID, token string) string {
	url := fmt.Sprintf("https://api.telegram.org/bot%s%s/sendMessage", botID, token)
	return url
}

func sendMessage(userID, text string) string {
	urls := botTokenAccess(BOT_ID, TOKEN)
	payload := fmt.Sprintf(`{"chat_id": "%s", "text": "%s", "disable_web_page_preview": true, "disable_notification": false, "reply_to_message_id": null}`, userID, text)
	response := ""
	client := &http.Client{}
	req, err := http.NewRequest("POST", urls, strings.NewReader(payload))
	if err != nil {
		fmt.Println(err)
		return response
	}
	req.Header.Add("accept", "application/json")
	req.Header.Add("User-Agent", "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)")
	req.Header.Add("content-type", "application/json")
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return response
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return response
	}
	response = string(body)
	return response
}

func main() {
	userID := "your_user_id"
	text := "Hello, World!"
	result := sendMessage(userID, text)
	fmt.Println(result)
}
