### Postgresql Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes),
you'll need to have a database installed on your system. I use postgres, so I recommend using it for optimal compatibility.

In the case of postgres, this is how you would set up a the database on a debian/ubuntu system. Other distributions may vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and db name.

### Redis Server Database

<b>Step 1: Prerequisites</b>

* System running <b>Ubuntu 22.04</b>
* Access <b>Terminal</b> Command line
* <b>Sudo</b> or <b>root</b> privileges on local or remote machines


<b>Step 2: Install Redis</b>

Redis packages are available under the default apt repository for the installation of Redis on an Ubuntu VPS.

Start by updating the packages to the latest version. Run the following command:

<code>sudo apt update</code>

<b>Install Redis using the following command</b>

<code>sudo apt install redis-server</code>

<b>Step 3: Configure Redis</b>

Redis can start without a configuration file using a built-in default configuration. Aim to make Any extra parameter exchange, you can use ict configuration file: <code>/etc/redis/redis.conf.</code> Edit the Redis configuration file in a text editor to make changes:

<code>sudo nano /etc/redis/redis.conf</code>

<b>Configure Memory</b>

Update the following values ​​in the Redis configuration file. You can use its configuration file <code>/etc/redis/redis.conf::</code>


<code>maxmemory 256mb
maxmemory-policy allkeys-lru</code>

<b>Configure supervisord</b>

For Ubuntu, we can safely select the systemd as the supervised so that Redis can interact with your supervision tree. You can use its configuration file <code>/etc/redis/redis.conf::</code>

<code>supervisord systemd</code>

<b>Binding to localhost</b>

By default, the Redis server doesn't accept remote connections. You can connect to Redis only from 127.0.0.1 (localhost) - the machine where Redis is running.

If you are using a single server setup where the client connecting to the database is also running on the same host, you should not enable remote access. You can use its configuration file <code>/etc/redis/redis.conf::</code>

<code>bind 127.0.0.1 ::1</code>

<b>Verify redis is listening on all interfaces on port 6379. Run the following command:</b>

<code>ss -an | grep 6379</code>

<b>Configure Password</b>

Configuring a Redis password enables one of its two built-in security features - the auth command, which requires clients to authenticate to access the database. You can use its configuration file <code>/etc/redis/redis.conf::</code>

<code>requirepass HackByRandy</code>

<b>Redis for the changes to take effect</b>

<code>sudo systemctl restart redis-server</code>

<b>Step 4: Connect to Redis Server</b>

Redis provides redis-cli utility to connect to the Redis server. Run the following command:

<code>redis-cli</code>

<b>Few more examples of the redis-cli command-line tool.</b>
```
redis-cli info
redis-cli info stats
redis-cli info server
```

<b>Step 5: Managing the Redis Service</b>

Now that you have your service up and running, let's go over basic management commands

To <b>stop</b> your service, run this command:

<code>sudo systemctl stop redis-server</code>

To <b>start</b> your service, run this command:

<code>sudo systemctl start redis-server</code>

To <b>disable</b> your service, run this command:

<code>sudo systemctl disable redis-server</code>

To <b>enable</b> your service, run this command:

<code>sudo systemctl enable redis-server</code>

To <b>status</b> your service, run this command:

<code>sudo systemctl status redis-server</code>

<b>Active: active (running)</b>
```
● redis-server.service - Advanced key-value store
     Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset:>
     Active: active (running) since Sat 2023-01-28 15:20:28 UTC; 3h 16min ago
       Docs: http://redis.io/documentation,
             man:redis-server(1)
   Main PID: 296675 (redis-server)
     Status: "Ready to accept connections"
      Tasks: 5 (limit: 9520)
     Memory: 2.6M
        CPU: 16.960s
     CGroup: /system.slice/redis-server.service
             └─296675 "/usr/bin/redis-server 127.0.0.1:6379" "" "" "" "" "" "" "" "" ">

```

### Mongo Database
```python
db.createUser({user:"username", pwd:"password", roles:[{role:"root", db:"admin"}]})
```

<b>Thank you</b> for reading this article !!
