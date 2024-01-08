# OpenVPN Server

* <b>How to Setup OpenVPN Server in Ubuntu 20.04/22.04 [The Easy Way]</b>

![allthings how-how-to-install-openvpn-server-on-ubuntu-20-04-openvpn-server-ubuntu-20 04](https://user-images.githubusercontent.com/90479255/215355535-9ee6d63b-ced5-4b0d-8d9d-7b4364663a78.png)

This simple tutorial shows how to easily setup OpenVPN in your Ubuntu 20.04 | 22.04 server and connect remotely in Windows or Linux with GNOME.

My PPTP and IKEv2 VPN server refused to work recently due to the Great Firewall (maybe). So I decided to setup OpenVPN in my Ubuntu VPS as a workaround.

DigitalOcean has a step by step setup guide, but it’s really long and complicated for beginners. Thankfully, there’s a free open-source script make things as easy as few commands.

* <b>Step 1: Install OpenVPN</b>

1. <b>First, connect to your Ubuntu/Debian server either via SSH or other method that you favorite. Then grab the script by wget:</b>

```
wget https://git.io/vpn -O openvpn-install.sh
```
In case wget command does not exist, install via <code>sudo apt install wget</code>

2. <b>After downloaded the script, add executable permission via command:</b>

```
chmod u+x openvpn-install.sh
```

3. <b>Finally, run the script:</b>
```
sudo bash openvpn-install.sh
```

It will ask you a few questions to confirm IP address if your server is running behind NAT, choose UDP or TCP, set which port to listen to, and select a NDS server. <b>For lazy men, it’s OK hit Enter to use default for all previous questions.</b>

But, you need to finally type a name for the client. It will create a <b>.ovpn</b> file with the name you just typed.

<b>Step 2: Copy & paste the .ovpn to client machine</b>

As the screenshot above shows you, it generates the .opvn file in /root directory in my case. In case you logged in via non-root user, copy the file to user’s home via:

```
sudo mv /root/*.ovpn ~/ && sudo chown $USER:$USER *.ovpn
```

Finally, you need to send the file to client machine, such as running the scp command below in your client PC <b>(run this command in client/local machine):</b>

```
scp -P 22 username@server-ip:~/*.ovpn ./
```

Replace * with the filename, though it works if there no other .ovpn files. And, change port number 22 if non-default SSH listening port in use.

<b>Step 3: Connect to OpenVPN server in Ubuntu/Fedora</b>

<b> Import Profile</b>

* select <b>files</b>

![Screenshot_20230130-042424_OpenVPN Connect](https://user-images.githubusercontent.com/90479255/215356549-f900bd73-d24a-408f-9406-24ad60208bab.jpg)

<b> Finally Screenshot</b>

* turn on vpn

![Screenshot_20230130-043030_OpenVPN Connect](https://user-images.githubusercontent.com/90479255/215356778-85b1800e-ca7f-4872-bfee-f6ba2f929b7c.jpg)

<b>Thank you</b> for reading this article !!

* BY [RANDY](https://t.me/xtsea)
