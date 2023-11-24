import os 

import subprocess

# Remplacez 'votre_commande' par la commande que vous souhaitez exécuter
commande = 'source /home/technicalteams/virtualenv/phishing/3.8/bin/activate && cd /home/technicalteams/phishing && pip install django'

# Exécute la commande
resultat = subprocess.run(commande, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
