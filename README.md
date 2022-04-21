# Guard Dog

## Was demo'd May 5th 2022 at Louisiana Tech University's IESB.

The code for our project lies in this repository

## Authors

Jack Branch

John Lambert

Andrew Bellucci

## Project Information

### Description:

This project aims to improve the lives of those who walk around campus
Something like three or four people have been hit by cars on Tech's campus this academic term
Guard Dog is a safety system designed to protect pedestrians walking the streets of LA Tech's campus.
It uses a railroad-inspired guard arm system to prevent cars from hitting pedestrians.
The arms are lowered when enough pressure is detected on the yellow, crossing squares.
Guard Dog also makes use of a GUI system to add emergency service contact functionality.
for this, the Twilio API is used.

### Technology Used:

#### The project makes use of the following hardware:

GPIO header on the raspberry pi 4

Two 0.5 inch pressure sensitive resistors

several male to male wires

several male to female wires

LCD touchscreen display for raspberry pi

Two SG98 servos

Many popsicle sticks

#### The project makes use of the following libraries:

Twilio API for making calls

Threading library for asynchronicity between GUI and arm system

TKinter library for GUI (Trash. Please don't use)

RPi.GPIO library for resistor detection

gpiozero for controlling servos

Time library for setting sleep intervals

PiGPIOFactory for mitigating jitter of servos

The other imports were our own

### Future Improvements

Ideally, the system would detect cars in proximity of the arm to prevent the arm from smacking cars

We would also implement safeguards to prevent spamming of phones, and pressure pads

The improvements should be simple enough to implement

### Addressing a few critiques

#### Guard Dog would slow down traffic

One of the critiques that we received claimed that the arm system would slow down traffic.
While this may be true to some extent, it's not as drastic as some might think.
If people actually stopped for pedestrians as they should, they'd be slowed down anyway.
So it makes little difference whether it's an arm or a person slowing you down.
This way, when someone gets impatient, instead of someone getting hit by a car, a
mechanical arm might break

#### Guard Dog would be abused for fun

Another critique we received claimed that the arm system could pretty easily be used to troll
drivers and slow them down. Continuously jumping on the pressure pads and resetting the timer for example.
In a realistic implementation and future iterations of the model, there would be safeguards in place to prevent
this sort of juvenile behavior