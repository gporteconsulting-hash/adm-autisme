# Contenus des pages du site ADM Autisme.
# {R} = chemin relatif vers la racine du site.

ETAPES = [
    ("etapes/comment-deposer.html", "Comment déposer ?"),
    ("etapes/pieces.html", "Les pièces à réunir"),
    ("etapes/certificat-medical.html", "Le certificat médical"),
    ("etapes/formulaire.html", "Remplir le formulaire"),
    ("etapes/projet-de-vie.html", "Le projet de vie"),
    ("etapes/situation-urgente.html", "Situation urgente"),
    ("etapes/deposer.html", "Déposer le dossier"),
    ("etapes/apres-le-depot.html", "Après le dépôt"),
    ("etapes/decision-et-recours.html", "La décision et les recours"),
]

PAGES = []

def page(path, title, body, etape=False, scripts=""):
    PAGES.append({"path": path, "title": title, "body": body, "etape": etape, "scripts": scripts})

# ---------------------------------------------------------------- Accueil
cartes_etapes = "\n".join(
    f'<a class="carte" href="{{R}}{h}"><span class="num">{i}</span><span class="titre">{t}</span></a>'
    for i, (h, t) in enumerate(ETAPES, 1))

page("index.html", "Accueil", f"""
<section class="couverture">
<img src="{{R}}assets/img/couverture.jpg" alt="ADM Autisme – Autour de Mohamed. Un enfant brise la bulle qui l'entoure pour rejoindre les autres enfants. Vers un monde plus adapté au TSA. Engagement international." width="1536" height="1024">
</section>
<section class="intro band">
<div class="wrap row" style="align-items:flex-end;justify-content:space-between">
<div class="grow stack">
<p style="font-weight:700;color:var(--bleu)">Un guide gratuit pour les familles</p>
<h1>Votre dossier MDPH, étape par étape. Et par vous-même.</h1>
<p class="lead">Des explications claires, des modèles à compléter et les textes de loi pour faire valoir les droits de votre enfant.</p>
<p class="slogan">Ce ne sont pas des faveurs. Ce sont des droits.</p>
</div>
<div class="btns">
<a class="btn" href="{{R}}etapes/comment-deposer.html">Commencer mon dossier</a>
<a class="btn clair" href="{{R}}etapes/situation-urgente.html">Ma situation est urgente</a>
</div>
</div>
</section>

<section class="bandeau-jaune">
<div class="wrap">
<img src="{{R}}assets/img/depot.jpg" alt="" loading="lazy">
<div class="texte">
<strong>N'attendez pas d'avoir tout pour déposer.</strong>
<p>Votre formulaire, le certificat médical et les pièces obligatoires sont prêts, mais un bilan est encore en attente ? Déposez déjà votre dossier : vous enverrez les documents manquants dès que vous les aurez.</p>
<p>Pourquoi ? Le droit à l'AEEH s'ouvre le 1er jour du mois qui suit le dépôt. Chaque mois d'attente peut être un mois de droits en moins.</p>
</div>
</div>
</section>

<section class="band">
<div class="wrap stack" style="gap:28px">
<div class="row" style="justify-content:space-between">
<div class="grow stack" style="max-width:640px">
<h2>Le parcours, en 9 étapes</h2>
<p>Suivez les étapes dans l'ordre, ou allez directement à celle dont vous avez besoin.</p>
</div>
<img class="photo" src="{{R}}assets/img/formulaire.jpg" alt="Des mains remplissent un formulaire administratif à côté d'un ordinateur portable" loading="lazy">
</div>
<div class="grille">
{cartes_etapes}
</div>
</div>
</section>

<section class="band bleu">
<div class="wrap row">
<img class="photo" src="{{R}}assets/img/generateur.jpg" alt="Des mains tapent sur un ordinateur à côté d'une liste de cases cochées" loading="lazy">
<div class="grow stack">
<p style="font-weight:700;color:var(--jaune)">L'outil phare du site</p>
<h2>Votre projet de vie : cochez, téléchargez, complétez</h2>
<p class="muted">Cochez tout ce qui correspond à votre situation. Le site prépare une base de projet de vie au format Word, avec les arguments et les articles de loi. Il ne vous reste qu'à compléter les trous et à l'adapter à votre famille.</p>
<div><a class="btn jaune" href="{{R}}etapes/projet-de-vie.html">Préparer mon projet de vie</a></div>
</div>
</div>
</section>

<section class="band pale">
<div class="wrap stack" style="gap:28px">
<div class="row" style="justify-content:space-between">
<div class="grow stack" style="max-width:640px">
<h2>Mes droits, classés simplement</h2>
<p>Partez de votre question. Chaque rubrique explique à quoi sert le droit, comment le demander et comment le justifier.</p>
</div>
<img class="photo" src="{{R}}assets/img/communication.jpg" alt="Une main d'enfant touche une tablette de communication avec des pictogrammes" loading="lazy">
</div>
<div class="grille">
<a class="carte" href="{{R}}mes-droits.html#revenus"><span class="titre">Compenser l'arrêt du travail et les frais</span><span>AEEH et compléments, PCH, droits du parent aidant</span></a>
<a class="carte" href="{{R}}mes-droits.html#ecole"><span class="titre">Scolariser mon enfant</span><span>AESH, UEMA, UEEA, ULIS</span></a>
<a class="carte" href="{{R}}mes-droits.html#accompagnement"><span class="titre">L'accompagnement spécialisé</span><span>SESSAD, IME</span></a>
<a class="carte" href="{{R}}mes-droits.html#equiper"><span class="titre">Équiper et sécuriser</span><span>Tablette de communication, logement, véhicule</span></a>
<a class="carte" href="{{R}}mes-droits.html#deplacer"><span class="titre">Se déplacer</span><span>Carte mobilité inclusion : priorité, stationnement</span></a>
</div>
</div>
</section>

<section class="band orange">
<div class="wrap row" style="justify-content:space-between">
<img src="{{R}}assets/img/entraide.jpg" alt="" style="width:200px;aspect-ratio:1;object-fit:cover;border-radius:20px" loading="lazy">
<div class="grow stack">
<h2>Votre situation ne peut pas attendre ?</h2>
<p style="font-size:18px">Demandez que votre dossier soit examiné en priorité, avec l'appui d'une synthèse sociale.</p>
<p style="font-size:16px"><strong>Le saviez-vous ?</strong> L'éducateur spécialisé ou le moniteur éducateur qui suit votre enfant, même en libéral, peut rédiger cette synthèse sociale.</p>
</div>
<a class="btn sombre" href="{{R}}etapes/situation-urgente.html">Comment faire</a>
</div>
</section>

<section class="band">
<div class="wrap row" style="align-items:flex-start">
<div class="grow stack">
<h2>ADM Autisme – Autour de Mohamed</h2>
<p>Notre association est née en 2014, autour de notre fils Mohamed. Autiste sévère et non oralisant, il vit aussi avec plusieurs maladies venues s'ajouter au fil des années. Nos premiers dossiers MDPH ont été refusés, encore et encore : notre situation était grave, mais nous ne savions pas l'exprimer.</p>
<p>Nous avons appris à nous outiller et à nous appuyer sur la loi. Puis nous avons aidé d'autres familles à monter leurs dossiers : plus de 90 % de leurs demandes ont été acceptées, en première demande ou après recours.</p>
<p style="font-weight:700;color:var(--marine)">Ce site transmet ce que nous avons appris, pour que chaque famille puisse se débrouiller par elle-même.</p>
<div><a class="btn clair" href="{{R}}notre-histoire.html">Lire notre histoire</a></div>
</div>
</div>
</section>
""")

