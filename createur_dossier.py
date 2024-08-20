from pathlib import Path

chemin = Path("CHEMIN ou créer les dossier")

d = {"Dossier 1 ": ["Sous-Dossier 1",
               "Sous-Dossier 2",
               "Sous-Dossier 3",
               "Sous-Dossier 4"],
     "D2": ["Sous-Dossier 1",
                  "Sous-Dossier 2",
                  "Sous-Dossier 3"],
     "D3": ["Sous-Dossier 2",
                   "Sous-Dossier 3",
                   "Sous-Dossier 4"]}


for i in d:
    chemin_doss = chemin / i
    chemin_doss.mkdir(exist_ok=True)
    for j in d.get(i):
        chemin_ssdoss = chemin / i / j
        chemin_ssdoss.mkdir(parents=True, exist_ok=True)