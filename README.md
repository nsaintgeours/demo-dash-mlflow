# Démo minimaliste Dash et MLFlow

## 1. Créer une application Dash et la déployer en local

### 1.1. Création du projet Python


**En bref**

On va initialiser un nouveau projet Python qui permettra de construire une application web minimaliste avec `Dash`.

**Prérequis**

- Python 3 installé sur mon PC avec la distribution `miniconda3` : voir [ici](https://docs.conda.io/en/latest/miniconda.html)
- PyCharm installé mon PC : voir [ici](https://www.jetbrains.com/fr-fr/pycharm/download)
- être familiarisé avec l'utilisation de Python, de PyCharm et de `conda`

**Etapes** : 

- dans **PyCharm**, créer un **nouveau projet** (menu *File / New project*) dans un nouveau dossier `C:/dev/demo`.

- dans la fenêtre de création du nouveau projet, on suit les recommandations de PyCharm et l'on crée un nouvel environnement virtuel `conda` utilisant **Python 3.8**. Ce nouvel environnement est nommé `demo` et il est associé à ce nouveau projet.

- créer un sous-dossier `C:/dev/demo/src` 

- créer un premier fichier `C:/dev/demo/src/app.py` qui définit notre application Dash minimaliste : 

```
import dash  
  
app = dash.Dash(__name__)  
app.layout = html.Div(children=[dash.html.H1('Ma démo')])  
  
if __name__ == '__main__':  
    app.run_server(host="0.0.0.0", port=8050)
```


- créer un second fichier `C:/dev/demo/requirements.txt` qui liste les dépendances Python du projet, avec le contenu suivant : 

```
dash
```

- installer les dépendances du projet dans l'environnement `conda`. Les commandes suivantes sont à taper dans le terminal *'Command Prompt'* de PyCharm :

```
C:\dev\demo> conda activate demo
C:\dev\demo (demo)> pip install -r requirements.txt
```

**Vérification**

Pour vérifier que notre application web fonctionne en local, il suffit d'exécuter le script `app.py` (bouton *Run* dans PyCharm). 
On doit obtenir un certain nombre d'informations en sortie, dont une ligne qui ressemble à ça (avec une adresse IP potentiellement différente) :  

```
(...)
Running on http://192.168.1.18:8050/ (Press CTRL+C to quit)
(...)
```

Si l'on clique sur l'adresse URL, notre navigateur web (chez moi Firefox) s'ouvre sur une page web vide, avec seulement un titre : *"Ma démo"*. 
Notre appli Dash minimaliste fonctionne en local ! On note quelle est disponible sur le port `8050` qui a été spécifié dans le code `app.run_server(host="0.0.0.0", port=8050)`.



### 1.2. Conténeuriser l'application avec Docker

**En bref**

On va maintenant "conténeuriser" notre application avec Docker, afin de faciliter son déploiement.

**Prérequis**

- Docker installé sur mon PC 
- être familiarisé avec l'utilisation de Docker

**Préparer la conténeurisation**

Dans notre projet PyCharm, créer un nouveau fichier `C:/dev/demo/Dockerfile` qui permettra de conténeuriser notre application. Ce fichier a le contenu suivant : 

```
FROM python:3.8  
  
COPY requirements.txt /  
RUN pip install -r /requirements.txt  
  
COPY ./ ./  
  
EXPOSE 8050  
  
CMD ["python", "./src/app.py"]
```

Ce Dockerfile donne les instructions pour construire la future "image" Docker de notre application : il indique qu'il faut d'abord installer Python 3.8, puis les dépendances Python du projet, puis copier l'ensemble des sources du projet, et exécuter le script Python  `app.py`. Le fichier Dockerfile indique aussi que notre application sera disponible sur le port 8050.

**Construire une image Docker de notre application**

Dans un but pédagogique, on montre ici comment conténeuriser notre application "en local", sur notre PC. Ceci nécessite d'avoir préalablement installé Docker sur son PC. 
Cependant, on peut décider de sauter cette étape, car la conténeurisation de notre application se fera in fine sur les serveurs de Github dans le cadre de l'intégration continue. 

- dans PyCharm, ouvrir un terminal bash à la racine du projet (`C:/dev/demo`) 

- construire une image Docker nommée `mon_image` à partir de notre dossier courant :   

```
$ docker build -t mon_image .
```

- afficher la liste des images Docker disponibles sur notre PC, on devrait y voir apparaître notre image `mon_image` nouvellement créée : 

```
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
mon_image    latest    33023f5dfedf   About a minute ago   1.1GB
```

### 1.3. Déployer notre application web en local

**En bref**

On va maintenant déployer notre application web "en local".


**Etapes**

- dans PyCharm, ouvrir un terminal bash à la racine du projet (`C:/dev/demo`) 

- démarrer un conteneur que l'on nomme `mon_conteneur` à partir de l'image Docker `mon_image` créée à l'étape précédente :

```
$ docker run --name mon_conteneur -d mon_image

1373fed42020c17efe20fbf34d63aa58fda886c57ca341537684e2e0910607b7
```

Noter l'option `-d` dans la commande : elle permet de lancer le conteneur en mode "détaché" et de reprendre la main sur la ligne de commande après. 

**Vérification**

On peut maintenant vérifier que notre application est bien démarrée.

- afficher la liste des conteneurs : 

```
$ docker container ls

CONTAINER ID   IMAGE       COMMAND                 CREATED          STATUS         PORTS      NAMES
da767e71a69a   mon_image   "python ./src/app.py"   10 seconds ago   Up 9 seconds   8050/tcp   mon_conteneur
```

- ouvrir un navigateur web (chez moi Firefox), puis entrer l'URL `localhost:8050` --> une page web vide s'affiche, avec seulement un titre : *"Ma démo"*. C'est bon, notre application web minimaliste est déployée en local !


**Arrêt de l'application**


- on peut maintenant arrêter notre conteneur : 

```
$ docker stop mon_conteneur
```

- si l'on veut tout supprimer sur Docker pour faire de la place et "repartir propre" :  

```
$ docker container rm mon_conteneur
$ docker rmi mon_image
$ docker image prune
```



### 1.4. Publier l'application sur Docker Hub


**En bref**

Nous allons maintenant publier l'image Docker de notre application sur un dépôt en ligne ([Docker Hub](https://hub.docker.com)), afin de permettre par la suite son déploiement sur un serveur distant. 


**Etapes**

- se créer un compte personnel gratuit sur **[Docker Hub](https://hub.docker.com)** : mon compte a pour login `nathaliesaintgeours`, et un mot de passe sauvegardé dans KeePassX

- dans PyCharm, ouvrir un terminal bash à la racine du projet (`C:/dev/demo`) 

- on commence par tagger l'image Docker `mon_image` (qui a été créée à l'étape 1.2) pour lui donner un nom plus explicite Ce nouveau nom est composé du nom de notre dépôt Docker Hub (ici `nathaliesaintgeours`), du nom de l'application (ici `demo`) et de la version de l'application (ici `latest`) : 

```
$ docker tag mon_image nathaliesaintgeours/demo:latest
```

- se connecter à Docker Hub avec le login et le mot de passe du compte personnel que l'on vient de créer :   

```
$ docker login -u nathaliesaintgeours -p XXXXXXXXX

WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Login Succeeded
```


- publier l'image Docker de notre application sur notre dépôt Docker Hub :  

```
$ docker push nathaliesaintgeours/demo:latest

The push refers to repository [docker.io/nathaliesaintgeours/demo]
3e27173a8d9a: Pushed
(...)
latest: digest: sha256:c0264ad47ef1921aec7d456f496cb8e2b3dab4578f028c79ed1576ea10c7a537 size: 2845
```

Et voilà, l'image Docker de notre application web est maintenant disponible en ligne sur notre compte Docker Hub ! On peut aller le vérifier en se connectant à [notre compte Docker Hub en ligne](https://hub.docker.com). 





## 2. Déployer notre application web sur AWS


### 2.1. Créer une instance EC2 (serveur virtuel) sur AWS

Le [service EC2 d'AWS](https://aws.amazon.com/fr/ec2) permet de créer facilement un serveur virtuel, que l'on peut allumer / éteindre à la demande, et sur lequel on va déployer notre application.

Je me suis déjà inscrite sur AWS (voir login / mot de passe sur KeePassX), puis j'ai créé une instance de calcul sur le service EC2 (en bénéficient d'une offre d'essai gratuit pour 750 heures d'utilisation). Par ailleurs, j'ai donné une IP statique (stable) à cette instance de calcul grâce au service "Elastic IP" d'EC2. 
Voici les caractéristiques de mon serveur virtuel : 

- IP statique : `18.117.63.135`
- user : `ec2-user`
- clé privée SSH : sur ma Dropbox, fichier `site web/aws/ec2_admin.pem`


### 2.2. Me connecter à mon serveur virtuel EC2 chez AWS

Pour me connecter à ce serveur, j'ai plusieurs options : 

- ouvrir une console bash sur mon PC, aller dans le dossier qui contient la clé privée SSH, et me connecter via SSH en tapant : 

```
ssh -i ec2_admin.pem ec2-user@18.117.63.135
```

- ouvrir une console via mon [interface de gestion du service EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances)

- utiliser un outil comme [WinSCP](https://winscp.net/eng/download.php) pour copier / coller / éditer des fichiers depuis mon PC sur le serveur virtuel EC2


### 2.3 Configuration du pare-feu de mon serveur virtuel EC2

L'application web que je vais créer va utiliser le port 8050 pour afficher son contenu (je pourrai choisir un autre port si je veux). 
Je dois donc ouvrir ce port sur mon serveur virtuel EC2. 
Cela se fait sur mon compte AWS, dans la [page de gestion des "Groupes de sécurité"](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#SecurityGroup:securityGroupId=sg-0f0503eaebf726097).


### 2.4. Installer Docker sur mon serveur virtuel EC2

Nous utilisons Docker pour le déploiement de notre application. Par défaut, Docker n'est pas installé sur les serveurs vrituels EC2. 
Il nous faut donc installer Docker, une seule fois, sur notre serveur virtuel EC2.


**Etapes**  

- se connecter au serveur virtuel EC2 depuis son PC avec : 

```
$ ssh -i ec2_admin.pem ec2-user@18.117.63.135
```

- une fois connectée au serveur EC2, installer docker : 

```
[ec2-user@ip-172-31-41-247 ~]$ sudo yum update -y
[ec2-user@ip-172-31-41-247 ~]$ sudo amazon-linux-extras install docker
[ec2-user@ip-172-31-41-247 ~]$ sudo service docker start
[ec2-user@ip-172-31-41-247 ~]$ sudo usermod -a -G docker ec2-user
[ec2-user@ip-172-31-41-247 ~]$ logout
```

Ca y est c'est fait !

**Vérification**

- se reconnecter au serveur virtuel EC2 : 

```
$ ssh -i ec2_admin.pem ec2-user@18.117.63.135
```

Vérifier que docker y est bien installé :

```
[ec2-user@ip-172-31-41-247 ~]$ docker --version
```


### 2.6 Déployer notre application sur le serveur virtuel EC2


Ca y est, nous sommes prêts à déployer notre application Dash dans le cloud !

**Etapes**  

- se connecter à notre serveur virtuel EC2 via SSH

- se connecter à [Docker Hub](https://hub.docker.com/) avec le login et le mot de passe du compte personnel que l'on a créé à l'**étape 1.4**

```
$ docker login -u nathaliesaintgeours -p XXXXXXXXX

WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Login Succeeded
```

- télécharger l'image Docker de notre application (qui s'appelle `nathaliesaintgeours/demo:latest`) sur notre serveur vrituel EC2 :   

```
$ docker pull nathaliesaintgeours/demo:latest

latest: Pulling from nathaliesaintgeours/demo
(...)
Status: Downloaded newer image for nathaliesaintgeours/demo:latest
docker.io/nathaliesaintgeours/demo:latest
```

- démarrer un conteneur Docker que l'on nomme `demo_dashboard` à partir de l'image Docker `nathaliesaintgeours/demo:latest` que l'on vient de télécharger :

```
$ docker run --name demo_dashboard -p 8050:8050 -d nathaliesaintgeours/demo:latest
```

On note ici l'option `-p 8050:8050` : cette syntaxe du type `-p to:from` signifie que l'on redirige la sortie de notre conteneur Docker, qui communique normalement sur le port `8050` (`from`) comme défini dans le fichier `Dockerfile`, vers le port `8050` (`to`). Ici comme les deux ports `from` et `to` sont identiques, la redirection n'a pas d'effet particulier. 

- **vérification** : aller voir le résultat en ouvrant l'URL `18.117.63.135:8050` dans un naviateur web


**Bravo, on vient de déployer une application Dash minimaliste sur le web !**


**Arrêt de l'application**

Toujours sur le serveur virtuel EC2, on peut maintenant arrêter le conteneur Docker, supprimer le conteneur et nettoyer :

```
$ docker stop demo_dashboard
$ docker rm demo_dashboard
$ docker system prune
```



### 2.7 Utiliser docker-compose pour faciliter le déploiement


**En bref**  
On peut simplifier un peu les étapes de déploiement en utilisant `docker-compose`.

**Etapes**

- sur son PC, à la racine de notre projet Python `C:\dev\demo`, créer un fichier `docker-compose.yml` : 
```
version: "3.7"

services:

  dashboard:
    image: nathaliesaintgeours/demo:latest
    container_name: demo_dashboard
    ports:
      - "8050:8050"
    environment:
      - TARGET=LIVE
    restart: unless-stopped
```

Que nous dit ce fichier ? Que l'on veut créer un "service" nommé `dashboard`. Ce service démarrera un conteneur nommé `demo_dashboard`, qui sera créé à partir de l'image Docker `nathaliesaintgeours/demo:latest`. Une redirection du port sortant du conteneur sera faite du port 8050 vers le port 8050 (= pas de redirection). Dans le conteneur Docker, une variable d'environnement sera automatiquement créée, nommée `TARGET` avec pour valeur `LIVE`.

- copier le fichier `docker-compose.yml` sur le serveur virtuel EC2, par exemple avec l'outil WinSCP


- se connecter en SSH au serveur virtuel EC2

- une fois connecté au serveur virtuel EC2, lancer l'application avec la commande suivante : 

```
$ docker-compose up -d
```

Et c'est tout !

**Vérification**

Notre application est lancée ! Nous pouvons vérifier cela : 

- afficher la liste des conteneurs qui sont "up" sur notre serveur virtuel EC2 : 

```
$ docker container ls

CONTAINER ID   IMAGE                             COMMAND                 CREATED          STATUS         PORTS                                       NAMES
83962a056ba4   nathaliesaintgeours/demo:latest   "python ./src/app.py"   11 seconds ago   Up 8 seconds   0.0.0.0:8050->8050/tcp, :::8050->8050/tcp   demo_dashboard
```

- aller voir notre application en ouvrant l'URL `18.117.63.135:8050` dans un navigateur web 


**Arrêt de l'application**

Pour arrêter notre application, une seule commande suffit : 

```
$ docker-compose down --rmi all
```
