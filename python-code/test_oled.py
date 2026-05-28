from machine import Pin, I2C
import ssd1306
import time

# I2C setup: GP0=SDA, GP1=SCL
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Scan I2C for OLED address
devices = i2c.scan()
print("I2C devices found:", [hex(d) for d in devices])

if not devices:
    print("No OLED found! Check wiring.")
else:
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    oled.fill(0)
    oled.text("Smart Bottle", 0, 0)
    oled.text("v1.0", 0, 10)
    oled.text("---", 0, 20)
    oled.text("Water: 0ml", 0, 35)
    oled.text("Temp: 25C", 0, 45)
    oled.text("Happy!", 0, 55)
    oled.show()

    print("OLED test passed! Display should show text.")
