import os
import pandas as pd

class SheetWorks:

    def load_sheet():
        sheet = pd.read_excel('docs/clients.xlsx')

        for _, transaction in sheet.iterrows():

            name = transaction['name']
            age = transaction['age']
            mood = transaction['mood']
            print(f"Cliente: {name}\nIdade: {age}\nHumor: {mood}")
