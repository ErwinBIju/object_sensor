# Sensor-Based LED and Buzzer System

This project demonstrates the integration of a distance sensor with LEDs and a buzzer to provide visual and auditory feedback based on the distance of an object. The system reacts dynamically to changes in proximity, with specific LED colors lighting up and the buzzer beeping depending on how close an object is.

## Features

- **Distance Measurement**: Uses a sensor to measure the distance of an object in real-time.
- **LED Feedback**:
  - Green LED lights up for distances above 15cm
  - Blue LED lights up for distances between 5cm and 15cm.
  - Red LED lights up for distances less than 5cm.
- **Buzzer Feedback**:
  - Buzzer beeps intermittently for distances between 5cm and 15cm.
  - Buzzer stays on continuously for distances less than 10cm.

## Hardware Components

- Distance sensor (e.g., ultrasonic or IR sensor)
- 3 LEDs (Red, Blue, Green)
- Buzzer
- Raspberry Pi (or any other microcontroller)
- Resistors (as required)
- Jumper wires
- Breadboard

## Software Requirements

- Python 3.x
- GPIO libraries (e.g., RPi.GPIO or gpiozero for Raspberry Pi)

## How It Works

1. The sensor continuously measures the distance of an object and converts it to centimeters.
2. Based on the measured distance:
   - LEDs light up in specific patterns to indicate proximity.
   - The buzzer provides audible feedback, either beeping intermittently or staying on, depending on the distance range.
3. The system is designed to poll the sensor in a loop, ensuring real-time updates without delays.

## Code Overview

- **Distance Measurement**: The sensor value is multiplied by 100 to convert it into centimeters.
- **LED Control**: The LEDs are toggled on/off based on predefined distance ranges.
- **Buzzer Control**: The buzzer's `beep` or `on` method is used for intermittent or continuous sound.

