/* Your Life Under Rome — the roll of the dice (sortes).
   Depends on window.LIVES (array) and window.UNREP, generated into
   js/lives-index.js by build.py. */
(function () {
  "use strict";

  function romanize(n) {
    if (n <= 0) return "N"; // Romans had no zero; 'nulla' / 'N'
    var map = [
      [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"],
      [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"],
      [5, "V"], [4, "IV"], [1, "I"]
    ];
    var out = "";
    for (var i = 0; i < map.length; i++) {
      while (n >= map[i][0]) { out += map[i][1]; n -= map[i][0]; }
    }
    return out;
  }

  // Fair integer in [1, max] using crypto when available.
  function rollDie(max) {
    if (window.crypto && window.crypto.getRandomValues) {
      var range = 4294967296; // 2^32
      var limit = range - (range % max); // reject bias
      var buf = new Uint32Array(1);
      do { window.crypto.getRandomValues(buf); } while (buf[0] >= limit);
      return (buf[0] % max) + 1;
    }
    return Math.floor(Math.random() * max) + 1;
  }
  function roll1000() { return rollDie(1000); }

  // The hidden life (Cleopatra), handed to us by lives-index.js. The dice reach
  // her about once in SECRET.odds throws — unless a quiet token sits in the URL.
  var SECRET = window.SECRET || null;

  function magicEngaged() {
    if (!SECRET || !SECRET.magic) return false;
    var url = (window.location.search + " " + window.location.hash).toLowerCase();
    return url.indexOf(SECRET.magic) !== -1; // e.g. ?alea=iacta — "the die is cast"
  }
  function secretHit() {
    if (!SECRET || !SECRET.odds) return false;
    return rollDie(SECRET.odds) === 1;
  }

  function findLife(roll) {
    var lives = window.LIVES || [];
    for (var i = 0; i < lives.length; i++) {
      if (roll >= lives[i].min && roll <= lives[i].max) return lives[i];
    }
    return null; // unrepresented band
  }

  function init() {
    var btn = document.getElementById("roll-btn");
    if (!btn) return;
    var readout = document.getElementById("die-num");
    var roman = document.getElementById("die-roman");
    var photo = document.getElementById("die-photo");
    var result = document.getElementById("dice-result");

    function renderSecret() {
      readout.textContent = "✦"; // ✦ — a throw off the table
      roman.textContent = "";
      result.classList.remove("empty", "unrep");
      result.classList.add("secret");
      result.innerHTML =
        '<p class="who">You are ' + SECRET.name + '.</p>' +
        '<p class="what">' + SECRET.tagline + '</p>' +
        '<a class="go" href="' + SECRET.url + '">Read this life &rarr;</a>';
    }

    function render(roll) {
      result.classList.remove("secret");
      readout.textContent = roll;
      roman.textContent = romanize(roll);
      var life = findLife(roll);
      result.classList.remove("empty");
      if (life) {
        result.classList.remove("unrep");
        result.innerHTML =
          '<p class="who">You are ' + life.name + '.</p>' +
          '<p class="what">' + life.role + ' &middot; ' + life.era +
          ' &middot; rolled ' + roll + ' of 1000 (this life: ' +
          life.min + '–' + life.max + ')</p>' +
          '<a class="go" href="' + life.url + '">Read this life &rarr;</a>';
      } else {
        result.classList.add("unrep");
        var u = window.UNREP || { text: "" };
        result.innerHTML =
          '<p class="who">An unwritten life.</p>' +
          '<p class="what">Roll ' + roll +
          ' falls in the unrepresented band (' +
          (u.min || 906) + '–' + (u.max || 1000) + '): ' + u.text + '</p>' +
          '<button class="go" id="recast-inline" type="button">Cast again &rarr;</button>';
        var again = document.getElementById("recast-inline");
        if (again) again.addEventListener("click", doRoll);
      }
    }

    var rolling = false;
    function doRoll() {
      if (rolling) return;
      rolling = true;
      btn.disabled = true;
      if (photo) photo.classList.add("tumbling");

      var start = performance.now();
      var duration = 1100;

      function tick() {
        var elapsed = performance.now() - start;
        readout.textContent = roll1000(); // flicker
        roman.textContent = "";
        if (elapsed < duration) {
          var t = elapsed / duration;
          var delay = 40 + t * t * 150; // ease-out: slows toward the end
          setTimeout(function () { window.requestAnimationFrame(tick); }, delay);
        } else {
          var final = roll1000();
          if (photo) photo.classList.remove("tumbling");
          if (magicEngaged() || secretHit()) {
            renderSecret();
          } else {
            render(final);
          }
          rolling = false;
          btn.disabled = false;
        }
      }
      window.requestAnimationFrame(tick);
    }

    btn.addEventListener("click", doRoll);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