# ---------------------------------------------------------------- Dossier MDPH (vue d'ensemble)
page("dossier-mdph.html", "Mon dossier MDPH", f"""
<section class="band intro">
<div class="wrap stack" style="gap:28px">
<div class="stack" style="max-width:720px">
<h1>Mon dossier MDPH, étape par étape</h1>
<p class="lead">Neuf étapes, du choix du mode de dépôt jusqu'à la décision. Commencez par la première, ou allez directement à celle dont vous avez besoin.</p>
</div>
<div class="grille">
{cartes_etapes}
</div>
<div class="encadre astuce"><span class="etiquette">Astuce</span><p>N'attendez pas d'avoir tout pour déposer : dès que le formulaire, le certificat médical et les pièces obligatoires sont prêts, déposez. Les bilans en attente suivront.</p></div>
</div>
</section>
""")

# ---------------------------------------------------------------- Étape 1
page("etapes/comment-deposer.html", "Comment déposer ?", """
<h1>Étape 1 · Comment déposer mon dossier ?</h1>
<p class="lead">Vous avez deux possibilités. Elles ont la même valeur : choisissez celle qui vous convient le mieux.</p>
<div class="choix">
<div class="carte">
<span class="titre">En ligne</span>
<p>Vous remplissez le dossier sur internet et vous joignez les pièces scannées ou photographiées.</p>
<ul>
<li>Pratique et rapide, sans déplacement.</li>
<li>Vous recevez une confirmation de dépôt.</li>
<li>Disponible si votre MDPH propose le service « MDPH en ligne ».</li>
</ul>
<a class="btn" href="https://mdphenligne.cnsa.fr" rel="noopener">Aller sur MDPH en ligne</a>
</div>
<div class="carte">
<span class="titre">Sur papier</span>
<p>Vous imprimez le formulaire, vous le remplissez, puis vous le déposez à l'accueil de votre MDPH ou vous l'envoyez par courrier.</p>
<ul>
<li>Par courrier : en recommandé avec accusé de réception, pour garder une preuve de la date.</li>
<li>À l'accueil : demandez un récépissé de dépôt.</li>
</ul>
<a class="btn clair" href="https://www.monparcourshandicap.gouv.fr/aides/formulaire-de-demande-la-mdph-cerfa-ndeg-1569201" rel="noopener">Télécharger le formulaire (Cerfa 15692*01)</a>
</div>
</div>
<div class="encadre astuce"><span class="etiquette">Astuce</span><p>Quel que soit votre choix, gardez une copie complète de tout ce que vous envoyez. Vous en aurez besoin pour suivre votre dossier et, si besoin, pour un recours.</p></div>
<h2>Les deux documents à avoir dans tous les cas</h2>
<ul>
<li><strong>Le formulaire de demande</strong> (Cerfa n° 15692*01) : le même pour les enfants et les adultes.</li>
<li><strong>Le certificat médical</strong> (Cerfa n° 15695*01) : rempli par le médecin qui suit votre enfant. <a href="https://www.monparcourshandicap.gouv.fr/demarches/certificat-medical-formulaire-cerfa-ndeg-1569501" rel="noopener">Le télécharger</a>.</li>
</ul>
<p>En Isère, votre interlocuteur est la Maison départementale de l'autonomie (MDA), qui joue le rôle de MDPH.</p>
""", etape=True)

