# **Projet Statapp** : Les entreprises françaises et leurs valeurs – analyse de millions d’offre d’emploi 

## **Introduction**  
Dans ce projet, nous analysons les valeurs des entreprises françaises à travers 17 millions d’offres d’emploi regroupées dans une BDD dont une partie est disponible sur ce dépôt Git ([Lien_du_dépôt](https://github.com/philipython/statapp)). 

Ici, les **valeurs** désignent les principes et qualités recherchés et promus par les employeurs, et seront regroupés en **catégories**. 

Notre étude (réalisée et détaillée dans le fichier [main.py](https://github.com/philipython/statapp/blob/main/main.ipynb)) repose sur une analyse textuelle et statistique de cette BDD (**NLP** : tokenization, TF-IDF, word embeddings ...
**Classification** : utilisation de modèles, supervisés ou non).

## Table des matières
1. [I. Une approche naïve](#i-une-approche-naïve)
2. [II. Utilisation d'un modèle non supervisé](#ii-utilisation-dun-modèle-non-supervisé)
3. [III. Modèles de classification supervisés](#iii-modèles-de-classification-supervisés)
4. [IV. Analyse des résultats et exploration des données supplémentaires](#iv-analyse-des-résultats-et-exploration-des-données-supplémentaires)
5. [Conclusion](#conclusion)

## **I. Une approche naïve** 

Dans cette première approche, nous adoptons une méthode simple et pragmatique pour analyser les valeurs des entreprises. Nous commençons par établir **arbitrairement des catégories de valeurs** (par exemple, "Innovation", "Responsabilité", "Travail d’équipe") en essayant de les choisir aussi disjointes que possible. Ces catégories seront ajustées au fur et à mesure si les résultats montrent que certaines ne conviennent pas ou ne sont pas suffisamment discriminantes ou pertinentes.

Une fois les catégories définies, nous procédons à un prétraitement des données textuelles : les offres sont d'abord **lématisées**, ensuite, nous appliquons une vectorisation à l'aide du **TF** (Term Frequency) puis du **TF-IDF** (Term Frequency-Inverse Document Frequency), en identifiant des **mots-clés spécifiques à chaque catégorie** afin d'observer l'**occurence** de ces mots dans les offres et ainsi les **classifier** avec les résultat obtenu.

Cette approche, bien que rudimentaire, nous permet de disposer d'une première segmentation des offres, en attendant de valider ou ajuster nos catégories et méthodes avec des techniques plus sophistiquées.

## **II. Utilisation d'un modèle non supervisé**  

Après l'approche naïve, nous appliquons un modèle **non supervisé** afin d'extraire automatiquement des structures dans les données sans définir de catégories a priori, ce qui est très pertinent puisqu'un bon choix de catégories est essentiel et difficile de manière arbitraire a priori, cette étape nous aide donc à aviser sur ces choix avec les données (établir des clusters regroupant celles qui "auraient une sémantique similaire").

Nous utilisons des méthodes de **clustering** : **K-means with Elbow Method** ici, pour regrouper les offres d'emploi en fonction de leurs similarités textuelles. Pour cela, nous représentons les offres sous forme de vecteurs (à 768 dimensions) à l'aide de **CamemBERT-base embeddings**, permettant ainsi de capturer le contexte sémantique dans les offres et lregroupons ces vecteurs dans des clusters.

L'objectif est d'**identifier des groupes d'offres partageant des valeurs similaires, sans imposer de catégories prédéfinies**. Une analyse des clusters obtenus (en lisant quelques offres de chacun des clusters ou en les donnant à un LLM compétent) nous permet ensuite d'**interpréter les résultats** (en faisant avec ces clusters des catégories) afin d'affiner la classification choisie arbitraiement dans la première partie, à partir de ces résultats.

## **III. Modèles de classification supervisés**

Une fois les **données en partie préclassifiées**, nous explorons l’utilisation de modèles de **classification supervisée** pour **prédire** les valeurs des entreprises à partir de leurs offres d'emploi.

### **Méthode**

Nous commençons par étiqueter un sous-ensemble des offres d'emploi en fonction des catégories de valeurs définies dans l'approche naïve puis affinées. Nous devons donc le faire la main et/ou à l'aide d'LLM compétents, cette tâche étant longue et difficile dans le cadre du sujet (beaucoup d'ambiguïtés dans le choix d'offres moins détaillées, offres parfois longues au contraire...). Ces étiquettes servent à entraîner les modèles, qui étiquetterons donc à leur tour.

Les modèles que nous utilisons incluent :  
- **Régression logistique** : simple et efficace, utile pour ce problème de classification multiclasse de petit dataset.  
- **Random Forests** : robuste et capable de gérer des relations complexes dans les données.
- **XGBoost** : algorithme de boosting, performant pour capturer des interactions complexes et efficace même sur des ensembles de données de petite taille.
- **SVM (Support Vector Machine)** : performant pour des classifications non linéaires même sur des petits dataset.  
- **Pas de réseaux de neurones** : manque de données labelisées malgrès la grande taille du dataset.

### **Entraînement et évaluation**

Nous divisons les données en un ensemble d’entraînement et un ensemble de test pour évaluer la performance des modèles. Les critères de performance incluent la **précision**, le **rappel**, et la **F-mesure** pour mesurer la qualité de la classification.

Cette approche supervisée permet d'améliorer la précision de la catégorisation des offres d'emploi (par rapport aux deux premières approches), en utilisant les informations contextuelles fournies par des modèles comme **CamemBERT-base **.

## **IV. Analyse des résultats et exploration des données supplémentaires**

Une fois que les offres ont été classifiées avec nos modèles supervisés, nous passons à l'analyse des résultats et à l'exploration des autres informations disponibles, telles que le **salaire**, la **localisation**, et le **secteur d'activité**.

### **Exploration des données supplémentaires**

Nous analysons ensuite les autres données associées aux offres d'emploi, telles que :  
- **Salaire** : Existe-t-il une corrélation entre les valeurs d'une entreprise (par exemple, "Responsabilité" ou "Innovation") et les niveaux de salaire proposés ?
- **Localisation** : Certaines régions ou villes sont-elles plus propices à certaines valeurs d'entreprise ?  
- **Secteur d'activité** : Le secteur (par exemple, "Technologie" ou "Santé") influence-t-il les valeurs mises en avant dans les offres ?

Cette analyse nous permet de mieux comprendre les tendances et de tirer des conclusions sur la manière dont les entreprises intègrent certaines valeurs dans leurs offres d'emploi, tout en tenant compte des autres facteurs influents comme la rémunération, la localisation géographique et le secteur d'activité.

## **Conclusion**

Ce projet nous a permis de mettre en place une analyse approfondie des valeurs recherchées et promues par les entreprises francaises dans leurs offres d'emploi. En combinant des approches naïves et plus avancées, telles que l’utilisation de modèles non supervisés (comme K-means with Elbow Method) et supervisés, nous avons pu classifier et analyser les entreprises en fonction de plusieurs critères.

L'exploration des données supplémentaires, telles que [mettre des trucs] , a enrichi notre compréhension des tendances et des facteurs influençant les valeurs des entreprises. 

Plusieurs pistes d'amélioration existent, notamment en affinant la classification avec des modèles plus sophistiqués, en ajustant toujours plus les catégories de valeurs ou en intégrant des données externes pour renforcer nos analyses. 

Ce travail ouvre la voie à une analyse encore plus fine des dynamiques entre les valeurs des entreprises et les différents facteurs économiques et sociaux, et peut servir de base pour de futures études plus détaillées dans le domaine des ressources humaines et de l'économie du travail.
