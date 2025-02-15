# pages/design.py

import reflex as rx
from ..states.state import QueryState
from ..templates.template import template

from ..routes import (
    routes, 
)

@rx.page(route=routes.DESIGN_ROUTE, title="Design")
@template
def design_page() -> rx.Component:
    child = rx.box(
        rx.vstack(
            # 1) Top section: Main heading
            rx.container(
                rx.heading("Design Input File", size="9"),
                width="100%",
                align="center",
                padding="0.5em",
        
            ),
            # 2) Middle section: Two columns (Select Category & Response)
            rx.hstack(
                # Left column
                rx.container(
                    rx.vstack(
                        rx.heading("Select Category", size="7"),
                        rx.select(
                            ["Knee System", "Hip System",],
                            placeholder="Select Category",
                            on_change=QueryState.set_category,
                            width="100%",
                        ),
                        rx.text("Select Test Type", size="5"),
                        rx.select(
                            [
                                "Biocompatibility",
                                "MRI",
                                "Design",
                                "Dimensions",
                                "Labelling",
                                "Sterilization",
                                "Surface Roughness",
                                "Packaging and Shipping",
                                "Wear Test",
                            ],
                            placeholder="Select Test Type",
                            on_change=QueryState.set_test_type,
                            width="100%",
                        ),
                        rx.text("Enter your query", size="5"),
                        rx.text_area(
                            placeholder="Type your query here...",
                            on_change=QueryState.set_query_text,
                            width="100%",
                        ),
                        rx.button("Generate", on_click=QueryState.generate_response),
                        spacing="2",
                        align_items="start",  # changed here
                    ),
                    width="50%",
                    padding="1em",
                ),
                # Right column
                rx.container(
                    rx.vstack(
                        rx.heading("Response", size="7"),
                        rx.markdown(QueryState.response),
                        spacing="2",
                        align_items="start",  # changed here
                    ),
                    width="50%",
                    padding="1em",
                ),
                align_items="start",     # changed here
                justify="between",       # changed here (instead of space-between)
                spacing="2",
                width="100%",
            ),
        ),
        id="container-gen-page",
        width="100%",
        padding="0.5em",
    )
    return child
