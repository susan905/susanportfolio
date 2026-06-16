import flet as ft
from pages.timeline import timeline_page
from pages.matlab import matlab_page
from pages.blog import blog_page
from pages.github import github_page


def main(page: ft.Page):
    page.title = "Web Portfolio 2026"
    page.bgcolor = "#0d1117"
    page.padding = 0
    page.scroll = "auto"

    nav_buttons = []

    def switch_page(index):
        for i, btn in enumerate(nav_buttons):
            btn.color = "#58a6ff" if i == index else "#8b949e"
        builders = [
            lambda: timeline_page(page),
            lambda: matlab_page(page),
            lambda: blog_page(),
            lambda: github_page(),
        ]
        content_area.controls.clear()
        content_area.controls.append(builders[index]())
        page.update()

    labels = ["🗓 Timeline", "🔢 MATLAB", "📝 Blog", "🐙 GitHub"]
    for i, label in enumerate(labels):
        btn = ft.TextButton(label, on_click=lambda e, idx=i: switch_page(idx))
        btn.color = "#58a6ff" if i == 0 else "#8b949e"
        nav_buttons.append(btn)

    navbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Portfolio 2026", size=18, color="#e6edf3", weight="bold"),
                ft.Row(controls=nav_buttons, spacing=8),
            ],
            alignment="spaceBetween",
        ),
        bgcolor="#161b22",
        border=ft.border.only(bottom=ft.BorderSide(1, "#30363d")),
        padding=ft.padding.symmetric(horizontal=32, vertical=14),
    )

    content_area = ft.Column(
        controls=[timeline_page(page)],
        scroll="auto",
        expand=True,
    )

    page.add(navbar)
    page.add(
        ft.Container(
            content=content_area,
            padding=ft.padding.symmetric(horizontal=32, vertical=24),
            expand=True,
        )
    )


ft.app(target=main, port=3000, view="web_browser", assets_dir="assets")