# ---------------------------------------------------------------- Étape 2
page("etapes/pieces.html", "Les pièces à réunir", """
<h1>Étape 2 · Les pièces à réunir</h1>
<p class="lead">Certaines pièces sont obligatoires : sans elles, le dossier n'est pas enregistré. D'autres ne sont pas obligatoires, mais ce sont souvent elles qui font la différence.</p>
<img class="photo" src="{R}assets/img/classeur.jpg" alt="Des mains rangent des feuilles dans un classeur à intercalaires de couleur" style="width:100%;max-width:520px" loading="lazy">
<h2>Les pièces obligatoires</h2>
<ul class="coche">
<li>Le formulaire de demande, complété, daté et signé.</li>
<li>Le certificat médical original, rempli par le médecin.</li>
<li>Une pièce d'identité de votre enfant et de son représentant légal (vous).</li>
<li>Un justificatif de domicile.</li>
</ul>
<div class="encadre attention"><span class="etiquette">Attention</span><p>Selon les MDPH, le certificat médical doit dater de moins de 6 mois ou de moins d'un an. Vérifiez auprès de la vôtre.</p></div>
<h2>Les pièces qui font la différence</h2>
<table>
<thead><tr><th>Pour quelle demande ?</th><th>Pièces utiles</th></tr></thead>
<tbody>
<tr><td>Toutes les demandes</td><td>Compte rendu du diagnostic, bilans (orthophonie, psychomotricité, ergothérapie, psychologue), attestations des professionnels qui suivent votre enfant.</td></tr>
<tr><td>Scolarité (AESH, orientation)</td><td>Le GEVA-Sco rempli par l'école, les comptes rendus des réunions de suivi.</td></tr>
<tr><td>Complément d'AEEH (travail)</td><td>Fiches de paie, avenant au contrat, lettre de démission ou de licenciement, rupture conventionnelle, déclarations URSSAF (auto-entrepreneur).</td></tr>
<tr><td>Frais liés au handicap</td><td>Factures, devis, relevés de dépenses non remboursées.</td></tr>
<tr><td>Matériel (PCH)</td><td>Plusieurs devis pour le même matériel.</td></tr>
</tbody>
</table>
<div class="encadre astuce"><span class="etiquette">Astuce</span><p>Tenez un carnet de bord : crises, appels de l'école, rendez-vous, frais. Ces notes deviennent des preuves pour votre projet de vie.</p></div>
""", etape=True)

# ---------------------------------------------------------------- Étape 3
page("etapes/certificat-medical.html", "Le certificat médical", """
<h1>Étape 3 · Le certificat médical</h1>
<p class="lead">C'est une pièce obligatoire, et l'une des plus importantes. La MDPH s'en sert pour comprendre la situation de votre enfant.</p>
<h2>Ce qui compte vraiment</h2>
<p>Le diagnostic ne suffit pas. Ce que la MDPH veut savoir, c'est <strong>l'impact du handicap sur la vie de tous les jours</strong> : ce que votre enfant ne peut pas faire seul, l'aide dont il a besoin, la surveillance qu'il demande, les soins et les rendez-vous.</p>
<h2>Comment bien préparer le rendez-vous</h2>
<ol>
<li>Prenez un rendez-vous dédié au certificat, pas une consultation pour autre chose.</li>
<li>Apportez une liste des difficultés du quotidien (repas, toilette, sommeil, communication, comportement, mise en danger).</li>
<li>Apportez les derniers bilans et comptes rendus.</li>
<li>Relisez le certificat avant de partir : tout ce qui compte doit y être.</li>
</ol>
<div class="encadre attention"><span class="etiquette">Attention</span><p>Le certificat « simplifié » n'est possible que si la situation n'a pas changé depuis le dernier certificat. Si elle a changé, demandez le certificat complet.</p></div>
<a class="btn clair" href="https://www.monparcourshandicap.gouv.fr/demarches/certificat-medical-formulaire-cerfa-ndeg-1569501" rel="noopener">Télécharger le certificat médical (Cerfa 15695*01)</a>
""", etape=True)

