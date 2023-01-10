
# PyTorch : Text-To-Speech from image

## Prérequis  

Ce projet utilise Python 3.10.9

Installez les dépendances : 

- [PyTorch](https://pytorch.org/get-started/locally/) : installez la version correspondant à votre gestionnaire de paquets (Conda, pip...)
Pour ce projet installez la version **CPU**, mais si votre machine est équipée d'un GPU envisagez la version CUDA pour vos futurs projets.

- EasyOCR et MatPlotLib : ``pip3 install easyocr matplotlib``

Placez vous à la racine du projet et lancez le script : 

``/bin/python3.10 "main.py" ``

Le script va se lancer et vous demander un URL ou chemin vers votre image. 

![enter image description here](https://i.ibb.co/FwWqBV2/2.png)
Un fichier est disponible dans le dossier assets pour tester le script.
Renseignez le chemin : ``assets/1.png``

Dans un premier temps, on utilise ``easyocr`` pour extraire les caractères de l'image. On assigne ensuite à chaque lettre extraite un code lui correspondant, et on construit un spectrogramme à partir des données récoltées. 

![enter image description here](https://i.ibb.co/bvk6H94/Figure-1.png)

Une fois le spectrogramme généré, le programme va le convertir en fichier audio (*fermez la preview du spectogramme pour générer le fichier*).

Le fichier ``tts.wav`` sera généré à la racine de votre dossier.

## NOTES : 

- Pour l'instant, seul l'Anglais est reconnu pour la génération du TTS. 
Néanmoins, le Français et bien d'autres langages sont bien reconnus par easyOCR. L'entraînement d'un modèle en Français permettrait de générer un TTS en Français.

- Certaines polices de caractères sont mal reconnues par easyOCR, c'est le cas avec le fichier ``1.png`` du dossier assets.

- Certains sites empêchent le téléchargement d'images et vous pouvez rencontrer une erreur lorsque vous renseignez une URL. 

