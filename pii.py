from manim import *
from math import cos, sin


class HowToGetPI(Scene):
    def construct(self):
        label = Text("How to get PI", font_size=30, font="Harrington")
        self.play(Write(label, run_time=2))
        self.wait()
        self.play(label.animate.to_edge(LEFT + UP).set_font_size(20))
        self.wait()
        circle = Circle(color=WHITE, stroke_width=2.1).scale(1)
        self.play(Create(circle))

        circle_d = Line(color=PINK, stroke_width=2).scale(1)
        d_number = Text("2", font_size=16, color=PINK).next_to(circle_d, DOWN)
        self.play(Create(circle_d, rate_func=smooth, run_time=1), Write(d_number))
        self.wait()
        parallels = VGroup(*[DashedLine(stroke_width=1).scale(1).set_angle(PI/2) for _ in range(2)]).arrange(RIGHT, buff=2).shift(UP)
        self.play(circle_d.animate.shift(UP*2), d_number.animate.shift(UP*2.5), AnimationGroup(*[Create(par) for par in parallels]))
        self.wait()

        polygon = RegularPolygon(6, color=WHITE, stroke_width=2).scale(1)
        polygon_side_length = Text("1", font_size=16, color=DARK_BLUE).shift(UP*0.7)
        polygon_side = Line(color=DARK_BLUE, stroke_width=2).scale(0.5).move_to(polygon.get_critical_point(UP))
        self.play(Create(polygon, rate_func=smooth, run_time=1))
        self.play(Create(polygon_side), Write(polygon_side_length))
        rays = VGroup(*[Line(stroke_width=1)
                                       .scale(0.5)
                                       .shift(RIGHT*0.5)
                                       .set_angle(i*PI/3)
                                for i in range(1, 7)])
        self.play(AnimationGroup(*[Create(ray) for ray in rays]), rate_functions=rush_from, run_time=2)
        self.play(polygon.animate.set_color(DARK_BLUE))
        self.remove(polygon_side)
        sides = VGroup(*[Text("1", font_size=16, color=DARK_BLUE).move_to([0.7*cos(i*PI/6), 0.7*sin(i*PI/6), 0]) for i in (1, 5, 7, 9, 11)])
        self.play(Write(sides))
        self.wait()
        polygon_perimeter = Text("6", font_size=16, color=DARK_BLUE).move_to(UP*0.7)
        self.play(AnimationGroup(*[side.animate.move_to(polygon_side_length.get_critical_point([0, 0, 0])) for side in sides],
                                 FadeOut(polygon_side_length)), ReplacementTransform(sides, polygon_perimeter))
        self.wait()
        self.play(polygon.animate.set_color(WHITE), circle.animate.set_color(DARK_BLUE), ReplacementTransform(sides, polygon_perimeter))
        self.play(polygon_perimeter.animate.shift(DOWN*2 + RIGHT*0.2))
        C = Text("C > ", font_size=16, color=DARK_BLUE).align_to(polygon_perimeter, DOWN).shift(LEFT*0.1)
        self.play(Write(C))
        self.wait()
        PI_ = Text("PI > 6/2", color=WHITE, font_size=40).shift(LEFT*3)
        self.play(Write(PI_), FadeOut(C, polygon_perimeter))
        self.wait()
        self.play(Transform(PI_, Text("PI > 3", color=WHITE, font_size=40).shift(LEFT*3)))
        square = Square(stroke_width=2)
        self.play(Create(square))
        self.bring_to_front(circle_d)
        self.play(circle_d.animate.move_to(square.get_critical_point(UP)),
                   d_number.animate.move_to(square.get_critical_point(UP)).shift(UP*0.2),
                   FadeOut(parallels))
        self.wait()
        self.play(square.animate.set_color(PINK))
        self.remove(circle_d)
        sides = VGroup(*[Text("2", font_size=18, color=PINK).move_to([1.3 * cos(i * PI / 2), 1.3 * sin(i * PI / 2), 0]) for i in (0, 2, 3)])
        self.play(Write(sides))
        self.wait()
        square_perimeter = Text("8", font_size=18, color=PINK).move_to(UP * 1.3)
        self.play(AnimationGroup(*[side.animate.move_to(d_number.get_critical_point([0, 0, 0])) for side in sides],
                                  FadeOut(d_number)), ReplacementTransform(sides, square_perimeter))
        self.wait()
        self.play(square.animate.set_color(WHITE), circle.animate.set_color(PINK),
                  ReplacementTransform(sides, square_perimeter))
        C = Text("C < ", font_size=18, color=PINK).align_to(polygon_perimeter, DOWN).shift(LEFT*0.1)
        self.play(square_perimeter.animate.align_to(C, DOWN).shift(RIGHT*0.35), FadeIn(C))
        self.wait()
        PI_2 = Text("PI < 8/2", color=WHITE, font_size=40).next_to(PI_, DOWN)
        self.play(Write(PI_2), FadeOut(C, square_perimeter))
        self.wait()
        self.play(Transform(PI_2, Text("PI < 4", color=WHITE, font_size=40).next_to(PI_, DOWN)))
        self.wait()
        inscribed_dodecagon = RegularPolygon(12, color=WHITE, stroke_width=2).scale(1)
        inscribed_dodecagon_rays = VGroup(*[Line(stroke_width=1)
                                       .scale(0.5)
                                       .shift(RIGHT*0.5)
                                       .set_angle(i*PI/6)
                                for i in range(1, 13)])
        self.play(ReplacementTransform(VGroup(polygon, rays), VGroup(inscribed_dodecagon, inscribed_dodecagon_rays)))
        inscribed_dodecagon_perimetr = Text("C > 6,212", color=BLUE_E, font_size=18).shift(DOWN*1.5)
        self.play(inscribed_dodecagon.animate.set_color(BLUE_E), circle.animate.set_color(WHITE), Write(inscribed_dodecagon_perimetr))
        self.wait()
        self.play(ReplacementTransform(PI_, Text("PI > 3,106", color=WHITE, font_size=40).shift(LEFT*3)), FadeOut(inscribed_dodecagon_perimetr))
        self.wait()
        circumscribed_dodecagon = RegularPolygon(12, color=BLUE_E, stroke_width=2).scale(1.05).rotate(PI/6)
        self.play(ReplacementTransform(square, circumscribed_dodecagon))
        circumscribed_dodecagon_perimetr = Text("C < 6,431", color=BLUE_E, font_size=18).shift(DOWN*1.5)
        self.play(circumscribed_dodecagon.animate.set_color(BLUE_E), circle.animate.set_color(WHITE), Write(circumscribed_dodecagon_perimetr))
        self.wait()
        self.play(ReplacementTransform(PI_2, Text("PI < 3,215", color=WHITE, font_size=40).next_to(PI_, DOWN)), FadeOut(circumscribed_dodecagon_perimetr))
        self.wait(2)





