from machine import Pin, PWM
from time import sleep

# Luo led olio
led = Pin("LED", Pin.OUT)

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# funktio ledin vilkuttamiselle
def vilkuta():
    led.on()
    sleep(2)
    led.off()


# liikkumus funktiot
def eteenpäin(nopeusR, nopeusL, aika):
    m1.value(1) # oikean moottorin suunta
    m2.value(1) # vasemman moottorin suunta
    e1.duty_u16(nopeusR) # oikean moottorin nopeus
    e2.duty_u16(nopeusL) # vasemman moottorin nopeus
    sleep(aika) # ajoaika

def käännyoikealle(nopeusR, nopeusL, aika):
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeusR)
    e2.duty_u16(nopeusL)
    sleep(aika)

def käännyvasemmalle(nopeusR, nopeusL, aika):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeusR)
    e2.duty_u16(nopeusL)
    sleep(aika)

def taaksepäin(nopeusR, nopeusL, aika):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeusR)
    e2.duty_u16(nopeusL)
    sleep(aika)

def pysähdy(nopeusR, nopeusL, aika):
    e1.duty_u16(nopeusR)
    e2.duty_u16(nopeusL)
    sleep(aika)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# tauko
pysähdy(0, 0, 2)

# vilkuttaa lediä
vilkuta()

# eteenpäin
eteenpäin(33000, 33000, 3)

# tauko
pysähdy(0, 0, 2)

# kääntyyoikealle
käännyoikealle(30000, 60000, 3)

# tauko 
pysähdy(0, 0, 2)

# taaksepäin oikealle
taaksepäin(60000, 23000, 2)

# tauko 
pysähdy(0, 0, 2)

# eteenpäin
eteenpäin(33000, 33000, 3)

# tauko 
pysähdy(0, 0, 2)

# vilkuttaa lediä
vilkuta()

