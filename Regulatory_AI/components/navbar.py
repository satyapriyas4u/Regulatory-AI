import reflex as rx

from ..routes import (
    routes, 
    # pages,
)

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="6", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="35%",
                    ),
                    rx.heading(
                        "Regulatory AI", size="8", weight="bold"
                    ),
                    align_items="center",
                    spacing="4",
                ),
                rx.hstack(
                    navbar_link("Home", routes.HOME_ROUTE),
                    navbar_link("Design", routes.DESIGN_ROUTE),
                    navbar_link("About", routes.ABOUT_US_ROUTE),
                    navbar_link("Contact", routes.CONTACT_US_ROUTE),
                    spacing="6",
                ),
                rx.hstack(
                    rx.color_mode.button(size="2", variant="soft"),
                    spacing="4",
                    justify="end",
                ),
                rx.hstack(
                    rx.button(
                        "Register",
                        size="4",
                        variant="outline",
                    ),
                    rx.button(
                        "Log In", 
                        size="4"
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )