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

- `WEB3FORMS_KEY` dans `build.py` : clé d'accès Web3Forms (voir ci-dessous).
- Mentions légales : siège, RNA/SIREN, directeur de la publication.

## Formulaires (Web3Forms)

Les formulaires de contact et de newsletter passent par [Web3Forms](https://web3forms.com)
(250 envois/mois gratuits, sans compte). Pour les activer :

1. Aller sur https://web3forms.com, saisir l'adresse de réception (`contact@art-impact.fr`).
2. La clé d'accès arrive par email.
3. Remplacer `WEB3FORMS_KEY` dans `build.py`, puis `python build.py` et commiter.

Après envoi, l'internaute est redirigé vers `merci.html`. Un champ honeypot `botcheck`
filtre les robots.
