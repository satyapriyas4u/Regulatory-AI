import reflex as rx 

from Regulatory_AI.components.base import base_page
from Regulatory_AI.templates.template import template

from ..routes import (
    routes, 
)

# @rx.page(route=routes.CONTACT_US_ROUTE, title="Regulatory AI")
# @template
def contact_page() -> rx.Component:
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