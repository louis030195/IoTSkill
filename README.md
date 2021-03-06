# IoTSkill

## Objectif

L'objectif est d'optimiser les temps d'attentes et la durée des trajets tout en réduisant la pollution émise par le traffic.

Pour cela nous mettons un arrêt de bus connecté.

![connected_bus_stop](Images/connected_bus_stop.png)

## Software-defined product

![SDP](Images/SDP.png)

### 1. Utilisation de plusieurs capteurs, idéalement déjà présent sur la carte

- Caméra dans les arrêts de bus

![object_detection](Images/object_detection.png)

### 2. Actuateur

- Bip cartes

### 3. Une logique business d'exploitation des données

Les clients bip à l'arrêt, dans le bus et à la sortie.
Cela nous permettra de déterminer le temps d'attente et la durée du trajet.
Nous promouvoyons un temps d'attente plus faible, avec des horaires plus adaptés aux utilisateurs ce qui permet d'avoir plus d'utilisateurs, moins de traffic, moins de pollution et donc nous pouvons nous engager sur un temps de trajet moyen, ce qui attirera plus d'utilisateurs ... = cercle vertueux.

![Cercle vertueux](Images/IoT.png)

L'objectif ultime en terme de business model serait de proposer une carte qui fonctionne de tel manière : l'utilisateur n'aurait pas à payer si le temps de trajet n'est pas respecté. Il s'agit d'un business model basé sur l'engagement.

### 4. Une logique d'analyse d'impact pour mesurer l'impact

- Fluctuation des statistiques avant - après

### Idées

- Transport "volant" cela permet de pallier aux besoins ponctuels lors d'évenements (festivals, concerts ...) rapportés par les capteurs qui détectent des changements de comportement.
- Pour les données externe possibilité de parser des médias (automatiquement biensur) pour voir quand un évenement arrive / API qui prévient d'évenement ? (pour les transports volant)

### Proof of concept

Le POC a été réalisé en utilisant du matériel déjà possédé par les acteurs du projet, c'est-à-dire:
- GOPRO Hero 4
- Raspberry PI 3

#### Installation

```
pip install -r requirements.txt
```