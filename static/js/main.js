// static/js/main.js

import { startRouter } from './router.js';

async function init() {
    // 1. Try to get saved theme from localStorage
    let currentTheme = localStorage.getItem('theme') || 'light';

    // 2. Ask Python for theme (if bridge is ready)
    if (window.pywebview?.api?.receiveMessage) {
        try {
            const pyTheme = await window.pywebview.api.receiveMessage('theme');
            if (pyTheme) currentTheme = pyTheme;
        } catch (err) {
            console.warn('Failed to get theme from Python:', err);
        }
    }

    // 3. Inject theme stylesheet
    const existing = document.getElementById('theme-css');
    if (existing) existing.remove();

    const link = document.createElement('link');
    link.id = 'theme-css';
    link.rel = 'stylesheet';
    link.href = `./css/themes/${currentTheme}.css`;
    document.head.appendChild(link);

    // 4. Start the router and render views
    startRouter({
        mode: 'hash',
        routes: {
            '/': () => {
                document.getElementById('app').innerHTML = `
                    <h1>Home Page</h1>
                    <button onclick="window.setTheme('dark')">Dark</button>
                    <button onclick="window.setTheme('light')">Light</button>
                    <p><a href="#/about">Go to About</a></p>`;
            },
            '/about': () => {
                document.getElementById('app').innerHTML = `
                    <h1>About ViewForge</h1>
                    <p><a href="#/">Back to Home</a></p>`;
            }
        }
    });
}

// 5. Utility to update theme and notify Python
window.setTheme = function(theme) {
    localStorage.setItem('theme', theme);
    if (window.pywebview?.api?.receiveMessage) {
        window.pywebview.api.receiveMessage(`theme:${theme}`);
    }
};

window.addEventListener('DOMContentLoaded', async () => {
    await init();

    // Wait until JS bridge is definitely injected
    while (!window.pywebview?.api?.receiveMessage) {
        await new Promise(resolve => setTimeout(resolve, 50));
    }

    await window.pywebview.api.receiveMessage("frontend:ready");
});
