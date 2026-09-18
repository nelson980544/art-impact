# -*- coding: utf-8 -*-
"""
Générateur statique du site Art Impact.
Chaque page est définie ci-dessous (titre, description, corps HTML) puis injectée
dans un gabarit commun (header, navigation, footer, SEO).

Usage :  python build.py
"""

from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://art-impact.org"
EMAIL = "contact@art-impact.org"
EMAIL_PRESSE = "presse@art-impact.org"
HELLOASSO = "https://www.helloasso.com/associations/art-for-good"
# Web3Forms — 250 envois/mois gratuits, sans compte.
# Récupérer la clé sur https://web3forms.com (saisir l'email de réception,
# la clé arrive par mail) puis la coller ci-dessous.
WEB3FORMS_KEY = "12908036-d737-40ae-87fd-17d9fc65e932"
FORM_ENDPOINT = "https://api.web3forms.com/submit"

NAV = [
    ("think-tank.html", "Le Think&nbsp;Tank"),
    ("rce.html", "La RCE"),
    ("observatoire.html", "Observatoire"),
    ("programmes.html", "Programmes"),
    ("ressources.html", "Ressources"),
    ("evenements.html", "Événements"),
    ("art-for-good.html", "Art&nbsp;for&nbsp;Good"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/{slug}">
<meta name="theme-color" content="#0A0E13">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Art Impact">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:image" content="{site}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Art Impact — think tank de la Responsabilité Culturelle des Entreprises">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/assets/img/og-image.jpg">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="author" content="Art Impact">
<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="apple-touch-icon" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>

<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="Art Impact, accueil">
      <svg class="brand-mark" viewBox="0 0 100 124" aria-hidden="true" focusable="false"><circle cx="50" cy="15" r="12.5"/><path fill-rule="evenodd" d="M40 36h20l32 82H71l-7.4-19H36.4L29 118H8L40 36zm10 20.5-9.2 25h18.4L50 56.5z"/></svg>
      <span>
        <span class="brand-name">Art Impact</span>
        <span class="brand-sub">Think Tank RCE</span>
      </span>
    </a>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu-principal">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-links" id="menu-principal">
      {nav}
      <li><a class="nav-cta" href="contact.html">Nous contacter</a></li>
    </ul>
  </div>
</header>

<main id="contenu">
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="brand" href="index.html">
          <svg class="brand-mark" viewBox="0 0 100 124" aria-hidden="true" focusable="false"><circle cx="50" cy="15" r="12.5"/><path fill-rule="evenodd" d="M40 36h20l32 82H71l-7.4-19H36.4L29 118H8L40 36zm10 20.5-9.2 25h18.4L50 56.5z"/></svg>
          <span>
            <span class="brand-name">Art Impact</span>
            <span class="brand-sub">Think Tank RCE</span>
          </span>
        </a>
        <p>Le think tank qui place la culture au cœur des stratégies d’impact des entreprises et des territoires.</p>
      </div>
      <div>
        <h4>Comprendre</h4>
        <ul>
          <li><a href="think-tank.html">Le Think Tank</a></li>
          <li><a href="rce.html">La RCE</a></li>
          <li><a href="observatoire.html">Observatoire National RCE</a></li>
          <li><a href="ressources.html">Plateforme de ressources</a></li>
        </ul>
      </div>
      <div>
        <h4>Agir</h4>
        <ul>
          <li><a href="programmes.html">Programmes &amp; Territoires</a></li>
          <li><a href="evenements.html">Événements</a></li>
          <li><a href="art-for-good.html">Art for Good</a></li>
          <li><a href="go-for-art.html">Go-for-Art.com</a></li>
        </ul>
      </div>
      <div>
        <h4>Dialoguer</h4>
        <ul>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="presse.html">Presse &amp; Médias</a></li>
          <li><a href="{helloasso}" target="_blank" rel="noopener">Faire un don</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <p>© 2026 Art Impact — Une initiative portée par l’association Art for Good.</p>
      <nav aria-label="Liens légaux">
        <a href="mentions-legales.html">Mentions légales</a>
        <a href="mentions-legales.html#donnees">Données personnelles</a>
        <a href="presse.html">Kit média</a>
      </nav>
    </div>
  </div>
</footer>

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

CTA_BAND = """
<section class="cta-band">
  <div class="wrap reveal">
    <p class="eyebrow solo" style="justify-content:center">Entrons en dialogue</p>
    <h2>Faisons de la culture un levier d’impact mesurable</h2>
    <p class="lead">Entreprises, collectivités, institutions, acteurs culturels&nbsp;: Art Impact vous accompagne
    pour structurer, déployer et évaluer votre stratégie culturelle.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html">Nous contacter <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="rce.html">Découvrir la RCE</a>
    </div>
  </div>
</section>
"""


def page_hero(eyebrow, h1, lead):
    return f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 1. ACCUEIL
# --------------------------------------------------------------------------
ACCUEIL = """
<section class="hero">
  <div class="wrap">
    <div class="logo-lockup">
      <svg class="lockup-mark" viewBox="0 0 100 124" aria-hidden="true" focusable="false">
        <circle cx="50" cy="15" r="12.5"/>
        <path fill-rule="evenodd" d="M40 36h20l32 82H71l-7.4-19H36.4L29 118H8L40 36zm10 20.5-9.2 25h18.4L50 56.5z"/>
      </svg>
      <p class="lockup-name">Art Impact</p>
      <p class="lockup-base">think tank &bull; culture &bull; entreprises &bull; territoires</p>
    </div>
    <p class="eyebrow">Think Tank &middot; Responsabilité Culturelle des Entreprises</p>
    <h1>La culture, pilier d’impact des organisations et des territoires.</h1>
    <p class="lead">Art Impact est né d’une conviction simple&nbsp;: la culture est l’un des leviers les plus
    puissants de transformation sociale, économique et territoriale.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="rce.html">Découvrir la RCE <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="think-tank.html">Le Think Tank</a>
    </div>
    <p class="hero-meta">
      <span>Analyses &amp; référentiels</span>
      <span>Observatoire national</span>
      <span>Programmes à impact</span>
      <span>Alliances territoriales</span>
    </p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">L’ambition</p>
      <h2>La culture n’est plus un supplément d’âme.</h2>
    </div>
    <div class="split reveal">
      <div>
        <p class="lead">Dans un monde en quête de sens, d’engagement et de cohésion, la culture devient
        un pilier d’impact, un vecteur d’innovation, un moteur d’attractivité, un outil de mobilisation collective.</p>
        <p>Longtemps considérée comme une dépense d’image, la culture s’impose aujourd’hui comme une
        infrastructure du lien&nbsp;: elle relie les équipes, réveille les imaginaires, ancre les organisations
        dans leur territoire et rend désirables les transitions à mener.</p>
      </div>
      <div class="split-side">
        <h3>Art Impact structure cette vision.</h3>
        <p class="dim">Nous sommes le think tank qui place la culture au cœur des stratégies d’impact des
        entreprises et des territoires&nbsp;: un espace de réflexion, d’action et d’influence.</p>
        <p style="margin-top:22px"><a class="link-more" href="think-tank.html">Notre raison d’être <span aria-hidden="true">&rarr;</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Les 4 piliers de la RCE</p>
      <h2>Une lecture nouvelle de l’impact</h2>
      <p class="lead">Intégrer la culture dans la stratégie globale des organisations, au même niveau que
      l’environnement, le social ou la gouvernance.</p>
    </div>
    <div class="grid grid-4 reveal">
      <article class="cell">
        <span class="num">01</span>
        <h3>Engagement &amp; Cohésion</h3>
        <p>La culture comme lien, comme respiration, comme énergie collective.</p>
      </article>
      <article class="cell">
        <span class="num">02</span>
        <h3>Innovation &amp; Créativité</h3>
        <p>La culture comme ouverture, comme imagination, comme capacité à inventer.</p>
      </article>
      <article class="cell">
        <span class="num">03</span>
        <h3>Territoires &amp; Attractivité</h3>
        <p>La culture comme moteur de développement local et de vitalité économique.</p>
      </article>
      <article class="cell">
        <span class="num">04</span>
        <h3>Environnement &amp; Sensibilisation</h3>
        <p>La culture comme vecteur de conscience écologique et de mobilisation citoyenne.</p>
      </article>
    </div>
    <div class="btn-row reveal">
      <a class="btn btn-ghost" href="rce.html">Explorer le référentiel RCE <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Nos champs d’action</p>
      <h2>Éclairer, accompagner, mesurer, relier</h2>
    </div>
    <div class="cards reveal">
      <article class="card">
        <h3>Observatoire National RCE</h3>
        <p>La première base de données française dédiée à l’impact culturel des organisations&nbsp;:
        baromètre annuel, études sectorielles, cartographie, indicateurs.</p>
        <p style="margin-top:22px"><a class="link-more" href="observatoire.html">La mesure <span aria-hidden="true">&rarr;</span></a></p>
      </article>
      <article class="card">
        <h3>Programmes &amp; Territoires</h3>
        <p>Des programmes culturels à impact conçus comme des alliances entre artistes, entreprises
        et territoires.</p>
        <p style="margin-top:22px"><a class="link-more" href="programmes.html">L’action <span aria-hidden="true">&rarr;</span></a></p>
      </article>
      <article class="card">
        <h3>Plateforme de ressources</h3>
        <p>Notes d’analyse, rapports, guides pratiques, vidéos, webinaires et bibliothèque RCE.</p>
        <p style="margin-top:22px"><a class="link-more" href="ressources.html">Le savoir <span aria-hidden="true">&rarr;</span></a></p>
      </article>
      <article class="card">
        <h3>Événements</h3>
        <p>Art Impact Live, rencontres entreprises, ateliers territoriaux, conférences — et le
        Marathon de l’Art 2027.</p>
        <p style="margin-top:22px"><a class="link-more" href="evenements.html">Le dialogue <span aria-hidden="true">&rarr;</span></a></p>
      </article>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap narrow">
    <div class="pull reveal">
      <p class="serif-quote">Pour transformer, il faut comprendre. Pour comprendre, il faut mesurer.</p>
      <p class="dim" style="margin:14px 0 0;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase">
        Observatoire National RCE</p>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">L’écosystème</p>
      <h2>Une origine, une plateforme, un think tank</h2>
    </div>
    <ul class="ed-list reveal">
      <li>
        <span class="k">01</span>
        <div>
          <h3>Art for Good — l’origine</h3>
          <p>L’initiative fondatrice qui porte Art Impact&nbsp;: programmes culturels, actions nationales,
          projets innovants et dispositifs de mécénat.
          <a class="link-more" style="margin-left:10px" href="art-for-good.html">En savoir plus <span aria-hidden="true">&rarr;</span></a></p>
        </div>
      </li>
      <li>
        <span class="k">02</span>
        <div>
          <h3>Art Impact — le prolongement stratégique</h3>
          <p>La dimension think tank&nbsp;: la vision, la structuration, l’influence, le cadre national partagé.
          <a class="link-more" style="margin-left:10px" href="think-tank.html">En savoir plus <span aria-hidden="true">&rarr;</span></a></p>
        </div>
      </li>
      <li>
        <span class="k">03</span>
        <div>
          <h3>Go-for-Art.com — l’accès</h3>
          <p>La plateforme phygitale qui démocratise l’accès à l’art&nbsp;: expositions, QR codes, artistes,
          parcours culturels.
          <a class="link-more" style="margin-left:10px" href="go-for-art.html">En savoir plus <span aria-hidden="true">&rarr;</span></a></p>
        </div>
      </li>
    </ul>
  </div>
</section>
""" + CTA_BAND


# --------------------------------------------------------------------------
# 2. LE THINK TANK
# --------------------------------------------------------------------------
THINK_TANK = page_hero(
    "Le Think Tank",
    "Penser, expérimenter et déployer la Responsabilité Culturelle des Entreprises.",
    "Art Impact rassemble celles et ceux qui font de la culture un levier stratégique reconnu, "
    "mesurable et durable."
) + """
<section class="sec">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="eyebrow">La raison d’être</p>
        <p class="lead">Nous produisons des analyses, des référentiels, des données, des programmes et des
        alliances pour installer durablement la culture dans les stratégies d’impact.</p>
        <p>Art Impact n’est ni un cabinet, ni une agence&nbsp;: c’est un espace de réflexion, d’action et
        d’influence. Nous réunissons des dirigeants, des élus, des chercheurs, des artistes et des
        responsables RSE autour d’une même question&nbsp;: comment faire de la culture une politique
        d’impact à part entière&nbsp;?</p>
        <p>Nos travaux sont publics, documentés et ouverts. Ils ont vocation à créer un cadre national
        partagé, compris par les décideurs comme par les acteurs culturels.</p>
      </div>
      <div class="split-side">
        <h3>Notre rôle</h3>
        <ul class="bullets">
          <li><strong>Éclairer</strong> les décideurs par la donnée et l’analyse.</li>
          <li><strong>Accompagner</strong> les entreprises dans la structuration de leur stratégie culturelle.</li>
          <li><strong>Soutenir</strong> les territoires dans leurs politiques d’attractivité.</li>
          <li><strong>Valoriser</strong> les acteurs culturels et leur contribution à l’intérêt général.</li>
          <li><strong>Créer</strong> un cadre national partagé de la RCE.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Méthode</p>
      <h2>Trois temps, une même exigence</h2>
    </div>
    <div class="grid grid-3 reveal">
      <article class="cell">
        <span class="num">Réflexion</span>
        <h3>Produire le cadre</h3>
        <p>Référentiel RCE, notes d’analyse, études sectorielles, méthodologie d’évaluation. Nous
        construisons le vocabulaire commun d’un sujet encore émergent.</p>
      </article>
      <article class="cell">
        <span class="num">Action</span>
        <h3>Expérimenter sur le terrain</h3>
        <p>Chaque hypothèse est testée dans des programmes réels, avec des entreprises et des
        collectivités, puis documentée et rendue réplicable.</p>
      </article>
      <article class="cell">
        <span class="num">Influence</span>
        <h3>Faire école</h3>
        <p>Publications, événements, alliances et prises de parole publiques pour inscrire la RCE
        dans l’agenda des organisations et des politiques publiques.</p>
      </article>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Communauté</p>
      <h2>Celles et ceux qui font Art Impact</h2>
      <p class="lead">Un think tank ouvert, en dialogue permanent avec les entreprises, les institutions,
      les territoires et les acteurs culturels.</p>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>4</b><span>piliers structurant le référentiel RCE</span></div>
      <div class="stat"><b>1</b><span>observatoire national dédié à l’impact culturel</span></div>
      <div class="stat"><b>4</b><span>familles de programmes à impact</span></div>
      <div class="stat"><b>2027</b><span>Marathon de l’Art, rendez-vous national</span></div>
    </div>
  </div>
</section>
""" + CTA_BAND


# --------------------------------------------------------------------------
# 3. RCE
# --------------------------------------------------------------------------
RCE = page_hero(
    "Responsabilité Culturelle des Entreprises",
    "La RCE&nbsp;: une lecture nouvelle de l’impact.",
    "Intégrer la culture dans la stratégie globale des organisations, au même niveau que "
    "l’environnement, le social ou la gouvernance."
) + """
<section class="sec">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="eyebrow">Définition</p>
        <p class="lead">La Responsabilité Culturelle des Entreprises donne aux organisations un cadre clair,
        ambitieux et opérationnel pour agir.</p>
        <p>Là où la RSE a structuré l’engagement environnemental, social et de gouvernance, la RCE
        propose le chaînon manquant&nbsp;: la dimension culturelle de la responsabilité. Elle ne se réduit
        ni au mécénat, ni à la communication&nbsp;; elle engage la stratégie, les équipes, le territoire et
        la raison d’être.</p>
      </div>
      <div class="split-side">
        <h3>Ce que la RCE change</h3>
        <ul class="bullets">
          <li>Un <strong>cadre commun</strong> pour parler d’impact culturel.</li>
          <li>Des <strong>indicateurs</strong> partagés et comparables.</li>
          <li>Une <strong>place stratégique</strong> pour la culture au comité de direction.</li>
          <li>Une <strong>articulation</strong> naturelle avec les politiques RSE existantes.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Le référentiel</p>
      <h2>Les 4 piliers de la RCE</h2>
    </div>
    <div class="grid grid-2 reveal">
      <article class="cell">
        <span class="num">Pilier 01</span>
        <h3>Engagement &amp; Cohésion</h3>
        <p>La culture comme lien, comme respiration, comme énergie collective. Elle crée des espaces
        partagés, réduit les distances hiérarchiques et redonne du sens au collectif de travail.</p>
      </article>
      <article class="cell">
        <span class="num">Pilier 02</span>
        <h3>Innovation &amp; Créativité</h3>
        <p>La culture comme ouverture, comme imagination, comme capacité à inventer. Elle déplace
        les regards et nourrit la capacité des organisations à se transformer.</p>
      </article>
      <article class="cell">
        <span class="num">Pilier 03</span>
        <h3>Territoires &amp; Attractivité</h3>
        <p>La culture comme moteur de développement local et de vitalité économique. Elle ancre,
        distingue et rend désirable un territoire comme une organisation.</p>
      </article>
      <article class="cell">
        <span class="num">Pilier 04</span>
        <h3>Environnement &amp; Sensibilisation</h3>
        <p>La culture comme vecteur de conscience écologique et de mobilisation citoyenne. Elle
        touche par l’émotion là où la donnée seule ne suffit plus.</p>
      </article>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Mise en œuvre</p>
      <h2>Du diagnostic au déploiement</h2>
    </div>
    <ul class="ed-list reveal">
      <li><span class="k">01</span><div><h3>Diagnostic</h3>
        <p>Cartographie des actions culturelles existantes, entretiens, positionnement par rapport
        au référentiel et aux données de l’Observatoire.</p></div></li>
      <li><span class="k">02</span><div><h3>Cadrage stratégique</h3>
        <p>Définition des priorités par pilier, articulation avec la feuille de route RSE, choix des
        indicateurs et des objectifs.</p></div></li>
      <li><span class="k">03</span><div><h3>Déploiement</h3>
        <p>Mise en œuvre des programmes, alliances avec les artistes et les acteurs du territoire,
        embarquement des équipes.</p></div></li>
      <li><span class="k">04</span><div><h3>Mesure &amp; valorisation</h3>
        <p>Évaluation des effets, reporting, contribution au baromètre national et valorisation
        publique des résultats.</p></div></li>
    </ul>
    <div class="btn-row reveal">
      <a class="btn btn-primary" href="contact.html">Engager une démarche RCE <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="observatoire.html">Voir l’Observatoire</a>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 4. OBSERVATOIRE
# --------------------------------------------------------------------------
OBSERVATOIRE = page_hero(
    "Observatoire National RCE",
    "Pour transformer, il faut comprendre. Pour comprendre, il faut mesurer.",
    "La première base de données française dédiée à l’impact culturel des organisations."
) + """
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Ce que produit l’Observatoire</p>
      <h2>Cinq productions de référence</h2>
    </div>
    <div class="grid grid-3 reveal">
      <article class="cell"><span class="num">01</span><h3>Baromètre annuel</h3>
        <p>L’état de la Responsabilité Culturelle des Entreprises en France, mesuré chaque année
        selon une méthodologie stable.</p></article>
      <article class="cell"><span class="num">02</span><h3>Études sectorielles</h3>
        <p>Des analyses par filière pour comprendre les dynamiques propres à chaque secteur
        d’activité.</p></article>
      <article class="cell"><span class="num">03</span><h3>Cartographie nationale</h3>
        <p>Une lecture territoriale des initiatives culturelles portées par les organisations.</p></article>
      <article class="cell"><span class="num">04</span><h3>Indicateurs</h3>
        <p>Un jeu d’indicateurs partagés pour rendre l’impact culturel lisible et comparable.</p></article>
      <article class="cell"><span class="num">05</span><h3>Méthodologie de référence</h3>
        <p>Un protocole documenté, ouvert et discutable, garant de la rigueur des travaux.</p></article>
      <article class="cell"><span class="num">&mdash;</span><h3>Une utilité concrète</h3>
        <p>Situer ses actions, progresser, se comparer, s’inspirer&nbsp;: l’Observatoire est un outil de
        pilotage autant qu’un outil de connaissance.</p></article>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="eyebrow">À qui s’adresse l’Observatoire</p>
        <h2>Un commun au service de la décision</h2>
        <p class="lead" style="margin-top:26px">Entreprises, collectivités, institutions, chercheurs et
        acteurs culturels disposent enfin d’une base commune pour situer et comparer leurs actions.</p>
      </div>
      <div class="split-side">
        <h3>Contribuer</h3>
        <p class="dim">L’Observatoire se nourrit des contributions de ses participants. Rejoindre le
        panel, c’est accéder aux résultats détaillés, se situer face à son secteur et faire progresser
        la connaissance collective.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">Rejoindre le panel <span class="arw">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>
""" + CTA_BAND


# --------------------------------------------------------------------------
# 5. PROGRAMMES
# --------------------------------------------------------------------------
PROGRAMMES = page_hero(
    "Programmes &amp; Territoires",
    "Des programmes culturels à impact, conçus comme des alliances.",
    "Chaque programme relie artistes, entreprises et territoires pour répondre aux enjeux concrets "
    "des organisations et des collectivités."
) + """
<section class="sec">
  <div class="wrap">
    <div class="grid grid-2 reveal">
      <article class="cell">
        <span class="num">Programme 01</span>
        <h3>Art &amp; Cohésion</h3>
        <p>Renforcer le lien interne, créer des espaces de respiration, mobiliser les équipes.
        Des dispositifs artistiques qui font se rencontrer les métiers, les sites et les générations.</p>
      </article>
      <article class="cell">
        <span class="num">Programme 02</span>
        <h3>Art &amp; Innovation</h3>
        <p>Stimuler l’imaginaire, ouvrir des perspectives, accompagner les transformations.
        La création comme méthode de travail et comme accélérateur de projets.</p>
      </article>
      <article class="cell">
        <span class="num">Programme 03</span>
        <h3>Art &amp; Environnement</h3>
        <p>Sensibiliser autrement, toucher par l’émotion, mobiliser par l’expérience.
        Faire de la transition écologique un récit partagé plutôt qu’une contrainte subie.</p>
      </article>
      <article class="cell">
        <span class="num">Programme 04</span>
        <h3>Art &amp; Attractivité territoriale</h3>
        <p>Faire de la culture un moteur de développement local, un marqueur identitaire,
        un facteur d’attractivité pour les habitants comme pour les entreprises.</p>
      </article>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Notre approche</p>
      <h2>Une alliance, pas une prestation</h2>
      <p class="lead">Chaque programme est co-construit avec les artistes, les équipes de l’organisation
      et les acteurs du territoire. Il est documenté, évalué et conçu pour durer.</p>
    </div>
    <ul class="ed-list reveal">
      <li><span class="k">01</span><div><h3>Écoute</h3>
        <p>Comprendre l’enjeu réel&nbsp;: cohésion, transformation, transition, ancrage territorial.</p></div></li>
      <li><span class="k">02</span><div><h3>Alliance</h3>
        <p>Identifier les artistes et partenaires culturels dont la démarche répond à cet enjeu.</p></div></li>
      <li><span class="k">03</span><div><h3>Expérience</h3>
        <p>Concevoir un dispositif vivant&nbsp;: résidence, création partagée, exposition, parcours, rencontre.</p></div></li>
      <li><span class="k">04</span><div><h3>Évaluation</h3>
        <p>Mesurer les effets selon les indicateurs RCE et nourrir l’Observatoire national.</p></div></li>
    </ul>
    <div class="btn-row reveal">
      <a class="btn btn-primary" href="contact.html">Construire un programme <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="go-for-art.html">Découvrir Go-for-Art.com</a>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 6. RESSOURCES
# --------------------------------------------------------------------------
RESSOURCES = page_hero(
    "Plateforme de ressources",
    "Comprendre, agir, mesurer.",
    "Un espace ouvert aux décideurs, aux chercheurs, aux entreprises, aux collectivités et aux "
    "acteurs culturels."
) + """
<section class="sec">
  <div class="wrap">
    <div class="cards reveal">
      <article class="card"><h3>Notes d’analyse</h3>
        <p>Des formats courts pour décrypter une tendance, un chiffre, une politique publique ou
        une pratique émergente.</p></article>
      <article class="card"><h3>Rapports</h3>
        <p>Les travaux de fond du think tank et de l’Observatoire National RCE.</p></article>
      <article class="card"><h3>Guides pratiques</h3>
        <p>Des méthodes opérationnelles pour lancer, structurer et évaluer une démarche RCE.</p></article>
      <article class="card"><h3>Vidéos</h3>
        <p>Interventions, témoignages, captations de programmes et formats pédagogiques.</p></article>
      <article class="card"><h3>Webinaires</h3>
        <p>Des rendez-vous en ligne pour approfondir un pilier de la RCE avec nos invités.</p></article>
      <article class="card"><h3>Bibliothèque RCE</h3>
        <p>Une sélection de références, d’études et de travaux académiques sur l’impact culturel.</p></article>
    </div>
    <div class="pull reveal" style="margin-top:56px">
      <p class="serif-quote">La plateforme s’enrichit au rythme des travaux du think tank.</p>
      <p class="dim" style="margin:14px 0 0">Les premières publications seront mises en ligne
      progressivement. Inscrivez-vous à la newsletter pour être informé de chaque parution.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html#newsletter">Recevoir les publications <span class="arw">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 7. ÉVÉNEMENTS
# --------------------------------------------------------------------------
EVENEMENTS = page_hero(
    "Événements",
    "Des moments pour penser ensemble, débattre, expérimenter, construire.",
    "Art Impact organise des rencontres pour faire avancer la réflexion et l’action."
) + """
<section class="sec">
  <div class="wrap">
    <div class="grid grid-2 reveal">
      <article class="cell"><span class="num">Format</span><h3>Art Impact Live</h3>
        <p>Le rendez-vous régulier du think tank&nbsp;: une idée forte, des intervenants engagés, un
        débat ouvert. En présentiel et en ligne.</p></article>
      <article class="cell"><span class="num">Format</span><h3>Rencontres entreprises</h3>
        <p>Des sessions à huis clos entre dirigeants et responsables RSE pour partager pratiques,
        obstacles et résultats.</p></article>
      <article class="cell"><span class="num">Format</span><h3>Ateliers territoriaux</h3>
        <p>Des temps de travail avec les collectivités et les acteurs culturels locaux, au plus près
        des réalités du terrain.</p></article>
      <article class="cell"><span class="num">Format</span><h3>Conférences thématiques</h3>
        <p>Un pilier de la RCE exploré en profondeur, avec chercheurs, artistes et praticiens.</p></article>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="eyebrow">Le grand rendez-vous national</p>
        <h2>Marathon de l’Art 2027</h2>
        <p class="lead" style="margin-top:26px">Une mobilisation nationale pour faire de la culture
        une cause partagée par les entreprises, les territoires et les citoyens.</p>
        <p>Pendant plusieurs jours, artistes, organisations et collectivités se relaient pour créer,
        exposer, débattre et démontrer, à l’échelle du pays, ce que la culture rend possible.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">Devenir partenaire <span class="arw">&rarr;</span></a>
        </div>
      </div>
      <div class="split-side">
        <h3>Replays</h3>
        <p class="dim">Les captations de nos rencontres sont mises à disposition sur la plateforme de
        ressources, accompagnées des synthèses écrites.</p>
        <p style="margin-top:20px"><a class="link-more" href="ressources.html">Accéder aux ressources <span aria-hidden="true">&rarr;</span></a></p>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 8. ART FOR GOOD
# --------------------------------------------------------------------------
ART_FOR_GOOD = page_hero(
    "Art for Good",
    "L’origine.",
    "Art for Good est l’initiative fondatrice qui porte Art Impact."
) + """
<section class="sec">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="lead">Art for Good développe des programmes culturels, des actions nationales, des
        projets innovants et des dispositifs de mécénat.</p>
        <p>L’association agit depuis le terrain&nbsp;: elle produit, expérimente, mobilise des artistes et
        des partenaires, et fait exister concrètement l’idée que la culture transforme.</p>
        <p><strong>Art Impact en est le prolongement stratégique</strong>&nbsp;: la dimension think tank,
        la vision, la structuration, l’influence. L’une agit, l’autre construit le cadre&nbsp;; ensemble,
        elles installent la Responsabilité Culturelle des Entreprises dans le paysage français.</p>
      </div>
      <div class="split-side">
        <h3>Soutenir l’association</h3>
        <p class="dim">Art for Good porte le think tank Art Impact. Votre don finance les travaux de
        recherche, l’Observatoire et les programmes culturels déployés sur les territoires.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="{helloasso}" target="_blank" rel="noopener">Faire un don sur HelloAsso <span class="arw">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Les champs d’intervention</p>
      <h2>Ce que fait Art for Good</h2>
    </div>
    <div class="grid grid-4 reveal">
      <article class="cell"><span class="num">01</span><h3>Programmes culturels</h3>
        <p>Créations, résidences, expositions et parcours menés avec les artistes.</p></article>
      <article class="cell"><span class="num">02</span><h3>Actions nationales</h3>
        <p>Des mobilisations d’ampleur, dont le Marathon de l’Art.</p></article>
      <article class="cell"><span class="num">03</span><h3>Projets innovants</h3>
        <p>De nouveaux formats d’accès à l’art, dont la plateforme Go-for-Art.com.</p></article>
      <article class="cell"><span class="num">04</span><h3>Mécénat</h3>
        <p>Des dispositifs permettant aux entreprises de soutenir la création.</p></article>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 9. GO FOR ART
# --------------------------------------------------------------------------
GO_FOR_ART = page_hero(
    "Go-for-Art.com",
    "L’accès.",
    "La plateforme phygitale qui démocratise l’accès à l’art."
) + """
<section class="sec">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="lead">Expositions, QR codes, artistes, parcours culturels&nbsp;: un outil simple, puissant
        et accessible pour les entreprises et les territoires.</p>
        <p>Go-for-Art.com relie le lieu physique et l’expérience numérique. Une œuvre installée dans
        un hall, un couloir, une médiathèque ou une rue devient le point d’entrée vers l’artiste,
        sa démarche, son univers — d’un simple scan.</p>
        <p>La culture devient un geste quotidien, un espace partagé, une expérience vivante.</p>
      </div>
      <div class="split-side">
        <h3>Pour qui</h3>
        <ul class="bullets">
          <li><strong>Entreprises</strong>&nbsp;: transformer les espaces de travail en lieux d’exposition.</li>
          <li><strong>Collectivités</strong>&nbsp;: déployer des parcours culturels sur le territoire.</li>
          <li><strong>Artistes</strong>&nbsp;: gagner en visibilité et rencontrer de nouveaux publics.</li>
          <li><strong>Publics</strong>&nbsp;: accéder à l’art là où l’on vit, travaille et circule.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="grid grid-3 reveal">
      <article class="cell"><span class="num">01</span><h3>Expositions</h3>
        <p>Des accrochages clés en main dans les espaces professionnels et publics.</p></article>
      <article class="cell"><span class="num">02</span><h3>QR codes</h3>
        <p>Chaque œuvre devient interactive&nbsp;: contexte, artiste, démarche, contenus complémentaires.</p></article>
      <article class="cell"><span class="num">03</span><h3>Parcours culturels</h3>
        <p>Des itinéraires conçus à l’échelle d’un bâtiment, d’un campus ou d’un territoire.</p></article>
    </div>
    <div class="btn-row reveal">
      <a class="btn btn-primary" href="https://go-for-art.com" target="_blank" rel="noopener">Visiter Go-for-Art.com <span class="arw">&rarr;</span></a>
      <a class="btn btn-ghost" href="contact.html">Déployer chez nous</a>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 10. PRESSE
# --------------------------------------------------------------------------
PRESSE = page_hero(
    "Presse &amp; Médias",
    "La visibilité.",
    "Art Impact met à disposition l’ensemble des ressources nécessaires pour relayer ses travaux "
    "et ses actions."
) + """
<section class="sec">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <p class="eyebrow">Ressources disponibles</p>
        <ul class="bullets">
          <li><strong>Communiqués de presse</strong> — annonces, publications et résultats de l’Observatoire.</li>
          <li><strong>Kit média</strong> — présentation du think tank, chiffres clés, éléments de langage.</li>
          <li><strong>Logos</strong> — identité Art Impact, Art for Good et Go-for-Art.com.</li>
          <li><strong>Visuels</strong> — photographies des programmes et des événements.</li>
          <li><strong>Contacts presse</strong> — interlocuteur dédié pour interviews et tribunes.</li>
        </ul>
        <p class="dim" style="margin-top:28px">Les éléments sont transmis sur demande, sous 48&nbsp;heures
        ouvrées.</p>
      </div>
      <div class="split-side">
        <h3>Contact presse</h3>
        <p class="dim">Pour toute demande d’interview, de tribune, d’intervention ou d’accès aux
        travaux en avant-première.</p>
        <p style="margin-top:18px"><a class="link-more" href="mailto:{email_presse}">{email_presse} <span aria-hidden="true">&rarr;</span></a></p>
        <div class="btn-row">
          <a class="btn btn-ghost" href="contact.html">Formulaire de contact</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 11. CONTACT
# --------------------------------------------------------------------------
CONTACT = page_hero(
    "Contact",
    "Le lien.",
    "Art Impact est un think tank ouvert, accessible, en dialogue permanent avec les entreprises, "
    "les institutions, les territoires et les acteurs culturels."
) + """
<section class="sec">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <h2 style="margin-bottom:28px">Écrivez-nous</h2>
        <form class="form" action="{form}" method="POST">
          <input type="hidden" name="access_key" value="{w3key}">
          <input type="hidden" name="subject" value="Art Impact — nouveau message depuis le site">
          <input type="hidden" name="from_name" value="Site Art Impact">
          <input type="hidden" name="replyto" value="email">
          <input type="hidden" name="redirect" value="{site}/merci.html">
          <input type="checkbox" name="botcheck" class="hp" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-row">
            <div class="field">
              <label for="nom">Nom et prénom</label>
              <input id="nom" name="nom" type="text" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="organisation">Organisation</label>
              <input id="organisation" name="organisation" type="text" autocomplete="organization">
            </div>
          </div>
          <div class="form-row">
            <div class="field">
              <label for="email">Email</label>
              <input id="email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="field">
              <label for="profil">Vous êtes</label>
              <select id="profil" name="profil">
                <option>Entreprise</option>
                <option>Collectivité / Territoire</option>
                <option>Institution</option>
                <option>Acteur culturel / Artiste</option>
                <option>Chercheur</option>
                <option>Presse</option>
                <option>Autre</option>
              </select>
            </div>
          </div>
          <div class="field">
            <label for="sujet">Sujet</label>
            <select id="sujet" name="sujet">
              <option>Engager une démarche RCE</option>
              <option>Rejoindre l’Observatoire National RCE</option>
              <option>Construire un programme culturel</option>
              <option>Partenariat / Mécénat</option>
              <option>Marathon de l’Art 2027</option>
              <option>Presse &amp; médias</option>
              <option>Autre</option>
            </select>
          </div>
          <div class="field">
            <label for="message">Message</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <label class="consent">
            <input type="checkbox" name="consentement" required>
            <span>J’accepte que mes données soient utilisées pour traiter ma demande, conformément
            à la <a href="mentions-legales.html#donnees" style="color:var(--gold)">politique de confidentialité</a>.</span>
          </label>
          <div class="btn-row" style="margin-top:8px">
            <button class="btn btn-primary" type="submit">Envoyer le message <span class="arw">&rarr;</span></button>
          </div>
        </form>
      </div>
      <div class="split-side">
        <h3>Email direct</h3>
        <p><a class="link-more" href="mailto:{email}">{email}</a></p>
        <p class="dim" style="margin-top:8px">Presse&nbsp;: <a href="mailto:{email_presse}" style="color:var(--gold)">{email_presse}</a></p>

        <h3 id="newsletter" style="margin-top:44px">Newsletter</h3>
        <p class="dim">Recevez les publications du think tank, les résultats de l’Observatoire et les
        invitations aux événements.</p>
        <form class="form" action="{form}" method="POST" style="margin-top:18px">
          <input type="hidden" name="access_key" value="{w3key}">
          <input type="hidden" name="subject" value="Art Impact — inscription newsletter">
          <input type="hidden" name="from_name" value="Site Art Impact">
          <input type="hidden" name="replyto" value="email">
          <input type="hidden" name="redirect" value="{site}/merci.html">
          <input type="checkbox" name="botcheck" class="hp" style="display:none" tabindex="-1" autocomplete="off">
          <input type="hidden" name="sujet" value="Inscription newsletter">
          <div class="field">
            <label for="news-email">Votre email</label>
            <input id="news-email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="btn-row" style="margin-top:0">
            <button class="btn btn-ghost" type="submit">S’inscrire</button>
          </div>
        </form>

        <h3 style="margin-top:44px">Soutenir</h3>
        <p class="dim">Faites un don à l’association Art for Good, qui porte le think tank.</p>
        <div class="btn-row" style="margin-top:18px">
          <a class="btn btn-primary" href="{helloasso}" target="_blank" rel="noopener">Faire un don <span class="arw">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 12. MENTIONS LÉGALES
# --------------------------------------------------------------------------
MENTIONS = page_hero(
    "Informations légales",
    "Mentions légales &amp; données personnelles",
    "Informations relatives à l’éditeur du site, à l’hébergement et au traitement des données."
) + """
<section class="sec">
  <div class="wrap narrow">
    <h2>Éditeur du site</h2>
    <p class="dim">Le site art-impact.org est édité par l’association <strong>Art for Good</strong>,
    association loi 1901, qui porte le think tank Art Impact.<br>
    Contact&nbsp;: <a href="mailto:{email}" style="color:var(--gold)">{email}</a></p>
    <p class="dim"><em>À compléter&nbsp;: adresse du siège, numéro RNA/SIREN, nom du directeur
    de la publication.</em></p>

    <h2 style="margin-top:56px">Hébergement</h2>
    <p class="dim">Le site est hébergé par GitHub&nbsp;Pages — GitHub,&nbsp;Inc.,
    88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.<br>
    Le nom de domaine est enregistré auprès d’OVH SAS, 2 rue Kellermann, 59100 Roubaix, France.</p>

    <h2 style="margin-top:56px">Propriété intellectuelle</h2>
    <p class="dim">L’ensemble des contenus de ce site (textes, identité visuelle, publications) est
    la propriété d’Art for Good et d’Art Impact, sauf mention contraire. Toute reproduction doit
    faire l’objet d’une autorisation préalable ou citer explicitement la source.</p>

    <h2 id="donnees" style="margin-top:56px">Données personnelles</h2>
    <p class="dim">Les données transmises via les formulaires de ce site sont utilisées uniquement
    pour répondre à votre demande ou, le cas échéant, vous adresser la newsletter du think tank.
    Elles ne sont ni vendues, ni cédées à des tiers.</p>
    <p class="dim">Conformément au RGPD, vous disposez d’un droit d’accès, de rectification,
    d’effacement et d’opposition sur vos données. Pour l’exercer, écrivez à
    <a href="mailto:{email}" style="color:var(--gold)">{email}</a>.</p>

    <h2 style="margin-top:56px">Cookies</h2>
    <p class="dim">Ce site ne dépose aucun cookie de mesure d’audience ni de publicité. Les polices
    de caractères sont chargées depuis Google&nbsp;Fonts.</p>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# 13. MERCI (page d'arrivée après envoi d'un formulaire)
# --------------------------------------------------------------------------
MERCI = page_hero(
    "Message envoyé",
    "Merci.",
    "Votre message a bien été transmis à l’équipe d’Art Impact."
) + """
<section class="sec">
  <div class="wrap narrow">
    <div class="reveal">
      <p class="lead">Nous revenons vers vous dans les meilleurs délais, généralement sous 48&nbsp;heures
      ouvrées.</p>
      <p class="dim">En attendant, vous pouvez poursuivre votre lecture&nbsp;:</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="index.html">Retour à l’accueil <span class="arw">&rarr;</span></a>
        <a class="btn btn-ghost" href="rce.html">Découvrir la RCE</a>
        <a class="btn btn-ghost" href="observatoire.html">L’Observatoire</a>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
PAGES = [
    # slug, titre <title>, meta description, corps
    ("index.html",
     "Art Impact — Think Tank de la Responsabilité Culturelle des Entreprises",
     "Art Impact est le think tank qui place la culture au cœur des stratégies d’impact "
     "des entreprises et des territoires. Référentiel RCE et Observatoire national.",
     ACCUEIL),
    ("think-tank.html",
     "Le Think Tank — Art Impact",
     "Analyses, référentiels, données et programmes : Art Impact fait de la culture un "
     "levier stratégique reconnu, mesurable et durable pour les organisations.",
     THINK_TANK),
    ("rce.html",
     "La RCE, Responsabilité Culturelle des Entreprises — Art Impact",
     "La Responsabilité Culturelle des Entreprises intègre la culture dans la stratégie "
     "globale des organisations. Découvrez les 4 piliers du référentiel RCE.",
     RCE),
    ("observatoire.html",
     "Observatoire National RCE — Art Impact",
     "La première base de données française sur l’impact culturel des organisations : "
     "baromètre annuel, études sectorielles, cartographie et indicateurs RCE.",
     OBSERVATOIRE),
    ("programmes.html",
     "Programmes &amp; Territoires — Art Impact",
     "Art & Cohésion, Art & Innovation, Art & Environnement, Art & Attractivité territoriale : "
     "des programmes culturels à impact conçus comme des alliances.",
     PROGRAMMES),
    ("ressources.html",
     "Plateforme de ressources — Art Impact",
     "Notes d’analyse, rapports, guides pratiques, vidéos, webinaires et bibliothèque RCE : "
     "un espace pour comprendre, agir et mesurer.",
     RESSOURCES),
    ("evenements.html",
     "Événements — Art Impact",
     "Art Impact Live, rencontres entreprises, ateliers territoriaux, conférences et "
     "Marathon de l’Art 2027 : les rendez-vous du think tank.",
     EVENEMENTS),
    ("art-for-good.html",
     "Art for Good — L’origine d’Art Impact",
     "Art for Good est l’initiative fondatrice qui porte Art Impact : programmes culturels, actions "
     "nationales, projets innovants et dispositifs de mécénat.",
     ART_FOR_GOOD),
    ("go-for-art.html",
     "Go-for-Art.com — La plateforme phygitale d’accès à l’art",
     "Expositions, QR codes, artistes, parcours culturels : un outil simple et accessible pour les "
     "entreprises et les territoires.",
     GO_FOR_ART),
    ("presse.html",
     "Presse &amp; Médias — Art Impact",
     "Communiqués, kit média, logos et contacts presse : toutes les ressources pour relayer les "
     "travaux et les actions d’Art Impact.",
     PRESSE),
    ("contact.html",
     "Contact — Art Impact",
     "Formulaire, email, newsletter et don : Art Impact dialogue avec les entreprises, "
     "les institutions, les territoires et les acteurs culturels.",
     CONTACT),
    ("merci.html",
     "Merci — Art Impact",
     "Votre message a bien été transmis à l’équipe d’Art Impact.",
     MERCI),
    ("mentions-legales.html",
     "Mentions légales — Art Impact",
     "Mentions légales, hébergement, propriété intellectuelle et politique de données personnelles "
     "du site Art Impact.",
     MENTIONS),
]


# --------------------------------------------------------------------------
# Donnees structurees (JSON-LD) — comprehension par Google et par les IA
# --------------------------------------------------------------------------
import json as _json
from datetime import date as _date

# Fil d'Ariane : slug -> libelle affiche dans les resultats de recherche
FIL = {
    "think-tank.html": "Le Think Tank",
    "rce.html": "Responsabilité Culturelle des Entreprises",
    "observatoire.html": "Observatoire National RCE",
    "programmes.html": "Programmes & Territoires",
    "ressources.html": "Ressources",
    "evenements.html": "Événements",
    "art-for-good.html": "Art for Good",
    "go-for-art.html": "Go-for-Art.com",
    "presse.html": "Presse & Médias",
    "contact.html": "Contact",
    "mentions-legales.html": "Mentions légales",
    "merci.html": "Merci",
}

# Questions reellement posees sur le sujet : ce sont elles que les moteurs
# generatifs citent. Reponses courtes, autonomes, factuelles.
FAQ = {
    "rce.html": [
        ("Qu’est-ce que la Responsabilité Culturelle des Entreprises (RCE) ?",
         "La Responsabilité Culturelle des Entreprises (RCE) est un cadre qui intègre la culture "
         "dans la stratégie globale d’une organisation, au même niveau que l’environnement, le "
         "social ou la gouvernance. Elle repose sur quatre piliers : Engagement & Cohésion, "
         "Innovation & Créativité, Territoires & Attractivité, Environnement & Sensibilisation."),
        ("Quelle est la différence entre la RSE et la RCE ?",
         "La RSE structure l’engagement environnemental, social et de gouvernance d’une entreprise. "
         "La RCE ajoute la dimension culturelle de la responsabilité : elle ne se réduit ni au "
         "mécénat ni à la communication, mais engage la stratégie, les équipes, le territoire et "
         "la raison d’être de l’organisation."),
        ("Quels sont les 4 piliers de la RCE ?",
         "Les quatre piliers de la RCE sont : 1) Engagement & Cohésion, la culture comme lien et "
         "énergie collective ; 2) Innovation & Créativité, la culture comme capacité à inventer ; "
         "3) Territoires & Attractivité, la culture comme moteur de développement local ; "
         "4) Environnement & Sensibilisation, la culture comme vecteur de conscience écologique."),
        ("Comment mettre en place une démarche RCE dans son entreprise ?",
         "Une démarche RCE se déroule en quatre étapes : un diagnostic des actions culturelles "
         "existantes, un cadrage stratégique définissant les priorités par pilier et les "
         "indicateurs, le déploiement des programmes avec les artistes et les acteurs du "
         "territoire, puis la mesure et la valorisation des effets obtenus."),
    ],
    "observatoire.html": [
        ("Qu’est-ce que l’Observatoire National RCE ?",
         "L’Observatoire National RCE est la première base de données française dédiée à l’impact "
         "culturel des organisations. Il produit un baromètre annuel, des études sectorielles, une "
         "cartographie nationale, des indicateurs et une méthodologie de référence."),
        ("Comment mesurer l’impact culturel d’une entreprise ?",
         "L’impact culturel se mesure à partir d’indicateurs partagés adossés aux quatre piliers "
         "de la RCE. L’Observatoire National RCE fournit une méthodologie de référence documentée "
         "qui permet à une organisation de situer ses actions, de se comparer à son secteur et de "
         "suivre sa progression dans le temps."),
    ],
    "think-tank.html": [
        ("Qu’est-ce qu’Art Impact ?",
         "Art Impact est le think tank français qui place la culture au cœur des stratégies "
         "d’impact des entreprises et des territoires. Il produit des analyses, des référentiels, "
         "des données et des programmes autour de la Responsabilité Culturelle des Entreprises "
         "(RCE). Il est porté par l’association Art for Good."),
    ],
    "index.html": [
        ("Pourquoi la culture est-elle un levier d’impact pour les entreprises ?",
         "La culture agit sur quatre dimensions mesurables : elle renforce la cohésion interne et "
         "l’engagement des équipes, stimule la créativité et la capacité d’innovation, nourrit "
         "l’attractivité des territoires, et sensibilise aux enjeux environnementaux par "
         "l’émotion et l’expérience plutôt que par la seule donnée."),
    ],
}


def faq_html(slug):
    """Rend la FAQ visible : Google exige que le balisage FAQPage corresponde
    a du contenu reellement affiche, et les moteurs generatifs citent ces
    reponses courtes et autonomes."""
    if slug not in FAQ:
        return ""
    items = "\n".join(
        """      <details class="qa"{ouvert}>
        <summary><h3>{q}</h3></summary>
        <p>{r}</p>
      </details>""".format(q=q, r=r, ouvert=" open" if i == 0 else "")
        for i, (q, r) in enumerate(FAQ[slug])
    )
    return """
<section class="sec sec-alt" id="questions">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Questions fréquentes</p>
      <h2>Ce qu'il faut retenir</h2>
    </div>
    <div class="faq reveal">
{items}
    </div>
  </div>
</section>
""".replace("{items}", items)


def jsonld_page(slug, title, desc):
    """Construit le graphe de donnees structurees d une page."""
    url = SITE + "/" + ("" if slug == "index.html" else slug)
    org_id, site_id = SITE + "/#organisation", SITE + "/#site"

    organisation = {
        "@type": ["Organization", "NGO"], "@id": org_id,
        "name": "Art Impact",
        "alternateName": "Think Tank de la Responsabilité Culturelle des Entreprises",
        "url": SITE, "email": EMAIL,
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/og-image.jpg",
                 "width": 1200, "height": 630},
        "image": SITE + "/assets/img/og-image.jpg",
        "description": "Art Impact est le think tank qui place la culture au cœur des stratégies "
                       "d’impact des entreprises et des territoires.",
        "areaServed": {"@type": "Country", "name": "France"},
        "knowsAbout": ["Responsabilité Culturelle des Entreprises", "RCE", "impact culturel",
                       "mécénat culturel", "RSE", "attractivité territoriale",
                       "politique culturelle", "engagement des salariés"],
        "parentOrganization": {"@type": "NGO", "name": "Art for Good", "url": HELLOASSO},
        "contactPoint": [{"@type": "ContactPoint", "email": EMAIL,
                          "contactType": "informations", "availableLanguage": "French"},
                         {"@type": "ContactPoint", "email": EMAIL_PRESSE,
                          "contactType": "presse", "availableLanguage": "French"}],
    }

    site_web = {
        "@type": "WebSite", "@id": site_id, "url": SITE, "name": "Art Impact",
        "inLanguage": "fr-FR", "publisher": {"@id": org_id},
    }

    page = {
        "@type": "WebPage", "@id": url + "#page", "url": url,
        "name": title, "description": desc, "inLanguage": "fr-FR",
        "isPartOf": {"@id": site_id}, "about": {"@id": org_id},
        "primaryImageOfPage": SITE + "/assets/img/og-image.jpg",
        "breadcrumb": {"@id": url + "#fil"},
    }

    graphe = [organisation, site_web, page]

    fil = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}]
    if slug in FIL:
        fil.append({"@type": "ListItem", "position": 2, "name": FIL[slug], "item": url})
    graphe.append({"@type": "BreadcrumbList", "@id": url + "#fil", "itemListElement": fil})

    if slug in FAQ:
        graphe.append({
            "@type": "FAQPage", "@id": url + "#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": r}}
                           for q, r in FAQ[slug]],
        })

    return _json.dumps({"@context": "https://schema.org", "@graph": graphe},
                       ensure_ascii=False, separators=(",", ":"))


