import { defineConfig } from 'vite';

export default defineConfig({
  base: './',
  build: {
    outDir: '../src/viewforge/static',
    rollupOptions: {
        input: 'index.html'
    }
  }
});
