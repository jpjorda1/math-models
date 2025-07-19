# projectile-simulator
This file is Python code for the trajectory of a baseball given user input exit speed and launch angle.

The code takes as input an exit speed (meters) and launch angle (degrees) and returns the flight time and distance for (1) no air resistance and (2) air resistance (linear and quadratic) using the scipy solve_ivp method. Additionally, the code returns a plot of the baseball's trajectory in both cases.

The example figure that has been included is a plot of Elly de la Cruz's 7/2/24 homer against the LA Dodgers. It left the bat at 51.32 m/s with a launch angle of 35 degrees and traveled approximately 425 ft (129.58 m). This program returns a value of 132.98 m (436.28 ft). This is a percent error of 2.6% and is likely due to imprecise drag coefficients.
