import pandas as pd

def load_parquet(file_path):
    """
    Charge un fichier Parquet à partir du chemin fourni.
    :param file_path: Chemin du fichier Parquet.
    :return: DataFrame Pandas contenant les données.
    """
    try:
        data = pd.read_parquet(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading Parquet file: {e}")
        return None

def check_missing_values(df):
    """
    Vérifie les valeurs manquantes dans chaque colonne du DataFrame.
    :param df: DataFrame Pandas.
    :return: Affiche le nombre de valeurs manquantes par colonne.
    """
    missing_values = df.isnull().sum()
    print("Valeurs manquantes par colonne :\n", missing_values)
    return missing_values


def clean_data(df):
    """
    Nettoie les données en supprimant les valeurs manquantes et en formatant les colonnes.
    :param df: DataFrame Pandas.
    :return: DataFrame Pandas nettoyé.
    """
    # Liste des colonnes à nettoyer
    columns_to_clean = [
        'libellemission', 'sous_postes', 'indicateurs_de_detail',
        'mission', 'nature_budgetaire', 'programme',
        'libelle_ministere', 'texte_1', 'texte_2'
    ]

    # Vérifie si chaque colonne existe avant de tenter de la remplir
    for col in columns_to_clean:
        if col in df.columns:
            df[col] = df[col].fillna(0)
        else:
            print(f"Colonne {col} absente, aucune action appliquée.")

    # Supprimer les lignes avec des valeurs manquantes restantes dans les autres colonnes
    df_cleaned = df.dropna()
    print(f"Data cleaned. Remaining rows: {len(df_cleaned)}")
    return df_cleaned


# Exemple d'utilisation
if __name__ == "__main__":
    file_path = "../data/2014-2023_balances_des_comptes_etat.parquet"
    df = load_parquet(file_path)
    if df is not None:
        check_missing_values(df)
        df_cleaned = clean_data(df)
        print(df_cleaned.head())  # Affiche les premières lignes des données nettoyées
