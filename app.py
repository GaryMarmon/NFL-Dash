from Dash import Dash
from src.components.layout import create_layout


app = Dash(supress_callback_exceptions=True)
app.layout = create_layout(app)

if __name__ == '__main__':
    app.run(debug=True)