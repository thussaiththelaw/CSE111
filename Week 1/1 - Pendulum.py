import math

length_of_pendulum = float(input('How Long is the pendulum?: '))
time = 2 * math.pi * (math.sqrt(length_of_pendulum / 9.81))

print (f'{time:.2f}')