import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Main {
    private static final String BOT_ID = "your_bot_id";
    private static final String TOKEN = "your_token";

    public static String bot_token_acces(String bot_id, String token) {
        String url = "https://api.telegram.org/bot" + bot_id + token + "/sendMessage";
        return url;
    }

    public static String send_message(String user_id, String text) {
        String urls = bot_token_acces(BOT_ID, TOKEN);
        String payload = "{\"chat_id\": \"" + user_id + "\", \"text\": \"" + text + "\", \"disable_web_page_preview\": true, \"disable_notification\": false, \"reply_to_message_id\": null}";
        String response = "";
        try {
            URL url = new URL(urls);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("accept", "application/json");
            conn.setRequestProperty("User-Agent", "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)");
            conn.setRequestProperty("content-type", "application/json");
            conn.setDoOutput(true);
            OutputStream os = conn.getOutputStream();
            os.write(payload.getBytes());
            os.flush();
            os.close();
            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            while ((line = br.readLine()) != null) {
                response += line;
            }
            br.close();
            conn.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return response;
    }

    public static void main(String[] args) {
        String user_id = "your_user_id";
        String text = "Hello, World!";
        String result = send_message(user_id, text);
        System.out.println(result);
    }
}
