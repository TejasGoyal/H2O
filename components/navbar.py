import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        brand="Nutritionist's Website",
        brand_href="/",
        color="primary",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Videos", href="/videos")),
            dbc.NavItem(dbc.NavLink("Fun Facts", href="/fun-facts")),
            dbc.NavItem(dbc.NavLink("BMI Calculator", href="/bmi-calculator")),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        ],
    )
    return navbar
