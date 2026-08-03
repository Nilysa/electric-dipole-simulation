from manim import *
import numpy as np

class PerfectDipoleSimulation(Scene):
    def construct(self):
        # تنظیمات صحنه
        self.camera.background_color = "#1e1e1e"

        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": GREY_D}
        )
        self.add(axes)

        # 1. ایجاد میدان الکتریکی یکنواخت با فلش‌های منظم
        electric_field = VGroup()
        rows = 5
        cols = 8
        for x in np.linspace(-6, 6, cols):
            for y in np.linspace(-3, 3, rows):
                arrow = Arrow(
                    start=ORIGIN,
                    end=RIGHT * 0.8,
                    color=YELLOW,
                    stroke_width=2,
                    tip_length=0.2,
                    buff=0
                ).move_to([x, y, 0])
                electric_field.add(arrow)

        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in electric_field], lag_ratio=0.05))
        self.wait(0.5)

        # 2. ایجاد دوقطبی کاملاً واضح
        dipole_length = 3.0
        
        # بار مثبت
        positive_charge = Dot(color=RED, radius=0.15).move_to(RIGHT * dipole_length / 2)
        plus_label = Tex("+", color=WHITE, font_size=36).move_to(positive_charge.get_center())
        
        # بار منفی
        negative_charge = Dot(color=BLUE, radius=0.15).move_to(LEFT * dipole_length / 2)
        minus_label = Tex("-", color=WHITE, font_size=36).move_to(negative_charge.get_center())
        
        # FIX 1: One cohesive green arrow for the dipole moment vector
        p_arrow = Arrow(
            start=negative_charge.get_center(),
            end=positive_charge.get_center(),
            color=GREEN,
            buff=0.15, # Prevents the arrow from completely covering the dots
            stroke_width=4,
            tip_length=0.3
        )
        p_label = Tex("$\\vec{p}$", color=GREEN).next_to(p_arrow.get_center(), UP, buff=0.1)

        # گروه‌بندی تمام اجزاء
        dipole = VGroup(
            p_arrow, 
            positive_charge, negative_charge,
            p_label,
            plus_label, minus_label
        )

        # تنظیم زاویه اولیه (60 درجه)
        initial_angle = 60 * DEGREES
        dipole.rotate(initial_angle, about_point=ORIGIN)

        self.play(FadeIn(dipole))
        self.wait(1)

        # 3. شبیه‌سازی فیزیکی حرکت دو قطبی
        E_strength = 2.0  
        p_magnitude = 1.5  
        damping = 0.15  

        current_angle = initial_angle
        angular_velocity = 0.0

        def update_dipole(mob, dt):
            nonlocal current_angle, angular_velocity

            torque = p_magnitude * E_strength * np.sin(current_angle)
            angular_acceleration = torque - damping * angular_velocity

            angular_velocity += angular_acceleration * dt
            current_angle += angular_velocity * dt

            mob.become(dipole.copy().rotate(
                current_angle - initial_angle,
                about_point=ORIGIN
            ))

        dynamic_dipole = dipole.copy()
        dynamic_dipole.add_updater(update_dipole)
        self.add(dynamic_dipole)
        self.remove(dipole)

        # 4. نمایش معادلات به صورت منظم
        equations = VGroup(
            Tex("$\\vec{\\tau} = \\vec{p} \\times \\vec{E}$"),
            Tex("$\\tau = pE \\sin\\theta$"),
            Tex("$\\alpha = \\frac{\\tau}{I} - b\\omega$")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_corner(UP + LEFT)

        # FIX 2: Added fill_color and fill_opacity to block the background arrows
        equation_box = SurroundingRectangle(
            equations, 
            buff=0.3, 
            color=BLUE,
            fill_color="#1e1e1e", 
            fill_opacity=0.9 
        )
        equation_group = VGroup(equation_box, equations)

        self.play(Create(equation_box), Write(equations))
        self.wait(10)

        # 5. نتیجه‌گیری به فارسی
        conclusion = Text(
            "حرکت دو قطبی در میدان الکتریکی\n"
            "با معادلات فیزیکی نمایش داده شد",
            font="B Nazanin",
            font_size=30,
            color=WHITE
        ).to_edge(DOWN)

        # Add a background block to the conclusion text as well for readability
        conclusion_box = SurroundingRectangle(
            conclusion,
            buff=0.3,
            color=BLACK,
            fill_color="#1e1e1e",
            fill_opacity=0.9,
            stroke_width=0
        )

        self.play(FadeIn(conclusion_box), Write(conclusion))
        self.wait(3)