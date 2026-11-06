// HybriX marketing pages: mobile menu and the enquiry form. No dependencies, no cookies, no tracking.
(function () {
  "use strict";

  var LEAD_URL = "https://nfybysksgmhfkpwfnzmk.supabase.co/functions/v1/lead-intake";
  var WHATSAPP = "https://wa.me/919947550033?text=" + encodeURIComponent("Hello HybriX, I'd like a quote for protected data storage.");

  // mobile menu
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { nav.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }

  // enquiry forms
  document.querySelectorAll("form[data-lead-form]").forEach(function (form) {
    var loaded = Date.now();
    var status = form.querySelector(".form-status");
    var button = form.querySelector("button[type=submit]");

    function show(kind, html) {
      status.hidden = false;
      status.className = "form-status " + kind;
      status.innerHTML = html;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var f = new FormData(form);
      var payload = {
        name: f.get("name"), company: f.get("company"), phone: f.get("phone"), email: f.get("email"),
        users: f.get("users"), message: f.get("message"), website: f.get("website"), t: loaded
      };
      button.disabled = true;
      var label = button.textContent;
      button.textContent = "Sending…";
      status.hidden = true;

      fetch(LEAD_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) })
        .then(function (res) { return res.json().catch(function () { return {}; }).then(function (body) { return { ok: res.ok, body: body }; }); })
        .then(function (r) {
          if (r.ok) {
            form.reset();
            loaded = Date.now();
            show("ok", "<strong>Thank you.</strong> We have your request and will contact you soon. If it's urgent, " +
              "<a href=\"" + WHATSAPP + "\">message us on WhatsApp</a>.");
          } else {
            var msg = (r.body && r.body.error) ? r.body.error : "Something went wrong.";
            show("err", msg.replace(/[<>&]/g, "") + " You can also <a href=\"" + WHATSAPP + "\">message us on WhatsApp</a>.");
          }
        })
        .catch(function () {
          show("err", "We couldn't send your request. Please check your connection, or <a href=\"" + WHATSAPP + "\">message us on WhatsApp</a>.");
        })
        .then(function () { button.disabled = false; button.textContent = label; });
    });
  });
})();
