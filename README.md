# Risk Intelligence Dashboard

## 🛡️ Qu’est-ce que c’est ?

**Risk Intelligence Dashboard** est un outil interactif permettant aux banques et institutions financières de **prévoir le risque de défaut de paiement d’un client**.  

Grâce à une interface claire et des graphiques visuels, les décideurs peuvent rapidement comprendre le **niveau de risque** et prendre des décisions éclairées pour l’octroi de crédits.

---

## 🎯 Objectifs du projet

1. **Réduire le risque financier** : anticiper les clients susceptibles de ne pas rembourser.  
2. **Faciliter la prise de décision** : interface intuitive avec visualisations simples.  
3. **Automatiser l’évaluation de risque** : transformer des données brutes en score clair et actionnable.  

---

## 🧩 Fonctionnalités

- Formulaire pour entrer les informations client :  
  - Limite de crédit, âge, sexe, statut marital.  
  - Historique de paiements : retards, montant de facture, dernier paiement.  
- Prédiction du **risque de défaut** à l’aide d’un **modèle Random Forest**.  
- Visualisation du score sous forme de **jauge interactive** avec couleur selon le niveau de risque.  
- Recommandations automatiques :  
  - **Risque faible** → approbation recommandée  
  - **Risque moyen** → dossier à surveiller  
  - **Risque élevé** → attention, garanties supplémentaires nécessaires  

---

## 🧠 Choix techniques

- **Langage :** Python  
- **Interface :** Streamlit (dashboard web interactif)  
- **Graphiques :** Plotly (jauge interactive, KPI visuels)  
- **Gestion de données :** Pandas  
- **Modèle prédictif :** Random Forest  
  - Robuste face aux erreurs ou valeurs manquantes  
  - Combinaison de plusieurs “arbres de décision” pour une prédiction fiable  
- **Optimisation :** Cache pour accélérer le chargement du modèle  

---

 Choix de design

Interface moderne et épurée avec cartes et en-tête stylisé.

KPI visuels pour résumer les informations importantes.

Couleurs intuitives pour signaler le niveau de risque : vert = faible, orange = moyen, rouge = élevé.

Disposition en colonnes pour afficher formulaire et résultats côte à côte.

 Remarques importantes

Le modèle peut être volumineux (>25 MB), il peut être stocké séparément ou téléchargé dynamiquement.

L’application est conçue pour être responsive et interactive, offrant une expérience proche d’un produit professionnel.

 Auteur

Ake Mobio Ivan Junior

Email : akeivanjr10@gmail.com


