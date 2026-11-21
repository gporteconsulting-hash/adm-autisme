/* Générateur de projet de vie – ADM Autisme.
   Tout se passe dans le navigateur : rien n'est envoyé ni enregistré.
   Les passages entre [crochets] sont à compléter par la famille. */
(function () {
  var GROUPES = [
    { titre: "La situation de votre enfant", section: "Notre situation", items: [
      { id: "tsa", label: "Il a un diagnostic de trouble du spectre de l'autisme",
        texte: "[Prénom] a reçu un diagnostic de trouble du spectre de l'autisme à l'âge de [âge au diagnostic], posé par [nom du médecin ou du centre]. Ce diagnostic a des conséquences importantes sur sa vie de tous les jours." },
      { id: "langage", label: "Il ne parle pas, ou très peu",
        texte: "[Prénom] ne s'exprime pas, ou très peu, par la parole. Pour communiquer, il utilise [gestes / pictogrammes / tablette / aucun moyen pour l'instant]. Il ne peut donc pas dire s'il a mal, s'il a peur ou ce dont il a besoin, ce qui demande une attention de chaque instant." },
      { id: "autonomie", label: "Il a besoin d'aide pour les gestes du quotidien",
        texte: "Au quotidien, [prénom] a besoin d'aide pour [la toilette / l'habillage / les repas / la propreté / le sommeil]. Par exemple : [décrire une journée type, avec des faits précis]." },
      { id: "crises", label: "Il fait des crises ou a des troubles du comportement",
        texte: "[Prénom] fait des crises [fréquence : plusieurs fois par jour / par semaine], déclenchées par [bruits / changements / attente / autre]. Pendant ces crises, [décrire ce qui se passe et ce que nous devons faire]." },
      { id: "fugues", label: "Il fugue ou se met en danger",
        texte: "[Prénom] a des comportements de fugue soudains et imprévisibles, sans conscience du danger. Par exemple : [décrire une ou deux situations réelles]. Il ne peut effectuer aucun déplacement seul et doit être surveillé en permanence par un adulte." },
      { id: "sante", label: "Il a d'autres problèmes de santé",
        texte: "En plus de son autisme, [prénom] vit avec [maladies ou troubles associés]. Cela demande [soins, traitements, surveillance, rendez-vous], ce qui alourdit encore notre quotidien." },
      { id: "structure", label: "Il n'a pas de place dans une structure adaptée",
        texte: "[Prénom] n'a pas de place dans une structure adaptée : [en attente d'une place en IME / SESSAD / autre] depuis [date]. En attendant, c'est nous qui assurons son accompagnement au quotidien." }
    ]},
    { titre: "Sa scolarité", section: "Sa scolarité", items: [
      { id: "tempspartiel", label: "Il est scolarisé à temps partiel",
        texte: "[Prénom] est scolarisé [nombre] heures par semaine, [avec / sans] AESH ([nombre d'heures attribuées]). Les horaires sont les suivants : [jours et horaires]. En dehors de ces heures, il ne peut pas être confié à un mode de garde classique." },
      { id: "appels", label: "L'école m'appelle souvent pour venir le chercher",
        texte: "Depuis [date / la rentrée], l'école m'a appelé(e) [nombre] fois pour venir chercher [prénom] avant la fin de la journée, à cause de [crises / absence de l'AESH / autre]. Je dois pouvoir partir à tout moment." }
    ]},
    { titre: "Votre situation professionnelle", section: "Ma situation professionnelle", items: [
      { id: "salarie", label: "J'ai réduit mon temps de travail (salarié)",
        texte: "Pour m'occuper de [prénom], j'ai réduit mon temps de travail à [X] % depuis le [date]. Avant, je travaillais à temps plein comme [métier]. Cette réduction m'a été imposée par [nombre de rendez-vous / absence de prise en charge / besoin de présence]. Justificatifs joints : avenant au contrat, fiches de paie avant et après." },
      { id: "arret", label: "J'ai arrêté de travailler",
        texte: "J'ai cessé toute activité professionnelle le [date] pour m'occuper de [prénom] ([démission / licenciement / rupture conventionnelle]). Justificatif joint : [lettre de démission / attestation de fin de contrat]." },
      { id: "ae", label: "Je suis auto-entrepreneur et mon activité a baissé",
        texte: "Je suis auto-entrepreneur depuis [date], en tant que [activité]. Depuis [date], mon chiffre d'affaires est passé de [montant] à [montant] par [mois / trimestre], soit une baisse de [X] %. Cette baisse s'explique par le temps que je consacre à [prénom]. Justificatif joint : déclarations de chiffre d'affaires URSSAF avant et après." },
      { id: "chomage", label: "Je suis au chômage",
        texte: "Je suis actuellement inscrit(e) à France Travail. Cette situation ne correspond pas à ma réalité : être demandeur d'emploi suppose d'être disponible et de chercher activement un travail, ce qui m'est impossible puisque je m'occupe de [prénom] au quotidien. Je ne suis pas sans emploi par choix : je suis un parent contraint de cesser son activité à cause du handicap de mon enfant, et je demande à être reconnu(e) dans cette situation." },
      { id: "imprevisible", label: "Je ne peux pas trouver d'emploi compatible",
        texte: "Les horaires de scolarisation de [prénom], les rendez-vous et les appels imprévus de l'école rendent impossible tout emploi stable : aucun employeur ne peut accepter des absences aussi fréquentes et imprévisibles." }
    ]},
    { titre: "Ce que vous demandez", section: "Nos demandes", items: [
      { id: "aeeh", label: "L'AEEH et un complément",
        texte: "Je demande l'allocation d'éducation de l'enfant handicapé et le complément correspondant à notre situation, pour compenser [la réduction / l'arrêt] de mon activité professionnelle [et les frais liés au handicap : préciser].",
        loi: "l'article L.541-1 du Code de la sécurité sociale (AEEH et compléments)" },
      { id: "pch", label: "La PCH",
        texte: "Je demande la prestation de compensation du handicap pour [aide humaine / aides techniques / aménagement du logement / autre], car [besoin précis]. Je souhaite que l'AEEH avec complément et la PCH soient évaluées toutes les deux, afin de pouvoir choisir la solution la plus adaptée.",
        loi: "les articles L.245-1 et suivants du Code de l'action sociale et des familles (PCH)" },
      { id: "materiel", label: "Du matériel (tablette de communication…)",
        texte: "Je demande le financement de [matériel, par exemple une tablette de communication avec une application de CAA]. La communication est un droit fondamental : ce matériel permettra à [prénom] de [exprimer ses besoins / ses émotions / faire des choix]. Devis joints : [nombre] devis." },
      { id: "aesh", label: "Une AESH individuelle",
        texte: "Je demande une aide humaine individuelle à l'école, à hauteur de [nombre] heures par semaine. [Prénom] a besoin d'un accompagnement continu pour [entrer dans les apprentissages / gérer ses émotions / sa sécurité / communiquer]. Sans cet accompagnement, il ne peut pas bénéficier de sa scolarité.",
        loi: "les articles L.112-1 et L.351-3 du Code de l'éducation (droit à la scolarisation et aide humaine)" },
      { id: "orientation", label: "Une orientation en UEMA, UEEA ou ULIS",
        texte: "Je demande une orientation en [UEMA / UEEA / ULIS]. En classe ordinaire, même avec une AESH, [prénom] ne peut pas bénéficier d'un temps de scolarisation complet. Dans ce dispositif, il aurait un temps complet, adapté à son profil, en petit groupe, avec [arguments liés aux particularités de votre enfant].",
        loi: "l'article L.112-1 du Code de l'éducation (droit à une scolarisation adaptée)" },
      { id: "cmis", label: "La carte mobilité inclusion, mention stationnement",
        texte: "Je demande la carte mobilité inclusion mention stationnement. Du fait de son autisme, [prénom] ne peut effectuer aucun déplacement seul, même après apprentissage : il doit être accompagné en permanence, car il risque de fuguer vers la circulation. Se garer près de l'entrée réduit ce danger.",
        loi: "l'article L.241-3 du Code de l'action sociale et des familles et l'arrêté du 13 mars 2006 (accompagnement par une tierce personne)" },
      { id: "cmip", label: "La carte mobilité inclusion, mention priorité",
        texte: "Je demande la carte mobilité inclusion mention priorité. L'attente dans une file ou à une caisse est très difficile pour [prénom] : elle déclenche [angoisse / crises / fugues]. Par exemple : [décrire une situation réelle].",
        loi: "l'article L.241-3 du Code de l'action sociale et des familles" }
    ]}
  ];

  var etat = {};
  var groupesEl = document.getElementById("groupes");
  var apercuEl = document.getElementById("apercu");
  var prenomEl = document.getElementById("prenom");
  var ageEl = document.getElementById("age");

  GROUPES.forEach(function (g) {
    var fs = document.createElement("fieldset");
    var lg = document.createElement("legend"); lg.textContent = g.titre; fs.appendChild(lg);
    g.items.forEach(function (it) {
      var lab = document.createElement("label");
      var cb = document.createElement("input"); cb.type = "checkbox"; cb.id = "c-" + it.id;
      cb.addEventListener("change", function () { etat[it.id] = cb.checked; rendre(); });
      var sp = document.createElement("span"); sp.textContent = it.label;
      lab.appendChild(cb); lab.appendChild(sp); fs.appendChild(lab);
    });
    groupesEl.appendChild(fs);
  });
  prenomEl.addEventListener("input", rendre);
  ageEl.addEventListener("input", rendre);

  function prenom() { return prenomEl.value.trim(); }
  function personnaliser(t) {
    var p = prenom();
    if (p) t = t.replace(/\[Prénom\]/g, p).replace(/\[prénom\]/g, p);
    return t;
  }
  // Construit le document : liste de { type: "titre"|"sous"|"para", texte }
  function construire() {
    var p = prenom(), age = ageEl.value.trim();
    var doc = [];
    doc.push({ type: "titre", texte: "Projet de vie de " + (p || "[prénom de votre enfant]") });
    doc.push({ type: "para", texte: "Ce document est une base. Complétez les passages entre crochets, supprimez ce qui ne vous concerne pas et ajoutez tout ce qui est propre à votre famille." });
    doc.push({ type: "sous", texte: "Présentation" });
    doc.push({ type: "para", texte: "Nous sommes [vos prénoms et noms], parents de " + (p || "[prénom]") + ", âgé(e) de " + (age || "[âge]") + ". Nous vivons à [commune], avec [composition de la famille]." });
    var lois = [];
    GROUPES.forEach(function (g) {
      var choisis = g.items.filter(function (it) { return etat[it.id]; });
      if (!choisis.length) return;
      doc.push({ type: "sous", texte: g.section });
      choisis.forEach(function (it) {
        doc.push({ type: "para", texte: personnaliser(it.texte) });
        if (it.loi) lois.push(it.loi);
      });
    });
    doc.push({ type: "sous", texte: "Conclusion" });
    var c ="Conformément à l'article L.114-1-1 du Code de l'action sociale et des familles, la personne handicapée a droit à la compensation des conséquences de son handicap.";
    if (lois.length) c += " Nos demandes s'appuient également sur " + lois.join(" ; ") + ".";
    c += " Ce que nous demandons n'est pas une faveur : c'est la compensation à laquelle " + (p || "[prénom]") + " a droit. Nous restons à votre disposition pour tout complément d'information.";
    doc.push({ type: "para", texte: c });
    doc.push({ type: "para", texte: "Fait à [commune], le [date]. Signature : [vos signatures]" });
    return doc;
  }

  function morceaux(t) { return t.split(/(\[[^\]]*\])/g).filter(function (s) { return s.length; }); }
  function echapper(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  function rendre() {
    var html = construire().map(function (b) {
      var inner = morceaux(b.texte).map(function (m) {
        return m.charAt(0) === "[" ? '<span class="trou">' + echapper(m) + "</span>" : echapper(m);
      }).join("");
      if (b.type === "titre") return "<h3>" + inner + "</h3>";
      if (b.type === "sous") return "<h4>" + inner + "</h4>";
      return "<p>" + inner + "</p>";
    }).join("");
    apercuEl.innerHTML = html;
  }

  document.getElementById("telecharger").addEventListener("click", function () {
    var D = window.docx;
    if (!D) { alert("Le téléchargement n'est pas disponible. Rechargez la page."); return; }
    var paras = construire().map(function (b) {
      var runs = morceaux(b.texte).map(function (m) {
        var trou = m.charAt(0) === "[";
        return new D.TextRun({ text: m, highlight: trou ? "yellow" : undefined,
          bold: b.type !== "para", size: b.type === "titre" ? 32 : b.type === "sous" ? 26 : 24, font: "Arial",
          color: b.type === "para" ? "1C2740" : "12357A" });
      });
      return new D.Paragraph({ children: runs, spacing: { before: b.type === "sous" ? 280 : 0, after: 160 } });
    });
    var doc = new D.Document({ sections: [{ properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } }, children: paras }] });
    D.Packer.toBlob(doc).then(function (blob) {
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "projet-de-vie" + (prenom() ? "-" + prenom().toLowerCase().replace(/[^a-z0-9]+/gi, "-") : "") + ".docx";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
    });
  });

  rendre();
})();
