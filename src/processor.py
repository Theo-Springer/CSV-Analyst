import pandas as pd

def get_stats(df):
    """Calcule les stats de base (Moyenne, Min, Max)."""
    return df.describe()

def get_missing_values(df):
    """Compte les cases vides par colonne."""
    return df.isnull().sum()

def filter_data(df, column, value):
    """Filtre le tableau selon une valeur précise."""
    return df[df[column] == value]