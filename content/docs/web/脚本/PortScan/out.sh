PORT    STATE    SERVICE        VERSION
22/tcp  open     ssh            OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 4c:58:5e:fa:87:5d:43:93:f6:a0:7d:5c:79:c4:b7:31 (RSA)
|   256 00:b2:4d:0a:34:ea:fb:2a:e0:58:89:72:02:08:cf:1d (ECDSA)
|_  256 2b:54:b0:5d:a8:4d:b7:15:29:d1:03:13:2d:a0:ba:a2 (ED25519)
53/tcp  open     domain         ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid:
|_  bind.version: 9.16.1-Ubuntu
80/tcp  open     http           Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: \xE9\x97\xBB\xE9\x81\x93\xE9\x9B\x86\xE5\x9B\xA2 - \xE7\xBD\x91\xE7\xAB\x99\xE5\xBB\xBA\xE8\xAE\xBE|\xE4\xBC\x81\xE4\xB8\x9A\xE7\xBD\x91\xE7\xAB\x99\xE5\xBB\xBA\xE8\xAE\xBE|PHPOK\xE7\xBD\x91\xE7\xAB\x99\xE5\xBB\xBA\xE8...
111/tcp open     rpcbind        2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
135/tcp filtered msrpc
139/tcp filtered netbios-ssn
445/tcp filtered microsoft-ds
593/tcp filtered http-rpc-epmap
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.67 seconds