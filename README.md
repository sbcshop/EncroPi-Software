# EncroPi

<img src ="https://cdn.shopify.com/s/files/1/1217/2104/products/enclosureBlack.jpg?v=1668683519&width=400" />

It is an innovative and highly efficient USB RTC stick based on the Raspberry Pi RP2040 microcontroller. It is a power booster product for all electronic enthusiasts and time setters. We have designed EncroPi in such a way that its powerful and advanced features will help you in your projects seamlessly. It is not just a Real Time Clock but combined with the power of the RP2040 microcontroller, it is a lightning-fast and extremely reliable product loaded with many features. 

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

## Downloading IDE
* To open upython(.py) files you should have Thonny IDE installed in your system, If you don’t have Thonny IDE follow the link below to install it
*  https://thonny.org/

### Uploading Micropython Firmware 
* Hold Boot Button and plug-in in your system after that release Boot button, you will get pop-up window of showing RaspberryPi as a mass storage device. Copy the downloaded fimware file(firmware.uf2) from this repository and paste it in resapberry pi board or you can also do this by simply drag and drop method. Now, your board has updated firmware in it.

<img src ="https://github.com/sbcshop/EncroPi/blob/main/images/Screenshot%20(29).png" />

### Installing CircuitPython Firmware
* For using the ***Image Display*** functionality in EncroPi, insert the circuit python to the EncroPi(it is circuit python firmware ***adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2***). for this first you need to press the boot button then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named "RPI-RP2" drag this file "adafruit-circuitpython- raspberry_pi_pico-en_US-7.1.1.uf2" to this device as shown in figure: this is the official website, or yoy can download from here https://circuitpython.org/board/raspberry_pi_pico/


 <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />  
When you properly insert the circuitpython then you see a new device that looks like the below image:
     
 <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />
     
After this go to run->select interpreter,choose device and port
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    
## For setup the Board in thonny </b>
* Now connect USB Cable on USB Port of Pico.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />

## Types of Code files and their functioning:

* File "EncroPi.py" is the liberary file of this board

* The "data_save_to_sdcard.py" file is for writing any data/file in SD card and Reading data from it

* The function of "gpio_test.py" file is to work with Additional GPIO pins for interfacing extrernal I/o devices

* "rtc_test.py" file is for using the RTC function of this board.

### The "Data_transfer_between_pc_and_EncroPi" Directory
Under this folder you will get two micropython files:

* One file is the library file i.e, "Encropi.py". This library is for the example code provided in this directory, library file have to save in your encropi board before running the example.  
* File 2nd, i.e "data_transfer_to_EncroPi.py" is the standard python code file for sending data from our Desktop/laptop to our EncroPi board 

### The "Encryption" directory
In this directory there are three code files :
* First one is the Library file for the examples provided in this folder
* 2nd file is for Encrypting data files from sdcard and store it in sdcard.
* 3rd file is for encrypting string data within the IDE.

### Display Images
Now, open the folder Display_Images, inside this folder their is sub-folder one is ***Display_Images from PC and another one is Dispaly images from SDCard*** folder.

 * **Display Images from PC** -> For display images in EncroPi we use CircuitPython because it is very easy, it is developed by adafruit industries, First of all, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2").   
You can also display your custom images, for this you need to go "images" folder and save your images by changing its formate and resolution according to lcd display.
You can online convert any image to BMP image (the size must be 240x240), i a websie below(there are various website)
https://image.online-convert.com/convert-to-bmp
Now, you need to run the pyhton code file provided in this folder (i.e, images_display.py).
    
  * **Display Images From SD Card** -> For this, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). 
 Now, follow all the process of **Display Images from PC**,you only have to simply save the images containing in this directory (Do not save images in any directory when storing in SDCard). Finally, run the python code provided in this directory (i.e, display_image_sdcard_circuitpython.py)


## Documentation

* [EncroPi Hardware](https://github.com/sbcshop/EncroPi-Hardware)
* [RaspberryPi PICO Getting Started with Micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [RaspberryPi PICO Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [RP2040 Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html)
* [Raspberry Pi Pico Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [RP2040 Hardware Design](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [Raspberry Pi Pico Pinout](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [SquaryPi](https://shop.sb-components.co.uk/products/squary?variant=40443840921683)

 ![SquaryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/1_5874b3b5-2a2f-453e-bf54-abbf2a26acb9.png?v=1670307456&width=400)


## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>
