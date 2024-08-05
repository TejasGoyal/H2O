from dash import html, dcc

def create_videos():
    return html.Div([
        html.H2("Nutritionist's Videos"),
        # Example of embedding a YouTube video
        html.Div([
            html.Iframe(
                src="https://www.youtube.com/embed/your_video_id",
                style={"height": "400px", "width": "100%"}
            ),
        ], style={"padding": "20px"}),
        # Add more video embeds as needed
    ])
