---


````markdown
# 🌱 ESP32 Soil Moisture Based Watering System

This project is a simple **automatic/manual soil watering system** built using an ESP32. It reads soil moisture using a **digital soil sensor (DO pin)** and controls a water pump via a web interface.

---

## 🔧 Features

- 💧 Manually start/stop the water pump from a mobile or laptop.
- 🌾 View **real-time soil moisture status**.
- 📡 ESP32 acts as a Wi-Fi Access Point, so **no internet required**.
- 🌐 Responsive web page with pump and soil status.

---

## 📷 Project Media

### 📸 Project Photos
> _Replace the placeholders below with actual images of your final setup._

![Project Setup Placeholder](https://mail.google.com/mail/u/0?ui=2&ik=3c17c968ae&attid=0.1&permmsgid=msg-f:1834543163020371978&th=19759b4974f3680a&view=fimg&realattid=19759b442f9cfd1ada71&disp=thd&attbid=ANGjdJ8EZW41f_uo6-lXjOu52zRZsj0WM_C5-3HufhnaNRLU_qSa93201oaY_E-bjHTWL-dPo6DRperHbetbob0NEWB4owFLCCTu38PNJJ0AZop4T9bZtPRGVkcW5LY&ats=2524608000000&sz=w1920-h946)
![Project Setup Placeholder](https://mail.google.com/mail/u/0?ui=2&ik=3c17c968ae&attid=0.2&permmsgid=msg-f:1834543163020371978&th=19759b4974f3680a&view=fimg&realattid=19759b442f9cfc396262&disp=thd&attbid=ANGjdJ9ML12JvaLGnoqnDxF0DEVjuxWQklvhs2QA7kA-j9Egy2uRUnt-cvFanhp8jynRe94LnFkeksR96PURDBJ0oAo6iNYcDsiQdW1quZNGgF_SvJwYP-s5EECr0b4&ats=2524608000000&sz=w1920-h946)

---

### 🎥 Demo Video
> _Upload your demo to YouTube or any platform, then embed or link below._

[![Watch the Demo](images/video-thumbnail-placeholder.jpg)](https://example.com)

---

### 🖼 Web Interface Screenshots

- **Pump ON**  
  ![Pump On Screenshot Placeholder](images/pump-on-placeholder.png)

- **Pump OFF**  
  ![Pump Off Screenshot Placeholder](images/pump-off-placeholder.png)

---

## 🧰 Hardware Required

| Component              | Description                         | Image Placeholder |
|------------------------|-------------------------------------|-------------------|
| ESP32 Dev Board        | Microcontroller with Wi-Fi          | ![ESP32](images/esp32-placeholder.jpg) |
| Soil Moisture Sensor (DO) | Digital soil sensor               | ![Soil Sensor](images/soil-sensor-placeholder.jpg) |
| 2-Channel Relay Module | To control the pump safely          | ![Relay Module](images/relay-placeholder.jpg) |
| Water Pump (5V or 12V) | Submersible pump                    | ![Pump](images/pump-placeholder.jpg) |
| Power Supply           | 5V/12V adapter or USB               | ![Power](images/power-placeholder.jpg) |
| Jumper Wires + Breadboard | For connections                  | ![Wires](images/wires-placeholder.jpg) |

---

## 🧠 Wiring Diagram

> _Here’s how to wire everything together (replace the placeholder with your wiring image later)_

![Wiring Diagram Placeholder](images/wiring-diagram-placeholder.jpg)

### 📌 Connections:

| ESP32 Pin | Connected To           |
|----------|------------------------|
| GPIO 12  | Relay IN1 (Pump control) |
| GPIO 13  | Relay IN2 (GND control or optional) |
| GPIO 15  | Soil Moisture Sensor DO |
| GND      | GND of all modules      |
| VIN/5V   | Relay VCC & Soil VCC    |

> 💡 Tip: Use an external power source for the pump if it draws high current.

---

## 🚀 How to Run the Project

1. **Flash the Code**  
   Upload the provided MicroPython code to your ESP32 board using `Thonny`, `uPyCraft`, or similar tools.

2. **Connect to ESP32 Wi-Fi**  
   After booting, search for Wi-Fi:  
   **SSID**: `abdulraheem's house watering system online`  
   **Password**: `12345678`

3. **Open Browser**  
   Go to:  
   `http://192.168.4.1`

4. **Use Interface**  
   View real-time soil moisture and control the water pump.

---
Created by **Abdulraheem**.

