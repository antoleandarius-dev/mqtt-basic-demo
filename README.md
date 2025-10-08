# MQTT Basic Demo

Lightweight example showing how two Python scripts can publish and subscribe using the public Mosquitto broker. Useful for quick MQTT experiments and connectivity checks.

---

## Project Layout

- `sender.py` – publishes five sample messages to `test/laptopA_to_laptopB`.
- `receiver.py` – subscribes to the same topic and prints incoming payloads.
- `requirements.txt` – dependencies shared by both scripts (`paho-mqtt`).

---

## Prerequisites

1. Python 3.8 or newer.
2. Internet access (the demo relies on the public broker `test.mosquitto.org`).
3. Optional but recommended: a Python virtual environment.

---

## Setup

```bash
cd mqtt-basic
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Running the Demo

1. **Start the receiver** in one terminal:
   ```bash
   python receiver.py
   ```
   You should see the subscription confirmation once the connection succeeds.

2. **Run the sender** in another terminal:
   ```bash
   python sender.py
   ```
   The script publishes five messages two seconds apart and then disconnects.

3. The receiver terminal will display each message as it arrives.

---

## Customizing

- Change `TOPIC` in both scripts to test different channels.
- Update `BROKER`/`PORT` if you want to target a self-hosted or secured MQTT broker.
- Adjust the loop, payload, or delay in `sender.py` to simulate different publishing patterns.

---

## Troubleshooting

- **No output on receiver**: Ensure the sender and receiver use the same topic and the public broker is reachable.
- **Connection refused**: Public brokers occasionally throttle clients; wait a minute or switch to another broker.
- **SSL/TLS required**: This demo uses plaintext port 1883. For encrypted connections, adapt the scripts with `tls_set()` and change the port to 8883 or another secure endpoint.

---

Happy hacking! Feel free to extend the scripts with QoS settings, retained messages, or authentication if you need a more realistic scenario.
