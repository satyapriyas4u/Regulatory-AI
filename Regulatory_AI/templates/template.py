from collections.abc import Callable
import reflex as rx
from ..components.base import base_page

def template(page: Callable[[], rx.Component]) -> rx.Component:
    """Reusable layout for all pages (decorator)."""
    return base_page(page())