# ---------------------------------------------------------------- Étape 4
page("etapes/formulaire.html", "Remplir le formulaire", """
<h1>Étape 4 · Remplir le formulaire</h1>
<p class="lead">Le formulaire est le même pour toutes les demandes. Vous ne remplissez que les parties qui vous concernent.</p>
<h2>D'abord : quel type de demande ?</h2>
<ul>
<li><strong>Première demande</strong> : vous n'avez jamais déposé de dossier.</li>
<li><strong>Renouvellement</strong> : un droit arrive à sa fin. Faites-le 6 mois avant la date de fin.</li>
<li><strong>Révision</strong> : la situation a changé avant la fin d'un droit.</li>
</ul>
<h2>Les parties du formulaire</h2>
<table>
<thead><tr><th>Partie</th><th>Ce qu'elle contient</th></tr></thead>
<tbody>
<tr><td>A · Identité</td><td>Votre enfant, ses représentants légaux, l'aidant familial.</td></tr>
<tr><td>B · Vie quotidienne</td><td>Les difficultés au quotidien, les besoins, et l'expression de vos attentes : c'est la place du projet de vie.</td></tr>
<tr><td>C · Scolarité</td><td>La situation scolaire, les besoins à l'école.</td></tr>
<tr><td>D · Situation professionnelle</td><td>Pour les adultes concernés par la demande.</td></tr>
<tr><td>E · Demandes</td><td>Les droits et aides que vous demandez.</td></tr>
<tr><td>F · Aidant familial</td><td>La situation et les besoins du parent aidant.</td></tr>
</tbody>
</table>
<div class="encadre astuce"><span class="etiquette">Astuce</span><p>Ne laissez pas une case vide parce que « ça va de soi ». Ce qui n'est pas écrit n'existe pas pour la commission.</p></div>
""", etape=True)

# ---------------------------------------------------------------- Étape 5 : présentation (l'outil est sur sa propre page)
page("etapes/projet-de-vie.html", "Le projet de vie", """
<h1>Étape 5 · Le projet de vie</h1>
<p class="lead">C'est la partie du dossier où vous expliquez, avec vos mots, votre quotidien et ce dont votre enfant a besoin. C'est souvent elle qui fait la différence.</p>
<h2>Ce qu'un bon projet de vie contient</h2>
<ul>
<li>La situation de votre enfant, avec des faits concrets plutôt que des généralités.</li>
<li>Les conséquences sur votre famille, y compris sur votre travail.</li>
<li>Chaque demande, justifiée par un fait de votre quotidien et, si possible, par une pièce jointe.</li>
<li>Les articles de loi sur lesquels vos demandes s'appuient.</li>
</ul>
<div class="encadre astuce"><span class="etiquette">Astuce</span><p>Ni trop long, ni trop court : précis. Ce qui n'est pas écrit n'existe pas pour la commission.</p></div>
<div class="appel-outil">
<p class="titre-outil">Besoin d'aide pour l'écrire ?</p>
<p>Notre outil vous aide à construire une base de projet de vie : vous cochez votre situation, il prépare un document Word à compléter.</p>
<a class="btn jaune" href="{R}projet-de-vie.html">Aide-moi à préparer mon projet de vie</a>
</div>
""", etape=True)

# ---------------------------------------------------------------- Outil projet de vie (page à part)
page("projet-de-vie.html", "Mon projet de vie", """
<section class="gen-hero">
<div class="wrap stack" style="gap:14px">
<p class="sur-titre">Outil gratuit</p>
<h1>Aide-moi à préparer mon projet de vie</h1>
<p class="lead">Cochez tout ce qui correspond à votre situation. Touchez les bulles <span class="info-demo" aria-hidden="true">i</span> pour voir les articles de loi et nos astuces. À la fin, téléchargez votre base de projet de vie au format Word, à compléter et à modifier.</p>
<ol class="gen-etapes">
<li><span>1</span>Je coche ma situation</li>
<li><span>2</span>Je regarde l'aperçu</li>
<li><span>3</span>Je télécharge mon Word</li>
<li><span>4</span>Je complète les passages en jaune</li>
</ol>
</div>
</section>
<section class="band" style="padding-top:28px">
<div class="wrap">
<div class="encadre attention" style="margin-bottom:22px"><span class="etiquette">Vos informations restent chez vous</span><p>Rien de ce que vous cochez ou écrivez ici n'est envoyé ni enregistré. Le document est fabriqué directement sur votre ordinateur ou votre téléphone.</p></div>
<div class="gen" id="generateur">
<form id="choix" onsubmit="return false">
<fieldset class="groupe g0">
<legend><span class="pastille">1</span>Votre enfant</legend>
<div class="champs">
<div class="champ"><label for="prenom" style="display:block">Prénom de votre enfant (facultatif)</label><input type="text" id="prenom" autocomplete="off"></div>
<div class="champ"><label for="age" style="display:block">Âge (facultatif)</label><input type="text" id="age" autocomplete="off"></div>
</div>
</fieldset>
<div id="groupes"></div>
</form>
<div class="apercu" aria-live="polite">
<div class="apercu-tete"><strong>Aperçu de votre projet de vie</strong><span id="compteur" class="compteur">0 élément coché</span></div>
<div id="apercu" class="feuille"></div>
<div class="actions">
<button type="button" class="btn" id="telecharger">Télécharger mon modèle Word</button>
<span class="muted" style="font-size:14px">Les passages surlignés en jaune sont à compléter.</span>
</div>
</div>
</div>
</div>
</section>
""", scripts='<script src="{R}assets/js/docx.iife.js"></script>\n<script src="{R}assets/js/generateur.js"></script>')

