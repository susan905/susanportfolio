import flet as ft


MATLAB_COURSES = [
    {"number": 1, "title": "MATLAB Onramp", "date": "28 April 2026", "pdf": "certificate_1.pdf"},
    {"number": 2, "title": "Machine Learning Onramp", "date": "28 April 2026", "pdf": "certificate_2.pdf"},
    {"number": 3, "title": "Make and Manipulate Matrices", "date": "28 April 2026", "pdf": "certificate_3.pdf"},
    {"number": 4, "title": "Explore Data with MATLAB Plots", "date": "28 April 2026", "pdf": "certificate_4.pdf"},
    {"number": 5, "title": "Calculations with Vectors & Matrices", "date": "28 April 2026", "pdf": "certificate_5.pdf"},
    {"number": 6, "title": "Dates and Times", "date": "28 April 2026", "pdf": "certificate_6.pdf"},
    {"number": 7, "title": "Simulink Fundamentals", "date": "30 April 2026", "pdf": "certificate_7.pdf"},
]


def matlab_page(page: ft.Page = None):
    def course_card(course):
        cert_url = f"/certificates/{course['pdf']}"

        def open_certificate(e):
            if page:
                page.launch_url(
                    cert_url,
                    web_window_name=f"certificate_{course['number']}",
                    web_popup_window=True,
                    window_width=1000,
                    window_height=760,
                )

        def on_hover(e):
            e.control.scale = 1.01 if e.data == "true" else 1.0
            e.control.shadow = (
                ft.BoxShadow(blur_radius=20, color="#58a6ff44", spread_radius=2)
                if e.data == "true"
                else ft.BoxShadow(blur_radius=0, color="#00000000")
            )
            e.control.update()

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(str(course["number"]), size=16, color="#58a6ff", weight="bold"),
                        bgcolor="#0d1f38",
                        border_radius=20,
                        width=36,
                        height=36,
                        alignment=ft.alignment.center,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(course["title"], size=15, color="#e6edf3", weight="bold"),
                            ft.Text(f"Completed: {course['date']}", size=11, color="#484f58"),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Text("Done", size=12, color="#3fb950", weight="bold"),
                    ft.ElevatedButton(
                        "Open Certificate",
                        on_click=open_certificate,
                        bgcolor="#238636",
                        color="#ffffff",
                    ),
                ],
                spacing=12,
                vertical_alignment="center",
            ),
            bgcolor="#161b22",
            border=ft.border.all(1, "#30363d"),
            border_radius=10,
            padding=16,
            animate_scale=ft.animation.Animation(300, "easeOut"),
            scale=1.0,
            on_hover=on_hover,
            shadow=ft.BoxShadow(blur_radius=0, color="#00000000"),
        )

    completed = len(MATLAB_COURSES)
    required = 7
    cards = [course_card(c) for c in MATLAB_COURSES]

    return ft.Column(
        controls=[
            ft.Text("MATLAB Achievement", size=28, color="#e6edf3", weight="bold"),
            ft.Text("Juuso Susan - MathWorks Learning Center Course Completions", size=14, color="#8b949e"),
            ft.Divider(color="#21262d"),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text("Overall Progress", size=14, color="#8b949e", expand=True),
                                ft.Text(f"{completed} / {required} courses", size=14, color="#58a6ff", weight="bold"),
                            ],
                        ),
                        ft.ProgressBar(value=completed / required, bgcolor="#21262d", color="#58a6ff", height=10),
                        ft.Text(f"{completed} of {required} courses completed!", size=12, color="#3fb950"),
                    ],
                    spacing=10,
                ),
                bgcolor="#161b22",
                border=ft.border.all(1, "#30363d"),
                border_radius=10,
                padding=20,
            ),
            ft.Divider(color="#21262d"),
            ft.Column(controls=cards, spacing=16),
        ],
        spacing=20,
        scroll="auto",
    )
