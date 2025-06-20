from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap"
    ]
)

df = pd.read_excel("vendas_exemplo.xlsx")

fig = px.bar(
    df.groupby("Mês", as_index=False)["Receita Total"].sum(),
    x="Mês",
    y="Receita Total",
    text_auto=True,
    title="Receita por Mês",
    color="Receita Total",
    color_continuous_scale="Blues"
)

app.layout = html.Div(
    children=[
        html.H1(
            'Vendas',
            style={
                'fontFamily': 'Poppins',
                'fontWeight': '800',
                'color': 'rgb(0, 51, 102)',
                'textShadow': '1px 1px 3px rgba(0,0,0,0.2)'
            }
        ),
        html.H2(
            'Gráfico com informações das Vendas',
            style={
                'fontFamily': 'Poppins',
                'fontWeight': '600',
                'color': 'rgb(47, 53, 66)',
                'textShadow': '1px 1px 3px rgba(0,0,0,0.1)'
            }
        ),
        html.Div(
            'Informações abaixo!!!',
            style={
                'fontFamily': 'Poppins',
                'fontWeight': '400',
                'color': 'rgb(85, 85, 85)',
                'textShadow': '1px 1px 2px rgba(0,0,0,0.1)'
            }
        ),
        dcc.Dropdown(
            options=[{'label': 'Todos', 'value': 'Todos'}] +
                    [{'label': mes, 'value': mes} for mes in df["Mês"].unique()],
            value='Todos',
            id='demo-dropdown'
        ),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ],
    style={
        'backgroundImage': 'url("https://png.pngtree.com/thumb_back/fh260/background/20210715/pngtree-business-geometric-technology-slide-hexagon-light-dot-light-blue-background-image_742356.jpg")',
        'backgroundSize': 'cover',
        'backgroundRepeat': 'no-repeat',
        'backgroundPosition': 'center',
        'minHeight': '100vh',
        'padding': '20px',
        'fontFamily': 'Poppins, sans-serif',
        'color': 'rgb(28, 28, 28)'
    }
)

@app.callback(
    Output('example-graph', 'figure'),
    Input('demo-dropdown', 'value')
)
def atualizar_grafico(mes_selecionado):
    if mes_selecionado == 'Todos':
        df_filtrado = df
    else:
        df_filtrado = df[df["Mês"] == mes_selecionado]

    agrupado = df_filtrado.groupby("Mês", as_index=False)["Receita Total"].sum()

    fig = px.bar(
        agrupado,
        x="Mês",
        y="Receita Total",
        text_auto=True,
        title=f"Receita em {mes_selecionado}" if mes_selecionado != 'Todos' else "Receita por Mês",
        color="Receita Total",
        color_continuous_scale="Blues"
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