# ---------------------------------------------------------------- Étape 6 : urgence
page("etapes/situation-urgente.html", "Situation urgente", """
<h1>Votre situation ne peut pas attendre ?</h1>
<p class="lead">Demandez que votre dossier soit examiné en priorité.</p>
<p>La MDPH a 4 mois pour répondre, et c'est souvent plus long en pratique. Quand la situation de votre famille est urgente, vous pouvez demander que votre dossier passe plus tôt en commission. Ce n'est pas automatique : c'est la MDPH qui décide. Mais un dossier qui montre clairement l'urgence a toutes ses chances d'être examiné en priorité.</p>
<h2>Qu'est-ce qu'une situation urgente ?</h2>
<ul>
<li>Votre enfant est déscolarisé, ou risque de l'être.</li>
<li>Votre enfant se met en danger, ou met en danger les autres.</li>
<li>Vous avez dû arrêter de travailler et vos ressources ne suffisent plus.</li>
<li>Vous risquez de perdre votre logement.</li>
<li>Vous êtes épuisé(e) et vous n'avez plus de relais.</li>
<li>Un accompagnement ou des soins vont s'arrêter.</li>
</ul>
<div class="encadre attention"><span class="etiquette">Attention</span><p>L'urgence doit être réelle et prouvée. Une demande d'urgence non justifiée ne fera pas avancer votre dossier, et elle peut affaiblir les suivantes.</p></div>
<h2>La clé : la synthèse sociale</h2>
<img class="photo" src="{R}assets/img/entraide.jpg" alt="Une personne tend un document à une autre, dans un geste d'entraide" style="width:100%;max-width:420px" loading="lazy">
<p>C'est un document rédigé par un travailleur social. Il reprend chacune de vos demandes et explique, avec un regard de professionnel, pourquoi elles sont justifiées. Il atteste aussi que votre situation est urgente et qu'attendre l'aggraverait. Pour la MDPH, c'est un avis extérieur et professionnel : il donne du poids à votre dossier.</p>
<p><strong>Qui peut la rédiger ?</strong> Tout professionnel qui a le statut de travailleur social : assistante sociale, éducateur spécialisé, moniteur éducateur, conseiller en économie sociale et familiale…</p>
<div class="encadre astuce"><span class="etiquette">Le saviez-vous ?</span><p>Un éducateur spécialisé ou un moniteur éducateur qui suit votre enfant, <strong>même en libéral</strong>, a le statut de travailleur social. Il peut donc rédiger une synthèse sociale pour votre dossier. Pensez à le lui demander : il connaît déjà votre enfant et votre quotidien.</p></div>
<h2>Où trouver un travailleur social ?</h2>
<ul>
<li>À la MDPH elle-même : demandez à rencontrer son assistante sociale.</li>
<li>Au CCAS de votre mairie, ou au centre médico-social de votre Département.</li>
<li>À la CAF.</li>
<li>À l'hôpital, au CMP ou au CAMSP qui suit votre enfant.</li>
<li>Auprès des professionnels qui accompagnent déjà votre enfant, y compris un éducateur spécialisé ou un moniteur éducateur en libéral.</li>
</ul>
<h2>Comment faire</h2>
<ol>
<li>Rassemblez les preuves de l'urgence : courriers de l'école, attestations, avis d'expulsion, arrêts de travail, carnet de bord…</li>
<li>Prenez rendez-vous avec un travailleur social et apportez-lui la trame ci-dessous.</li>
<li>Joignez la synthèse sociale à votre dossier, avec une lettre demandant un examen prioritaire.</li>
<li>Une à deux semaines après le dépôt, appelez la MDPH pour vérifier que la demande d'urgence a bien été prise en compte.</li>
</ol>
<h2>La trame de synthèse sociale, à apporter au rendez-vous</h2>
<ol>
<li><strong>Le professionnel</strong> : nom, fonction, service ; depuis quand et à quel titre il connaît la famille.</li>
<li><strong>La famille</strong> : composition, logement, ressources, situation professionnelle des parents.</li>
<li><strong>L'enfant au quotidien</strong> : ce que le professionnel a constaté lui-même.</li>
<li><strong>Les demandes de la famille</strong> : chaque demande, avec l'avis argumenté du professionnel.</li>
<li><strong>L'urgence</strong> : les risques concrets si le dossier tarde.</li>
<li><strong>Conclusion</strong> : une demande explicite d'examen prioritaire du dossier.</li>
</ol>
<h2>Bon à savoir</h2>
<ul>
<li>La commission peut utiliser une procédure simplifiée pour décider plus vite en cas d'urgence.</li>
<li>PCH : en cas d'urgence attestée, vous pouvez joindre à votre demande de PCH une demande particulière. Le président du Département doit alors statuer en 15 jours ouvrés et fixer un montant provisoire.</li>
</ul>
<div class="encadre loi"><span class="etiquette">La loi</span><p>Articles L.245-2 et R.245-36 du Code de l'action sociale et des familles ; arrêté du 27 juin 2006 (conditions de l'urgence attestée).</p></div>
""", etape=True)

