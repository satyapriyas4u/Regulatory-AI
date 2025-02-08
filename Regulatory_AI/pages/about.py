# Regulatory_AI/pages/about.py

import reflex as rx 

from ..components.base import base_page
from ..templates.template import template

from ..routes import (
    routes, 
)

# @rx.page(route=routes.ABOUT_US_ROUTE, title="Regulatory AI")
# @template
def about_page() -> rx.Component:
    child = rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "Something cool about us.",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(child)