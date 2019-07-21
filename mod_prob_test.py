''' Test using the DS18B20 Probe '''

import os
import glob
import time

os.system('modprob w1-gpio')
os.system('modprob w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file,'r') as f:
        data = f.readlines()
    return data

def read_temp(scale):
    data = read_temp_raw()
    if 'yes' in data[0].lower():
        c = float((data[-1][data[-1].index('t=')+2:]))/1000
        f = c * 9.0 / 5.0 + 32.0
    else:
        'Invalid Temp'
    
    if scale.lower() == 'c':
        return "Temperature: {:,.2f} Celsius".format(c)
    else:
        return "Temperature: {:,.2f} Fahrenheit".format(f)
    
while True:
    print(read_temp('f'))
    