# ---------------------------------------------------------------- Étape 7
page("etapes/deposer.html", "Déposer le dossier", """
<h1>Étape 7 · Déposer le dossier</h1>
<div class="encadre astuce"><span class="etiquette">N'attendez pas d'avoir tout pour déposer</span><p>Votre formulaire, le certificat médical et les pièces obligatoires sont prêts, mais un bilan est encore en attente ? Déposez déjà votre dossier : vous enverrez les documents manquants dès que vous les aurez. Le droit à l'AEEH s'ouvre le 1er jour du mois qui suit le dépôt : chaque mois d'attente peut être un mois de droits en moins.</p></div>
<h2>Avant d'envoyer, vérifiez</h2>
<ul class="coche">
<li>Le formulaire est daté et signé.</li>
<li>Le certificat médical est l'original.</li>
<li>Les pièces obligatoires sont jointes.</li>
<li>Le projet de vie est joint.</li>
<li>Vous avez gardé une copie complète de tout.</li>
</ul>
<h2>Gardez une preuve de la date</h2>
<ul>
<li>En ligne : enregistrez ou imprimez la confirmation.</li>
<li>Par courrier : recommandé avec accusé de réception.</li>
<li>À l'accueil : demandez un récépissé.</li>
</ul>
<p>Notez la date de dépôt : c'est elle qui compte pour l'ouverture de vos droits.</p>
""", etape=True)

# ---------------------------------------------------------------- Étape 8
page("etapes/apres-le-depot.html", "Après le dépôt", """
<h1>Étape 8 · Après le dépôt</h1>
<p class="lead">Votre dossier est déposé. Voici ce qui va se passer, et ce que vous pouvez faire.</p>
<h2>Le délai</h2>
<p>La MDPH a 4 mois pour répondre. Sans réponse au bout de 4 mois, la demande est considérée comme refusée, et vous pouvez faire un recours.</p>
<h2>Le plan de compensation</h2>
<p>Avant la décision, la MDPH peut vous envoyer une proposition de plan personnalisé de compensation. Vous avez 15 jours pour faire part de vos observations. Lisez-le attentivement : si une demande manque ou si un besoin est mal évalué, dites-le par écrit.</p>
<h2>Être entendu par la commission</h2>
<p>Vous pouvez demander à être reçu par la commission (CDAPH) qui prend la décision, et vous faire accompagner par la personne de votre choix.</p>
<div class="encadre astuce"><span class="etiquette">Astuce</span><p>Si un bilan arrive après le dépôt, envoyez-le tout de suite en rappelant votre numéro de dossier.</p></div>
""", etape=True)

# ---------------------------------------------------------------- Étape 9
page("etapes/decision-et-recours.html", "La décision et les recours", """
<h1>Étape 9 · La décision, et que faire en cas de refus</h1>
<h2>Lire la notification</h2>
<ul>
<li>Ce qui est accordé, et ce qui est refusé.</li>
<li>Le taux d'incapacité retenu.</li>
<li>La durée des droits : notez la date de fin, et prévoyez le renouvellement 6 mois avant.</li>
</ul>
<div class="encadre attention"><span class="etiquette">Attention</span><p>Une orientation n'est pas une place. Après une orientation vers un établissement ou un service, contactez vous-même les structures pour vous inscrire.</p></div>
<h2>En cas de refus : ne vous arrêtez pas là</h2>
<p>Beaucoup de familles abandonnent au premier refus. Pourtant, de nombreuses décisions changent après un recours bien argumenté.</p>
<ol>
<li><strong>Le recours administratif préalable obligatoire</strong> : un courrier à la MDPH, dans les 2 mois qui suivent la décision. Expliquez ce qui n'a pas été pris en compte, avec les articles de loi et les pièces qui le prouvent.</li>
<li><strong>Le recours en justice</strong>, si le premier recours n'aboutit pas.</li>
<li><strong>La conciliation</strong> et le <strong>Défenseur des droits</strong> peuvent aussi vous aider.</li>
</ol>
<div class="encadre loi"><span class="etiquette">Notre règle</span><p>Ne pas chercher la compassion, mais la reconnaissance de vos droits : réclamer ce qui est dû, et montrer précisément ce qui n'a pas été compensé comme la loi le prévoit.</p></div>
""", etape=True)

