from manim import *

class VectorIntroduction(Scene):
    def construct(self):
        # Configuración
        self.camera.background_color = "#1e1e1e"
        VECTOR_COLOR = "#ff69b4"  # Rosa
        
        # Crear plano
        plane = NumberPlane(
            x_range=[-6, 6],
            y_range=[-4, 4],
            x_length=12,
            y_length=8,
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

        # Mostrar plano suavemente
        self.play(Create(plane, lag_ratio=0.1), run_time=1.5)
        self.wait(0.5)
        
        # Posiciones para la animación
        positions = [
            [2, 1],    # Posición inicial
            [3, 2],    # Segunda posición
            [-2, 2],   # Tercera posición
            [1, -2],   # Cuarta posición
            [2, 1]     # Volver al inicio
        ]
        
        # Crear punto inicial
        point = Dot(
            point=plane.c2p(*positions[0]),
            color=VECTOR_COLOR,
            radius=0.12
        )
        
        # Coordenadas como punto
        point_coords = Text(
            f"({positions[0][0]}, {positions[0][1]})",
            font_size=24,
            color=VECTOR_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8, buff=0.1)

        # Mostrar punto y coordenadas
        self.play(
            FadeIn(point, scale=0.5),
            Write(point_coords),
            run_time=1
        )
        
        # Efecto de pulso en el punto
        self.play(
            point.animate.scale(1.5),
            rate_func=there_and_back,
            run_time=0.8
        )
        self.wait(0.5)

        # Crear vector
        vector = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*positions[0]),
            buff=0,
            color=VECTOR_COLOR,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        # Coordenadas como vector
        vector_coords = Text(
            f"[{positions[0][0]}, {positions[0][1]}]",
            font_size=24,
            color=VECTOR_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8, buff=0.1)

        # Transformar punto en vector
        self.play(
            Transform(point, vector),
            Transform(point_coords, vector_coords),
            run_time=1.5
        )
        self.wait(0.5)

        # Animación del vector moviéndose a través de diferentes posiciones
        for i in range(1, len(positions)):
            # Crear nuevo vector para la posición objetivo
            new_vector = Arrow(
                start=plane.c2p(0, 0),
                end=plane.c2p(*positions[i]),
                buff=0,
                color=VECTOR_COLOR,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.15
            )
            
            # Nuevas coordenadas
            new_coords = Text(
                f"[{positions[i][0]}, {positions[i][1]}]",
                font_size=24,
                color=VECTOR_COLOR
            ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8, buff=0.1)
            
            # Animar la transición
            self.play(
                Transform(point, new_vector),
                Transform(vector_coords, new_coords),
                run_time=1.5,
                rate_func=smooth
            )
            self.wait(0.5)

        # Mostrar doble representación final
        final_point = Dot(
            point=plane.c2p(*positions[-1]),
            color=VECTOR_COLOR,
            radius=0.12
        )
        
        final_point_coords = Text(
            f"({positions[-1][0]}, {positions[-1][1]})",
            font_size=24,
            color=VECTOR_COLOR
        ).to_corner(UR).add_background_rectangle(BLACK, opacity=0.8, buff=0.1)

        # Transformar vector de vuelta a punto
        self.play(
            Transform(point, final_point),
            Transform(vector_coords, final_point_coords),
            run_time=1.5
        )
        self.wait(0.5)

        # Mostrar ambas representaciones
        final_vector = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(*positions[-1]),
            buff=0,
            color=VECTOR_COLOR,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15,
            stroke_opacity=0.5
        )

        self.play(
            FadeIn(final_vector),
            run_time=1
        )
        self.wait(1)

        # Fade out final
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )