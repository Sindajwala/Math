from manim import *
import numpy as np
import math

class math2(Scene):
    def construct(self):

       

        def dot_updater(mob, ref_dot, direction):
            mob.next_to(ref_dot, direction)

        # def d1_updater(mob):
        #     mob.next_to(d1,RIGHT)
        #     return mob

        # def d2_updater(mob):
        #     mob.next_to(d2,LEFT)
        #     return mob

        #Appearance of Dot START

        d0 = Dot(point=ORIGIN)
        d0_t = MathTex('d_0=[0,0]').next_to(d0,DOWN).scale(0.7)
        mob = Circle(radius=4, color=TEAL_A)

        self.play(FadeIn(d0),
        #Broadcast(mob),
        Create(d0_t))
        self.wait()

        #Appearance of dot END

        #Appearance of line START

        l1 = Line(start=[-2,0,0],end=[2,0,0])
        d1= Dot(point=[2,0,0],color=RED)
        d2= Dot(point=[-2,0,0,],color=BLUE)
        
        d2_t = MathTex('d_2=[-2,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d2,LEFT))
        d2_t1= MathTex('d_2=[-2,-2]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d2,LEFT))

        d1_t = MathTex('d_1=[2,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d1,RIGHT))
        d1_t1 = MathTex('d_1=[2,2]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d1, RIGHT))
        
       
      
        self.play(GrowFromPoint(d1, d0), GrowFromPoint(d2, d0), FadeIn(d1_t), Create(d2_t), GrowFromCenter(l1))
        self.wait(2)

        #Appearance of line END

        #Transformation of line START

        eq1_t = MathTex('y=mx+c').to_corner(UL).scale(1.2).shift(RIGHT*1.5)
        plane = NumberPlane(

            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

          # Axes aligned with the NumberPlane
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE},
            tips=False
        )
        # Match the center of the NumberPlane
        axes.move_to(plane.get_center())

        d0_t.generate_target()
        d0_t.target.next_to(d0,RIGHT+DOWN*0.2)
        d1.generate_target()
        d1.target.shift([0,2,0])
        d2.generate_target()
        d2.target.shift([0,-2,0])

        self.play(MoveToTarget(d0_t),
                  MoveToTarget(d1),
                  ReplacementTransform(d1_t,d1_t1) ,
                  MoveToTarget(d2),
                  ReplacementTransform(d2_t,d2_t1),
                  l1.animate.put_start_and_end_on([-2, -2, 0], [2, 2, 0]),
                  Create(eq1_t),
                  FadeIn(plane),
                  FadeIn(axes)
                )

        self.wait(3)

        #linear equation END

        #Quadratic equation START

        axes2 = Axes(
            x_range=[-1, 13, 1],
            y_range=[-4, 4, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE, "include_numbers": True},
            tips=False
        )

        eq2 = lambda x: (-0.121 * x**2) + (1.7 * x) - 2.9
        eq2_t = MathTex('y = ax^2 + bx + c').to_corner(UL).scale(1.2).shift(RIGHT*1.5)
        plot2 = axes2.plot(eq2,x_range=[-2,13])

        d2.generate_target()
        d2.target.shift([-2,2,0])
        d2_t2 = MathTex('[-2,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d2,LEFT+UP))

        d1.generate_target()
        d1.target.shift([4,-2,0])
        d1_t2 = MathTex('[12,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d1,LEFT*1.5+UP))

        d0.generate_target()
        d0.target.shift([1.02,3.06,0])
        d0_t2 = MathTex('[7,3]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d0,UP))

        self.play(ReplacementTransform(axes,axes2), 
                  FadeOut(plane), 
                  ReplacementTransform(l1,plot2,run_time=3),
                  ReplacementTransform(eq1_t,eq2_t),
                  MoveToTarget(d2),
                  ReplacementTransform(d2_t1,d2_t2),
                  MoveToTarget(d1),
                  ReplacementTransform(d1_t1,d1_t2),
                  MoveToTarget(d0),
                  ReplacementTransform(d0_t,d0_t2),
                  )
        self.wait(4)

        # quad1 = lambda x: -0.2*(x-2)*(x-5)
        # quad2 = lambda x: -0.2*(x-2)*(x-6)
        # quad3 = lambda x: -0.2*(x-2)*(x-7)
        # quad4 = lambda x: -0.2*(x-2)*(x-8)
        # quad5 = lambda x: -0.16*(x-2)*(x-10)

        # plotq1 = axes2.plot(quad1,x_range=[2,5])
        # plotq2 = axes2.plot(quad2,x_range=[2,6])
        # plotq3 = axes2.plot(quad3,x_range=[2,7])
        # plotq4 = axes2.plot(quad4,x_range=[2,8])
        # plotq5 = axes2.plot(quad5,x_range=[2,10])

        # self.play(Create(plotq1),
        #           Create(plotq2),
        #           Create(plotq3),
        #           Create(plotq4),
        #           Create(plotq5),
                
        #           )
        
        # self.wait(2)
        

        functions = [
            lambda x: -0.2*(x-2)*(x-5),
            lambda x: -0.2*(x-2)*(x-6),
            lambda x: -0.2*(x-2)*(x-7),
            lambda x: -0.2*(x-2)*(x-8),
            lambda x: -0.16*(x-2)*(x-10),
        ]

        range = [[2,5],
                 [2,6],
                 [2,7],
                 [2,8],
                 [2,10]
        ]

        colors = [RED, BLUE, GREEN, ORANGE, PURPLE]

        # Plot each function with a moving dot and dashed line
        for i, func in enumerate(functions):
            # Generate the curve
            curve = axes2.plot(func, range[i], color=colors[i])

            # Convert solid line to dashed line
            dashed_curve = DashedVMobject(curve, num_dashes=30)

            # Create a dot at the start of the curve
            start_x = 2
            start_y = func(start_x)
            dot = Dot(color=colors[i]).move_to(axes2.c2p(start_x, start_y))

            # Animate the curve and the moving dot together
            # self.play(Create(dashed_curve),
            #           MoveAlongPath(dot, curve), 
            #           run_time=2
            #           )
            # self.wait(1)

        self.wait(2)

      

        axes3 = Axes(
            x_range=[-7, 7, 1],
            y_range=[-2, 6, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE,"include_numbers": True},
            tips=False
        )
        # Match the center of the NumberPlane
        axes3.move_to(plane.get_center())

        eq3 = lambda x: (-1 * math.sqrt(16 - x**2))+2.65
        plot3 = axes3.plot(eq3,x_range=[-3,3])

        d0.generate_target()
        d0.target.shift([-1,0,0])
        d0_t3 = MathTex('[0,5]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d0,RIGHT))

        d1.generate_target()
        d1.target.shift([-3.02,-2,0])
        d1_t3 = MathTex('[3,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d1,UP))

        d2.generate_target()
        d2.target.shift([1.02,-2,0])
        d2_t3 = MathTex('[-3,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d2,UP))


        self.play(ReplacementTransform(axes2,axes3),
                  ReplacementTransform(plot2,plot3),
                  MoveToTarget(d2),
                  ReplacementTransform(d2_t2,d2_t3),
                  MoveToTarget(d1),
                  ReplacementTransform(d1_t2,d1_t3),
                  MoveToTarget(d0),
                  ReplacementTransform(d0_t2,d0_t3),
                  )
        self.wait(2)



        # l3 = DashedLine(start = [0,3,0], end = [3,-2,0], dash_length=0.2)

        #   # Define the parabola curve
        # pcurve = lambda x: (-1 * np.sqrt(16 - x**2)) + 2.65
        # curve2 = axes3.plot(pcurve, x_range=[3, -3], color=BLUE)

        # # Create a dashed version of the curve
        # dashed_curve2 = DashedVMobject(curve2, num_dashes=15)

        # # Place a dot on the curve at x=2
        # start_x = 2
        # start_y = pcurve(start_x)
        # dot2 = Dot().move_to(axes3.c2p(start_x, start_y))

        # # Animate the dashed curve and the dot moving along it
        # self.play(Create(dashed_curve2), MoveAlongPath(dot2, curve2), run_time=2)


         # Define the curve equation
        pcurve = lambda x: (-1 * math.sqrt(16 - x**2)) + 2.65

        # Plot the curve
        curve2 = axes3.plot(pcurve, x_range=[-3, 3], color=BLUE)
        dashed_curve2 = DashedVMobject(curve2, num_dashes=20)

        # Initial position of the dot
        start_x = -3
        start_y = pcurve(start_x)
        dot2 = Dot(point=axes3.c2p(start_x, start_y), color=RED)
        self.add(dot2)

        end_x = 3
        end_y = pcurve(end_x)
        end_point = axes3.c2p(end_x, end_y)

        l3 = DashedLine(start=axes3.c2p(0, 3), end=end_point, dash_length=0.2)

        # Animate the dot along the curve
        self.play(Create(dashed_curve2),MoveAlongPath(dot2, curve2), run_time=4)

        # Calculate the endpoint based on the final x value
        

        # Create the dashed line from the origin to the final dot position
        

        self.wait(2)
        


        





