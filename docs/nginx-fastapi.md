### Steps to Run FastAPI on a VPS with a Domain

#### 1. **Deploy FastAPI on Your VPS**
You need to set up your VPS to run your FastAPI application. To do this, you typically use a production server like **Uvicorn** or **Gunicorn** and a web server like **Nginx** as a reverse proxy.

#### Prerequisites:
- A VPS (e.g., DigitalOcean, AWS EC2, etc.)
- A domain name
- A FastAPI project

#### 2. **Install FastAPI and Uvicorn on VPS**
Log into your VPS and install the required packages.

```bash
ssh root@YOUR_VPS_IP
sudo apt update
sudo apt install python3-pip python3-venv -y
```

Create a virtual environment and install FastAPI and Uvicorn:

```bash
mkdir fastapi_app
cd fastapi_app
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

#### 3. **Create a FastAPI Application**
Create a simple `main.py` file with your FastAPI code:

```bash
nano main.py
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
```

#### 4. **Run FastAPI using Uvicorn**
Test your FastAPI app by running Uvicorn:

```bash
uvicorn main:app --reload
```

This will start FastAPI on `http://YOUR_VPS_IP:8000`. You should now be able to access your application using your VPS IP.

#### 5. **Install Nginx and Configure a Reverse Proxy**
Nginx will act as a reverse proxy to forward traffic from your domain to the FastAPI app.

1. **Install Nginx**:

```bash
sudo apt install nginx -y
```

2. **Configure Nginx for Your FastAPI App**:

```bash
sudo nano /etc/nginx/sites-available/fastapi
```

Add the following configuration, replacing `example.com` with your actual domain:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

• You can multiple port
```nginx
server {
    listen 80;
    server_name custom.example.com;

    # Proxy all normal requests to port 8080
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # Proxy requests to /v1/ to the service running on port 1337
    location /v1 {
        proxy_pass http://127.0.0.1:1337;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

```


3. **Enable the Nginx Configuration**:

```bash
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled/
```

4. **Restart Nginx**:

```bash
sudo systemctl restart nginx
```

#### 6. **Point Your Domain to Your VPS**
You need to point your domain to your VPS IP address.

1. Go to your domain registrar (e.g., Namecheap, GoDaddy).
2. Edit the DNS settings to add an `A` record:
   - **Host**: `@` (or `www`)
   - **Points to**: Your VPS IP address
3. Save the settings and wait for the DNS propagation (may take up to 24 hours).

#### 7. **Enable HTTPS with Let's Encrypt (Optional)**
To secure your FastAPI app with HTTPS, you can use **Let's Encrypt** to obtain a free SSL certificate.

1. **Install Certbot**:

```bash
sudo apt install certbot python3-certbot-nginx -y
```

2. **Obtain an SSL Certificate**:

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

3. **Follow the prompts** to complete the SSL setup.

4. **Test the SSL certificate renewal**:

```bash
sudo certbot renew --dry-run
```

#### 8. **Access FastAPI via Domain**
Now, you can access your FastAPI app via your domain at:

- `http://example.com` (without HTTPS)
- `https://example.com` (with HTTPS, if SSL is set up)

### Conclusion
With these steps, you'll have FastAPI running on your VPS with your domain, and optionally secured with HTTPS via Let's Encrypt. You can scale this setup by using Docker, Gunicorn with Uvicorn workers, and more advanced deployment techniques if necessary.

### Solution: Increase Nginx Header Buffer Sizes

1. **Edit the Nginx Configuration**:
   You will need to modify your Nginx configuration file (`/etc/nginx/nginx.conf` or the specific configuration file for your site in `/etc/nginx/sites-available/`).

   Add the following directives to increase the buffer sizes:

   ```nginx
   http {
       ...

       # Increase the buffer sizes for reading headers
       proxy_buffer_size 16k;
       proxy_buffers 4 32k;
       proxy_busy_buffers_size 64k;
       proxy_temp_file_write_size 64k;
   }
   ```

   If you are working with a specific server block (e.g., `/etc/nginx/sites-available/fastapi`), you can also add these directives inside the `server` or `location` block:

   ```nginx
   server {
       listen 80;
       server_name your_domain_or_ip;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;

           # Increase the buffer sizes for this location
           proxy_buffer_size 16k;
           proxy_buffers 4 32k;
           proxy_busy_buffers_size 64k;
           proxy_temp_file_write_size 64k;
       }
   }
   ```

2. **Save the Configuration**.

3. **Test the Nginx Configuration**:
   Always check if the Nginx configuration is valid before restarting it.

   ```bash
   sudo nginx -t
   ```

   If the output says `syntax is ok` and `test is successful`, you can proceed.

4. **Restart Nginx**:
   Restart Nginx to apply the changes.

   ```bash
   sudo systemctl restart nginx
   ```

### Additional Considerations:

- If the error persists, you can further increase the buffer sizes (e.g., increase `proxy_buffer_size` to `32k` or adjust `proxy_buffers` accordingly).
- Ensure your FastAPI application is not sending excessively large headers, such as very large cookies, unnecessary data, or multiple headers that can be optimized.

By increasing the buffer size, Nginx should now be able to handle larger headers without throwing the "upstream sent too big header" error.
