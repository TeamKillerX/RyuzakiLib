To install and configure **Fail2Ban** with **Nginx** and **FastAPI** on a server, you can follow these steps. Fail2Ban is a security tool that helps protect your server from brute-force attacks and other malicious activities by banning IP addresses that show suspicious activity.

### Step 1: Install Fail2Ban
First, install **Fail2Ban** on your server. Run the following commands:

```bash
sudo apt update
sudo apt install fail2ban
```

### Step 2: Configure Fail2Ban for Nginx
Fail2Ban comes with default configurations for various services, including Nginx. However, you need to enable them and configure them to work with your specific setup.

1. **Create a Local Jail Configuration File**:
   
   To prevent your custom configuration from being overwritten by updates, create a local jail file:
   
   ```bash
   sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
   ```

2. **Enable Nginx Protection in Fail2Ban**:

   Open the `/etc/fail2ban/jail.local` file in a text editor:
   
   ```bash
   sudo nano /etc/fail2ban/jail.local
   ```

   Add or uncomment the following sections to protect your Nginx from various types of attacks:

   ```ini
   [nginx-http-auth]
   enabled  = true
   filter   = nginx-http-auth
   logpath  = /var/log/nginx/error.log
   maxretry = 3

   [nginx-badbots]
   enabled  = true
   filter   = nginx-badbots
   logpath  = /var/log/nginx/access.log
   maxretry = 2
   bantime  = 86400

   [nginx-noscript]
   enabled  = true
   filter   = nginx-noscript
   logpath  = /var/log/nginx/error.log
   maxretry = 2
   bantime  = 86400

   [nginx-404]
   enabled  = true
   filter   = nginx-404
   logpath  = /var/log/nginx/access.log
   maxretry = 3
   bantime  = 86400

   [nginx-limit-req]
   enabled  = true
   filter   = nginx-limit-req
   logpath  = /var/log/nginx/error.log
   maxretry = 10
   bantime  = 86400
   ```

   These jails will monitor different aspects of Nginx logs and ban IPs based on the filters you set.

### Step 3: Create Nginx Filters for Fail2Ban
Fail2Ban uses filter files to define what logs it should look for. The filters for Nginx may already exist, but if not, you can create them.

1. **Create a New Filter for 404 Errors**:
   
   Create the filter file:

   ```bash
   sudo nano /etc/fail2ban/filter.d/nginx-404.conf
   ```

   Add the following content to monitor 404 errors:

   ```ini
   [Definition]
   failregex = ^<HOST> -.* "(GET|POST).* HTTP/.*" (404|403)
   ignoreregex =
   ```

2. **Create Other Filters (if necessary)**: You can define additional filters by checking Nginx logs and defining what patterns indicate malicious activity.

### Step 4: Enable Fail2Ban with FastAPI
Since Fail2Ban works by monitoring logs, you can make sure that your **FastAPI** application logs critical events (such as failed login attempts, 404 errors, or unusual API requests).

- Ensure your FastAPI app is logging to a file.
- You can then configure Fail2Ban to monitor this log file in the same way as you did for Nginx.

Example jail for **FastAPI**:

```ini
[fastapi]
enabled  = true
filter   = fastapi-auth
logpath  = /path/to/your/fastapi/logfile.log
maxretry = 5
bantime  = 3600
```

You would also need to create a `fastapi-auth.conf` filter file in `/etc/fail2ban/filter.d/` that specifies what patterns to look for in your FastAPI logs.

### Step 5: Restart and Test Fail2Ban
Restart the Fail2Ban service to apply your changes:

```bash
sudo systemctl restart fail2ban
```

You can check the status of Fail2Ban with:

```bash
sudo fail2ban-client status
sudo fail2ban-client status nginx-404
```

### Step 6: Test the Configuration
To test that Fail2Ban is correctly banning IPs:

1. Trigger a few failed requests that match your filter (e.g., try accessing non-existing pages).
2. Check if Fail2Ban has banned the IP:

```bash
sudo fail2ban-client status nginx-404
```

You should see the IPs that have been banned.

### Step 7: Monitoring Fail2Ban
You can view the logs for Fail2Ban using:

```bash
sudo tail -f /var/log/fail2ban.log
```

This will show you all the recent bans and unbans performed by Fail2Ban.

---

By following these steps, you should have a working setup of **Fail2Ban** to protect both **Nginx** and **FastAPI** from malicious activity, banning suspicious IP addresses based on your configured rules.
