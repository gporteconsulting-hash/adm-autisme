#!/usr/bin/env python3
"""Assemble les pages du site à partir des contenus de _build/pages.py.
Lancer depuis la racine du site : python3 _build/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, ETAPES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MENU = [
    ("index.html", "Accueil"),
    ("dossier-mdph.html", "Dossier MDPH et droits"),
    ("education.html", "Éducation"),
    ("international.html", "International"),
    ("notre-histoire.html", "Notre histoire"),
]
SOUS_MENU_MDPH = [
    ("dossier-mdph.html", "La rubrique"),
    ("etapes/comment-deposer.html", "Le parcours en 9 étapes"),
    ("projet-de-vie.html", "Mon projet de vie"),
    ("mes-droits.html", "Mes droits"),
    ("etapes/situation-urgente.html", "Situation urgente"),
]

def rubrique(path):
    if path.startswith(("etapes/", "droits/")) or path in ("dossier-mdph.html", "projet-de-vie.html", "mes-droits.html"):
        return "dossier-mdph.html"
    return path

def rel(path, target):
    depth = path.count("/")
    return "../" * depth + target

def head(path, title):
    r = lambda t: rel(path, t)
    menu = "\n".join(
        f'<a href="{r(h)}"{" aria-current=\"page\"" if h == rubrique(path) else ""}>{label}</a>' for h, label in MENU)
    sous = ""
    if rubrique(path) == "dossier-mdph.html":
        actif = lambda h: h == path or (h == "etapes/comment-deposer.html" and path.startswith("etapes/") and path != "etapes/situation-urgente.html") or (h == "mes-droits.html" and path.startswith("droits/"))
        sous = '<nav class="sous-menu" aria-label="Dossier MDPH et droits"><div class="wrap">' + "".join(
            f'<a href="{r(h)}"{" aria-current=\"page\"" if actif(h) else ""}>{label}</a>' for h, label in SOUS_MENU_MDPH) + "</div></nav>"
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – ADM Autisme</title>
<meta name="description" content="ADM Autisme – Autour de Mohamed : un guide gratuit pour aider les familles à constituer elles-mêmes leur dossier MDPH et faire valoir les droits de leur enfant autiste.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r('assets/css/style.css')}">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site">
<div class="wrap">
<a class="marque" href="{r('index.html')}">ADM Autisme <span>– Autour de Mohamed</span></a>
<nav class="menu" aria-label="Menu principal">
{menu}
</nav>
</div>
{sous}
</header>
<main id="contenu">
"""

def foot(path, scripts=""):
    r = lambda t: rel(path, t)
    return f"""</main>
<footer class="site">
<div class="wrap">
<div class="stack" style="gap:6px;max-width:420px">
<strong>ADM Autisme – Autour de Mohamed</strong>
<span>Association fondée en 2014 · L'Isle-d'Abeau (38080), Nord-Isère</span>
<span>Président : Grégory Porte, consultant en autisme</span>
<span>E-mail : <a href="mailto:gporte.consulting@gmail.com">gporte.consulting@gmail.com</a></span>
<span>Téléphone : <a href="tel:+33972190922">09 72 19 09 22</a> · Portable et WhatsApp : <a href="tel:+33675404376">06 75 40 43 76</a></span>
</div>
<div class="stack" style="gap:6px;max-width:460px">
<span>Informations juridiques vérifiées en novembre 2026.</span>
<span>Ce guide aide les familles à préparer leur dossier. Il ne remplace pas un conseil juridique.</span>
<a href="{r('mentions-legales.html')}">Mentions légales</a>
</div>
</div>
</footer>
{scripts}
</body>
</html>
"""

def etapes_nav(path):
    r = lambda t: rel(path, t)
    links = "\n".join(
        f'<a href="{r(h)}"{" aria-current=\"page\"" if h == path else ""}>{i}. {t}</a>'
        for i, (h, t) in enumerate(ETAPES, 1))
    return f'<nav class="etapes-nav" aria-label="Les étapes du dossier"><strong>Les étapes</strong>\n{links}\n</nav>'

def suite(path):
    r = lambda t: rel(path, t)
    paths = [h for h, _ in ETAPES]
    if path not in paths:
        return ""
    i = paths.index(path)
    prev = f'<a class="btn clair" href="{r(ETAPES[i-1][0])}">← {ETAPES[i-1][1]}</a>' if i > 0 else '<span></span>'
    nxt = f'<a class="btn" href="{r(ETAPES[i+1][0])}">{ETAPES[i+1][1]} →</a>' if i < len(ETAPES) - 1 else ''
    return f'<div class="suite">{prev}{nxt}</div>'

for p in PAGES:
    path = p["path"]
    body = p["body"].replace("{R}", "../" * path.count("/"))
    if p.get("etape"):
        body = f"""<div class="wrap fil"><a href="{rel(path,'dossier-mdph.html')}">Dossier MDPH et droits</a> › {p['title']}</div>
<section class="band" style="padding-top:20px"><div class="wrap page">
<div class="contenu">
{body}
{suite(path)}
</div>
{etapes_nav(path)}
</div></section>"""
    scripts = p.get("scripts", "").replace("{R}", "../" * path.count("/"))
    out = head(path, p["title"]) + body + foot(path, scripts)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(out)
    print("écrit", path)
