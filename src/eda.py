import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def eda_overview(df):
    """
    Analyse exploratoire des données, y compris l'affichage des premières lignes, info et description.
    :param df: DataFrame Pandas.
    """
    print("Aperçu des données :")
    print(df.head())
    print("\nInformations sur les données :")
    print(df.info())
    print("\nDescription statistique :")
    print(df.describe())


def visualize_budget_distribution(df):
    """
    Visualise la répartition du budget par ministère et année.
    :param df: DataFrame Pandas contenant les colonnes 'année', 'ministère', 'dépenses'.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='année', y='dépenses', data=df, hue='ministère')
    plt.title('Répartition des dépenses par ministère et par année')
    plt.xticks(rotation=45)
    plt.show()


# Exemple d'utilisation
if __name__ == "__main__":
    from data_preparation import load_parquet, clean_data

    file_path = "../data/2014-2023_balances_des_comptes_etat.parquet"
    df = load_parquet(file_path)
    if df is not None:
        df_cleaned = clean_data(df)
        eda_overview(df_cleaned)
        visualize_budget_distribution(df_cleaned)
