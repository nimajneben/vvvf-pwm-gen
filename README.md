# vvvf-pwm-gen
 VVVF PWM waveform reproduction

This python script takes three WAVE files:

* signalu.wav - original AC sine wave (preferably -10db)
* signalv.wav - the same AC sine wave, but 120 degrees out of phase (preferably -10dB)
* carrier.wav - the carrier wave (0 dB)

The three files need to be all mono, have the exact samplerate, and have the same duration.

The script will generate three files:

* pwmu.wav - the generated PWM based on signalu.wav
* pwmv.wav - the generated PWM based on signalv.wav
* pwm.wav - (pwmu.wav - pwmv.wav) final pwm wave.

# How the PWM is generated

The script checks for each frame of audio:

    if the amplitude of the signal wave at the frame

    is greater than 

    the amplitude of the carrier wave at the same frame.
    
    if so the PWM amplitude at the frame would be 1.
    if not the PWM amplitude at the frame would be 0.
    
 The script generates two PWM, one where signal is in phase, and one where signal is 120 degrees out of phase.
 
##
This script is based on yuppi5's guidance on PWM waveform reproduction.

https://yuppi5.hateblo.jp/entry/pwm-toc
