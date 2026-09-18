# Publier un article sur art-impact.org

## Le principe

Un article = **un fichier Markdown** dans le dossier `contenu/`.
`python build.py` génère automatiquement :

- la page de l'article (`publications/<nom-du-fichier>.html`)
- sa fiche dans l'index (`publications.html`)
- son entrée dans le flux RSS (`flux.xml`) et le `sitemap.xml`
- ses données structurées `Article` (auteur, date, mots-clés) pour Google et les IA

## Le format

Créer `contenu/mon-article.md`. Le nom du fichier devient l'adresse de la page,
donc **en minuscules, sans accent, mots séparés par des tirets** — c'est aussi un
critère de référencement.

```
titre: Le titre complet de l'article
description: Résumé de 150 caractères maximum, affiché par Google sous le titre.
date: 2026-09-18
auteur: Laurent Mayer
categorie: Note d'analyse
motscles: RCE, culture, entreprise
---

Le corps de l'article en **Markdown**.

## Un sous-titre

Un paragraphe. Les mots en **gras** ressortent, et les [liens](https://exemple.fr)
fonctionnent normalement.

- Une liste à puces
- Un second point

> Une citation mise en valeur.
```

L'en-tête s'arrête à la ligne `---`. Tout ce qui suit est le contenu.

### Les champs

| Champ | Rôle |
|---|---|
| `titre` | Titre H1 de la page et balise `<title>` |
| `description` | Meta description Google — **viser 120 à 158 caractères** |
| `date` | Format `AAAA-MM-JJ`. Détermine l'ordre d'affichage |
| `auteur` | Affiché sur la page et dans les données structurées |
| `categorie` | Ex. `Note d'analyse`, `Rapport`, `Actualité`, `Tribune` |
| `motscles` | Séparés par des virgules, affichés en bas d'article |

Le temps de lecture est calculé automatiquement.

## Publier

```bash
python build.py
git add -A
git commit -m "Publie : titre de l'article"
git push
```

La mise en ligne prend une à deux minutes.

## Bonnes pratiques de référencement

- **Un H1 unique** : c'est le `titre`. Dans le corps, commencer les sections en `##`.
- **Des sous-titres qui posent une question** (`## Pourquoi la culture engage-t-elle ?`)
  sont davantage repris par les moteurs génératifs.
- **Répondre dès le premier paragraphe** sous chaque titre : les IA citent des
  passages courts et autonomes.
- **800 mots minimum** pour une note de fond ; en dessous, l'article pèse peu.
- **Faire des liens** vers les autres pages du site (`../rce.html`, `../observatoire.html`) :
  cela répartit la popularité et aide à la compréhension du sujet.

---

## Le circuit avec Laurent Mayer

### Dépôt

Laurent dépose ses textes dans le dossier Google Drive
**« Art Impact — Articles à publier »**
(`1GtVN-nnA_jZ67PNGPGFm21llEJwWSsO6`), partagé avec `laurent@art-for-good.org`
en tant que contributeur. Le dossier contient un mode d'emploi à son intention.

### Traitement

Sur demande, le traitement consiste à :

1. liste les documents du dossier et repère les nouveaux ;
2. lit le contenu et en extrait titre, résumé, catégorie, auteur, date ;
3. convertit en Markdown dans `contenu/<slug>.md` ;
4. optimise le référencement : titre, meta description calibrée, structure des
   titres, sous-titres interrogatifs, maillage interne, mots-clés ;
5. génère le site et **présente le résultat pour validation** ;
6. publie après accord.

### Notification

Une fois l'article en ligne, un document « Article publié — <titre> »
est créé avec le lien et le récapitulatif des optimisations, puis
**partagé avec `laurent@art-for-good.org`**. Google envoie alors
automatiquement un email de notification.

### Règle d'attribution

Le champ `auteur` d'un article doit correspondre à la personne qui a
**réellement écrit** le texte. Aucun article ne doit être signé du nom d'une
personne sans son accord explicite.
