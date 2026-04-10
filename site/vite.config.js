import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/projects-overview/',
  server: {
    port: 5174,
    proxy: {
      '/api': 'http://localhost:3457'
    }
  },
  test: {
    environment: 'jsdom',
  }
});
