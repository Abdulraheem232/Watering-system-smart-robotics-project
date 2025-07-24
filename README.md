

---

## 🔧 Features

* 💧 Manually start/stop the water pump from a mobile or laptop.
* 🌾 View **real-time soil moisture status**.
* 📡 ESP32 acts as a Wi-Fi Access Point, so **no internet required**.
* 🌐 Responsive web page with pump and soil status.

---

## 📷 Project Media

### 📸 Project Photos

<img src="https://www3.lunapic.com/do-not-link-here-use-hosting-instead/174955794841545997?9219435722" alt="Project Setup" width="400" height="300">
<img src="https://www3.lunapic.com/editor/working/174955794841545997?6657517204" alt="Project Setup 2" width="400" height="300">

---

### 🎥 Demo Video

[![Watch the Demo](images/video-thumbnail-placeholder.jpg)](https://example.com)

---

### 🖼 Web Interface Screenshots

<img src="https://www3.lunapic.com/do-not-link-here-use-hosting-instead/174955794841545997?20399306265" alt="Pump On Screenshot" width="400" height="300">

---

## 🧰 Hardware Required

| Component                 | Description                | Image Placeholder                                                                                                                                                                      |
| ------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ESP32 Dev Board           | Microcontroller with Wi-Fi | <img src="https://electronation.pk/wp-content/uploads/2023/05/ESP-WR2-1.jpg" width="100">                                                                                              |
| Soil Moisture Sensor (DO) | Digital soil sensor        | <img src="https://arduinodiy.wordpress.com/wp-content/uploads/2020/08/simplesensor2.png" width="100">                                                                                  |
| L298n motor driver Module | To control the pump safely | <img src="https://electronation.pk/wp-content/uploads/2023/05/51OLJML2OL._AC_UF10001000_QL80_.jpg" width="100">                                                                        |
| Water Pump (5V or 12V)    | Submersible pump           | <img src="https://digilog.pk/cdn/shop/files/Mini5VWaterPumpDiaphragmPumpMicroSelfPrimingSuctionDrinkingFountainWaterPumpWaterDispenserPump_6.webp?v=1734007520&width=720" width="100"> |
| Power Supply              | 5V/12V adapter or USB      | <img src="https://m.media-amazon.com/images/I/71SJEh+4jDL.jpg" width="100">                                                                                                            |
| Jumper Wires + Breadboard | For connections            | <img src="https://electronation.pk/wp-content/uploads/2023/05/758-04-1.jpg" width="100">                                                                                               |

---

## 🧠 Wiring Diagram

### 📌 Connections:

| ESP32 Pin | Connected To                        |
| --------- | ----------------------------------- |
| GPIO 12   | L298n IN1 (Pump control)            |
| GPIO 13   | L298n IN2 (GND control or optional) |
| GPIO 15   | Soil Moisture Sensor DO             |
| GND       | GND of all modules                  |
| VIN/5V    | Relay VCC & Soil VCC                |

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
You can buy all this in less than 20 dollars if you are in pakistan
---

Created by **Abdulraheem**

---

