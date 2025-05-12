import { defineConfig } from 'vite';

export default defineConfig({
  base: './', // important for file:// protocol
  build: {
    outDir: './dist',
    assetsDir: 'assets',
  }
});
