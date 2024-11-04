from manim import *

class VectorOperations(Scene):
    def construct(self):
        # Configuración
        self.camera.background_color = "#000000"
        VECTOR_COLOR = "#ff69b4"  # Rosa
        VECTOR_COLOR_2 = "#00ff00"  # Verde para el segundo vector
        RESULT_COLOR = "#ffffff"  # Blanco para el resultado
        SPACE_COLOR = "#ffff00"   # Amarillo
        SUBSPACE_COLOR = "#00cccc"  # Cyan
        
        # Crear plano
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            x_length=16,
            y_length=10,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "include_numbers": False,
                "include_tip": True
            }
        )

        # Mostrar plano
        self.play(Create(plane, lag_ratio=0.1), run_time=1)

        # Demostración de suma de vectores
        v1 = [3, 0]  # Vector horizontal
        v2 = [0, 2]  # Vector vertical
        v_sum = [v1[0] + v2[0], v1[1] + v2[1]]  # Vector suma

        # Crear vectores
        vector1 = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*v1),
            buff=0,
            color=VECTOR_COLOR,
            stroke_width=6
        )
        
        vector2 = Arrow(
            start=plane.c2p(*v1),
            end=plane.c2p(*v_sum),
            buff=0,
            color=VECTOR_COLOR_2,
            stroke_width=6
        )
        
        vector_sum = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*v_sum),
            buff=0,
            color=RESULT_COLOR,
            stroke_width=6
        )

        # Coordenadas
        v1_coords = Text(
            f"[{v1[0]}, {v1[1]}]",
            font_size=24,
            color=VECTOR_COLOR
        ).next_to(vector1, DOWN).add_background_rectangle(BLACK, opacity=0.8)

        v2_coords = Text(
            f"[{v2[0]}, {v2[1]}]",
            font_size=24,
            color=VECTOR_COLOR_2
        ).next_to(vector2, LEFT).add_background_rectangle(BLACK, opacity=0.8)

        sum_coords = Text(
            f"[{v_sum[0]}, {v_sum[1]}]",
            font_size=24,
            color=RESULT_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8)

        # Mostrar suma de vectores
        self.play(GrowArrow(vector1), Write(v1_coords))
        self.wait(0.5)
        self.play(GrowArrow(vector2), Write(v2_coords))
        self.wait(0.5)
        self.play(GrowArrow(vector_sum), Write(sum_coords))
        self.wait()

        # Limpiar para multiplicación escalar
        self.play(
            *[FadeOut(mob) for mob in [vector1, vector2, v1_coords, v2_coords]]
        )

        # Demostración de multiplicación escalar
        scalar = 2
        scaled_sum = [scalar * v_sum[0], scalar * v_sum[1]]

        scaled_vector = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*scaled_sum),
            buff=0,
            color=VECTOR_COLOR,
            stroke_width=6
        )

        scaled_coords = Text(
            f"{scalar}[{v_sum[0]}, {v_sum[1]}] = [{scaled_sum[0]}, {scaled_sum[1]}]",
            font_size=24,
            color=VECTOR_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8)

        # Mostrar multiplicación escalar
        self.play(
            Transform(vector_sum, scaled_vector),
            Transform(sum_coords, scaled_coords)
        )
        self.wait()

        # Mostrar espacio vectorial
        space = Rectangle(
            width=16,
            height=10,
            fill_color=SPACE_COLOR,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        space_text = Text(
            "Espacio Vectorial R²",
            font_size=24,
            color=SPACE_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8)

        self.play(
            FadeIn(space),
            Write(space_text),
            FadeOut(vector_sum),
            FadeOut(sum_coords)
        )

        # Subespacio y movimientos finales (similar al código anterior)
        subspace_line = Line(
            start=plane.c2p(-8, -2.67),
            end=plane.c2p(8, 2.67),
            color=SUBSPACE_COLOR,
            stroke_width=4,
            stroke_opacity=0.8
        )
        
        subspace_text = Text(
            "Subespacio Vectorial R¹",
            font_size=24,
            color=SUBSPACE_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8)

        self.play(
            Create(subspace_line),
            Transform(space_text, subspace_text)
        )

        # Vector moviéndose en el subespacio
        positions = [
            [3, 1],
            [-3, -1],
            [1.5, 0.5],
            [-1.5, -0.5],
            [3, 1]
        ]

        vector = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*positions[0]),
            buff=0,
            color=VECTOR_COLOR,
            stroke_width=6
        )
        
        self.play(GrowArrow(vector))

        for pos in positions[1:]:
            new_vector = Arrow(
                start=plane.c2p(0, 0),
                end=plane.c2p(*pos),
                buff=0,
                color=VECTOR_COLOR,
                stroke_width=6
            )
            
            self.play(
                Transform(vector, new_vector),
                run_time=1.5
            )
            self.wait(0.3)

        # Fade out final
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )