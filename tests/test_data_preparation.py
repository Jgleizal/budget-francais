import unittest
from src.data_preparation import load_parquet, clean_data
import pandas as pd


class TestDataPreparation(unittest.TestCase):

    def test_load_parquet(self):
        file_path = "../data/2014-2023_balances_des_comptes_etat.parquet"
        df = load_parquet(file_path)
        self.assertIsInstance(df, pd.DataFrame, "Le fichier Parquet n'est pas chargé correctement en DataFrame.")

    def test_clean_data(self):
        # DataFrame simplifié pour le test
        df = pd.DataFrame({
            'annee': [2021, 2022, None],
            'balance_sortie': [1000, 2000, None]
        })

        # Nettoyage des données (ne référencer que les colonnes présentes)
        df_cleaned = clean_data(df)

        # Vérification que les lignes avec des valeurs manquantes dans 'annee' ont été supprimées
        self.assertEqual(len(df_cleaned), 2,
                         "La fonction de nettoyage n'a pas supprimé les lignes avec des valeurs manquantes.")


if __name__ == '__main__':
    unittest.main()
