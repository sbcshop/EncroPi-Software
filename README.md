# EncroPi

### It is an innovative and highly efficient USB RTC stick based on the Raspberry Pi RP2040 microcontroller. It is a power booster product for all electronic enthusiasts and time setters. We have designed EncroPi in such a way that its powerful and advanced features will help you in your projects seamlessly. It is not just a Real Time Clock but combined with the power of the RP2040 microcontroller, it is a lightning-fast and extremely reliable product loaded with many features. 

<img src ="https://github.com/sbcshop/EncroPi/blob/main/images/EncroPi%20(1).png" />

### RP2040
Raspberry Pi RP2040 Microcontroller Chip is the debut microcontroller from Raspberry Pi. It brings high performance, low cost, and ease of use to the microcontroller space. The RP2040 has a large on-chip memory, symmetric dual-core processor complex, deterministic bus fabric, and rich peripheral set. It's augmented with a unique Programmable I/O (PIO) subsystem and provides unrivaled power and flexibility.
### DS3231(RTC)
IT is a Real time clock IC that has very low-power consumption, a digital temperature sensor, and two-time day alarms. Its operating voltage is 2.3V-5.5V. 
### SD Card Slot
It is provided for storing data in your SD card that you want to run.
### Battery Holder
It is provided for holding the power backup battery For keeping time. It holds a button cell to do so.
### LCD Display
The 1.14-inch LCD has a resolution of 240x135 pixels for showing date and time or other data the user wants to show on the Display of  EncroPi.
### USB Type-C Port 
Just like USB 2.0 user can also debug programmes via type-cable and can be used for power-up EncroPi via C-type USB cable.

### Boot Button, Status LED and Power LED
The onboard boot button is provided for uploading the firmware into RP2040 of EncroPi. Status is connected on GPIO-15 and it's fully  user configurable. Power LED is for indicating power.

### Additional GPIO's
In this board we are providing some extra GPIO pins for connecting any external Input/output(such as sensors) to RP2040 of EncroPi board.
These GPIO's are 5v, GND, 3v, GP4, GP3, GP14, GP15.

## Features Of EncroPi

EncropPi has many powerful and advance features wich will help users in many Projects. Some of the key features of EncroPi are:
Data Read/Write, Data Encryption, Data Logger, Real Time Clock(RTC), etc.

#### Encryption:
 Now encrypt the data which you run on your USB RTC. Make use of EncroPi as an encrypted key and secure your codes and application sources.
 
 classcryptolib.aes¶
classmethod__init__(key, mode[, IV])¶
Initialize cipher object, suitable for encryption/decryption. Note: after initialization, cipher object can be use only either for encryption or decryption. Running decrypt() operation after encrypt() or vice versa is not supported.

Parameters are:

key is an encryption/decryption key (bytes-like).

mode is:

1 (or cryptolib.MODE_ECB if it exists) for Electronic Code Book (ECB).

2 (or cryptolib.MODE_CBC if it exists) for Cipher Block Chaining (CBC).

6 (or cryptolib.MODE_CTR if it exists) for Counter mode (CTR).

IV is an initialization vector for CBC mode.

For Counter mode, IV is the initial value for the counter.

encrypt(in_buf[, out_buf])¶
Encrypt in_buf. If no out_buf is given, the result is returned as a newly allocated bytes object. Otherwise, the result is written into mutable buffer out_buf. in_buf and out_buf can also refer to the same mutable buffer, in which case data is encrypted in-place.

decrypt(in_buf[, out_buf])¶
Like encrypt(), but for decryption.

#### Data Logger:
No more worries about losing your data or loading it over and over again every time. EncroPi has a dedicated SD card slot to store your data safely.

#### RTC:
Real-time for your personal computers, embedded systems, servers, or any electronic device that may require accurate time keeping

## Uploading Firmware 
* Hold Boot Button and plug-in in your system after that release Boot button, you will get pop-up window of showing RaspberryPi as a mass storage device. Copy the downloaded fimware file(firmware.uf2) from this repository and paste it in resapberry pi board or you can also do this by simply drag and drop method. Now, your board has updated firmware in it.

## Downloading IDE
* To open upython(.py) files you should have Thonny IDE installed in your system, If you don’t have Thonny IDE follow the link below to install it
*  https://thonny.org/

## For setup the Board in thonny </b>
* Now connect USB Cable on USB Port of Pico.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />

## Types of Code files and thier funtioning:

* File "encropi.py" is the liberary file of this board

* The funtion of "encryption_sdcard.py" file is to encrypt the data/file in SD card and store that file in SD card

* ThData_logging_FromPCe function of "gpio_test.py" file is to work with Additional GPIO pins for interfacing extrernal I/o devices

* The "sdcard_read_write.py" file is for writing any data/file in SD card and Reading data from it

* "encryption_test.py" file is for teting encrption and decrptions of any data within the IDE

### The "Data_logging_FromPC" Directory
Under this folder you will get three micropython files:

* One file is simply the liberary file i.e, "encropi.py"
* File 2nd, i.e "data_transfer_to_EncroPi (1).py" is the standard python code file for sending data from our Desktop/laptop to our EncroPi board 
* The third file(data_save_to_sdcard.py) is the main file for recieving data to our encroPi. This file should save in EncroPi board as "main.py" file before sending     any data to it.
