# Analog Clock

A simple Python analog and digital clock made with the `turtle` module.

## Run

```bash
python3 analog_clock.py
```

Close the Turtle window to stop the program.

## Method

The program uses Python's `turtle` module to draw the clock face, tick marks, and hands. It gets the current time with `datetime`, converts each time value into an angle, and updates the analog and digital displays 6 times per second.

## Design Summary

The design combines a blue analog clock face with green, yellow, and red hands for the seconds, minutes, and hours. A blue digital display below the clock shows the current time in a large, easy-to-read format.
