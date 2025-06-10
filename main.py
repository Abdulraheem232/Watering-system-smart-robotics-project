import network
import socket
from machine import Pin

# GPIO Setup
in1 = Pin(12, Pin.OUT)
in2 = Pin(13, Pin.OUT)
soil = Pin(15, Pin.IN)  # Using DO (Digital Output)

# Start with pump OFF
in1.value(0)
in2.value(0)
pump_status = "OFF"

# Create Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="abdulraheem's house watering system online", password="12345678", authmode=3)

print("Starting Access Point...")
while not ap.active():
    pass
print("AP IP address:", ap.ifconfig()[0])

# HTML Page Template
def web_page(pump_status, moisture):
    moisture_status = "Dry" if moisture else "Wet"
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Watering System</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f2f2f2;
        }}
        h2 {{
            color: #333;
        }}
        .status {{
            padding: 10px;
            margin: 20px auto;
            background-color: #fff;
            width: 300px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }}
        .btn {{
            display: inline-block;
            padding: 15px 30px;
            margin: 10px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }}
        .btn-on {{
            background-color: #4CAF50;
            color: white;
        }}
        .btn-off {{
            background-color: #f44336;
            color: white;
        }}
    </style>
</head>
<body>
    <h2>Abdulraheem's House Watering System</h2>
    <div class="status">
        <p><strong>Pump Status:</strong> {pump_status}</p>
        <p><strong>Soil Moisture:</strong> {moisture_status}</p>
        <a href="/on"><button class="btn btn-on">Start Pump 💧</button></a>
        <a href="/off"><button class="btn btn-off">Stop Pump ⛔</button></a>
    </div>
</body>
</html>"""

# Start Web Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Web server running on http://", ap.ifconfig()[0])

while True:
    conn, addr = s.accept()
    print('Client connected from', addr)
    request = conn.recv(1024)
    request = str(request)

    # Handle pump control
    if '/on' in request:
        in1.value(1)
        in2.value(0)
        pump_status = "ON"
    elif '/off' in request:
        in1.value(0)
        in2.value(0)
        pump_status = "OFF"

    # Read soil moisture sensor
    soil_value = soil.value()  # 1 = dry, 0 = wet

    # Respond with HTML
    response = web_page(pump_status, soil_value)
    conn.send('HTTP/1.1 200 OK\r\n')
    conn.send('Content-Type: text/html\r\n')
    conn.send('Connection: close\r\n\r\n')
    conn.sendall(response)
    conn.close()
