# Regulatory_AI/pages/home.py

import reflex as rx 

from ..components.base import base_page
from ..templates.template import template

from ..routes import (
    routes, 
)


@rx.page(route=routes.HOME_ROUTE, title="Regulatory AI")
@template
def home_page() -> rx.Component:
    child = rx.vstack(
                rx.vstack(
                    rx.heading(
                        "Welcome to Regulatory AI!", 
                        size="9",
                        color=rx.color("accent", 9),
                        animation="slide-in",
                        transition="all 1s ease-in",
                        transform="translateY(10px)",
                        _hover={
                        "transform": "scale(1.25)",
                        "transition": "transform 0.5s ease-in-out",
                        },
                    ),
                    rx.text(
                        "Get started by creating Design History File",
                        size="7",
                        color=rx.color("jade", 7),
                    ),
                    rx.link(
                        rx.button("Get Started!"),
                        href=routes.DESIGN_ROUTE,
                    ),
                    spacing="5",
                    justify="center",
                    min_height="85vh",
                    width="70%",
                ),
        spacing="5",
        justify="center",
        align="center",
        min_height="80vh",
        id='my-child'
    )
    return child