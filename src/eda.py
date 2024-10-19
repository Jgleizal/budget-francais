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
    Visualise la répartition du budget par ministère et année, triée du plus petit au plus grand.
    :param df: DataFrame Pandas contenant les colonnes 'annee', 'balance_sortie', 'libelle_ministere'.
    """
    # Convertir la colonne 'annee' en numérique au cas où elle serait mal formatée
    df['annee'] = pd.to_numeric(df['annee'], errors='coerce')

    # Trier les données par année
    df_sorted = df.sort_values(by='annee', ascending=True)

    # Créer le barplot avec les années triées
    plt.figure(figsize=(12, 6))
    sns.barplot(x='annee', y='balance_sortie', data=df_sorted, hue='libelle_ministere')

    # Ajuster la taille de la légende pour les ministères
    plt.title('Répartition des dépenses par ministère et par année (triée)')
    plt.xticks(rotation=45)

    # Placer la légende en dehors du graphique
    plt.legend(title='Ministère', fontsize=8, title_fontsize='10', bbox_to_anchor=(1.05, 1), loc='upper left',
               borderaxespad=0.)

    # Ajuster les marges pour que la légende soit bien visible
    plt.tight_layout()

    # Afficher le graphique
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
