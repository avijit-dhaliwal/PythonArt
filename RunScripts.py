import pygame
import sys

# Import all your animation scripts
import CosmicBloom
import FractalTree
import Hyperdimensional
import QuantumVisualizer
import FluidDynamics
import Mandelbrot
import Fractal
import ParticleLife
import Bioluminescent
import QuantumWave

def run_animation(animation_module):
    animation_module.run()
    pygame.quit()

animations = {
    '1': ('Cosmic Bloom', CosmicBloom),
    '2': ('Fractal Tree Explorer', FractalTree),
    '3': ('Hyperdimensional Wormhole', Hyperdimensional),
    '4': ('Quantum Entanglement Visualizer', QuantumVisualizer),
    '5': ('Neon Fluid Dynamics', FluidDynamics),
    '6': ('Mandelbrot Set Explorer', Mandelbrot),
    '7': ('Fractal Dimension Shifter', Fractal),
    '8': ('Particle Life Simulation', ParticleLife),
    '9': ('Bioluminescent Ecosystem', Bioluminescent),
    '10': ('Quantum Wave Visualization', QuantumWave)
}

def main():
    while True:
        print("\nWelcome to the Python Art Gallery!")
        for key, (name, _) in animations.items():
            print(f"{key}: {name}")
        print("Q: Quit")

        choice = input("Choose an animation to run (or 'Q' to quit): ").upper()

        if choice == 'Q':
            sys.exit()
        elif choice in animations:
            print(f"Running {animations[choice][0]}...")
            run_animation(animations[choice][1])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()