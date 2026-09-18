# Art Impact — site officiel

Site statique du think tank **Art Impact**, Responsabilité Culturelle des Entreprises (RCE).

- **Production :** https://art-impact.fr (GitHub Pages)
- **Technologie :** HTML/CSS/JS statique, aucune dépendance, aucun build obligatoire.

## Modifier le contenu

Tout le contenu éditorial vit dans `build.py`. Après modification :

```bash
python build.py
```

Les fichiers `.html`, `sitemap.xml` et `robots.txt` sont régénérés, puis commités normalement.
Il est également possible d'éditer directement les `.html` (attention : une régénération les écrase).

## Structure

| Fichier | Page |
|---|---|
| `index.html` | Accueil — L'ambition |
| `think-tank.html` | Le Think Tank |
| `rce.html` | La RCE et ses 4 piliers |
| `observatoire.html` | Observatoire National RCE |
| `programmes.html` | Programmes & Territoires |
| `ressources.html` | Plateforme de ressources |
| `evenements.html` | Événements & Marathon de l'Art 2027 |
| `art-for-good.html` | Art for Good |
| `go-for-art.html` | Go-for-Art.com |
| `presse.html` | Presse & Médias |
| `contact.html` | Contact, newsletter, don |
| `merci.html` | Confirmation d'envoi de formulaire |
| `mentions-legales.html` | Mentions légales & RGPD |

## À compléter

- Mentions légales : siège, RNA/SIREN, directeur de la publication.

## Formulaires (Web3Forms)

Les formulaires de contact et de newsletter passent par [Web3Forms](https://web3forms.com)
(250 envois/mois gratuits, sans compte). Pour les activer :

La clé est renseignée dans `WEB3FORMS_KEY` (`build.py`). Pour changer l'adresse de
réception, il faut regénérer une clé sur https://web3forms.com et remplacer la valeur.

L'`access_key` Web3Forms est conçue pour être publique (elle vit dans le HTML côté
navigateur) : elle ne donne accès qu'à l'envoi vers l'adresse associée.

Après envoi, l'internaute est redirigé vers `merci.html`. Un champ honeypot `botcheck`
filtre les robots.
