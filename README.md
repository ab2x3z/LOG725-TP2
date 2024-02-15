# Moon Tank (Base)
ÉTS, LOG725, TP2. 
Par Gabriel C. Ullmann, 2024.

## Dépot Github
- https://github.com/ab2x3z/LOG725-TP2.git

## Instructions
- Installez pygame : `pip install pygame`
- Exécutez le jeu : `python main.py`

## Description
- Le joueur peut démarer le jeu en appuyant sur start. Il peut contrôler le tank à l'aide des touche "wasd". J'ai opter pour un différent systeme de munition. Le joueur peut appuyer sur "q" pour changer la munition active (indiqué par l'indicateur en haut à gauche), puis il peut appuyer sur la barre d'espace pour tirer. Le joueur doit sortir du niveau en completant le puzzle, pour ce faire, le joueur doit trouver le bon chemin en utilisant une quandtité limité de balles. Une fois que le joueur sort du niveau (en bas à droite), il est récompensé par un écran de victoire. Il peut alors quitter le jeu en appuyant sur n'importe quelle touche. Je n'ai pas implémenter la fonction reset par manque de temps, le joueur doit alors quitter et relancer le jeu lorsque celui-ci est coincé par manque de balle. Pour la même raison, je n'ai pas implémenter la fonction pour reprendre des balles placer dans le niveau. Finalement, je n'ai aussi pas implémenter d'option pour enlever les sons, le joueurs devras les écouter qu'il le veuille ou non!

## Fonctionnalités déjà implémentées
- 3 entités (Player, Wall et Bullet)
- Chargement des sprites pour les entités
- Collision
- Mouvement
- Tire de bullets
- Système de changement de bullets
- Destruction des murs de même couleur que la balle
- nombre limité de balle
- 3 type de balle différentes
- SFX et background music
- Menu principal avec fonction start et quit

## Sprites
- Tank: https://www.pngkey.com/download/u2q8a9w7t4u2e6r5_tanks-2d-top-down-tank/
- Les autres sprites sont par Gabriel C. Ullmann, 2017

## Sounds and musics
- menuBackground.mp3 : Mii Channel (Plaza)
- mainBackground.mp3 : Theme of Samus Aran, Space Warrior
- shoot.wav : Super Smash Bros. Ultimate, Bowser Jr. special 2
- destroy.wav : Super Smash Bros. Ultimate, Bowser Jr. special 3
- excellent.wav : Super Smash Bros. Ultimate, Announcer
- nailedit.wav : Super Smash Bros. Ultimate, Announcer
- waytogo.wav : Super Smash Bros. Ultimate, Announcer
- congratulation.wav : Super Smash Bros. Ultimate, Announce