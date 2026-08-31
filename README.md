# AntiCheat
Trace the behavior of anti-cheat software in order to find out what is beeing done with user data. 

### Read Me
This is the first stage of the code development. This file will be updated with relevant informations as the project goes on.

#### About the server
The file `server.py` is a simple server with three types of requests [`GET, POST, PUT`]. While the server is online, in other terminal, you may run TCPDUMP to trace the packages communication.

**Terminal 1:**
>Runs the server
```bash
pyhton3 server.py
Server online in: http://0.0.0.0:8000 (Ctrl + C to stop)
127.0.0.1 - - [30/Aug/2026 20:41:25] "GET / HTTP/1.1" 200 -
...
```

**Terminal 2:**
>Runs TCPDUMP and writes the output in `test.pcap`
```bash
sudo tcpdump -i lo -w test.pcap port 8000
```

**Terminal 3:**
>Executes the requests
```bash
curl http://localhost:8000/
curl http://localhost:8000/status
curl -X POST -d '{"name": "Giovanna"}' -H "Content-Type: application/json" http://localhost:8000/dados
curl -X PUT -d '{"nome": "Gigi"}' -H "Content-Type: application/json" http://localhost:8000/dados/1
```

To analyse the `test.pcap` file, open it with wirechark: `wireshark test.pcap`