import '@shoelace-style/shoelace/dist/themes/light.css';
import '@shoelace-style/shoelace/dist/shoelace.js';

document.addEventListener("DOMContentLoaded", () => {
    // Used for calling Python event handlers
    window.vf = (name, ...args) => {
      if (window.pywebview?.api?.handle_event) {
        window.pywebview.api.handle_event(name, ...args);
      } else {
        console.warn("[vf] pywebview not ready:", name);
      }
    };

    // Used internally by ViewForge for DOM updates
    window.vf_update = (id, html) => {
      const el = document.getElementById(id);
      if (el) {
        el.outerHTML = html;
      } else {
        console.warn("[vf_update] No element with ID", id);
      }
    };
});