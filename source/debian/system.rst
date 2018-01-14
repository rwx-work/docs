Installation d’une distribution GNU/Linux Debian

---

TODO etc/motd

```
```

# Décisions

1. ## disposer de miroirs à jour

    TODO

* ## choisir les paquets indispensables

    paquets proposés pour pouvoir travailler correctement

    |||
    |||
    | locales         | générer des locales binaires pour les messages
    | apt-utils       | sinon la configuration des paquets est repoussée
    | dialog          | sans quoi APT remonte des messages d’alerte

* ## décider du type de système souhaité

    * le système sera-t-il architecturé
        * en 64 bits ?
        * en 32 bits ?
        * les 2 ?!
    * le système sera-t-il exécuté
        * sur une machine physique ?
        * dans une machine virtuelle ?
        * dans un conteneur ?
        * dans un conteneur dans une machine virtuelle ?
    * le système sera-t-il utilisé
        * en écriture, sur un support de stockage ?
        * en lecture, chargé en mémoire au démarrage ?

# Installer les outils nécessaires

|||
|||
| debootstrap    | générer un système de fichiers de base minimal
| squashfs-tools | compresser ou décompresser une image de système

```bash
apt-get install "debootstrap squashfs-tools"
```

# Créer une arborescence de base

## préparer le chroot

* devenir root
* créer un répertoire, et s’y positionner

```bash
su
```
```bash
mkdir -p "chemin"
cd "chemin"
```

## générer le système de fichiers

```bash
debootstrap \
--arch="amd64" \
--include="locales,apt-utils,dialog" \
--variant="minbase" \
"stretch" \
. \
"miroir"
```

# Configurer les paquets préinstallés

## définir les claviers par défaut

* /etc/default/keyboard

```bash
XKBMODEL="pc105"
XKBLAYOUT="fr,fr"
XKBVARIANT="oss,bepo"
XKBOPTIONS=""
BACKSPACE="guess"
```

## définir les locales à générer

* etc/default/locale

```
LANG=en_US.UTF-8
LANGUAGE=en_US
LC_CTYPE="fr_FR.UTF-8"
LC_NUMERIC="fr_FR.UTF-8"
LC_TIME="fr_FR.UTF-8"
LC_COLLATE="fr_FR.UTF-8"
LC_MONETARY="fr_FR.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="fr_FR.UTF-8"
LC_NAME="fr_FR.UTF-8"
LC_ADDRESS="fr_FR.UTF-8"
LC_TELEPHONE="fr_FR.UTF-8"
LC_MEASUREMENT="fr_FR.UTF-8"
LC_IDENTIFICATION="fr_FR.UTF-8"
```

* etc/locale.gen

```
en_US.UTF-8 UTF-8
fr_FR.UTF-8 UTF-8
```

## [configurer l’interpréteur de commandes](../bash/index.md)

## [configurer le gestionnaire de paquets](../apt/index.md)

## redéfinir le nom d’hôte

```bash
echo "hostname" > "etc/hostname"
```

## renseigner les volumes connus

* etc/fstab

Volume temporaire en RAM

```
tmpfs /tmp tmpfs auto,mode=1777 0 0
```

# Installation

## changer de contexte

```bash
mount --bind /proc proc
mount --bind /sys sys
chroot .
```
TODO ? /dev

## générer les locales

```bash
locale-gen
```

## définir le mot de passe root

```bash
passwd
```

## utilisateur, invité, sudo

```bash
apt-get install sudo

useradd -s /bin/bash user
mkdir /home/user
chown user: /home/user
adduser user sudo

useradd -s /bin/bash guest
chown guest: /home/guest
```

## authentifications : mots de passe, clés SSH

TODO

## mettre le système à jour

* dans tous les cas :

```bash
apt-get update
apt-get upgrade
```

* si besoin, car des paquets rétroportés modifient la distribution :

```bash
apt-get dist-upgrade
```

## appliquer le type de système choisi

|||
|||
| linux-image-amd64 | s’il ne s’agit pas d’un conteneur
| live-boot         | si à destination de boot live
| systemd-sysv      | sans quoi le système ne démarrera pas complètement

```bash
apt-get install -t stretch-backports "linux-image-amd64"
apt-get install "live-boot"
```

---

## définir les paramètres d’initialisation
```bash
apt-get install -t stretch-backports "systemd-sysv"
```


* etc/sysctl.conf

Espace mémoire maximum allouable (à augmenter si hébergement de conteneurs)  
Pourcentage de RAM disponible avant utilisation de la partition d’échange  

```ini
vm.max_map_count=1048576
vm.swappiness=0
```

## pour s’en tenir au strict nécessaire

```bash
apt-get install --no-install-recommends …
```

## installer des paquets utiles

```bash
apt-get install \
bash-completion \
lxc \
less nano vim \
pciutils usbutils \
python3 \
squashfs-tools \
```

```bash
apt-get install -t "stretch-backports" \
debootstrap \
```

## installer des paquets au choix

[Choix de paquets commentés](packages.md)

```bash
apt-get install "package1" …
apt-get install -t stretch-backports "package1" …
```

## sortir correctement du contexte

* vider le cache d’APT

```bash
apt-get clean
```

* s’extraire de l’environnement

```bash
exit
```

* démonter les liens au système hôte

```bash
umount sys
umount proc
```

## épurer l’historique des commandes

* root/.bash_history

# Configurer les paquets installés

# Archiver le système de fichiers

```bash
mksquashfs . "../name.squashfs" -comp "xz"
```
