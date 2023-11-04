from manim import *
import random
import math

class Marjorie(Scene):
    
    # Each animation will be done during two beats
    tempo = 5.0/4.0
    limit_up = 2
    limit_down = 2
    movement_range = 2.0
    
    def move_rectangle(self, limit_left, limit_right, box_x, box_y):
        # random movement directions
        vx = random.uniform(-self.movement_range, self.movement_range)
        vy = random.uniform(-self.movement_range, self.movement_range)
        # normalize
        l = math.sqrt(vx*vx + vy*vy)
        vx/=l
        vy/=l
        
        # Stay within limits
        if (box_x + vx > limit_right):
            vx = min(vx, -vx)
            
        elif (box_x + vx < limit_left):
            vx = max(vx, -vx)
            
        if (box_y + vy > self.limit_up):
            vy = min(vy, -vy)
            
        elif (box_y + vy < self.limit_down):
            vy = max(vy, -vy)
            
        return [vx, vy]
        
    def construct(self):
    
        # Rectangle that's the main character
        box = Rectangle (stroke_color = GREEN_C, fill_color=RED_B, fill_opacity=0.5, height=0.5, width=0.5)
        self.add(box)

        # Initial movement limits prior any lyrics
        limit_left = -10
        limit_right = 10
        
        line = NumberLine(
            x_range=[-20, 20, 2],
            length = 10,
            color=BLUE,
            include_numbers=False
        )
        self.add(line)
       
        # Song intro      
        for i in range(6):
            bx = box.get_center()[0]
            by = box.get_center()[1]
            mov = self.move_rectangle(limit_left, limit_right, bx, by)
            print(bx, by)
            # animate
            self.play(box.animate.shift(RIGHT*mov[0] + UP*mov[1]), run_time=self.tempo)
        
        # Never be so kind you for get to be clever
        t1 = Text("Never be so kind you forget to be clever", font_size=12)
        t1.set_y(2)
        self.add(t1)
        limit_right = 3
        for i in range(8):
            bx = box.get_center()[0]
            by = box.get_center()[1]
            print(bx, by)
            mov = self.move_rectangle(limit_left, limit_right, bx, by)
            # animate
            self.play(box.animate.shift(RIGHT*mov[0] + UP*mov[1]), run_time=self.tempo)
            
        # Never be so clever you for get to be kind
        t2 = Text("Never be so clever you forget to be kind", font_size=12)
        t2.set_y(-2)
        self.add(t2)
        limit_left = -3
        for i in range(8):
            bx = box.get_center()[0]
            by = box.get_center()[1]
            print(bx, by)
            mov = self.move_rectangle(limit_left, limit_right, bx, by)
            # animate
            self.play(box.animate.shift(RIGHT*mov[0] + UP*mov[1]), run_time=self.tempo)    
            