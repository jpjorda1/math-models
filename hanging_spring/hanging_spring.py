1# Write your code here :-)
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint

# Parameters
g = 9.80665 #m/s^2

while True:
    m = float(input("Mass (kg): ")) #kg
    if m > 0:
        break
    else:
        print("Mass must be positive.")


while True:
    k = float(input("Spring constant (kg/s^2): ")) #spring constant kg/s^2

    if k >= 0: #k = 0 is  a valid choice but w2 is not defined because the motion is not periodic
        if k == 0:
            print("k = 0 is free fall and damping ratio is irrelevant.")
            d=0
        else:
            while True:
                d = float(input("Damping ratio (crit=1): "))
                if d >= 0:
                    break
                else:
                    print("Damping ratio must be positive.")
        break
    else:
        print("Spring constant must be non-negative.")

w2 = k / m #natural freq squared (Hz^2)
if w2 != 0:
    L = g / w2 #natural length (m)
    print('===========')
    print(f'The natural frequency is {np.sqrt(w2):.2f}Hz')
    print(f'The natural length is {L:.2f}m')
    print('===========')

#Initial conditions
v0y = float(input("Initial velocity (m/s): "))
y0 = float(input("Initial position (m): "))

#Terminal time
t_final = float(input("How long should I simulate (s)? "))

#Newton's second law with no damped resistance
def oscillator(t, U):
    #x in m, v in m/s
    y, vy = U
    ay = - g - w2 * y #m/s^2
    return [vy, ay]

def damped_oscillator(t, U):
    #x in m, v in m/s
    y, vy = U
    ay = - g - w2 * y - 2 * d * np.sqrt(w2) * vy #m/s^2
    return [vy, ay]


# Run simulation
t_pts = np.linspace(0,t_final,num = 100)
results_osc = spint.solve_ivp(oscillator, (0, t_final), [y0,v0y], t_eval = t_pts)
results_damped = spint.solve_ivp(damped_oscillator, (0, t_final), [y0,v0y], t_eval=t_pts)

#Plot
plt.plot(t_pts, results_osc.y[0,:],  label = "Harmonic Oscillator")
plt.plot(t_pts, results_damped.y[0,:], label = "Damped Harmonic Oscillator")
plt.plot(0,0)
#plt.plot(results_osc.y[0,:],np.zeros(len(results_osc.y[0,:])), label = "ground") #ground
plt.title("Harmonic Oscillator")
plt.xlabel("Time (s)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.show()# Write your code here :-)