# ---------------------------------------------------------------- Mes droits
page("mes-droits.html", "Mes droits", """
<section class="band intro">
<div class="wrap stack" style="gap:24px;max-width:860px">
<h1>Mes droits, classés simplement</h1>
<p class="lead">Partez de la question que vous vous posez.</p>

<h2 id="revenus">Compenser l'arrêt du travail et les frais</h2>
<div class="carte"><span class="titre">AEEH et ses compléments</span><p>L'allocation d'éducation de l'enfant handicapé aide à faire face aux frais liés au handicap. Ses 6 compléments compensent en plus la réduction ou l'arrêt de l'activité d'un parent, l'embauche d'une personne pour s'occuper de l'enfant, ou des frais importants.</p><p><strong>Comment le prouver :</strong> fiches de paie, avenant au contrat, lettre de démission ou de licenciement, rupture conventionnelle ; pour un auto-entrepreneur, les déclarations URSSAF qui montrent la baisse du chiffre d'affaires.</p></div>
<div class="carte"><span class="titre">PCH (prestation de compensation du handicap)</span><p>Elle finance des besoins précis : aide humaine, matériel, aménagements, certains frais, aide animalière. Vous pouvez demander à la fois l'AEEH avec complément et la PCH : la MDPH évalue les deux, puis vous choisissez.</p><a href="{R}droits/pch.html">Tout comprendre sur la PCH →</a></div>
<div class="carte"><span class="titre">Les droits du parent aidant</span><p>Allocation journalière de présence parentale, assurance vieillesse du parent au foyer : arrêter de travailler pour son enfant ne doit pas coûter sa retraite. <em>Rubrique en préparation.</em></p></div>

<h2 id="ecole">Scolariser mon enfant</h2>
<div class="encadre loi"><span class="etiquette">Le fil rouge</span><p>L'école n'est pas une option : c'est une obligation et un droit pour tout enfant, y compris en situation de handicap.</p></div>
<div class="carte"><span class="titre">AESH</span><p>Un accompagnant à l'école. Demandez une aide humaine individuelle, avec un nombre d'heures, quand votre enfant a besoin d'un accompagnement continu.</p></div>
<div class="carte"><span class="titre">UEMA, UEEA, ULIS</span><p>Des classes adaptées : unités d'enseignement en maternelle (UEMA) ou en élémentaire (UEEA) pour les enfants autistes, ULIS pour un enseignement en petit groupe. Argument clé : permettre un temps de scolarisation complet, adapté au profil de l'enfant.</p></div>

<h2 id="accompagnement">L'accompagnement spécialisé</h2>
<div class="carte"><span class="titre">SESSAD, IME</span><p>Un service qui intervient là où vit l'enfant (SESSAD), ou un établissement spécialisé (IME). <em>Rubrique en préparation.</em></p></div>

<h2 id="equiper">Équiper et sécuriser</h2>
<div class="carte"><span class="titre">Tablette de communication et autre matériel</span><p>Financés par la PCH (aides techniques). La communication est un droit fondamental. Faites plusieurs devis, puis envoyez-les avec votre argumentation.</p></div>
<div class="carte"><span class="titre">Logement et véhicule</span><p>Sécuriser le logement contre les fugues, adapter le véhicule : c'est l'élément 3 de la PCH, le seul cumulable avec un complément d'AEEH.</p></div>

<h2 id="deplacer">Se déplacer</h2>
<div class="carte"><span class="titre">Carte mobilité inclusion</span><p><strong>Mention priorité</strong> : passer en priorité dans les files d'attente. <strong>Mention stationnement</strong> : souvent refusée aux familles d'enfants autistes, alors qu'elle peut être accordée quand le handicap impose qu'un adulte accompagne l'enfant dans tous ses déplacements, par exemple en cas de fugues.</p></div>
<div class="encadre loi"><span class="etiquette">La loi</span><p>Article L.241-3 du Code de l'action sociale et des familles ; arrêté du 13 mars 2006 (critère d'accompagnement par une tierce personne pour les altérations des fonctions mentales, cognitives, psychiques ou sensorielles).</p></div>
</div>
</section>
""")

# ---------------------------------------------------------------- PCH
page("droits/pch.html", "La PCH", """
<section class="band"><div class="wrap stack" style="gap:20px;max-width:860px">
<div class="fil"><a href="{R}mes-droits.html">Mes droits</a> › La PCH</div>
<h1>La PCH, c'est quoi ?</h1>
<p class="lead">La prestation de compensation du handicap finance des besoins précis liés au handicap de votre enfant. Elle est versée par le Département.</p>
<h2>Est-ce que mon enfant y a droit ?</h2>
<p>Avant 20 ans, trois conditions sont nécessaires :</p>
<ol>
<li>Toucher l'AEEH.</li>
<li>Avoir droit à un complément d'AEEH.</li>
<li>Avoir des difficultés importantes au quotidien : une difficulté absolue (il ne peut pas faire du tout sans aide) pour au moins 1 activité, ou une difficulté grave pour au moins 2 activités, en comparant avec un enfant du même âge.</li>
</ol>
<div class="encadre astuce"><span class="etiquette">Bon à savoir</span><p>Depuis le 1er janvier 2023, la PCH est plus accessible aux troubles du neurodéveloppement, dont l'autisme, avec une nouvelle aide : le « soutien à l'autonomie ».</p></div>
<h2>Les 5 éléments de la PCH</h2>
<div class="carte"><span class="titre">1 · L'aide humaine</span><p>Une personne qui aide votre enfant au quotidien : toilette, habillage, repas, surveillance, et soutien à l'autonomie. Ce peut être un professionnel, ou un parent (dédommagement de l'aidant familial).</p></div>
<div class="carte"><span class="titre">2 · Les aides techniques</span><p>Du matériel conçu pour compenser le handicap, par exemple une tablette de communication avec une application de CAA. Joignez plusieurs devis.</p></div>
<div class="carte"><span class="titre">3 · Logement, véhicule, transport</span><p>Les travaux ou frais rendus nécessaires par le handicap, par exemple sécuriser le logement. Pour le logement : jusqu'à 10 000 € sur 10 ans. Seul élément cumulable avec un complément d'AEEH.</p></div>
<div class="carte"><span class="titre">4 · Charges spécifiques ou exceptionnelles</span><p>Des dépenses liées au handicap et non couvertes ailleurs : régulières (spécifiques) ou ponctuelles (exceptionnelles).</p></div>
<div class="carte"><span class="titre">5 · L'aide animalière</span><p>Un animal qui aide à l'autonomie, par exemple un chien d'assistance éduqué par un organisme reconnu.</p></div>
<h2>PCH ou complément d'AEEH ? Le droit d'option</h2>
<p>Vous pouvez demander les deux. La MDPH évalue, puis vous choisissez :</p>
<ol>
<li>AEEH de base + complément ;</li>
<li>AEEH de base + PCH ;</li>
<li>AEEH de base + complément + élément 3 de la PCH.</li>
</ol>
<p>Ce choix n'est pas définitif : vous pourrez changer à la fin du droit. L'évaluation de la PCH se fait souvent à domicile : c'est à vous de décider si vous souhaitez cette visite.</p>
</div></section>
""")

