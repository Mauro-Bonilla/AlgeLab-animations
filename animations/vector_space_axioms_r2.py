from manim import *

class VectorSpaceAxiomsR2(Scene):
    def construct(self):
        self.title = Text("Axiomas de Espacios Vectoriales", font_size=40).to_edge(UP)
        self.add(self.title)

        self.introduce_vector_space()
        self.closure_under_addition()
        self.closure_under_scalar_multiplication()
        self.associativity()
        self.commutativity()
        self.zero_vector()
        self.additive_inverse()
        self.distributive_properties()

    def introduce_vector_space(self):
        intro_text = Text("Un espacio vectorial es un conjunto con operaciones de suma y multiplicación escalar", font_size=24)
        intro_text.next_to(self.title, DOWN)
        self.play(Write(intro_text))
        self.wait(3)
        self.play(FadeOut(intro_text))

    def closure_under_addition(self):
        axiom_title = Text("1. Cerradura bajo la suma", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5])
        self.play(Create(plane))

        v1 = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE, buff=0)
        v2 = Arrow(start=ORIGIN, end=[1, 2, 0], color=RED, buff=0)
        sum_v = Arrow(start=ORIGIN, end=[3, 3, 0], color=PURPLE, buff=0)

        v1_label = MathTex("\\vec{v}", color=BLUE).next_to(v1.get_end(), RIGHT)
        v2_label = MathTex("\\vec{w}", color=RED).next_to(v2.get_end(), UP)
        sum_label = MathTex("\\vec{v} + \\vec{w}", color=PURPLE).next_to(sum_v.get_end(), RIGHT)

        explanation = Text("La suma de dos vectores siempre resulta en otro vector del espacio", font_size=24)
        explanation.next_to(plane, DOWN)

        self.play(Create(v1), Write(v1_label))
        self.play(Create(v2), Write(v2_label))
        self.wait()
        self.play(Create(sum_v), Write(sum_label))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(plane), FadeOut(v1), FadeOut(v2), FadeOut(sum_v), 
                  FadeOut(v1_label), FadeOut(v2_label), FadeOut(sum_label), 
                  FadeOut(explanation), FadeOut(axiom_title))

    def closure_under_scalar_multiplication(self):
        axiom_title = Text("2. Cerradura bajo multiplicación escalar", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5])
        self.play(Create(plane))

        v = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE, buff=0)
        scaled_v = Arrow(start=ORIGIN, end=[4, 2, 0], color=GREEN, buff=0)

        v_label = MathTex("\\vec{v}", color=BLUE).next_to(v.get_end(), RIGHT)
        scaled_label = MathTex("2\\vec{v}", color=GREEN).next_to(scaled_v.get_end(), RIGHT)

        explanation = Text("Multiplicar un vector por un escalar produce otro vector en el espacio", font_size=24)
        explanation.next_to(plane, DOWN)

        self.play(Create(v), Write(v_label))
        self.wait()
        self.play(Transform(v.copy(), scaled_v), Write(scaled_label))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(plane), FadeOut(v), FadeOut(scaled_v), 
                  FadeOut(v_label), FadeOut(scaled_label), 
                  FadeOut(explanation), FadeOut(axiom_title))

    def associativity(self):
        axiom_title = Text("3. Asociatividad", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        equation = MathTex("(\\vec{u} + \\vec{v}) + \\vec{w} = \\vec{u} + (\\vec{v} + \\vec{w})")
        explanation = Text("El orden de agrupación en la suma de vectores no afecta el resultado", font_size=24)
        explanation.next_to(equation, DOWN)

        self.play(Write(equation))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(equation), FadeOut(explanation), FadeOut(axiom_title))

    def commutativity(self):
        axiom_title = Text("4. Conmutatividad", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5])
        self.play(Create(plane))

        v1 = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE, buff=0)
        v2 = Arrow(start=ORIGIN, end=[1, 2, 0], color=RED, buff=0)
        sum_v = Arrow(start=ORIGIN, end=[3, 3, 0], color=PURPLE, buff=0)

        equation = MathTex("\\vec{v} + \\vec{w} = \\vec{w} + \\vec{v}")
        explanation = Text("El orden de la suma de vectores no afecta el resultado", font_size=24)
        explanation.next_to(plane, DOWN)

        self.play(Create(v1), Create(v2))
        self.play(Create(sum_v))
        self.play(Write(equation))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(plane), FadeOut(v1), FadeOut(v2), FadeOut(sum_v), 
                  FadeOut(equation), FadeOut(explanation), FadeOut(axiom_title))

    def zero_vector(self):
        axiom_title = Text("5. Existencia del vector cero", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5])
        self.play(Create(plane))

        v = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE, buff=0)
        zero = Dot3D(ORIGIN, color=RED)

        equation = MathTex("\\vec{v} + \\vec{0} = \\vec{v}")
        explanation = Text("Existe un vector cero que al sumarse a cualquier vector, no lo altera", font_size=24)
        explanation.next_to(plane, DOWN)

        self.play(Create(v), Create(zero))
        self.play(Write(equation))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(plane), FadeOut(v), FadeOut(zero), 
                  FadeOut(equation), FadeOut(explanation), FadeOut(axiom_title))

    def additive_inverse(self):
        axiom_title = Text("6. Existencia del inverso aditivo", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5])
        self.play(Create(plane))

        v = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE, buff=0)
        v_inv = Arrow(start=ORIGIN, end=[-2, -1, 0], color=RED, buff=0)

        equation = MathTex("\\vec{v} + (-\\vec{v}) = \\vec{0}")
        explanation = Text("Para cada vector existe un inverso aditivo que al sumarse da el vector cero", font_size=24)
        explanation.next_to(plane, DOWN)

        self.play(Create(v), Create(v_inv))
        self.play(Write(equation))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(plane), FadeOut(v), FadeOut(v_inv), 
                  FadeOut(equation), FadeOut(explanation), FadeOut(axiom_title))

    def distributive_properties(self):
        axiom_title = Text("7. Propiedades distributivas", font_size=36).next_to(self.title, DOWN)
        self.play(Write(axiom_title))

        equations = VGroup(
            MathTex("a(\\vec{u} + \\vec{v}) = a\\vec{u} + a\\vec{v}"),
            MathTex("(a + b)\\vec{v} = a\\vec{v} + b\\vec{v}")
        ).arrange(DOWN)
        
        explanation = Text("La multiplicación escalar se distribuye sobre la suma de vectores y escalares", font_size=24)
        explanation.next_to(equations, DOWN)

        self.play(Write(equations))
        self.play(Write(explanation))

        self.wait(3)
        self.play(FadeOut(equations), FadeOut(explanation), FadeOut(axiom_title))

# Para renderizar:
# manim -pql vector_space_axioms_r2.py VectorSpaceAxiomsR2