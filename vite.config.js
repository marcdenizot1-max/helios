import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        equipe: resolve(__dirname, 'equipe.html'),
        blog: resolve(__dirname, 'blog.html'),
        'articles/guide-calcul-empreinte': resolve(__dirname, 'articles/guide-calcul-empreinte.html'),
        'articles/analyse-cycle-vie': resolve(__dirname, 'articles/analyse-cycle-vie.html'),
        'articles/projet-archives-vienne': resolve(__dirname, 'articles/projet-archives-vienne.html'),
        'articles/reporting-csrd': resolve(__dirname, 'articles/reporting-csrd.html'),
        'articles/anthony-viaux-intervenant': resolve(__dirname, 'articles/anthony-viaux-intervenant.html'),
        contact: resolve(__dirname, 'contact.html')
      },
    },
  },
})
