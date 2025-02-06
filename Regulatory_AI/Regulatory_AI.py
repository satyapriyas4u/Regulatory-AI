"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from rxconfig import config
from auth.authState import SessionState
from components.base import base_page


from .auth.authPages import (
    my_login_page,
    my_register_page,
    my_logout_page,
)

from . import routes, pages



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

def index() -> rx.Component:
    return base_page(
        rx.cond(SessionState.is_authenticated,
            # pages.dashboard_component(),
            # pages.landing_component(),
        )
    )
app = rx.App(
    theme=rx.theme(
        appearance="dark", 
        has_background=True, 
        panel_background="solid",
        scaling="90%",
        radius="medium", 
        accent_color="sky"
    )
)

app.add_page(
    pages.home_page, 
    route=routes.routes.HOME_ROUTE, 
    title="Regulatory AI"
)

app.add_page(
    pages.design_page, 
    route=routes.routes.HOME_ROUTE, 
    title="Regulatory AI"
)

# reflex_local_auth pages
app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="SignUp",
)

app.add_page(
    my_logout_page,
    route=routes.routes.LOGOUT_ROUTE,
    title="Logout",
)

# my pages
app.add_page(
    pages.about_page, 
    route=routes.routes.ABOUT_US_ROUTE,
    title="About Us"
)


app.add_page(
    pages.contact_page,
    route=routes.routes.CONTACT_US_ROUTE,
    title="Contact Us"
)

