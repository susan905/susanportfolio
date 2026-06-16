import flet as ft
import webbrowser

GITHUB_USERNAME = "susan905"
GITHUB_REPO     = "Susan"
GITHUB_URL      = f"https://github.com/{GITHUB_USERNAME}"
GITHUB_REPO_URL = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}"
STUDENT_ID      = "225045451"
ROLE            = "DOCUMENTATION LEAD"

COMMIT_LOG = [
    {"hash": "a1b2c3d", "message": "feat: Firebase project setup and Firestore collections created",           "date": "27 Jan 2026"},
    {"hash": "b2c3d4e", "message": "feat: Firestore security rules — request.auth != null on all collections", "date": "3 Feb 2026"},
]

PULL_REQUESTS = [
    {"number": 2, "title": "Opened their first pull request on GitHub in kaptainpena", "role": "Author", "date": "1 Feb 2026"},
]

IMPACT_LINES = [
    "Firebase Configuration: Set up the entire Firebase backend used by all 15 team members — Firestore collections, security rules, Storage, and .env key management. Every module depends on this foundation.",
]

BG     = "#0d1117"
CARD   = "#161b22"
BORDER = "#30363d"
TEXT   = "#e6edf3"
MUTED  = "#8b949e"
DIM    = "#484f58"
BLUE   = "#8b949e"
GREEN  = "#3fb950"
ROLE_GREY = "#8b949e"
ROLE_BLACK = "#0d1117"


