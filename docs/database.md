---
icon: square-reddit
---

# database

#### Postgresql Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes), you'll need to have a database installed on your system. I use postgres, so I recommend using it for optimal compatibility.

In the case of postgres, this is how you would set up a the database on a debian/ubuntu system. Other distributions may vary.

* install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

* change to the postgres user:

`sudo su - postgres`

* create a new database user (change YOUR\_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

* create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR\_USER and YOUR\_DB\_NAME appropriately.

* finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal. By default, YOUR\_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc) repeat for your username, password, hostname (localhost?), port (5432?), and db name.

#### Redis Server Database

Step 1: Prerequisites

* System running Ubuntu 22.04
* Access Terminal Command line
* Sudo or root privileges on local or remote machines

Step 2: Install Redis

Redis packages are available under the default apt repository for the installation of Redis on an Ubuntu VPS.

Start by updating the packages to the latest version. Run the following command:

`sudo apt update`

Install Redis using the following command

`sudo apt install redis-server`

Step 3: Configure Redis

Redis can start without a configuration file using a built-in default configuration. Aim to make Any extra parameter exchange, you can use ict configuration file: `/etc/redis/redis.conf.` Edit the Redis configuration file in a text editor to make changes:

`sudo nano /etc/redis/redis.conf`

Configure Memory

Update the following values ​​in the Redis configuration file. You can use its configuration file `/etc/redis/redis.conf::`

`maxmemory 256mb maxmemory-policy allkeys-lru`

Configure supervisord

For Ubuntu, we can safely select the systemd as the supervised so that Redis can interact with your supervision tree. You can use its configuration file `/etc/redis/redis.conf::`

`supervisord systemd`

Binding to localhost

By default, the Redis server doesn't accept remote connections. You can connect to Redis only from 127.0.0.1 (localhost) - the machine where Redis is running.

If you are using a single server setup where the client connecting to the database is also running on the same host, you should not enable remote access. You can use its configuration file `/etc/redis/redis.conf::`

`bind 127.0.0.1 ::1`

Verify redis is listening on all interfaces on port 6379. Run the following command:

`ss -an | grep 6379`

Configure Password

Configuring a Redis password enables one of its two built-in security features - the auth command, which requires clients to authenticate to access the database. You can use its configuration file `/etc/redis/redis.conf::`

`requirepass HackByRandy`

Redis for the changes to take effect

`sudo systemctl restart redis-server`

Step 4: Connect to Redis Server

Redis provides redis-cli utility to connect to the Redis server. Run the following command:

`redis-cli`

Few more examples of the redis-cli command-line tool.

```
redis-cli info
redis-cli info stats
redis-cli info server
```

Step 5: Managing the Redis Service

Now that you have your service up and running, let's go over basic management commands

To stop your service, run this command:

`sudo systemctl stop redis-server`

To start your service, run this command:

`sudo systemctl start redis-server`

To disable your service, run this command:

`sudo systemctl disable redis-server`

To enable your service, run this command:

`sudo systemctl enable redis-server`

To status your service, run this command:

`sudo systemctl status redis-server`

Active: active (running)

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

#### Mongo Database

```python
db.createUser({user:"username", pwd:"password", roles:[{role:"root", db:"admin"}]})
```

Thank you for reading this article !!
