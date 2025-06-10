![image](https://github.com/user-attachments/assets/29da5306-b604-44a9-9576-9634a0b70878)
## 🔧 Features

- 💧 Manually start/stop the water pump from a mobile or laptop.
- 🌾 View **real-time soil moisture status**.
- 📡 ESP32 acts as a Wi-Fi Access Point, so **no internet required**.
- 🌐 Responsive web page with pump and soil status.

---

## 📷 Project Media

### 📸 Project Photos

![Project Setup Placeholder](https://www3.lunapic.com/do-not-link-here-use-hosting-instead/174955794841545997?9219435722)
![Project Setup Placeholder](https://www3.lunapic.com/editor/working/174955794841545997?6657517204)

---

### 🎥 Demo Video

[![Watch the Demo](images/video-thumbnail-placeholder.jpg)](https://example.com)

---

### 🖼 Web Interface Screenshots

  ![Pump On Screenshot Placeholder](images/pump-on-placeholder.png)

  ![Pump Off Screenshot Placeholder](images/pump-off-placeholder.png)

---

## 🧰 Hardware Required

| Component              | Description                         | Image Placeholder |
|------------------------|-------------------------------------|-------------------|
| ESP32 Dev Board        | Microcontroller with Wi-Fi          | ![ESP32](https://electronation.pk/wp-content/uploads/2023/05/ESP-WR2-1.jpg) |
| Soil Moisture Sensor (DO) | Digital soil sensor               | ![Soil Sensor](https://arduinodiy.wordpress.com/wp-content/uploads/2020/08/simplesensor2.png) |
| L298n motor driver Module | To control the pump safely          | ![L298n motor driver](https://electronation.pk/wp-content/uploads/2023/05/51OLJML2OL._AC_UF10001000_QL80_.jpg) |
| Water Pump (5V or 12V) | Submersible pump                    | ![Pump](https://digilog.pk/cdn/shop/files/Mini5VWaterPumpDiaphragmPumpMicroSelfPrimingSuctionDrinkingFountainWaterPumpWaterDispenserPump_6.webp?v=1734007520&width=720) |
| Power Supply           | 5V/12V adapter or USB               | ![Power](https://m.media-amazon.com/images/I/71SJEh+4jDL.jpg) |
| Jumper Wires + Breadboard | For connections                  | ![Wires](https://electronation.pk/wp-content/uploads/2023/05/758-04-1.jpg) |

---

## 🧠 Wiring Diagram


### 📌 Connections:

| ESP32 Pin | Connected To           |
|----------|------------------------|
| GPIO 12  | L298n IN1 (Pump control) |
| GPIO 13  | L298n IN2 (GND control or optional) |
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

