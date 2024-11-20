#!/usr/bin/python3
# Original author: M. Heidenreich (c)
# Adapted by: Erwin Biju

"""
    Program: HC-SR04 Sensor Demo (sensor-threaded.py)
    Author:  M. Heidenreich, (c) 2020

    Description:

    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/JvQKZXCYMUM

    This example shows how to use the HC-SR04 sensor to provide a continuous
    distance readout with Raspberry Pi using a multi-threaded approach.

    THIS SOFTWARE AND LINKED VIDEO TOTORIAL ARE PROVIDED "AS IS" AND THE
    AUTHOR DISCLAIMS ALL WARRANTIES INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor, Buzzer, LED

reading = True
sensor = DistanceSensor(echo=20, trigger=21)
buzzer = Buzzer(24)
green_led = LED(13)
blue_led = LED(19)
red_led = LED(26)


def safe_exit(signum, frame):
    exit(1)


def read_distance():
    while reading:
        distance_cm = sensor.value * 100
        print(f"Distance: {distance_cm:.2f} cm")
        if 15.00 < distance_cm < 30.00:
            red_led.off()
            blue_led.off()
            green_led.on()
            buzzer.off()
        elif 5.00 < distance_cm < 15.00:
            blue_led.on()
            red_led.off()
            green_led.off()
            buzzer.beep(0.05, 0.05)
        elif distance_cm < 5.00:
            green_led.off()
            blue_led.off()
            red_led.on()
            buzzer.on()
        sleep(0.1)


try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    reader = Thread(target=read_distance, daemon=True)
    reader.start()
    pause()

except KeyboardInterrupt:
    pass

finally:
    reading = False
    reader.join()
    sensor.close()
    buzzer.close()
    red_led.off()
    blue_led.off()
    green_led.off()
