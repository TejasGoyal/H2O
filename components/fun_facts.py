from dash import html
import datetime

def get_fun_fact():
    # Example fun facts dictionary
    fun_facts = {
        1: "Eating fruits and vegetables can boost your mood!",
        2: "Staying hydrated is crucial for overall health.",
        3: "Regular physical activity can help prevent chronic diseases.",
        # Add more fun facts
    }
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    return fun_facts[day_of_year % len(fun_facts)]

def create_fun_facts():
    return html.Div([
        html.H2("Daily Fun Fact"),
        html.P(get_fun_fact(), style={"font-size": "20px", "padding": "20px"})
    ])
