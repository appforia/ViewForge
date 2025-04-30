// static/js/router.js

export function startRouter({ mode = 'hash', routes = {} }) {
    const getPath = () => {
        if (mode === 'hash') return window.location.hash.slice(1) || '/';
        return window.location.pathname || '/';
    };

    const render = () => {
        const path = getPath();
        const handler = routes[path];
        if (handler) {
            handler();
        } else {
            document.body.innerHTML = `<h1>404 Not Found: ${path}</h1>`;
        }
    };

    if (mode === 'hash') {
        window.addEventListener('hashchange', render);
    } else {
        window.addEventListener('popstate', render);
    }

    window.addEventListener('load', render);
}
