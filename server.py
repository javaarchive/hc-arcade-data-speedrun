from dash import Dash, html

app = Dash()

app.layout = [html.Div(children='I love speedrunning figuring out frameworks.')]



if __name__ == '__main__':
    app.run(debug=True)