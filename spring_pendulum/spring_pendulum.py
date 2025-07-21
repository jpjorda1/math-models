# Write your code here :-)
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

w2 = k / m #natural freq squared (1/s^2) of spring osc

if w2 != 0:
    L = g / w2 #natural length (m)
    #w2pend = g / L #natural freq squared of pendulum osc
    print('===========')
    print(f'The natural spring frequency is {np.sqrt(w2):.2f}Hz')
    print(f'The natural length is {L:.2f}m')
    print('===========')

#Initial conditions
v0 = 0 #Primarily interested in pulling the spring.
r0 = float(input("Initial pull length (m): "))
theta0 = float(input("Initial angle (deg): ")) #angle measured at (0,0) with hanging pend as hypotenuse
#Terminal time
t_final = 100 * np.sqrt(w2) #simulating for two natural periods

#Cartesian coordinates
x0 = r0 * np.sin(np.radians(theta0))
y0 = -r0 * np.cos(np.radians(theta0))

v0x = 0 #makes it easier to add non-zero initial velocity later
v0y = 0

#Newton's second law for spring pedulum with damping
def spring_pendy(t, U):
    #x in m, v in m/s
    x, y, vx, vy = U
    ax = - w2 * x - 2 * d * np.sqrt(w2) * (vx * x + vy * y) * x / (x**2 + y**2)
    ay = -g - w2 * y - 2 * d * np.sqrt(w2) * (vx * x + vy * y) * y / (x**2 + y**2) #m/s^2
    return [vx, vy, ax, ay]


# Run simulation
t_pts = np.linspace(0,t_final,num = 10000)
results_spring_pend = spint.solve_ivp(spring_pendy, (0, t_final), [x0, y0, v0x, v0y], t_eval = t_pts)

#Plot

#Plotting x and y as a function of time for testing
plt.plot(t_pts, results_spring_pend.y[0,:], label = f"k={k:.2f}kg/s^2, m={m:.2f}kg, d={d:.2f}")
plt.title("Spring Pendulum x-axis")
plt.show()
plt.plot(t_pts, results_spring_pend.y[1,:], label = f"k={k:.2f}kg/s^2, m={m:.2f}kg, d={d:.2f}")
plt.title("Spring Pendulum y-axis")
plt.show()

#Plotting the spring on x and y
plt.plot(results_spring_pend.y[0,:], results_spring_pend.y[1,:], label = f"k={k:.2f}kg/s^2, m={m:.2f}kg, d={d:.2f}")
plt.plot(0,0,'ro',label = 'Origin')
plt.title("Spring Pendulum")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
