import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

PLOTLY_LOGO = ""


dropdown = dbc.DropdownMenu(
    children=[
        dbc.NavItem(dbc.NavLink("Spotipush", href="/spotipush")),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)

# Navbar
main_navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Spotipush", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="http://127.0.0.1:8050/",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="primary",
    className="mb-5",
    sticky="top",
)


def navbar():
    return main_navbar
