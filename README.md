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
| `mentions-legales.html` | Mentions légales & RGPD |

## À compléter

- `FORM_ENDPOINT` dans `build.py` : identifiant Formspree (ou autre service) pour les formulaires.
- `HELLOASSO` : URL exacte de la page de don HelloAsso d'Art for Good.
- Mentions légales : siège, RNA/SIREN, directeur de la publication.
