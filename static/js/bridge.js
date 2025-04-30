// static/js/bridge.js

/**
 * Send a message to the Python backend via pywebview.
 * @param {string} message - A string message (e.g., "theme:dark")
 */
window.sendToPython = function(message) {
    if (window.pywebview?.api?.receiveMessage) {
        console.log("[JS → Python]", message);
        window.pywebview.api.receiveMessage(message)
            .then(response => {
                console.log("[Python → JS Response]", response);
                if (typeof window.receiveFromPython === "function") {
                    window.receiveFromPython(response);
                }
            })
            .catch(err => {
                console.warn("Error sending message to Python:", err);
            });
    } else {
        console.warn("window.pywebview.api not ready");
    }
};

/**
 * Hook for Python to call JS with a message.
 * This can be overridden by the app.
 * @param {any} message - Message sent from Python to JS
 */
window.receiveFromPython = function(message) {
    console.log("[Python → JS]", message);
    // Override this in main.js if you want to react to Python data
};