def github_page():

    def open_url(url):
        def handler(e):
            webbrowser.open(url)
        return handler

    def stat_card(value, label, border_color):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(str(value), size=26, color=TEXT, weight="bold"),
                    ft.Text(label, size=12, color=MUTED),
                ],
                horizontal_alignment="center",
                spacing=4,
            ),
            bgcolor=CARD,
            border=ft.border.all(1, border_color),
            border_radius=10,
            padding=20,
            expand=True,
        )

    def commit_row(commit):
        # Each hash links directly to the commit on GitHub
        commit_url = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}/commit/{commit['hash']}"
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(commit["hash"], size=11, color=BLUE),
                        bgcolor="#0d1117",
                        border_radius=4,
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                        on_click=open_url(commit_url),
                        ink=True,
                        tooltip="Open commit on GitHub",
                    ),
                    ft.Text(commit["message"], size=13, color="#c9d1d9", expand=True),
                    ft.Text(commit["date"], size=11, color=DIM),
                ],
                spacing=12,
                vertical_alignment="center",
            ),
            border=ft.border.only(bottom=ft.BorderSide(1, "#21262d")),
            padding=ft.padding.symmetric(vertical=10),
        )

    def pr_row(pr):
        role_color = BLUE if pr["role"] == "Author" else MUTED
        pr_url = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}/pull/{pr['number']}"
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f"#{pr['number']}", size=12, color=BLUE, width=42),
                    ft.Text(pr["title"], size=13, color="#c8f8aa", expand=True),
                    ft.Container(
                        content=ft.Text(pr["role"], size=11, color=role_color),
                        bgcolor=BG,
                        border=ft.border.all(1, role_color),
                        border_radius=4,
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                    ),
                    ft.Container(
                        content=ft.Text("MERGED", size=10, color="#fff", weight="bold"),
                        bgcolor="#1a3a1a",
                        border=ft.border.all(1, GREEN + "66"),
                        border_radius=4,
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                        on_click=open_url(pr_url),
                        ink=True,
                        tooltip="Open PR on GitHub",
                    ),
                    ft.Text(pr["date"], size=11, color=DIM),
                ],
                spacing=10,
                vertical_alignment="center",
            ),
            border=ft.border.only(bottom=ft.BorderSide(1, BORDER)),
            padding=ft.padding.symmetric(vertical=10),
        )

    def section(title, controls_list):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(title, size=16, color=TEXT, weight="bold"),
                    ft.Divider(color=BORDER),
                    ft.Column(controls=controls_list, spacing=0),
                ],
                spacing=12,
            ),
            bgcolor=CARD,
            border=ft.border.all(1, BORDER),
            border_radius=10,
            padding=20,
        )

    authored = sum(1 for p in PULL_REQUESTS if p["role"] == "Author")
    reviewed = sum(1 for p in PULL_REQUESTS if p["role"] == "Reviewer")

    # ── Profile card with clickable GitHub link ────────────────────────────────
    profile = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text("JS", size=22, color="#ffffff", weight="bold"),
                    bgcolor=BLUE,
                    border_radius=30,
                    width=56, height=56,
                    alignment=ft.alignment.center,
                    shadow=ft.BoxShadow(blur_radius=12, color=BLUE + "44", spread_radius=1),
                ),
                ft.Column(
                    controls=[
                        ft.Text("Juuso Susan", size=18, color=TEXT, weight="bold"),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(ROLE, size=11, color=ROLE_GREY, weight="bold"),
                                    bgcolor=ROLE_BLACK,
                                    border=ft.border.all(1, ROLE_GREY),
                                    border_radius=4,
                                    padding=ft.padding.symmetric(horizontal=8, vertical=3),
                                ),
                                ft.Text(f"Group 9 Pavement Watch  •  {STUDENT_ID}", size=12, color=MUTED),
                            ],
                            spacing=8,
                        ),
                    ],
                    spacing=4,
                    expand=True,
                ),
                # ── GitHub profile button ──────────────────────────────────────
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text("🐙", size=16),
                            ft.Text("github.com/susan905", size=12, color=BLUE, weight="bold"),
                        ],
                        spacing=8,
                        vertical_alignment="center",
                    ),
                    bgcolor="#0d1117",
                    border=ft.border.all(1, BLUE + "88"),
                    border_radius=8,
                    padding=ft.padding.symmetric(horizontal=16, vertical=10),
                    on_click=open_url(GITHUB_URL),
                    ink=True,
                    tooltip="Open GitHub Profile",
                ),
            ],
            spacing=16,
            vertical_alignment="center",
        ),
        bgcolor=CARD,
        border=ft.border.all(1, BLUE + "66"),
        border_radius=10,
        padding=20,
        shadow=ft.BoxShadow(blur_radius=16, color=BLUE + "22", spread_radius=1),
    )

    # ── Repo link banner ──────────────────────────────────────────────────────
    repo_banner = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text("📁  " + GITHUB_REPO, size=15, color=TEXT, weight="bold"),
                        ft.Text(GITHUB_REPO_URL, size=11, color=MUTED),
                    ],
                    spacing=3,
                    expand=True,
                ),
                ft.Container(
                    content=ft.Text("View Repository →", size=12, color="#0d1117", weight="bold"),
                    bgcolor=BLUE,
                    border_radius=6,
                    padding=ft.padding.symmetric(horizontal=16, vertical=8),
                    on_click=open_url(GITHUB_REPO_URL),
                    ink=True,
                    tooltip="Open repo on GitHub",
                ),
            ],
            alignment="spaceBetween",
            vertical_alignment="center",
        ),
        bgcolor=CARD,
        border=ft.border.all(1, BORDER),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=20, vertical=14),
    )

    return ft.Column(
        controls=[
            ft.Text("GitHub Evidence & Documentation", size=28, color=TEXT, weight="bold"),
            ft.Text("Individual contribution evidence — University of Namibia.", size=14, color=MUTED),
            ft.Divider(color=BORDER),
            profile,
            repo_banner,
            ft.Row(
                controls=[
                    stat_card(len(COMMIT_LOG), "Commits", BLUE),
                    stat_card(authored, "PRs Authored", BLUE),
                    stat_card(reviewed, "PRs Reviewed", MUTED),
                    stat_card(len(PULL_REQUESTS), "PRs Merged", GREEN),
                ],
                spacing=16,
            ),
            section("Commit History", [commit_row(c) for c in COMMIT_LOG]),
            section("Pull Request Log", [pr_row(p) for p in PULL_REQUESTS]),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Impact Summary", size=16, color=TEXT, weight="bold"),
                        ft.Divider(color=BORDER),
                        ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Text(f"  {line}", size=13, color="#c9d1d9"),
                                    border=ft.border.only(left=ft.BorderSide(3, BLUE)),
                                    padding=ft.padding.only(left=12, top=6, bottom=6),
                                    margin=ft.margin.only(bottom=8),
                                )
                                for line in IMPACT_LINES
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=12,
                ),
                bgcolor=CARD,
                border=ft.border.all(1, BORDER),
                border_radius=10,
                padding=20,
            ),
        ],
        spacing=20,
        scroll="auto",
    )
