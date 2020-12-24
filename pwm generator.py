# Takes two input files (in wave) for the signal wave and the carrier wave.
# The two input files must have the exact samplerate, frames, and number of channels.
# For now, I'll work with mono audio.

# Generates a new 

# two's complement from https://stackoverflow.com/a/9147327/9837377
def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is


import wave
import numpy

# input files
signalu = wave.open('signalu.wav','rb')
signalv = wave.open('signalv.wav','rb')
carrier = wave.open('carrier.wav','rb')

if (signalu.getparams() != carrier.getparams()):
    print("wave files not exactly the same!")
    exit

nsample = signalu.getnframes() if signalu.getnframes() < carrier.getnframes() else carrier.getnframes()

# the generated pwm file
finalu = wave.open('pwmu.wav','wb')
finalv = wave.open('pvmv.wav','wb')
final = wave.open('pwm.wav','wb')

finalu.setparams(signalu.getparams())
finalv.setparams(signalu.getparams())
final.setparams(signalu.getparams())

signalu_data = numpy.frombuffer(signalu.readframes(-1),numpy.int16)
signalv_data = numpy.frombuffer(signalv.readframes(-1),numpy.int16)
carrier_data = numpy.frombuffer(carrier.readframes(-1),numpy.int16)
finalu_data = []
finalv_data = []
final_data = []

print('done converting')

for i in range(nsample):
    if (signalu_data[i] > carrier_data[i]):
        finalu_data.append(127) #max 8-bit signed num
    else:
        finalu_data.append(0)
    
    if (signalv_data[i] > carrier_data[i]):
        finalv_data.append(127)
    else:
        finalv_data.append(0)

    final_data.append(finalu_data[i] - finalv_data[i])
    
    # "two's complement" negative values
    if (final_data[i] < 0):
        final_data[i] = 128
        #print(final_data[i])
        #final_data[i] = twos_comp(final_data[i],8)
        #print(final_data[i])
    
print('done generating u & v pwm')

finalu.writeframes(bytearray(finalu_data))
finalv.writeframes(bytearray(finalv_data))
final.writeframes(bytearray(final_data))

print('done writing u,v, and final pwm')
finalu.close()
finalv.close()
final.close()