### Step 1: Install Fail2Ban

Fail2Ban is an intrusion prevention software framework that protects your server from brute-force attacks. It monitors log files and bans IP addresses that show malicious signs.

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
### Custom Fail2ban
```bash
# Get list of all Fail2ban jails
for jail in $(sudo fail2ban-client status | grep 'Jail list:' | sed 's/.*://;s/,//g'); do
    # Print the current jail name
    echo "Jail: $jail"
    # Display banned IPs for the current jail
    sudo fail2ban-client status $jail | grep 'Banned IP'
done
```

- Default Parameter
```bash
sudo nano /etc/fail2ban/jail.d/custom.conf
```
**Override the base configurations**: All default parameters and configurations are found in the file `/etc/fail2ban/jail.conf`. Here is a list of important parameters to override and adapt according to the behavior you desire:
- **bantime**: Defines the duration of an IP ban (default 10 minutes, recommended several hours or days).
- **findtime**: Period during which anomalies are searched for in the logs.
- **ignoreip**: List of IPs to ignore, including yours to avoid self-banning.
- **maxretry**: Number of failed attempts allowed before banning.
Also define the use of UFW to take control of the banning (banaction and banaction_allports).

Here is an example of a drastic configuration, banning any first intrusion attempt for 1 day. We also define the use of UFW, (note the local IP addresses that you may need to adjust according to your local network configuration):

```ini
[DEFAULT]
bantime = 1d
findtime = 1d
ignoreip = 127.0.0.1/8 192.168.0.0/16
maxretry = 1

banaction = ufw
banaction_allports = ufw
```
- Step 8: Add Jails to Your Configuration

To add these jails to the Fail2Ban configuration in the `custom.conf` file, follow these steps:
```bash
sudo nano /etc/fail2ban/jail.d/custom.conf
```
- Add jail configurations: Copy and paste the following configurations at the end of the file:
```ini
[sshd]
enabled = true

[nginx-4xx]
enabled = true
port     = http,https
filter   = nginx-4xx
logpath  = %(nginx_error_log)s

[nginx-http-auth]
enabled = true
port     = http,https
filter   = nginx-http-auth
logpath  = %(nginx_error_log)s

[nginx-botsearch]
enabled = true
port     = http,https
filter   = nginx-botsearch
logpath  = %(nginx_access_log)s

[nginx-forbidden]
enabled = true
port    = http,https
filter  = nginx-forbidden
logpath = %(nginx_error_log)s

[nginx-sslerror]
enabled = true
port    = http,https
filter  = nginx-sslerror
logpath = %(nginx_error_log)s

[ufw]
enabled = true
filter  = ufw
logpath = /var/log/ufw.log
```
### Configuring Custom Logpaths in Fail2Ban
In Fail2Ban, if you're creating a custom configuration file such as `custom.conf`, and you want to set the `logpath` for a specific jail to `/var/log/nginx/access.log`, you can do it directly under the jail configuration.

For example, if you want to define the log path for monitoring Nginx access logs in your custom configuration (`custom.conf`), you can structure it like this:

```ini
[nginx-4xx]
enabled = true
port     = http,https
filter   = nginx-4xx
logpath  = /var/log/nginx/access.log

[nginx-http-auth]
enabled = true
port     = http,https
filter   = nginx-http-auth
logpath  = /var/log/nginx/access.log

[nginx-botsearch]
enabled = true
port     = http,https
filter   = nginx-botsearch
logpath  = /var/log/nginx/access.log

[nginx-forbidden]
enabled = true
port    = http,https
filter  = nginx-forbidden
logpath = /var/log/nginx/access.log

[nginx-sslerror]
enabled = true
port    = http,https
filter  = nginx-sslerror
logpath = /var/log/nginx/access.log
```

In this example:
- Each `[nginx-*]` jail has a `logpath` specified, which points to `/var/log/nginx/access.log` for Nginx access logs.
- Ensure that `/var/log/nginx/access.log` exists and is the correct file where Nginx logs access attempts.

## Custom Configuration File Placement

### Important: Place `custom.conf` in `/etc/fail2ban/jail.d/`

Fail2Ban reads configuration files from this directory and combines them with the main configuration.
- This custom configuration file should be placed in `/etc/fail2ban/jail.d/` as `custom.conf`. Fail2Ban reads configuration files from this directory and combines them with the main configuration.

Example steps:
```bash
sudo nano /etc/fail2ban/jail.d/custom.conf
```

Add the custom jail configurations there, save the file, and restart Fail2Ban:
```bash
sudo systemctl restart fail2ban
```

### Important:
- Make sure that `/var/log/nginx/access.log` is being actively written by Nginx. You can check this by running:
  ```bash
  tail -f /var/log/nginx/access.log
  ```
- The filters like `nginx-4xx`, `nginx-http-auth`, etc., should have matching patterns in `/etc/fail2ban/filter.d/` to detect suspicious behavior.

This setup ensures Fail2Ban monitors the correct log file for blocking malicious access attempts.

# UFW Ban IP
You ban him manually by adding his IP to the firewall. If you are using UFW, then you write something like this in your command line:
```bash
ufw insert 1 deny from <ip> to any

# Warning: Manual IP banning carries risks:
# - Potential blocking of legitimate traffic
# - Increased maintenance overhead
# - Difficulty in managing multiple banned IPs
# Consider using automated tools like fail2ban for better management
```
