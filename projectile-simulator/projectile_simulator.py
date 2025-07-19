# Write your code here :-)
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint

# Parameters
m = .145 #kgs (baseball)
g = 9.81 #m/s^2
initial_velocity = float(input("Exit velocity (m/s): ")) #51.32  # m/s
launch_angle = float(input("Launch angle (degs): ")) #35      # degrees, <=90
c1 = .000155 #baseball
c2 = .00164 #baseball

#Initial position (0,0)
x0=0
y0=0

#Initial velocity
v0x = initial_velocity * np.cos(np.radians(launch_angle))
v0y = initial_velocity * np.sin(np.radians(launch_angle))

#Final time - no air resistance
t_hit = 2 * v0y / g
t_final = t_hit +.001

#Newton's second law with no air resistance
def forces_vacuum(t, U):
    #x in m, v in m/s
    x, y, vx, vy = U
    ax = 0
    ay = -g #m/s^2
    return [vx, vy, ax, ay]

def forces_air(t, U):
    #x in m, v in m/s
    x, y, vx, vy = U
    ax = (- c1 * vx - .5 * c2 * np.sqrt(vx**2 + vy**2) * vx)/m
    ay = -g + (-c1 * vy - .5 * c2 * np.sqrt(vx**2 + vy**2) * vy)/m #m/s^2
    return [vx, vy, ax, ay]

def hit_ground(t,U):
    return U[1]

hit_ground.terminal = True
hit_ground.direction = -1


# Run simulation
t_pts = np.linspace(0,t_final,num = 100)
results_vacuum = spint.solve_ivp(forces_vacuum, (0, t_final), [x0,y0,v0x,v0y], t_eval = t_pts, events = hit_ground)
results_air = spint.solve_ivp(forces_air, (0, t_final), [x0,y0,v0x,v0y], t_eval=t_pts, events = hit_ground)

#Plot
print("=========")
plt.plot(results_vacuum.y[0,:], results_vacuum.y[1,:], label = "trajectory in vacuum")
print(f"Flight distance in vacuum: {results_vacuum.y_events[0][0][0]:.2f}m")
print(f"Flight time in vacuum: {results_vacuum.t_events[0][0]:.2f}s")
print("---------")
plt.plot(results_air.y[0,:], results_air.y[1,:], label = "trajectory in air")
print(f"Flight distance in air: {results_air.y_events[0][0][0]:.2f}m")
print(f"Flight time in air: {results_air.t_events[0][0]:.2f}s")
plt.plot(results_vacuum.y[0,:],np.zeros(len(results_vacuum.y[0,:])), label = "ground") #ground
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.show()
