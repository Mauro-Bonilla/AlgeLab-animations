from manim import *

class LinearCombinations(Scene):
    def construct(self):
        # Configuración
        self.camera.background_color = "#1a1a1a"
        VECTOR_1_COLOR = "#ff1493"  # Rosa fosforescente para v
        VECTOR_2_COLOR = "#00ffff"  # Cyan para w
        RESULT_COLOR = "#CCCCCC"    # Gris claro para u
        AXIS_COLOR = "#ffff00"      # Amarillo fosforescente para los ejes
        
        # Crear plano con configuración básica y rango expandido
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-12, 12, 1],
            x_length=12,           # Reducido para evitar cortes
            y_length=12,           # Reducido para evitar cortes
            background_line_style={
                "stroke_color": GREY_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).scale(0.9)  # Escalar todo el plano

        # Colorear ejes
        plane.x_axis.set_color(AXIS_COLOR)
        plane.y_axis.set_color(AXIS_COLOR)

        # Añadir números manualmente con mejor posicionamiento
        x_numbers = VGroup(*[
            Text(str(i), color=AXIS_COLOR, font_size=24)
            .move_to(plane.c2p(i, -0.4))
            for i in range(-8, 9) if i != 0
        ])
        
        y_numbers = VGroup(*[
            Text(str(i), color=AXIS_COLOR, font_size=24)
            .move_to(plane.c2p(-0.4, i))
            for i in range(-8, 9) if i != 0
        ])

        # Crear grupo con plano y números
        grid_group = VGroup(plane, x_numbers, y_numbers)
        # Centrar todo
        grid_group.move_to(ORIGIN)

        # Mostrar plano y números
        self.play(
            Create(plane),
            Write(x_numbers),
            Write(y_numbers)
        )

        # Vectores base
        v = [2, 1]
        w = [-1, 2]

        # Panel de información (abajo a la derecha)
        info_panel = VGroup()
        info_panel.add(Text("Vectores base:", color=WHITE).scale(0.7))
        info_panel.add(Text("v = (2,1)", color=VECTOR_1_COLOR).scale(0.9))
        info_panel.add(Text("w = (-1,2)", color=VECTOR_2_COLOR).scale(0.9))
        
        # Organizar panel verticalmente
        info_panel.arrange(DOWN, aligned_edge=LEFT)
        info_panel.to_corner(DR)
        info_panel.shift(UP * 0.5 + LEFT * 1)  # Ajustado para evitar cortes

        # Mostrar panel de información
        self.play(Write(info_panel))

        # Vectores base (mismo grosor)
        vector_v = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*v),
            buff=0,
            color=VECTOR_1_COLOR,
            stroke_width=6,
            stroke_opacity=0.3
        )
        
        vector_w = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*w),
            buff=0,
            color=VECTOR_2_COLOR,
            stroke_width=6,
            stroke_opacity=0.3
        )

        # Mostrar vectores base
        self.play(
            GrowArrow(vector_v),
            GrowArrow(vector_w)
        )
        self.wait(2)
        
        # Desvanecer vectores base
        self.play(
            FadeOut(vector_v),
            FadeOut(vector_w)
        )

        # Ejemplos de combinaciones
        examples = [
            {"a": 2, "b": 1},   # 2v + w
            {"a": 1, "b": 2},   # v + 2w
            {"a": -1, "b": 1},  # -v + w
        ]

        for example in examples:
            a, b = example["a"], example["b"]
            result = [a*v[0] + b*w[0], a*v[1] + b*w[1]]

            # Texto de operación con escalares del color del vector
            operation_text = Text(f"{a}", color=VECTOR_1_COLOR).scale(0.9)
            v_text = Text("v", color=VECTOR_1_COLOR).scale(0.9)
            plus_text = Text(" + ", color=WHITE).scale(0.9)
            b_text = Text(f"{b}", color=VECTOR_2_COLOR).scale(0.9)
            w_text = Text("w", color=VECTOR_2_COLOR).scale(0.9)
            equals_text = Text(" = u", color=WHITE).scale(0.9)
            
            operation = VGroup(operation_text, v_text, plus_text, b_text, w_text, equals_text).arrange(RIGHT, buff=0.1)
            result_text = Text(f"u = ({result[0]},{result[1]})", color=RESULT_COLOR).scale(0.9)
            
            combo_text = VGroup(operation, result_text).arrange(DOWN, aligned_edge=LEFT)
            combo_text.to_corner(UL).shift(DOWN * 0.5 + RIGHT * 1)

            # Vector resultado
            vector_result = Arrow(
                start=plane.c2p(0, 0),
                end=plane.c2p(*result),
                buff=0,
                color=RESULT_COLOR,
                stroke_width=6
            )

            # Etiqueta del vector resultado
            result_label = Text(
                f"({result[0]},{result[1]})",
                color=RESULT_COLOR,
                font_size=24
            ).next_to(vector_result.get_end(), UP + RIGHT, buff=0.1)

            # Mostrar combinación
            self.play(
                Write(combo_text),
                GrowArrow(vector_result),
                Write(result_label)
            )

            # Vectores escalados
            scaled_v = Arrow(
                start=plane.c2p(0, 0),
                end=plane.c2p(a*v[0], a*v[1]),
                buff=0,
                color=VECTOR_1_COLOR,
                stroke_width=6
            )
            
            scaled_w = Arrow(
                start=plane.c2p(a*v[0], a*v[1]),
                end=plane.c2p(*result),
                buff=0,
                color=VECTOR_2_COLOR,
                stroke_width=6
            )

            # Mostrar construcción
            self.play(Create(scaled_v))
            self.play(Create(scaled_w))
            
            self.wait(2)

            # Limpiar para siguiente ejemplo
            self.play(
                FadeOut(vector_result),
                FadeOut(scaled_v),
                FadeOut(scaled_w),
                FadeOut(combo_text),
                FadeOut(result_label)
            )

        self.wait()

        # Fade out final
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )