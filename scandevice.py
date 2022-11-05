import machine
sda = machine.Pin(8)
slc = machine.Pin(9)
i2c = machine.I2C(0,sda=sda, slc=slc,freq=400000)

print("Scan i2c bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c devices")
else:
    print("i2c device found: ", len(devices))
    
    for device in devices:
        prinf("Decimal address: ", device, "| Hexa adress: ", hex(device))