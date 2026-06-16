import flet as ft
import threading
import time
import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_b64(filename):
    path = os.path.join(BASE_DIR, "assets", filename)
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception:
        return None

TIMELINE_ENTRIES = [
    {
        "week": "Week 2", "date": "21 Feb – 27 Feb 2026",
        "title": "Distribution Of Roles And Responsibilities",
        "contributions": [
            "Was responsible for the app layout with a focus on user experience.",
        ],
        "module": "DOCUMENTATION LEAD", "commits": 2,
    },
    {
        "week": "Week 5", "date": "3 – 16 May 2026",
        "title": "Attempetted File Submissions",
        "contributions": [
            "submitted the ui documentation report.",
           
        ],
        "module": "DOCUMENTATION LEAD", "commits": 2,
    },
   
]

MODULE_COLORS = {
    "DOCUMENTATION LEAD":     "#8b949e",
    "Portfolio / Assessment": "#19c7a1",
}


def timeline_page(page: ft.Page = None):
    total_commits = sum(e["commits"] for e in TIMELINE_ENTRIES)
    profile_b64   = load_b64("profile_nobg.jpg")

    # ── Photo circle ──────────────────────────────────────────────────────────
    photo_circle = ft.Container(
        content=ft.Image(
            src_base64=profile_b64,
            width=150, height=150,
            fit="cover",
        ) if profile_b64 else ft.Text("JS", size=40, color="#fff", weight="bold"),
        width=150, height=150,
        border_radius=75,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor="#0d1117",
    )

    # ── Shining diamond sparkles ──────────────────────────────────────────────
    def sparkle(size, color):
        return ft.Container(
            width=size, height=size,
            bgcolor=color,
            border_radius=size // 2,
            opacity=0.0,
            animate_opacity=ft.animation.Animation(500, "easeInOut"),
            shadow=ft.BoxShadow(blur_radius=8, color=color, spread_radius=2),
        )

    # Blue diamond border ring
    ring = ft.Container(
        width=162, height=162,
        border_radius=81,
        border=ft.border.all(2, "#8b949e"),
        opacity=1.0,
        animate_opacity=ft.animation.Animation(800, "easeInOut"),
        shadow=ft.BoxShadow(blur_radius=12, color="#8b949e44", spread_radius=1),
    )

    # Blue outer ring
    ring2 = ft.Container(
        width=172, height=172,
        border_radius=86,
        border=ft.border.all(1, "#00a44f66"),
        opacity=0.4,
        animate_opacity=ft.animation.Animation(1000, "easeInOut"),
    )

    # Sparkle dots at compass points around the circle
    sp_n  = sparkle(10, "#8b949e")  # top
    sp_e  = sparkle(7,  "#ffffff")  # right
    sp_s  = sparkle(10, "#8b949e")  # bottom
    sp_w  = sparkle(7,  "#8b949e")  # left
    sp_ne = sparkle(6,  "#ffffff")  # top-right
    sp_nw = sparkle(6,  "#8b949e")  # top-left
    sp_se = sparkle(5,  "#ffffff")  # bottom-right
    sp_sw = sparkle(5,  "#8b949e")  # bottom-left

    photo_stack = ft.Stack(
        width=190, height=190,
        controls=[
            ft.Container(content=ring2,  alignment=ft.alignment.center, width=190, height=190),
            ft.Container(content=ring,   alignment=ft.alignment.center, width=190, height=190),
            ft.Container(content=photo_circle, alignment=ft.alignment.center, width=190, height=190),
            # compass sparkles
            ft.Container(content=sp_n,  top=2,   left=90),
            ft.Container(content=sp_s,  bottom=2,left=90),
            ft.Container(content=sp_e,  top=91,  right=2),
            ft.Container(content=sp_w,  top=91,  left=2),
            ft.Container(content=sp_ne, top=20,  right=20),
            ft.Container(content=sp_nw, top=20,  left=20),
            ft.Container(content=sp_se, bottom=20, right=20),
            ft.Container(content=sp_sw, bottom=20, left=20),
        ],
    )

   
    all_sparkles = [sp_n, sp_ne, sp_e, sp_se, sp_s, sp_sw, sp_w, sp_nw]

    def shine():
        while True:
            try:
                # Brighten rings
                ring.opacity  = 1.0;  ring.update()
                ring2.opacity = 0.9;  ring2.update()
                time.sleep(0.3)

                # Flash sparkles clockwise one by one
                for sp in all_sparkles:
                    sp.opacity = 1.0
                    sp.update()
                    time.sleep(0.07)

                time.sleep(0.4)

             
                for sp in all_sparkles:
                    sp.opacity = 0.0
                    sp.update()
                    time.sleep(0.05)

                ring.opacity  = 0.35; ring.update()
                ring2.opacity = 0.15; ring2.update()
                time.sleep(0.9)

            except Exception:
                break

    threading.Thread(target=shine, daemon=True).start()

    hero = ft.Container(
        content=ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Image(
                        src_base64=profile_b64,
                        fit="cover",
                        width=2000,
                        height=280,
                    ) if profile_b64 else ft.Container(bgcolor="#161b22"),
                    width=2000,
                    height=280,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    opacity=0.35,
                ),
                # dark overlay
                ft.Container(bgcolor="#0d1117cc", width=2000, height=280),
                # foreground
                ft.Container(
                    content=ft.Row(
                        controls=[
                            photo_stack,
                            ft.Column(
                                controls=[
                                    ft.Text("Juuso Susan", size=28, color="#e6edf3", weight="bold"),
                                    ft.Text("225045451", size=14, color="#8b949e"),
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Text("Documentation Lead", size=12, color="#8b949e", weight="bold"),
                                                bgcolor="#0d1117",
                                                border=ft.border.all(1, "#8b949e"),
                                                border_radius=4,
                                                padding=ft.padding.symmetric(horizontal=10, vertical=4),
                                            ),
                                            ft.Container(
                                                content=ft.Text("Pavement Watch - GR 9", size=12, color="#8b949e"),
                                                bgcolor="#0d1117",
                                                border=ft.border.all(1, "#8b949e"),
                                                border_radius=4,
                                                padding=ft.padding.symmetric(horizontal=10, vertical=4),
                                            ),
                                            ft.Container(
                                                content=ft.Text("UNAM", size=12, color="#31eabf", weight="bold"),
                                                bgcolor="#2d0000",
                                                border=ft.border.all(1, "#e03131"),
                                                border_radius=4,
                                                padding=ft.padding.symmetric(horizontal=10, vertical=4),
                                            ),
                                        ],
                                        spacing=8,
                                        wrap=True,
                                    ),
                                ],
                                spacing=10,
                                expand=True,
                            ),
                        ],
                        spacing=24,
                        vertical_alignment="center",
                    ),
                    padding=ft.padding.symmetric(horizontal=32, vertical=24),
                    height=280,
                    alignment=ft.alignment.center_left,
                ),
            ],
        ),
        border_radius=12,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.border.all(1, "#30363d"),
    )

    # ── Stat cards ────────────────────────────────────────────────────────────
    def stat_card(value, label, color):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(str(value), size=26, color="#e6edf3", weight="bold"),
                    ft.Text(label, size=12, color="#8b949e"),
                ],
                horizontal_alignment="center",
                spacing=4,
            ),
            bgcolor="#161b22",
            border=ft.border.all(1, color),
            border_radius=10,
            padding=20,
            expand=True,
        )

    # ── Timeline cards with staggered animation ───────────────────────────────
    card_refs = []

    def entry_card(entry):
        color = MODULE_COLORS.get(entry["module"], "#30363d")

        def on_hover(e):
            e.control.border = ft.border.all(1, color if e.data == "true" else "#30363d")
            e.control.shadow = ft.BoxShadow(
                blur_radius=18, color=color + "55", spread_radius=1,
            ) if e.data == "true" else None
            e.control.update()

        card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(entry["module"], size=11, color=color, weight="bold"),
                                bgcolor="#161b22",
                                border=ft.border.all(1, color),
                                border_radius=4,
                                padding=ft.padding.symmetric(horizontal=8, vertical=3),
                            ),
                            ft.Text(f"{entry['commits']} commits", size=12, color="#484f58"),
                        ],
                        spacing=8,
                    ),
                    ft.Text(entry["title"], size=16, color="#e6edf3", weight="bold"),
                    ft.Text(f"{entry['week']}  •  {entry['date']}", size=11, color="#484f58"),
                    ft.Divider(color="#21262d"),
                    ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text(f"  {c}", size=13, color="#c9d1d9"),
                                border=ft.border.only(left=ft.BorderSide(3, color)),
                                padding=ft.padding.only(left=12, top=4, bottom=4),
                            )
                            for c in entry["contributions"]
                        ],
                        spacing=6,
                    ),
                ],
                spacing=8,
            ),
            padding=20,
            bgcolor="#161b22",
            border=ft.border.all(1, "#30363d"),
            border_radius=10,
            on_hover=on_hover,
            opacity=0,
            offset=ft.transform.Offset(0, 0.3),
            animate_opacity=ft.animation.Animation(500, "easeOut"),
            animate_offset=ft.animation.Animation(500, "easeOut"),
        )
        card_refs.append(card)
        return card

    cards = [entry_card(e) for e in TIMELINE_ENTRIES]

    def animate_cards():
        time.sleep(0.4)
        for card in card_refs:
            time.sleep(0.15)
            card.opacity = 1
            card.offset = ft.transform.Offset(0, 0)
            try:
                card.update()
            except Exception:
                pass

    threading.Thread(target=animate_cards, daemon=True).start()

    return ft.Column(
        controls=[
            hero,
            ft.Divider(color="#21262d"),
            ft.Row(
                controls=[
                    stat_card(len(TIMELINE_ENTRIES), "Weeks Logged", "#8b949e"),
                    stat_card(total_commits, "Total Commits", "#8b949e"),
                    stat_card(4, "PRs Authored", "#8b949e"),
                    stat_card(2, "PRs Reviewed", "#e3b341"),
                ],
                spacing=16,
            ),
            ft.Divider(color="#21262d"),
            ft.Text("Weekly Contributions", size=18, color="#e6edf3", weight="bold"),
            ft.Column(controls=cards, spacing=16),
        ],
        spacing=20,
        scroll="auto",
    )
