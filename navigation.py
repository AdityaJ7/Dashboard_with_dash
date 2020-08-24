import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink(
            "Exploratory Data Analysis", href="/page-eda")),

        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Survival Functions", href="/page-1"),
                dbc.DropdownMenuItem(
                    "Cumulative Hazard Functions", href="/page-2"),
                dbc.DropdownMenuItem(
                    "Cox Proportional Hazard Model", href="/page-3"),
                dbc.DropdownMenuItem("Custom Models", href="/page-4"),
                dbc.DropdownMenuItem("Kaplan Meier Curves", href="/page-5"),
                dbc.DropdownMenuItem("Nelson Aalen Estimator", href="/page-6"),
            ],
            nav=True,
            in_navbar=True,
            label="Further Analysis",
        ),
        dbc.NavItem(dbc.NavLink(
            "Code Behind This", href="https://github.com/cipheraxat/Survival-Analysis")),
        dbc.NavItem(dbc.NavLink("Contact Us", href="/page-contact")),
    ],
    brand="Survival Analysis with Python",
    brand_href="/",
    color="dark",
    dark=True,
)
