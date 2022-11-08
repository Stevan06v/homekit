# https://docs.micropython.org/en/latest/esp8266/quickref.html#ssd1306-driver
# https://randomnerdtutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/

# Display Image & text on I2C driven ssd1306 OLED display
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import machine
import utime
import framebuf
from machine import Pin, SPI
import socket

prefixes = ["connecting", "init", "ip addr"]

fan = machine.Pin(11, machine.Pin.OUT)


fan.value(1)

# Raspberry Pi logo as 32x32 bytearray
# image into hex -> bytearray
# bytearray function takes a hex value and cenverts i into an bytearry, 
buffer_raspi = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

BUFFER_RASPI_WIDTH = 32
BUFFER_RASPI_HEIGHT = 32

sda=machine.Pin(8) # init sda default GPIO-Pin 8
scl=machine.Pin(9) # init slc default GPIO-Pin 9

WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height
BORDER = 5 # oled border

i2c = I2C(0, scl=scl, sda=sda, freq=200000)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # init oled-display

fb = framebuf.FrameBuffer(buffer_raspi, BUFFER_RASPI_WIDTH, BUFFER_RASPI_HEIGHT, framebuf.MONO_HLSB)

def clear_screen():
    oled.fill(0)

def display_curr_process():
    oled.text(prefixes[1] + "...", 0, BUFFER_RASPI_HEIGHT + 1)
    oled.show()

def start_up_screen():
    center_startup = 20
    clear_screen()
    oled.blit(fb, 0, center_startup)
    
    # show date
    oled.text("00:00", 0, 0)
    oled.text("01.09", 89, 0)

    # centered logo + text
    oled.text("Homekit 0.1v", BUFFER_RASPI_WIDTH + 1, int(BUFFER_RASPI_HEIGHT / 2 - 10 + center_startup))
    oled.text("by Stevan V.", BUFFER_RASPI_WIDTH + 1, int(BUFFER_RASPI_HEIGHT / 2 + center_startup))

    oled.show()


def start_up():
    start_up_screen()
    

start_up()

# animation  for display
# max speed : 3 else pixel error

# scroll out horizontally [y]
def scroll_out_screen(speed):
  for x in range ((oled.width+1)/speed):
    for y in range (HEIGHT):
      oled.pixel(x, y, 0)
    oled.scroll(speed , 0)
    oled.show()

# scroll out vertically [x]
def scroll_out_screen_v(speed):
  for i in range ((15) / speed):
    for j in range (oled.width):
      oled.pixel(j, i, 0)
    oled.scroll(0, speed)
    oled.show()



