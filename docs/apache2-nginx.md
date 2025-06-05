---
icon: user-vneck
---

# apache2-nginx

If you're running **FastAPI** with **Nginx**, it is possible that Nginx is already using ports 80 or 443, which could be causing the conflict with Apache. Here’s how you can handle this situation:

#### Step 1: Check Nginx Status

To check if Nginx is running and using the ports:

```bash
sudo systemctl status nginx
```

#### Step 2: Decide Which Server to Use

*   If **Nginx** is your main reverse proxy for FastAPI and you don't need Apache, you can keep Nginx running and disable Apache:

    ```bash
    sudo systemctl stop apache2
    sudo systemctl disable apache2
    ```

    This way, Apache won't start at boot and won’t conflict with Nginx.
* If you need both **Nginx** and **Apache**, consider configuring them to use different ports:
  * For example, let Apache use port 8080 and Nginx use port 80.

#### Step 3: Modify Apache Configuration (if necessary)

1.  Open your Apache configuration file:

    ```bash
    sudo nano /etc/apache2/ports.conf
    ```
2.  Change the `Listen` directive to a different port:

    ```apache
    Listen 8080
    ```
3.  Save the file and restart Apache:

    ```bash
    sudo systemctl restart apache2
    ```

#### Step 4: Configure Nginx to Work with FastAPI

If Nginx is serving as a reverse proxy for FastAPI, ensure that your Nginx configuration is correct. Here’s a basic example:

```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;  # FastAPI running on port 8000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

* Make sure FastAPI is running on the specified port (e.g., `8000`).

#### Step 5: Restart Nginx

After making any changes to the Nginx configuration, restart Nginx:

```bash
sudo systemctl restart nginx
```

#### Summary

* **Option 1**: If you don’t need Apache, disable it.
* **Option 2**: Use Apache and Nginx on different ports if necessary.

Let me know if this setup works for you or if there are any more conflicts!
