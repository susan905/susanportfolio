import flet as ft


VIDEO_FILE = "/portfolio_video.mp4"

BLOG_POSTS = [
    {
        "id": 1,
        "title": "Understanding Variables & Data Types in Python",
        "date": "15 Feb 2026",
        "tags": ["Python", "Fundamentals"],
        "body": [
            "A variable is a named container that stores a value in memory. Python is dynamically typed - the interpreter infers the type at runtime.",
            "The four primitive types you'll use most often are: int (whole numbers), float (decimals), str (text), and bool (True/False).",
            "Type coercion lets you convert between types using int(), float(), and str(). Always validate user input before coercion to avoid ValueError exceptions.",
        ],
    },
    {
        "id": 2,
        "title": "Control Flow: Conditionals & Loops",
        "date": "22 Feb 2026",
        "tags": ["Python", "Control Flow"],
        "body": [
            "Control flow determines the order statements execute. Python provides conditionals (if/elif/else) and loops (for / while).",
            "for loops iterate over any iterable - lists, ranges, strings, dicts. while loops repeat as long as a condition holds.",
            "break exits a loop early; continue skips the rest of the current iteration. Together they give fine-grained control over iteration.",
        ],
    },
    {
        "id": 3,
        "title": "Functions: Reusable Blocks of Logic",
        "date": "1 Mar 2026",
        "tags": ["Python", "Functions"],
        "body": [
            "A function is a named, reusable block of code that accepts inputs (parameters) and returns an output.",
            "Key concepts: default parameters, *args and **kwargs for variable-length argument lists, and scope (variables inside a function are local).",
            "Defining logic in functions follows the DRY principle - Don't Repeat Yourself - making code easier to test and maintain.",
        ],
    },
]

TAG_COLORS = {
    "Python": "#58a6ff",
    "Fundamentals": "#0cb5a1",
    "Control Flow": "#a371f7",
    "Functions": "#e3b341",
}

BG = "#0d1117"
CARD = "#161b22"
CARD2 = "#1c2333"
BORDER = "#30363d"
TEXT = "#e6edf3"
MUTED = "#8b949e"
DIM = "#484f58"
RED = "#ff4444"


def blog_page():
    def tag_chip(tag):
        color = TAG_COLORS.get(tag, BORDER)
        return ft.Container(
            content=ft.Text(tag, size=11, color=color, weight="bold"),
            bgcolor=BG,
            border=ft.border.all(1, color),
            border_radius=20,
            padding=ft.padding.symmetric(horizontal=10, vertical=3),
        )

    video_banner = ft.Container(
        content=ft.Column(
            controls=[
                ft.Video(
                    playlist=[ft.VideoMedia(VIDEO_FILE)],
                    width=760,
                    height=430,
                    aspect_ratio=16 / 9,
                    fit=ft.ImageFit.CONTAIN,
                    show_controls=True,
                    autoplay=False,
                    muted=False,
                    fill_color=BG,
                ),
                ft.Text(
                    "Python Programming Explanation",
                    size=15,
                    color=TEXT,
                    weight="bold",
                    text_align="center",
                ),
            ],
            spacing=14,
            horizontal_alignment="center",
        ),
        bgcolor=CARD2,
        border=ft.border.all(1, RED + "55"),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=24, vertical=20),
    )

    def post_card(post):
        body_controls = [
            ft.Row(
                controls=[
                    ft.Container(
                        width=4,
                        height=4,
                        bgcolor=DIM,
                        border_radius=2,
                        margin=ft.margin.only(top=7),
                    ),
                    ft.Text(line, size=13, color="#c9d1d9", expand=True),
                ],
                spacing=10,
                vertical_alignment="start",
            )
            for line in post["body"]
        ]

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                post["title"],
                                size=17,
                                color=TEXT,
                                weight="bold",
                                expand=True,
                            ),
                            ft.Text(post["date"], size=11, color=DIM),
                        ],
                    ),
                    ft.Row(controls=[tag_chip(t) for t in post["tags"]], spacing=6),
                    ft.Divider(color=BORDER),
                    ft.Column(controls=body_controls, spacing=8),
                ],
                spacing=14,
            ),
            bgcolor=CARD,
            border=ft.border.all(1, BORDER),
            border_radius=10,
            padding=24,
        )

    return ft.Column(
        controls=[
            ft.Text("Technical Blog", size=28, color=TEXT, weight="bold"),
            ft.Text(
                "Confidence in Concepts - written explanations paired with a recorded video.",
                size=14,
                color=MUTED,
            ),
            ft.Divider(color=BORDER),
            video_banner,
            ft.Container(height=4),
            ft.Column(controls=[post_card(p) for p in BLOG_POSTS], spacing=20),
        ],
        spacing=20,
        scroll="auto",
    )
