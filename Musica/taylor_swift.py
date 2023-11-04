from manim import *
import random
import math

class Marjorie(Scene):
    def construct(self):
    
        # Rectangle that's the main character
        box = Rectangle (stroke_color = GREEN_C, fill_color=RED_B, fill_opacity=0.5, height=0.5, width=0.5)
        self.add(box)
        # Normalized velocity vector to be updated every 
        vx = random.uniform(-2,2)
        vy = random.uniform(-2,2)
        l = math.sqrt(vx*vx + vy*vy)
        vx/=l
        vy/=l
        
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=False
        )
        self.add(l0)
        
        # Each animation will be done during two beats
        for i in range (6):
            # The animation corresponds to half of Marjorie's bpm
            self.play(box.animate.shift(RIGHT*vx + UP*vy), run_time=5.0/4.0)
            vx = random.uniform(-2.0,2.0)
            vy = random.uniform(-2.0,2.0)
            l = math.sqrt(vx*vx + vy*vy)
            vx/=l
            vy/=l
            
        