# ---------------------------------------------------------------- Notre histoire
page("notre-histoire.html", "Notre histoire", """
<section class="band"><div class="wrap stack" style="gap:18px;max-width:800px">
<h1>Notre histoire</h1>
<p class="lead">ADM Autisme – Autour de Mohamed est née en 2014, autour de notre fils.</p>
<p>Mohamed a aujourd'hui 15 ans. Il a reçu un diagnostic de trouble du spectre de l'autisme à 2 ans et demi : un autisme sévère, sans langage oral. Au fil des années, d'autres maladies sont venues s'ajouter, les unes après les autres : un diabète de type 1 insulinodépendant, une insuffisance pancréatique exocrine et une épilepsie. À chaque étape, il a fallu tout justifier pour faire reconnaître la gravité de la situation.</p>
<h2>Des refus, encore et encore</h2>
<p>Nos premiers dossiers MDPH ont été refusés, les uns après les autres. Notre situation était pourtant grave, et bien réelle. Mais nous n'étions pas outillés : nous ne savions pas exposer notre situation ni exprimer nos besoins. Alors, malgré la gravité de ce que nous vivions, nous n'étions pas entendus.</p>
<p><strong>C'est la leçon la plus importante de notre parcours : une situation grave mal expliquée peut être refusée.</strong></p>
<h2>Apprendre à faire valoir nos droits</h2>
<p>Nous avons appris, pas à pas. À décrire précisément nos besoins. À justifier chaque demande, pièce à l'appui. À manier les articles de loi pour que l'on cesse de nous refuser des choses simplement parce que nous ne savions pas les demander.</p>
<h2>Aider d'autres familles</h2>
<p>Ensuite, nous avons commencé à monter des dossiers MDPH avec d'autres familles. Plus de 90 % de leurs demandes ont été acceptées, en première demande ou après recours.</p>
<h2>Notre règle</h2>
<ul>
<li>Demander ce qui est proportionné à la situation de la famille. Ni plus, ni moins.</li>
<li>En cas de refus, ne pas attendre : répondre tout de suite, avec les articles de loi qui mettent la commission face à ses responsabilités.</li>
<li>Ne pas chercher la compassion, mais la reconnaissance de nos droits : réclamer ce qui est dû, et montrer ce qui n'a pas été compensé comme la loi le prévoit.</li>
</ul>
<h2>Pourquoi ce site</h2>
<p>Ce site n'est pas là pour faire votre dossier à votre place, ni pour vous dicter quoi écrire. Il est là pour vous outiller : pour que vous puissiez, vous aussi, faire valoir les droits de votre enfant, par vous-même, selon votre situation.</p>
<div class="carte" id="contact"><span class="titre">Nous contacter</span><p>E-mail : <a href="mailto:gporte.consulting@gmail.com">gporte.consulting@gmail.com</a></p><p>Téléphone : <a href="tel:+33972190922">09 72 19 09 22</a></p><p>Portable et WhatsApp : <a href="tel:+33675404376">06 75 40 43 76</a></p><p>L'Isle-d'Abeau (38080), Nord-Isère</p></div>
</div></section>
""")

# ---------------------------------------------------------------- Mentions légales
page("mentions-legales.html", "Mentions légales", """
<section class="band"><div class="wrap stack" style="gap:14px;max-width:800px">
<h1>Mentions légales</h1>
<p><strong>Éditeur du site :</strong> Association ADM Autisme – Autour de Mohamed, L'Isle-d'Abeau (38080). Contact : gporte.consulting@gmail.com, 09 72 19 09 22.</p>
<p><strong>Directeur de la publication :</strong> Grégory Porte, président de l'association.</p>
<p><strong>Hébergement :</strong> Cloudflare Pages (Cloudflare, Inc.).</p>
<p><strong>Données personnelles :</strong> ce site ne collecte aucune donnée. Le générateur de projet de vie fonctionne entièrement sur votre appareil : rien de ce que vous saisissez n'est envoyé ni enregistré.</p>
<p><strong>Responsabilité :</strong> les informations de ce site sont fournies pour aider les familles à préparer leur dossier. Elles ne remplacent pas un conseil juridique. Les textes de loi évoluent : vérifiez toujours les informations auprès de votre MDPH.</p>
</div></section>
""")
