# Regulatory_AI/components/base.py
# Description: Base layout for all pages


import reflex as rx

# from ..auth.state import SessionState
from .navbar import navbar
# from ..pages.dashboard import base_dashboard_page

def base_layout_component(child, *args, **kwargs) -> rx.Component:
    return rx.fragment( # renders no css
        navbar(),
        rx.box(
            child,
            # bg=rx.color("accent", 3),
            padding_x="0.5em",
            width="100%",
            id="my-content-area-el"
        ),
    )

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx. Component):
        child = rx.heading("this is not a valid child element")
    # return rx.cond(
    #     SessionState.is_authenticated,
    #     base_dashboard_page(child, *args, **kwargs),
    #)
    return base_layout_component(child, *args, **kwargs )
