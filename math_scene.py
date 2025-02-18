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

            # # Animate the curve and the moving dot together
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
        d1.target.shift([-2.9,-2,0])
        d1_t3 = MathTex('[3,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d1,UP))

        d2.generate_target()
        d2.target.shift([1.1,-2,0])
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
        bob = Dot(point=axes3.c2p(start_x, start_y), color=RED).scale(2)
        rod = Line(start=axes3.c2p(0, 5), end=bob.get_center(), color=WHITE)

        rod.add_updater(lambda r: r.put_start_and_end_on(axes3.c2p(0, 5), bob.get_center()))

        # Animate the dot along the curve

        pendulum_animation = MoveAlongPath(bob, curve2, run_time=5, rate_func=there_and_back)

        self.add(rod, bob)
        self.play(AnimationGroup(pendulum_animation,pendulum_animation,pendulum_animation))
        self.wait(2)
        
        self.play(Uncreate(bob),Uncreate(rod))
        self.wait()


        axes4 = Axes(
            x_range=[-1, 13, 1],
            y_range=[-4, 4, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE},
            tips=False
        )
        axes4.x_axis.set_color(BLACK)

        axes5 = Axes(
            x_range=[-4, 10, 1],
            y_range=[-4, 4, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE},
            tips=False
        )

        d0.generate_target()
        d0.target.shift([-6,-1.5,0])
        d0_t4 = MathTex('[0,5]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d0,RIGHT+UP))

        d2.generate_target()
        d2.target.shift([-3.1,2,0])
        d1_t4 = MathTex('[3,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d1,RIGHT+UP))

        d1.generate_target()
        d1.target.shift([-9.1,0.5,0])
        d2_t3 = MathTex('[-3,0]').scale(0.7).add_updater(lambda mob: dot_updater(mob,d2,RIGHT+UP))

        convex1_eq = lambda x: (-1 * math.sqrt(16 - x**2)) + 3.48
        convex1 = axes5.plot_parametric_curve(lambda t: np.array([convex1_eq(t),t,0]),
                                             t_range=[-2, 2],
                                             color=BLUE
                                            )

        convex2_eq = lambda x: (1 * math.sqrt(16 - x**2)) - 3.48
        convex2 = axes5.plot_parametric_curve(lambda t: np.array([convex2_eq(t),t,0]),
                                             t_range=[-2, 2],
                                             color=BLUE
                                            )


        self.play(ReplacementTransform(axes3,axes4),
                #   ReplacementTransform(plot2,plot3),
                  MoveToTarget(d0),
                #   ReplacementTransform(d2_t2,d2_t3),
                  MoveToTarget(d1),
                #   ReplacementTransform(d1_t2,d1_t3),
                  MoveToTarget(d2),
                #   ReplacementTransform(d0_t2,d0_t3),
                ReplacementTransform(curve2, convex1),
                Uncreate(plot3),
                Create(convex2)
                  )
        self.wait(2)
        
        def create_line_between_axes(axes_start, axes_end, start_point, end_point, color=WHITE, dash_length= 0.1):
            start = axes_start.c2p(*start_point)
            end = axes_end.c2p(*end_point)
            return DashedLine(start, end, color=color)

        axes6 = Axes(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE},
            tips=False
        )

        axes7 = Axes(
            x_range=[-10, 3, 1],
            y_range=[-4, 4, 1], 
            x_length=14,  # Match the default scale of NumberPlane
            y_length=8,   # Match the default scale of NumberPlane
            axis_config={"color": WHITE},
            tips=False
        )



        lray1 = create_line_between_axes(axes4, axes5, [0,1.5,0], [0,1.5,0], color = WHITE, dash_length= 0.1)
        lray2 = create_line_between_axes(axes4, axes5, [0,0,0], [0,0,0], color = BLUE, dash_length= 0.1)
        lray3 = create_line_between_axes(axes4, axes5, [0,-1.5,0], [0,-1.5,0], color = RED, dash_length= 0.1)

        lray4 = create_line_between_axes(axes5, axes6, [0,1.5,0], [0,0.75,0], color = WHITE, dash_length= 0.1)
        lray5 = create_line_between_axes(axes5, axes6, [0,0,0], [0,0,0], color = BLUE, dash_length= 0.1)
        lray6 = create_line_between_axes(axes5, axes6, [0,-1.5,0], [0,-0.75,0], color = RED, dash_length= 0.1)

        lray7 = create_line_between_axes(axes6, axes7, [0,0.75,0], [0,1.5,0], color = WHITE, dash_length= 0.1)
        lray8 = create_line_between_axes(axes6, axes7, [0,0,0], [0,0,0], color = BLUE, dash_length= 0.1)
        lray9 = create_line_between_axes(axes6, axes7, [0,-0.75,0], [0,-1.5,0], color = RED, dash_length= 0.1)

        lray10 = create_line_between_axes(axes7, axes7, [0,1.5,0], [2,1.5,0], color = WHITE, dash_length= 0.1)
        lray11 = create_line_between_axes(axes7, axes7, [0,0,0], [2,0,0], color = BLUE, dash_length= 0.1)
        lray12 = create_line_between_axes(axes7, axes7, [0,-1.5,0], [2,-1.5,0], color = RED, dash_length= 0.1)

        concave1_eq = lambda x: (-1 * math.sqrt(16 - x**2)) + 4.2
        concave1 = axes6.plot_parametric_curve(lambda t: np.array([concave1_eq(t), t, 0]), 
                                                t_range=[-2, 2], 
                                                color=WHITE)

        concave2_eq = lambda x: (1 * math.sqrt(16 - x**2)) - 4.2
        concave2 = axes6.plot_parametric_curve(lambda t: np.array([concave2_eq(t), t, 0]), 
                                               t_range=[-2, 2], 
                                               color=WHITE)

        concave3 = Line(start=axes6.c2p(-0.75, 2, 0), 
                          end=axes6.c2p(0.75, 2, 0), 
                          color=WHITE)

        concave4 = Line(start=axes6.c2p(-0.75, -2, 0), 
                          end=axes6.c2p(0.75, -2, 0), 
                          color=WHITE)


        planner_eq = lambda x: (1 * math.sqrt(36 - x**2)) - 6.2
        planner1 = axes7.plot_parametric_curve(lambda t: np.array([planner_eq(t), t, 0]), 
                                               t_range=[-2, 2], 
                                               color=WHITE)
        planner2 = Line(start=axes7.c2p(-0.52, 2, 0), 
                          end=axes7.c2p(0.2, 2, 0), 
                          color=WHITE)

        planner3 = Line(start=axes7.c2p(-0.52, -2, 0), 
                          end=axes7.c2p(0.2, -2, 0), 
                          color=WHITE)

        planner4 = Line(start=axes7.c2p(0.2, -2, 0), 
                          end=axes7.c2p(0.2, 2, 0), 
                          color=WHITE)

        d0.generate_target()
        d0.target.shift([3,0,0])

        d1.generate_target()
        d1.target.shift([3,0,0])

        d2.generate_target()
        d2.target.shift([3,0,0])

        self.play(
                 Create(lray1),
                  Create(lray2),
                  Create(lray3),
                  MoveToTarget(d0),
                  MoveToTarget(d1),
                  MoveToTarget(d2),

                #   Create(concave1),
                #   Create(concave2),
                #   Create(concave3),
                #   Create(concave4),
                #   Create(lray4),
                #   Create(lray5),
                #   Create(lray6),
                #   Create(planner1),
                #   Create(planner2),
                #   Create(planner3),
                #   Create(planner4),
                #   Create(lray7),
                #   Create(lray8),
                #   Create(lray9),
                #   Create(lray10),
                #   Create(lray11),
                #   Create(lray12),
        )

        self.wait()

        d0.generate_target()
        d0.target.shift([3,-0.75,0])

        d1.generate_target()
        d1.target.shift([3,0.75,0])

        d2.generate_target()
        d2.target.shift([3,0,0])

        self.play(
            Create(concave1),
            Create(concave2),
            Create(concave3),
            Create(concave4),
            Create(lray4),
            Create(lray5),
            Create(lray6),
            MoveToTarget(d0),
            MoveToTarget(d1),
            MoveToTarget(d2),

        )

        self.wait()
        
        d0.generate_target()
        d0.target.shift([3.75,0.75,0])

        d1.generate_target()
        d1.target.shift([3.75,-0.75,0])

        d2.generate_target()
        d2.target.shift([3.75,0,0])

        self.play(
            Create(planner1),
            Create(planner2),
            Create(planner3),
            Create(planner4),
            Create(lray7),
            Create(lray8),
            Create(lray9),
            MoveToTarget(d0),
            MoveToTarget(d1),
            MoveToTarget(d2),
        )

        self.wait()

        self.play(
             Create(lray10),
             Create(lray11),
             Create(lray12),
        )
        self.play(
            *[obj.animate.shift(LEFT * 6).set_opacity(0) for obj in [
                lray1, lray2, lray3,convex1,convex2, concave1, concave2, concave3, concave4,
                lray4, lray5, lray6, planner1, planner2, planner3, planner4, lray7, lray8, lray9
            ]],
            

            lray10.animate.move_to(axes4.c2p(1, 1.5, 0)),
            lray11.animate.move_to(axes4.c2p(1, 0, 0)),
            lray12.animate.move_to(axes4.c2p(1, -1.5, 0)),
            run_time=3

        )
            
        self.wait()


        acwave1 = axes7.plot(lambda t: 1.5 * math.sin(20 * PI * t), color=RED)

        self.play(
            Create(acwave1)
        )
