from time import sleep
import threading
import logging
import ctypes
import serial
import os

if os.name == "posix":
    COMPORT_BASE = "/dev/"
else:
    COMPORT_BASE = ""

dirName = 'imp'
if not os.path.exists(dirName):
        os.mkdir(dirName)
        
class SerialComm(object):
    """
    Low level serial operations
    """
    log = logging.getLogger("serial")
    log.addHandler(logging.StreamHandler())
    logging.basicConfig(filename='imp/.log.log', level=logging.DEBUG)

    def __init__(self, handlerNotification=None, *args, **kwargs):
        self.__ser = None

        self.alive = False
        self.timeout = 0.01
        self.rxThread = None
        self.rxData = []
        self._txLock = threading.Lock()
        self.handlerNotification = handlerNotification

    def connect_port(self, port='COM8', baud_rate=115200, timeout=0.5):
        """
        Connects to the Comm Port
        """
        try:
            # open serial port
            self.__ser = serial.Serial(port=port, baudrate=baud_rate,
                                       timeout=timeout)
            self.alive = True
            self.rxThread = threading.Thread(target=self._readLoop)
            self.rxThread.daemon = True
            self.rxThread.start()
            self.log.info("Connected with {} at {} "
                          "baudrate.".format(port, baud_rate))
            return True
        except serial.serialutil.SerialException:
            self.alive = False
            self.log.error("Couldn't connect with {}.".format(port))
            return False

    def disconnect(self):
        """
        Stops read thread, waits for it to exit cleanly and close serial port
        """
        self.alive = False
        if self.rxThread:
            self.rxThread.join()
        self.close_port()
        self.log.info("Serial Port Disconnected")

    def read_port(self, n=1):
        """
        Read n number of bytes from serial port
        :param n: Number of bytes to read
        :return: read bytes
        """
        return self.__ser.read(n)

    def read_line(self):
        return self.__ser.readline()
        # return self.__ser.readall()

    def write_port(self, data):
        """
        :param data: data to send to servo, type: bytearray
        :return: Number of bits sent
        """
        return self.__ser.write(data)

    def close_port(self):
        """
        Check if the port is open.
        Close the Port if open
        """
        if self.__ser and self._connected:
            self.__ser.close()
        self.alive = False

    def flush_input(self):
        self.__ser.reset_input_buffer()

    def flush_output(self):
        self.__ser.reset_output_buffer()

    @property
    def _connected(self):
        if self.__ser:
            return self.__ser.is_open

    @property
    def _waiting(self):
        if self.__ser:
            return self.__ser.inWaiting()

    def _readLoop(self):
        """
        Read thread main loop
        """
        try:
            while self.alive:
                data = self.read_line()
                if data != b'':
                    self.log.info("Serial Response: %s", data)
                    self.rxData.append(data)
                    self.update_rx_data(data)
                    #self.rxData = []

        except serial.SerialException as SE:
            self.log.error("Serial Exception: {}.".format(SE))
            self.close_port()

    def write(self, data):
        """
        Write data to serial port
        """
        with self._txLock:
            self.log.info("Serial Write: {}".format(data))
            self.write_port(data)
            self.flush_input()
            return True

    def update_rx_data(self, data):
        pass

class USB(SerialComm):
    def __init__(self):
        SerialComm.__init__(self)
    def connect(self, port, baud_rate):
        self.connect_port(port=port, baud_rate=baud_rate, timeout=0.5)

    def disconnect(self):
        self.disconnect()

    def transmit_message(self, data):
        self.write(data)

    def set_variables(self):
        pass
