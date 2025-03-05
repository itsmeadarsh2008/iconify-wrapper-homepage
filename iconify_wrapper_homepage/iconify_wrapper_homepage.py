"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex.components.radix.themes.color_mode import position_map
from iconify import icon
from reflex.style import set_color_mode, color_mode


class State(rx.State):
    """The app state."""

    ...


usage = """from iconify import icon

# Usage (just like rx.icon)
rx.button(icon(icon='tabler:arrow-down-to-arc'))
"""


def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            icon(icon="line-md:monitor", height=20),
            value="system",
        ),
        rx.segmented_control.item(
            icon(icon="line-md:sunny-loop", height=20),
            value="light",
        ),
        rx.segmented_control.item(
            icon(icon="line-md:moon-rising-filled-loop", height=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )


font = "Space Grotesk, sans-serif"


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.container(
            rx.flex(
                dark_mode_toggle(),
                rx.button(
                    icon(icon="octicon:mark-github-16", height=20),
                    variant="soft",
                    size="2",
                    on_click=rx.redirect(
                        "https://github.com/itsmeadarsh2008/iconify", is_external=True
                    ),
                ),
                spacing="3",
            ),
            float="right",
        ),
        rx.vstack(
            rx.heading(
                "iconify.design",
                size="9",
                font_family=font,
                cursor="pointer",
                on_click=rx.redirect(
                    "https://icon-sets.iconify.design/", is_external=True
                ),
            ),
            rx.text(
                "Access to 120 icon sets and 200K+ icons with Reflex. All of them in a single API 🪄. Load on demand 🔮",
                font_family=font,
                size="3",
                color_scheme="gray",
            ),
            rx.text(
                "Wrapper over official @iconify/react library.",
                font_family=font,
                size="3",
                color_scheme="gray",
            ),
            rx.code_block(usage, language="python"),
            rx.flex(
                *[
                    icon(
                        icon=i,
                        height=24,
                        width=24,
                        color=rx.color_mode_cond(light="#293132", dark="#87BBA2"),
                    )
                    for i in [
                        "line-md:beer-alt-twotone-loop",
                        "svg-spinners:bouncing-ball",
                        "bxs:check-circle",
                        "lets-icons:arhive-fill-duotone",
                        "svg-spinners:clock",
                    ]
                ],
                spacing="4",
            ),
            spacing="5",
            justify="center",
            min_height="100vh",
        ),
        background_color=rx.color_mode_cond(light="#f5f3f4", dark="#293132"),
        width="100%",
    )


app = rx.App(
    theme=rx.theme(has_background=True, accent_color="teal"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap"
    ],
)
app.add_page(index)
