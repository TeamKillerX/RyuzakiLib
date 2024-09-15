### 1. **Block Access to Sensitive Files**
You can prevent access to specific files (like `.env` or `.git/config`) by configuring Nginx to block requests to those paths.

#### Example: Block Access to Sensitive Files
```nginx
server {
    location ~ /\. {
        deny all;
        return 403;
    }

    location ~* ^/(.git|.env|config|package\.json|composer\.json|composer\.lock) {
        deny all;
        return 403;
    }
}
```
This configuration:
- Denies access to any file that begins with a `.` (like `.env` or `.git`).
- Blocks access to common sensitive files such as `config`, `package.json`, and `composer.json`.

### 2. **Prevent Path Traversal Attacks**
To avoid directory traversal (`../`) attacks, you can add rules to normalize paths and block dangerous patterns.

#### Example: Prevent Path Traversal
```nginx
server {
    location / {
        if ($request_uri ~* "/\.\./") {
            return 403;
        }
    }
}
```
This rule checks the request URI and returns a `403 Forbidden` response if the request contains any path traversal patterns like `../`.

### 3. **Restrict Access to Upload Directories**
If your web app has an upload directory, make sure Nginx is configured to prevent execution of files within that directory (such as PHP files or scripts uploaded by attackers).

#### Example: Restrict Execution in Uploads
```nginx
server {
    location /uploads/ {
        # Disable execution of PHP or other scripts in the uploads directory
        location ~* \.(php|php3|php4|php5|phtml)$ {
            deny all;
            return 403;
        }
    }
}
```
This configuration blocks execution of any PHP or script files uploaded to the `/uploads/` directory.

### 4. **Limit File Types That Can Be Accessed**
You can specify which file types are allowed to be served by Nginx and block the rest. For example, allow only `.html`, `.css`, and image files to be accessed by users.

#### Example: Restrict File Types
```nginx
server {
    location / {
        # Allow only specific file types
        location ~* \.(jpg|jpeg|png|gif|css|js|html)$ {
            allow all;
        }

        # Deny access to all other file types
        location ~* \.(php|exe|sh|bat)$ {
            deny all;
            return 403;
        }
    }
}
```

### 5. **Implement Security Headers**
You can add security headers in Nginx to improve protection against XSS, clickjacking, and other vulnerabilities.

#### Example: Security Headers
```nginx
server {
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
    add_header Content-Security-Policy "default-src 'self';";
}
```

### 6. **Block Specific Paths**
You can configure Nginx to block specific paths that attackers commonly probe for, such as vulnerable PHP scripts, default admin pages, or paths that don’t exist on your server.

#### Example: Block Probing for Vulnerable Paths
```nginx
server {
    location ~* /(config|install|db_backup|admin|phpmyadmin|shell\.php)$ {
        deny all;
        return 403;
    }

    location ~* /actuator {
        deny all;
        return 403;
    }
}
```

### 7. **Use a Web Application Firewall (WAF)**
A Web Application Firewall like **ModSecurity** can detect and block various kinds of attacks including SQL injections, XSS, and directory traversal. You can configure Nginx to use ModSecurity for additional protection.

#### Example: Enable ModSecurity with Nginx
1. Install ModSecurity.
2. Configure Nginx to use ModSecurity:
```nginx
server {
    modsecurity on;
    modsecurity_rules_file /etc/nginx/modsec/main.conf;

    location / {
        proxy_pass http://localhost:8080;
    }
}
```

### Summary of Sensitive Paths to Block:
Here’s a list of sensitive paths that are often targeted by attackers. You can use Nginx to block access to these:

- `/.env`
- `/.git/`
- `/wp-admin/`
- `/wp-config.php`
- `/config.php`
- `/index.php`
- `/vendor/`
- `/phpinfo.php`
- `/phpmyadmin/`
- `/backup/`
- `/install.php`
- `/actuator/`
- `/web-console/`
- `/admin/`
- `/app.php`
- `/shell.php`
- `/db_backup/`
- `/logs/`
- `/cache/`
- `/debug/`
- `/composer.lock`
- `/composer.json`
- `/package.json`
- `/error.log`
- `/access.log`

By configuring Nginx properly with these rules, you can significantly reduce the risk of your server being exploited through directory traversal, file probing, or path manipulation attacks.
