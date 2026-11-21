/* Page Éducatif et pratique : filtres par thème et lecture des vidéos sur place. */
(function () {
  var filtres = document.querySelectorAll(".filtre");
  var capsules = document.querySelectorAll(".capsule");
  filtres.forEach(function (f) {
    f.addEventListener("click", function () {
      var cat = f.getAttribute("data-cat");
      filtres.forEach(function (g) { g.setAttribute("aria-pressed", g === f ? "true" : "false"); });
      capsules.forEach(function (c) { c.hidden = !!cat && c.getAttribute("data-cat") !== cat; });
    });
  });
  document.querySelectorAll(".vignette").forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.getAttribute("data-id");
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label");
      f.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      var cadre = document.createElement("div"); cadre.className = "vignette lecture-en-cours";
      cadre.appendChild(f);
      b.replaceWith(cadre);
    });
  });
})();
