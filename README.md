# YOLOv3_coco_dataset

Le but de ce dépôt git est d'illustrer la méthode de détection d'objets **YOLOv3**  pré-entrainée avec le jeu de données [coco](https://cocodataset.org/#home) qui contient 330K images et 80 classes d'objets ,en reprenant le [code](https://www.kaggle.com/code/aruchomu/yolo-v3-object-détection-in-tensorflow)  source de **HEARTKILLA** sur Kaggle.

Pour reproduire le travail presenté dans ce dépôt  git, on propose de suivre le mini-guide ci-dessous:

NB:L'installation de [anaconda](https://www.anaconda.com/download/) et [pip](https://pip.pypa.io/en/stable/installation/) est suppposée déjà faite. 

## 1.Création d'un envirenement 

créer un envirenement de travail à l'aide de la commande:

`conda create --name yolov3`

## 2.Installation des packages 

- Installation des packages python nécessaires pour tourner le script `yolov3_script.py` avec la commande:

`pip install -r Requirements.txt`

- Installation du client **GIT LFS** pour pouvoir cloner les fichier lourds:

    - [Mac](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) 

    - [Windows](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage?platform=windows) 

    - [Linx](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage?platform=linux) 


## 3.Clonner le repo git 

Clonner le dépot git via la commande: 

`git lfs clone git@github.com:oualidlamrini/YOLOv3_coco_dataset.git`


## 4.Composition du repo git

- `coco.names `: contient les 80 classes d'objets du jeu de données *coco* .
- `dog.jpg` et `office.jpg`:representent les images sur lesquelles on applique la méthode *yolov3* .
- `futur.ttf`: font de police avec lequel on affiche la classe de l'objet détecté.
- `yolov3.weights`: contient les estimations des paramettres d'apprentisssage.
- `yolov3_source.py`: contient les fonctions sources.
- `yolov3_script.py`: le script codant la détection d'objets.

## 5.Execution 
Afin d'executer le script `yolov3_script.py`,il suffit d'ouvrir le dossier **YOLOv3_coco_dataset** via **vscode**, puis executer les deux cellules du script.

NB:On paurrait juste tapper la commande `python yolov3_script.py`,pourtant on a rencontré des erreurs de compatibilité de versions du package `tensorflow` qui empêche l'execution normale du script.



