# Démo : une appli Dash et MLFlow déployée sur AWS EC2

## Table des matières

- [1. Créer une application Dash et la déployer en local](https://github.com/nsaintgeours/demo/blob/master/README.md#1-cr%C3%A9er-une-application-dash-et-la-d%C3%A9ployer-en-local)

   - [1.1. Création du projet Python](https://github.com/nsaintgeours/demo/blob/master/README.md#11-cr%C3%A9ation-du-projet-python)
   - [1.2. Conténeuriser l'application avec Python](https://github.com/nsaintgeours/demo/blob/master/README.md#12-cont%C3%A9neuriser-lapplication-avec-docker)
   - [1.3. Déployer notre application web en local](https://github.com/nsaintgeours/demo/blob/master/README.md#13-d%C3%A9ployer-notre-application-web-en-local)
   - [1.4. Publier l'application sur Docker Hub](https://github.com/nsaintgeours/demo/blob/master/README.md#14-publier-lapplication-sur-docker-hub)

- [2. Déployer notre application web sur AWS](https://github.com/nsaintgeours/demo/blob/master/README.md#2-d%C3%A9ployer-notre-application-web-sur-aws)

   - [2.1. Créer une instance EC2 (serveur virtuel) sur AWS](https://github.com/nsaintgeours/demo/blob/master/README.md#21-cr%C3%A9er-une-instance-ec2-serveur-virtuel-sur-aws)
   - [2.2. Me connecter à mon serveur virtuel EC2 chez AWS](https://github.com/nsaintgeours/demo/blob/master/README.md#22-me-connecter-%C3%A0-mon-serveur-virtuel-ec2-chez-aws)
   - [2.3. Configuration du pare-feu de mon serveur virtuel EC2](https://github.com/nsaintgeours/demo/blob/master/README.md#23-configuration-du-pare-feu-de-mon-serveur-virtuel-ec2)
   - [2.4. Installer Docker sur mon serveur virtuel EC2](https://github.com/nsaintgeours/demo/blob/master/README.md#24-installer-docker-sur-mon-serveur-virtuel-ec2)
   - [2.5. Déployer notre application sur le serveur virtuel EC2](https://github.com/nsaintgeours/demo/blob/master/README.md#25-d%C3%A9ployer-notre-application-sur-le-serveur-virtuel-ec2)
   - [2.6. Utiliser docker-compose pour faciliter le déploiement](https://github.com/nsaintgeours/demo/blob/master/README.md#26-utiliser-docker-compose-pour-faciliter-le-d%C3%A9ploiement)

- [3. Déploiement automatisé avec Github Actions](https://github.com/nsaintgeours/demo/blob/master/README.md#3-d%C3%A9ploiement-automatis%C3%A9-avec-github)

   - [3.1. Versionner le code source de notre projet avec Github](https://github.com/nsaintgeours/demo/blob/master/README.md#31-versionner-le-code-source-de-notre-projet-avec-github)
   - [3.2. Créer un accès SSH de Github vers le serveur AWS](https://github.com/nsaintgeours/demo/blob/master/README.md#32-cr%C3%A9er-un-acc%C3%A8s-ssh-de-github-vers-le-serveur-aws)
   - [3.3. Mettre en place un processus de déploiement avec Github Actions](https://github.com/nsaintgeours/demo/blob/master/README.md#33-mettre-en-place-un-processus-de-d%C3%A9ploiement-avec-github-actions)

- [4. Ajouter un modèle prédictif avec MLFlow](https://github.com/nsaintgeours/demo/blob/master/README.md#4-ajouter-un-mod%C3%A8le-pr%C3%A9dictif-avec-mlflow)

   - [4.1. Entraîner et sauvegarder un modèle prédictif avec MLflow](https://github.com/nsaintgeours/demo/blob/master/README.md#41-entra%C3%AEner-et-sauvegarder-un-mod%C3%A8le-pr%C3%A9dictif-avec-mlflow)
   - [4.2. Déploiement](https://github.com/nsaintgeours/demo/blob/master/README.md#42-d%C3%A9ploiement)

- [5. Bonus](https://github.com/nsaintgeours/demo/blob/master/README.md#5-bonus)

   - [5.1. Requêter l'API de prédiction en ligne de commande](https://github.com/nsaintgeours/demo/blob/master/README.md#51-requ%C3%AAter-lapi-de-pr%C3%A9diction-en-ligne-de-commande)
   - [5.2. Créer un accès SSH d'un serveur distant vers notre repository sur Github](https://github.com/nsaintgeours/demo/blob/master/README.md#52-cr%C3%A9er-un-acc%C3%A8s-ssh-dun-serveur-distant-vers-notre-repository-sur-github)


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

- une fois connectée au serveur EC2, installer Docker : 

```
[ec2-user@ip-172-31-41-247 ~]$ sudo yum update -y
[ec2-user@ip-172-31-41-247 ~]$ sudo amazon-linux-extras install docker
[ec2-user@ip-172-31-41-247 ~]$ sudo service docker start
[ec2-user@ip-172-31-41-247 ~]$ sudo usermod -a -G docker ec2-user
[ec2-user@ip-172-31-41-247 ~]$ logout
```


- nous aurons aussi besoin pour plus tardn d'installer Docker Compose, autant le faire dès maintenant : 

```
[ec2-user@ip-172-31-41-247 ~]$ wget https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) 
[ec2-user@ip-172-31-41-247 ~]$ sudo mv docker-compose-$(uname -s)-$(uname -m) /usr/local/bin/docker-compose
[ec2-user@ip-172-31-41-247 ~]$ sudo chmod -v +x /usr/local/bin/docker-compose
```


Ca y est c'est fait !

> 📝 Note : en cas de souci, [plus d'infos par ici](https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/).


**Vérification**

- se reconnecter au serveur virtuel EC2 : 

```
$ ssh -i ec2_admin.pem ec2-user@18.117.63.135
```

Vérifier que docker y est bien installé :

```
[ec2-user@ip-172-31-41-247 ~]$ docker --version
```


Vérifier que docker-compose y est bien installé :

```
[ec2-user@ip-172-31-41-247 ~]$ docker-compose --version
```



### 2.5 Déployer notre application sur le serveur virtuel EC2


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



### 2.6 Utiliser docker-compose pour faciliter le déploiement


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


## 3. Déploiement automatisé avec Github


### 3.1. Versionner le code source de notre projet avec Github

**Prérequis** 

- avoir installé Git sur mon PC, et savoir l'utiliser

**Etapes**

- se créer un compte personnel gratuit sur [Github](github.com) : le mien a pour nom  *[https://github.com/nsaintgeours](https://github.com/nsaintgeours)*

- sur mon compte Github, créer un nouveau repository : menu *Repositories / New*, l'appeler `demo`. On suit les options par défaut proposées par Github : on indique que le projet est privé, et on l'initialise avec un fichier `README` et un fichier `.gitignore`.

- sur mon compte Github, récupérer l'adresse du nouveau repository : aller sur la page principale du repository, puis bouton *Code*. L'adresse de mon repo est :  `git@github.com:nsaintgeours/demo.git`


- clé SSH pour Github **A PRECISER**

- On va maintenant synchroniser le projet Python qi existe déjà sur notre PC avec le nouveau repository que l'on vient de créer sur Github. Pour cela, dans *PyCharm* sur son PC, on ouvre un terminal `Git Bash`, on se place dans le dossier `C:\dev\demo` qui contient notre projet, et on le synchronise avec les commandes suivantes :  

```
C:\dev\demo> git init
C:\dev\demo> git remote add origin git@github.com:nsaintgeours/demo.git
C:\dev\demo> git fetch -a
C:\dev\demo> git pull origin master
```

- Il nous reste à pousser le code de notre PC vers le repository sur Github, sur une nouvelle branche que l'on nomme `bootstrap` :  

```
$ git branch bootstrap
$ git checkout bootstrap
$ git add src
$ git add requirements.txt
$ git add Dockerfile
$ git add docker-compose.yml
$ git commit -m "project bootstrap"
$ git push --set-upstream origin bootstrap
```

Et voilà ! 


### 3.2. Créer un accès SSH de Github vers le serveur AWS

Pour pouvoir déployer l'application chez AWS depuis Github (déploiement automatisé), il faut d'abord que Github soit autorisé à accéder au serveur virtuel EC2 chez AWS. Pour cela, il nous faut créer une paire de clés SSH : notre serveur virtuel EC2 aura une clé publique, tandis que notre compte Github aura la clé privée correspondant à cette clé publique. 

**Etapes :**

- se connecter au serveur virtuel EC2 chez AWS (cf. section 2.)
- créer une paire de clés SSH de type RSA, de loingueur 4096, avec pour nom *GithubActions*. On laisse les noms de fichiers par défaut, et on ne donne pas de passphrase :  

```
$ cd ~/.ssh
$ ssh-keygen -t rsa -b 4096 -C GithubActions

Generating public/private rsa key pair.
Enter file in which to save the key (/home/ec2-user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase):
Enter same passphrase again: 
```

- deux fichiers ont été créés dans le dossier `.ssh` : une clé publique `id_rsa.pub`, et une clé privée `id_rsa`
- il faut ajouter la clé publique nouvellement créée à la liste des clés publiques "autorisées" sur notre serveur virtuel EC2, qui sont stockées dans le fichier `authorized_keys` : 

```
ec2-user@ip-172-26-15-30:~/.ssh$ cat id_rsa.pub >> authorized_keys
```

- on télécharge ensuite le fichier contenant la **clé privée** `id_rsa` **sur notre PC avec WinSCP**


- on peut maintenant supprimer les deux fichiers contenant la clé publique et la clé privée de notre serveur virtuel EC2 : 

```
ec2-user@ip-172-26-15-30:~/.ssh$ rm id_rsa.pub
ec2-user@ip-172-26-15-30:~/.ssh$ rm id_rsa
```

- sur notre PC, ouvir le fichier `id_rsa` contenant la clé SSH privée (que l'on vient de télécharger) avec Notepad++

- dans Notepad++, copier le contenu du fichier `id_rsa` avec `Ctrl+A`

- ouvrir le repository `demo` sur notre compte Github, et aller dans le menu **[Setting / Secrets / Action secrets](https://github.com/nsaintgeours/demo/settings/secrets/actions)**

- cliquer sur le bouton **New repository secret**, et spécifier : 

		- *Name* : `AWS_EC2_SSH_KEY`
		- *Value* : copier ici le contenu de la clé SSH privée

Et voilà ! Notre repository Github peut désormais accèder en SSH à notre serveur virtuel EC2 chez AWS. 


### 3.3. Mettre en place un processus de déploiement avec Github Actions

Nous allons utiliser les fonctionnalités de **[Github Actions](https://github.com/nsaintgeours/demo/actions)** pour automatiser le déploiement de notre application sur le serveur virtuel EC2 chez AWS. Nous aurons à la fin un simple bouton dans GitHub qui nous permettra de déployer notre application dans le cloud à la demande. Le processus de déploiement automatisé exécutera les tâches suivantes :  

- construire l'image Docker de notre application à partir du `Dockerfile`
- pousser cette image Docker sur notre dépôt distant sur **DockerHub**
- se connecter en SSH au serveur virtuel EC2 chez AWS
- sur le serveur virtuel EC2, télécharger l'image Docker de notre application
- sur le serveur virtuel EC2, lancer notre application conténeurisée à partir du fichier `docker-compose.yml`


**Etapes**  

- notre processus de déploiement automatisé sur Github va avoir besoin de se connecter à notre compte sur DockerHub. Nous allons donc ajouter le mot de passe de notre compte DockerHub aux clés secrètes de notre repository Github. Pour cela, ouvrir le repository `demo` sur notre compte Github, et aller dans le menu **[Setting / Secrets / Action secrets](https://github.com/nsaintgeours/demo/settings/secrets/actions)**, cliquer sur le bouton **New repository secret**, et spécifier : 

		- *Name* : `DOCKER_PASSWORD`
		- *Value* : donner ici le mot de passe de mon compte DockerHub


- nous allons maintenant définir notre processus de déploiement automatisé en créant un nouveau fichier `/.github/workflows/deploy.yml` dans notre projet. On ne détaille pas comment ajouter ce fichier au code source du projet (création de branche, commit, pull request, etc.). Voici le contenu de ce fichier `deploy.yml` :

```
name: Deploy to production server

on:
  workflow_dispatch

env:
    APP_NAME: demo
    APP_VERSION: latest
    DOCKER_USER: nathaliesaintgeours
    DOCKER_PASSWORD: ${{secrets.DOCKER_PASSWORD}}
    SSH_HOST: 18.117.63.135
    SSH_USERNAME: ec2-user
    SSH_KEY: ${{ secrets.AWS_EC2_SSH_KEY }}

jobs:

   publish_docker:
     runs-on: ubuntu-latest

     steps:
     - uses: actions/checkout@v2

     - name: Build Docker container
       run: docker build -t $DOCKER_USER/$APP_NAME:$APP_VERSION .

     - name: Docker login
       run: docker login -u $DOCKER_USER -p $DOCKER_PASSWORD

     - name: Publish dockerized app on Docker Hub
       run: docker push $DOCKER_USER/$APP_NAME:$APP_VERSION

   deploy_production:
     runs-on: ubuntu-latest

     needs: publish_docker

     steps:
     - uses: actions/checkout@v2

     - name: Copy Docker Compose file to production server (through SSH)
       uses: appleboy/scp-action@master
       with:
         host: $SSH_HOST
         username: $SSH_USERNAME
         key: $SSH_KEY
         source: "docker-compose.yml"
         target: "~"

     - name: Run Docker containers on production server (through SSH)
       uses: appleboy/ssh-action@master
       with:
         host: $SSH_HOST
         username: $SSH_USERNAME
         key: $SSH_KEY
         script: |
           cd ~
           sudo service docker start           
           docker-compose down --rmi all
           docker-compose up -d
```

Prenons le temps de décortiquer un peu le contenu de ce fichier. On commence par dire comment sera déclenché notre processus de déploiement automatisé : 

```
on:
  workflow_dispatch
```

Ceci signifie que notre processus de déploiement sera déclenché manuellement. On pourrait aussi décider de le déclencher automatiquement à chaque merge dans master, ou bien à chaque tag, etc.


On définit ensuite plusieurs variables d'environnement qui seront utilisées par notre processus de déploiement :  

```
env:
    APP_NAME: demo
    APP_VERSION: latest
    DOCKER_USER: nathaliesaintgeours
    DOCKER_PASSWORD: ${{secrets.DOCKER_PASSWORD}}
    SSH_HOST: 18.117.63.135
    SSH_USERNAME: ec2-user
    SSH_KEY: ${{ secrets.AWS_EC2_SSH_KEY }}
```

Parmi ces variables d'environnement, deux sont récupérées depuis la liste des "secrets" de notre repository Github. Cela évite que les mots de passe soient renseignés en clair dans le code !



On définit ensuitee deux `jobs`, nommés `publish_docker` et `deploy_production`. Ces jobs seront **exécutés sur un serveur de Github** : 

- le job `publish_docker` comprend trois étapes : construction de l'image Docker de notre application, connexion à DockerHub, push de l'image sur DockerHub.
- le job `deploy_production` est un peu plus complexe. Il s'exécute une fois que le job `publish_docker` est terminé (`needs: publish_docker`). Il utilise les deux extensions `appleboy/scp-action@master` et `appleboy/ssh-action@master` pour se conneter à notre serveur virtuel EC2 depuis le serveur Github (via SSH), et y exécuter des commandes. Dans une première étape, il copie le fichier `docker-compose.yml` depuis notre code source vers le serveur virtuel EC2 chez AWS. Dans une seconde étape il lance l'application dockerisée sur notre serveur virtuel EC2 avec `docker-compose`, qui télécharge l'image Docker de notre application depuis le DockerHub puis lance le conteneur.


**Vérification**
 
Maintenant que notre processus de déploiement automatisé est défini (oce mergé dans la branche `master`), nous pouvons le lancer depuis notre repository Github. 
Aller dans le [menu *Actions*](https://github.com/nsaintgeours/demo/actions), sélectionner le workflow *Deploy to production server*, puis bouton *Run workflow*. C'est parti, l'application se déploie sur le serveur virtuel EC2 chez AWS ! On peut aller voir notre application **en ouvrant l'URL `18.117.63.135:8050` dans un navigateur web**.



> 📝 Note : attention, le déploiement ne fonctionnera que si notre serveur virtuel EC2 est allumé à ce moment là... On peut allumenr le serveur virtuel EC2 depuis la [console de gestion du service AWS EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances).



## 4. Ajouter un modèle prédictif avec MLFlow


### 4.1. Entraîner et sauvegarder un modèle prédictif avec MLflow

On commence par compléter notre code source Python pour venir entraîner et sauvegarder un simple modèle de régression linéaire. 
Nous allons pour cela utiliser les librairies `numpy`, `scikit-learn` et `mlflow`. On va entraîner notre modèle sur un jeu de données généré aléatoirement, c'est juste à titre d'illustration.

**Etapes**

* compléter le fichier `./requirements.txt` comme suit : 

```
dash
mlflow
numpy
scikit-learn
```

* dans *PyCharm*, ouvrir un terminal puis installer les librairies dans l'environnement `conda` associé au projet : 

```
C:\dev\demo> conda activate demo
C:\dev\demo (demo)> pip install -r requirements.txt
```

* créer un nouveau script Python `C:/dev/demo/scripts/train_model.py` avec le contenu suivant :  

```
import mlflow
import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(
    X=np.random.rand(1000, 3),
    y=np.random.rand(1000, 1)
)
mlflow.sklearn.save_model(sk_model=model, path='../mlflow_model')

```

* exécuter le script (bouton *Run* dans *PyCharm*) : un nouveau dossier `mlflow_model` est créé à la racine du projet, il contient le modèle de régression linéaire entraîné, sauvegardé au format MLflow.

* pousser ces modifications sur votre repository GitHub

### 4.2. Déploiement

Nous allons maintenant déployer notre modèle prédictif sur notre serveur virtuel EC2, sous la forme d'une API qui recevra en entrée les valeurs de `x1`, `x2`, `x3` (i.e., les trois entrées du modèle) renverra la valeur `y` prédite par le modèle. Les étapes que l'on va suivre sont les suivantes : 
* ajouter une étape dans le processus de déploiement avec **Github Actions**
* compléter notre fichier `docker-compose.yml` 
* configurer le pare-feu de notre serveur virtuel EC2 
* déployer enfin notre application complète sur le serveur virtuel EC2

**4.2.1. Compléter le workflow de déploiement avec Github Actions**

Nous allons ajouter un `job` nommé `publish_mlflow_model` dans le processus de déploiement automatisé sur **Github Actions**. Ce nouveau job va exécuter les tâches suivantes :    

* construction d'une image Docker pour notre modèle de régression en utilisant les fonctionnalités de déploiement de la librairie `MLflow`
* publication de cette image Docker sur DockerHub

*Etapes*

- Voici la section à ajouter au fichier `./.github/workflows/deploy.yml` pour définir ce nouveau job : 

```
(...)

	publish_mlflow_model:
	     runs-on: ubuntu-latest

	     steps:
	     - uses: actions/checkout@v2

	     - name: Set up Python 3.9
	       uses: actions/setup-python@v2
	       with:
		 python-version: 3.9

	     - name: Install mlflow
	       run: |
		 python -m pip install --upgrade pip
		 pip install mlflow

	     - name: Build Docker container from MLflow model
	       run: |
		 mlflow models build-docker -m  ${GITHUB_WORKSPACE}/mlflow_model -n "$MODEL_NAME"

	     - name: Docker login
	       run: |
		 docker login -u $DOCKER_USER -p $DOCKER_PASSWORD

	     - name: Publish dockerized model on Docker Hub
	       run: |
		 docker tag $MODEL_NAME $DOCKER_USER/$MODEL_NAME:$MODEL_VERSION
		 docker push $DOCKER_USER/$MODEL_NAME:$MODEL_VERSION

(...)
```

- ce nouveau job utilise deux variables d'environnement `MODEL_NAME` et `MODEL_VERSION` qui spécifient le nom du conteneur Docker construit à partir du modèle de régression, et sa version. On doit donc ajouter ces deux nouvelles variables d'environnement dans la section `env` du fichier `./.github/workflows/deploy.yml` que l'on complète ainsi :

```
env:
    (...)
    
    MODEL_NAME: demo_mlflow_model
    MODEL_VERSION: latest

    (...)
 ```

- enfin, on doit préciser que le job déjà existant `deploy_production` doit maintenant attendre que les deux jobs `publis_docker` et `publish_mlflow_model` soient terminés avant de se lancer. On édite donc la description du job comme suit : 

```
   deploy_production:
     runs-on: ubuntu-latest

     needs: [publish_docker, publish_mlflow_model]
```
 
Et voilà, notre workflow de déploiement automatisé est prêt !


> 📝 Note : je n'ai malheureusement pas pu tester ce workflow de déploiement de manière manuelle, que ce soit sur mon PC ou sur le serveur virtuel EC2 chez AWS. En effet, la construction de l'image Docker du modèle de régression avec la commande `mlflow models build-docker` m'a posé quelques soucis... Sur mon PC, cette commande plante, visiblement à cause de problèmes de compatibilité entre Docker et Windows, je ne suis pas allée plus loin dans la résolution du problème. Sur le serveur virtuel EC2 d'AWS, le problème est différent : je n'ai pas les droits suffisants sur ce serveur pour installer `mlflow` sans galérer. Le gestionnaire de paquet `pip` n'est pas présent par défaut pour le serveur, et je ne suis pas parvenue à l'installer correctement. J'ai laissé tomber ! Donc la commande de construction de l'image Docker du modèle de régression avec `mlflow` ne fonctionne que sur les serveurs Linux de Github.


**4.2.2 Définir un nouveau service avec `docker-compose`**

Nous allons maintenant éditer le fichier `./docker-compose.yml`, pour indiquer que notre application a désormais besoin de deux conteneurs Docker pour fonctionner : un premier conteneur Docker nommé `demo_dashboard` pour l'application Dash, et un second conteneur nommé `demo_model` pour notre modèle de régression. Ces deux conteneurs seront lancés à partir des deux images Docker qui auront été publiées sur DockerHub par notre workflow de déploiement automatisé (voir étape précédente 4.2.2). A chacun de ces deux conteneurs correspond un *service*, nommés respectivement `dashboard` et `model`. 

Le conteneur `demo_model` qui sera lancé avec notre modèle de régression exposera son API sur le **port `8080`** : c'est le port utilisé par défaut par `mlflow`. La redirection de port `8080:8080` fait le choix de conserver ce port par défaut et de ne pas le rediriger sur un autre port. 

Enfin, nous allons avoir besoin de **faire communiquer nos deux services `dashboard` et `model` ensemble** ! En effet, nous souhaitons pouvoir appeler notre modèle de régression depuis l'application Dash. Pour cela, nous faisons passer à notre service `dashboard`, et à son conteneur Docker `demo_dashboard`, une nouvelle variable d'environnement que l'on nomme `MODEL_API`, avec pour valeur `http://model:8080/invocations`. L'adresse `http://model:8080` signifie qu'il faut contacter le conteneur Docker associé au service nommé `model` dans `docker-compose.yml`, sur le port `8080`. L'ajout du endpoint `invocations` permet d'accéder au endpoint de prédiction de notre modèle de régression (voir aide en ligne de `mlflow`).

Voici donc notre nouvelle version du fichier `docker-compose.yml` : 

```
version: "3.7"

services:

  dashboard:
    image: nathaliesaintgeours/demo:${APP_VERSION}
    container_name: demo_dashboard
    ports:
      - "8050:8050"
    environment:
      - TARGET=LIVE
      - MODEL_API=http://model:8080/invocations
    restart: unless-stopped

  model:
    image: nathaliesaintgeours/demo_mlflow_model:${MODEL_VERSION}
    container_name: demo_model
    ports:
        - "8080:8080"
    restart: unless-stopped
```

> 📝 Note : dans un fichier `docker-compose.yml`, il faut veiller à ce que les différents services communiquent sur des ports différents, sinon ça crée des interférences.


**4.2.3. Configuration du pare-feu de l'instance EC2 chez AWS**

L'API de prédiction créée par le conteneur `demo_model` va utiliser le port `8080` pour afficher son contenu (j'aurais pu choisir un autre port si je l'avais souhaité, en définissant une redirection de ports dans le fichier `docker-compose.yml`). Je dois donc ouvrir ce port `8080` sur mon serveur virtuel EC2. 
Cela se fait sur mon compte AWS, dans la [page de gestion des "Groupes de sécurité"](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#SecurityGroup:securityGroupId=sg-0f0503eaebf726097). Il faut redémarrer le serveur virtuel EC2 pour que la modification soit bien prise en compte. 


> 📝 Note : l'ouverture du port `8080` vers l'extérieur n'est en fait nécessaire que si je veux accéder à l'API de prédiction directement depuis l'extérieur de mon serveur virtuel EC2, sans passer par mon application Dash, par exemple depuis mon PC. Je n'ai pas besoin d'ouvrir ce port vers l'extérieur pour que mes deux services `dashboard` et `model` définis dans le fichier `docker-compose.yml` puissent communiquer, car ils se trouvent tous les deux sur mon serveur virtuel EC2. 

**4.2.4. Requêter l'API de prédiction via l'application Dash**

Nous allons maintenant compléter le code notre application web, afin de permettre à l'utilisateur de :
* saisir les valeurs des trois entrées du modèle `x1`, `x2` et `x3`
* lancer le modèle de régression avec ces trois valeurs d'entrées, en requêtant l'API exposée par notre service `model` sur le port `8080`
* afficher le résultat `y` fourni par le modèle de régression

Je passe le détail des modifications faites au code, on peut aller voir directement [le dossier ./src/ du projet](https://github.com/nsaintgeours/demo/tree/master/src) pour voir comment ces différentes fonctionnalités ont été implémentées.

Je fais seulement un zoom sur la manière dont on requête en Python l'API de prédiction exposée par notre service `model` sur le port `8080` . Cette requête est faite par la fonction `predict()` définie dans le fichier [`mlflow_model_client.py`](https://github.com/nsaintgeours/demo/blob/master/src/mlflow_model_client.py) : 

```
"""
Function that sends a request to the MLflow model REST API to get a prediction from some input data.
"""
import os
from typing import List

import requests


def predict(x: List[float]) -> float or str:
    try:
        response = requests.post(
            url=os.getenv("MODEL_API"),
            headers={'content-type': 'application/json'},
            json={"data": [x]},
        )
        response.raise_for_status()
        output = str(response.json()[0])
    except (requests.HTTPError, IOError) as err:
        output = str(err)
    return output
```

On utilise la librairie `requests` pour requêter l'API de prédiction. L'URL de l'API est donnée par la variable d'environnement `MODEL_API`, dont la valeur a été définie dans le fichier `docker-compose.yml`, et passée au conteneur `demo_dashboard` lors de son lancement.


**4.2.5. Déployer l'application sur le serveur virtuel EC2**

Ca y est, nous sommes prêts !

Une fois toutes les modifications commitées et mergées sur la branche `master` du repository `demo` de notre compte Github, nous pouvons enfin déployer notre application complète sur le serveur virtuel EC2 chez AWS. 

Pour cela : 

* si cela n'est pas déjà fait, allumer le serveur virtuel EC2 chez AWS : cela se fait via la [console de gestion du service AWS EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances).

* ouvrir un navigateur web et aller sur son compte **GitHub**, sur le [repository `demo`](https://github.com/nsaintgeours/demo/tree/master/src)

* ouvrir l'onglet **Actions**

* sélectionner le workflow *Deploy to production server*, puis cliquer sur le bouton *Run workflow*

C'est parti ! Au bout de quelques (dizaines) de minutes, votre application est déployée sur le serveur EC2 chez AWS. 

Pour vérifier que ça marche,  on peut aller voir notre application **en ouvrant l'URL `18.117.63.135:8050` dans un navigateur web**.


## 5. Bonus

### 5.1. Requêter l'API de prédiction en ligne de commande


On peut utiliser la commande `curl` dans un terminal `bash` pour requêter l'API de prédiction exposée par notre conteneur Doker `demo_model` sur le port `8080`.
Pour cela : 

```
curl 18.117.63.135:8080/invocations -H 'Content-Type: application/json' -d '{ "data": [[1, 2, 3]]}'
```

On doit recevoir une valeur numérique en réponse. 

Si on veut requêter l'API en étant déjà connecté sur le serveur virtuel EC2, on peut utiliser l'adresse `0.0.0.0:8080` au lieu de `18.117.63.135:8080`.

### 5.2. Créer un accès SSH d'un serveur distant vers notre repository sur Github

Pour déployer notre application sur le serveur virtuel EC2 d'AWS, nous avons fait le choix de passer par des images Docker publiées sur DockerHub. Ces images sont construites sur un serveur de Github lors de l'exécution du workflow de déploiement automatisé, elles sont poussées sur DockerHub, puis elles sont téléchargées depuis le serveur virtuel EC2. 

Il existait une autre option, que nous n'avons pas mise en oeuvre : on aurait pu choisir de synchroniser le code source de notre application sur le serveur virtuel EC2, puis de construire les images Docker directement sur le serveur virtuel EC2, et enfin de lancer nos conteneurs. Nous n'aurions alors pas eu à push/pull les images Docker sur DockerHub.

Pour mettre en oeuvre cette option, il faut que le serveur virtuel EC2 puisse accéder au repository Github qui contient le code source de notre application. **Il faut donc que notre serveur virtuel EC2 puisse accéder en SSH à notre dépôt Github**. Pour ce faire, on suit les étapes décrites ci-dessous. 

**Création des clés SSH**

* se connecter au serveur EC2 chez AWS (par exemple en SSH depuis un terminal `bash` sur mon PC)
* créer une paire de clés SSH, en nommant les fichiers `demo_deploy_key`, et en ne donnant pas de passphrase : 

```
ec2-user@ip-172-26-15-30:~$ cd /home/ec2-user/.ssh
ec2-user@ip-172-26-15-30:~/.ssh$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ec2-user/.ssh/id_rsa): demo_deploy_key
Enter passphrase (empty for no passphrase):
Enter same passphrase again: 
```

* deux fichiers ont été créés dans le dossier `.ssh` : une clé publique `demo_deploy_key.pub`, et une clé privée `demo_deploy_key`

**Enregistrement de la clé privée sur le serveur AWS**

* on va ajouter un nouvel hôte distant dans la configuration SSH de notre serveur virtuel EC2, en indiquant que l'on accédera à cet hôte distant en utilisant la clé privée nouvellement créée. Pour cela, on ajoute les lignes suivantes dans le fichier `/home/ec2-user/.ssh/config` : 

```
Host github.com-demo
    Hostname github.com
    IdentityFile=/home/ec2-user/.ssh/demo_deploy_key
```

> 📝 Si le fichier `/home/ec2-user/.ssh/config` n'existe pas, il faut d'abord le créer. Pour créer / éditer ce fichier, on peut soit passer par un éditeur de code dans la console bash (mais je sais pas les utiliser), soit créer / éditer le fichier en local sur son PC, puis le copier sur le serveur AWS en utilisant un logiciel comme WinSCP. 

**Enregistrement de la clé publique sur notre compte Github**

* en utilisant un logiciel comme [WinSCP](https://winscp.net/eng/download.php) ou la ligne de commande, copier la clé **publique**  `demo_deploy_key.pub` depuis le serveur virtuel EC2 vers votre PC.
* une fois sur votre PC, ouvrir le fichier  `demo_deploy_key.pub` avec **Notepad++**
* ouvrir le dépôt du projet sur notre compte Github
* dans Github, aller dans le menu **Setting / Deploy keys**
* cliquer sur le bouton **Add deploy key**, et spécifier : 
   
  - *Title* : `DEPLOY_TO_EC2`
  - *Key* : copier ici le contenu de la clé SSH publique

**Synchronisation du code source sdu projet ur le serveur EC2**

Enfin, je dois définir un dépot git en local sur mon serveur virtuel EC2 et le lier à mon déppot sur Github. 
Pour cela, je me place dans le dossier `/home/ec2-user/demo` (à créer s'il n'existe pas), puis :  

```
ec2-user@ip-172-26-15-30:~$ cd /home/ec2-user/demo
ec2-user@ip-172-26-15-30:~$ git init
ec2-user@ip-172-26-15-30:~$ git remote set-url origin git@github.com-demo:nsaintgeours/demo.git
```

Et voilà ! Notre serveur virtuel EC2 peut désormais synchroniser le code source de notre application depuis notre dépôt Github. 






