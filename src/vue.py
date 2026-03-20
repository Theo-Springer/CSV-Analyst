import plotly.express as px

def plot_histogram(df, column):
    """Crée un histogramme pour une colonne numérique."""
    fig = px.histogram(df, x=column, title=f"Distribution de {column}", 
                       template="plotly_white")
    return fig

def plot_scatter(df, col_x, col_y):
    """Crée un nuage de points pour voir la corrélation."""
    fig = px.scatter(df, x=col_x, y=col_y, title=f"{col_x} vs {col_y}")
    return fig