def ecrire_llms():
    """llms.txt : standard emergent qui donne aux moteurs generatifs une
    synthese fiable du site, en Markdown, sans avoir a interpreter le HTML."""
    txt = """# Art Impact

> Art Impact est le think tank français qui place la culture au cœur des stratégies
> d’impact des entreprises et des territoires. Il structure et diffuse la
> Responsabilité Culturelle des Entreprises (RCE).

Art Impact produit des analyses, des référentiels, des données, des programmes et des
alliances pour faire de la culture un levier stratégique reconnu, mesurable et durable.
Le think tank est porté par l’association Art for Good.

## Définitions de référence

- **Responsabilité Culturelle des Entreprises (RCE)** : cadre qui intègre la culture dans
  la stratégie globale d’une organisation, au même niveau que l’environnement, le social
  ou la gouvernance. Elle repose sur quatre piliers.
- **Les 4 piliers de la RCE** : Engagement & Cohésion ; Innovation & Créativité ;
  Territoires & Attractivité ; Environnement & Sensibilisation.
- **Observatoire National RCE** : première base de données française dédiée à l’impact
  culturel des organisations (baromètre annuel, études sectorielles, cartographie
  nationale, indicateurs, méthodologie de référence).
- **Différence RSE / RCE** : la RSE couvre l’environnemental, le social et la gouvernance ;
  la RCE ajoute la dimension culturelle, au-delà du mécénat et de la communication.

## Pages principales

- [Accueil](SITEURL/) : l’ambition et la vision d’Art Impact.
- [Le Think Tank](SITEURL/think-tank.html) : raison d’être, rôle, méthode en trois temps.
- [La RCE](SITEURL/rce.html) : définition, 4 piliers, mise en œuvre du diagnostic au déploiement.
- [Observatoire National RCE](SITEURL/observatoire.html) : la mesure de l’impact culturel.
- [Programmes & Territoires](SITEURL/programmes.html) : Art & Cohésion, Art & Innovation,
  Art & Environnement, Art & Attractivité territoriale.
- [Plateforme de ressources](SITEURL/ressources.html) : notes d’analyse, rapports, guides,
  vidéos, webinaires, bibliothèque RCE.
- [Événements](SITEURL/evenements.html) : Art Impact Live, rencontres entreprises, ateliers
  territoriaux, conférences, Marathon de l’Art 2027.

## Écosystème

- [Art for Good](SITEURL/art-for-good.html) : l’association fondatrice qui porte Art Impact.
- [Go-for-Art.com](SITEURL/go-for-art.html) : plateforme phygitale d’accès à l’art
  (expositions, QR codes, parcours culturels).

## Contact

- [Contact](SITEURL/contact.html) — ADRMAIL
- [Presse & Médias](SITEURL/presse.html) — ADRPRESSE

## Citation

Source à citer : Art Impact, think tank de la Responsabilité Culturelle des Entreprises,
SITEURL
"""
    txt = (txt.replace("SITEURL", SITE)
              .replace("ADRPRESSE", EMAIL_PRESSE)
              .replace("ADRMAIL", EMAIL))
    (ROOT / "llms.txt").write_text(txt, encoding="utf-8")
    print("  + llms.txt")


