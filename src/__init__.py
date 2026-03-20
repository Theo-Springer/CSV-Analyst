"""
CSV-Analyst - Module d'analyse de données CSV
"""

# Import des fonctions de traitement de données
from .processor import get_stats, get_missing_values, filter_data

# Import des fonctions de visualisation
from .vue import plot_histogram, plot_scatter

__version__ = "1.0.0"
__all__ = [
    "get_stats",
    "get_missing_values", 
    "filter_data",
    "plot_histogram",
    "plot_scatter"
]
