# AntiCheat
Trace the behavior of anti-cheat software in order to find out what is beeing done with user data. 

### Read Me
This is the first stage of the code development. This file will be updated with relevant informations as the project goes on.

#### About the server
The file `server.py` is a simple server with three types of requests [`GET, POST, PUT`]. While the server is online, in other terminal, you may run TCPDUMP to trace the packages communication.

**Terminal 1:**
>Runs the server and generates the certificate
```bash
# 1. Certfile (do it only once)
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout key.pem -out cert.pem -days 365 \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

# 2. Runs the server
python3 server.py
```

**Terminal 2:**
>Runs TCPDUMP and writes the output in `test.pcap`
```bash
sudo tcpdump -i lo -w test.pcap port 8443
```

**Terminal 3:**
>Executes the requests
> Obs: These request must be executed in the same directory where `cert.pem` is saved.
```bash
curl --cacert cert.pem https://localhost:8443/status

curl --cacert cert.pem -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "Giovanna"}' \
  https://localhost:8443/dados

curl --cacert cert.pem -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "Gigi"}' \
  https://localhost:8443/dados/1

# TSL details, headers sent and received
curl --cacert cert.pem -v https://localhost:8443/status

# Only headers(server must answer with 501)
curl --cacert cert.pem -I https://localhost:8443/status

# Text (UTF-8)
curl --cacert cert.pem -X POST \
  -H "Content-Type: text/plain; charset=utf-8" \
  -d 'Olá, mundo! Ação e coração' \
  https://localhost:8443/texto

# Repeated requests
for i in $(seq 1 10); do
  curl --cacert cert.pem -s -o /dev/null -w "$i: %{http_code}\n" \
    https://localhost:8443/status
done
```

To analyse the `test.pcap` file, open it with wirechark: `wireshark test.pcap`