def build():
    for slug, title, desc, body in PAGES:
        nav = "\n      ".join(
            '<li><a href="{h}"{cur}>{label}</a></li>'.format(
                h=href, label=label,
                cur=' aria-current="page"' if href == slug else "")
            for href, label in NAV
        )
        body = body.format(
            email=EMAIL, email_presse=EMAIL_PRESSE,
            helloasso=HELLOASSO, form=FORM_ENDPOINT, site=SITE,
            w3key=WEB3FORMS_KEY,
        ) if "{" in body else body
        body = body + faq_html(slug)
        html = TEMPLATE.format(
            jsonld=jsonld_page(slug, title.replace("&amp;", "&"), desc),
            title=title, desc=desc.replace('"', "&quot;"),
            slug="" if slug == "index.html" else slug,
            site=SITE, email=EMAIL, helloasso=HELLOASSO,
            nav=nav, body=body,
        )
        (ROOT / slug).write_text(html, encoding="utf-8")
        print("  +", slug)

    # sitemap.xml
    urls = "\n".join(
        "  <url><loc>{}/{}</loc><lastmod>{}</lastmod>"
        "<changefreq>monthly</changefreq><priority>{}</priority></url>".format(
            SITE, "" if s == "index.html" else s, _date.today().isoformat(),
            "1.0" if s == "index.html" else "0.8")
        for s, _, _, _ in PAGES if s != "merci.html"
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "\n</urlset>\n", encoding="utf-8")
    print("  + sitemap.xml")

    # Autorisation explicite des robots d indexation ET des moteurs generatifs.
    # Sans mention, certains crawlers IA s abstiennent par defaut.
    ia = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User",
          "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Perplexity-User",
          "Google-Extended", "Applebot", "Applebot-Extended", "Bingbot",
          "meta-externalagent", "Amazonbot", "DuckAssistBot", "cohere-ai",
          "MistralAI-User", "YouBot"]
    lignes = ["User-agent: *", "Allow: /", ""]
    for bot in ia:
        lignes += ["User-agent: " + bot, "Allow: /", ""]
    lignes += ["Sitemap: {}/sitemap.xml".format(SITE), ""]
    (ROOT / "robots.txt").write_text("\n".join(lignes), encoding="utf-8")
    print("  + robots.txt")
    ecrire_llms()
    print("  + robots.txt")


if __name__ == "__main__":
    print("Construction du site Art Impact…")
    build()
    print("Terminé.")
