# Electric Dipole Simulation
![Electric Dipole Simulation](assets/dipole_animation.gif)
## Overview
A programmatic physics simulation of an electric dipole aligning within a uniform electric field, developed entirely in Python using the Manim animation engine. I built this project to visually model damped harmonic oscillation by continuously recalculating torque and angular velocity frame-by-frame.

## Technical Stack
* **Language:** Python
* **Libraries:** Manim (Mathematical Animation Engine), NumPy

## Mathematical Model & Physics Engine
Rather than relying on pre-built animation paths, I implemented a custom physics updater function that relies on numerical integration to simulate realistic, damped movement. 

The simulation dynamically calculates the following at every frame (`dt`):
* **Torque:** `tau = p_magnitude * E_strength * sin(theta)`
* **Angular Acceleration:** Applied with a damping coefficient (`damping = 0.15`) to simulate resistance and eventual alignment with the electric field.
* **Euler Integration:** Continuously updates the angular velocity and current angle to rotate the VGroup objects accurately in 2D space.

## Setup & Execution
1. Ensure Python 3.8+ is installed.
2. Install the required dependencies:
```bash
      pip install manim numpy
```
3. Run the simulation and generate the video output:
```Bash
      manim -pql main.py PerfectDipoleSimulation
```
(Note: The -pql flag renders the video in low quality for rapid previewing. Use -pqh for high quality, 1080p 60fps rendering).