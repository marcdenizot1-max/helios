# Hélios Junior Conseil — Site Web

## Contexte projet
Refonte du site de la junior-entreprise de l'ENSIP (École Nationale Supérieure d'Ingénieurs de Poitiers), spécialisée en résilience climatique, bilan carbone et conseil environnemental.

- **Site original (Wix)** : https://www.helios-juniorconseil.com/
- **Repo GitHub** : https://github.com/marcdenizot1-max/helios
- **Site déployé** : https://site-helios.vercel.app
- **Compte Vercel** : `ensiphelios-9328` (compte Hélios, pas le compte personnel Marc)

## Déploiement
Toujours déployer avec `vercel --prod` depuis `/Users/marc/DEV/Site_Helios`.
Le CLI Vercel est connecté au compte Hélios (`ensiphelios` — vérifier avec `vercel whoami`).
Ne jamais déployer via GitHub Actions ou via le compte personnel Marc.

## Build
Le site utilise **Vite** pour le build (`npm run build`).
**Toute nouvelle page HTML doit être déclarée dans `vite.config.js`** sous `rollupOptions.input`, sinon elle ne sera pas incluse dans le build et retournera une 404.

```js
// vite.config.js — exemple
input: {
  main:    resolve(__dirname, 'index.html'),
  equipe:  resolve(__dirname, 'equipe.html'),
  blog:    resolve(__dirname, 'blog.html'),
  contact: resolve(__dirname, 'contact.html'),
  'articles/mon-article': resolve(__dirname, 'articles/mon-article.html'),
}
```

## URLs — cleanUrls
`vercel.json` a `"cleanUrls": true` : les `.html` sont retirés des URLs.
Utiliser **toujours des chemins sans extension** dans les liens internes :
- `href="/equipe"` ✓ — `href="equipe.html"` ✗
- `href="/contact"` ✓ — `href="contact.html"` ✗
- `href="/articles/mon-article"` ✓

## Design : Design 5
Style éditorial minimaliste inspiré des grands cabinets de conseil.

**Typographie**
- Titres : `Lora` (serif, Google Fonts)
- Corps : `Manrope` (sans-serif, Google Fonts)

**Palette**
```css
--bleu-encre:  #051024   /* quasi-noir, fond section sombre */
--bleu-helios: #1B4F8A   /* bleu logo Hélios */
--blanc-casse: #F9F9F9   /* fond général */
--gris-texte:  #5A6069   /* texte secondaire */
--ligne-fine:  rgba(5,16,36,0.1) /* séparateurs */
```

## Pages du site
| Fichier | URL | Description |
|---|---|---|
| `index.html` | `/` | Page d'accueil (hero, stats, citation, expertises, méthode, partenaires, blog teaser) |
| `equipe.html` | `/equipe` | Équipe par promotion avec onglets 2026 / 2027 |
| `blog.html` | `/blog` | Liste de tous les articles |
| `contact.html` | `/contact` | Page contact dédiée avec formulaire |
| `articles/*.html` | `/articles/*` | Articles individuels du blog |

### Structure de index.html (sections dans l'ordre)
1. Header sticky — logo + nav
2. Hero — titre animé + description + image parallaxe
3. Stats bar — 4 chiffres clés
4. Quote — Mot du Président (fond bleu encre)
5. Expertises — liste éditoriale
6. Méthodologie — 4 étapes en grille
7. Partenaires clients — carte Archives de la Vienne
8. Partenaires institutionnels — logos ENSIP, Univ. Poitiers, etc.
9. Blog teaser — 4 cartes d'articles
10. Footer

> La section Équipe a été retirée de index.html et déplacée dans `/equipe`.
> Le formulaire Contact a été retiré de index.html et déplacé dans `/contact`.

## Navigation
Liens de la nav dans l'ordre : Expertises · Méthode · Équipe · Blog · Contact
```html
<a href="/#expertises">Expertises</a>
<a href="/#methode">Méthode</a>
<a href="/equipe">Équipe</a>
<a href="/blog">Blog</a>
<a href="/contact" class="nav-contact-btn">Contact</a>
```

## Articles du blog
| Fichier | URL | Titre |
|---|---|---|
| `articles/anthony-viaux-intervenant.html` | `/articles/anthony-viaux-intervenant` | Anthony Viaux chez Hélios (intervention, débat fictif) |
| `articles/guide-calcul-empreinte.html` | `/articles/guide-calcul-empreinte` | Calcul d'empreinte carbone |
| `articles/analyse-cycle-vie.html` | `/articles/analyse-cycle-vie` | Analyse du Cycle de Vie (ACV) |
| `articles/projet-archives-vienne.html` | `/articles/projet-archives-vienne` | Projet Archives de la Vienne |
| `articles/reporting-csrd.html` | `/articles/reporting-csrd` | CSRD & reporting |

Ajouter un article = créer le fichier HTML + le déclarer dans `vite.config.js` + ajouter une carte dans `blog.html` et `index.html` (section blog teaser).

## Équipe 2026
### Pôle Bureau
- Raphaël Herraïz — Président
- Lilian Coupet — Secrétaire
- Tom Catalao — Trésorier

### Études Carbone & Synthèse
- Raphaël Herraïz — Chargé d'étude carbone
- Thomas Damiron — Chargé d'étude carbone · Coordinateur évènementiel
- Cléa Joassard — Chargée de synthèse

### Pôle Communication
- Marc Denizot — Site internet
- Baptiste Pamies — Site internet
- Tom Catalao — Site internet
- Line Le Rudulier — Compte Instagram

> Pas de photos individuelles — la section équipe utilise des avatars avec initiales.

## Contenu clé
- **Citation président** : *"Une junior entreprise reflète bien souvent l'identité de son école..."* — Raphaël Herraïz
- **Expertise principale** : Bilan Carbone (méthode BASE EMPREINTE ADEME)
- **Fondée en** : 2025
- **Contact** : contact@helios-juniorconseil.com
- **LinkedIn** : https://www.linkedin.com/company/helios-jconseil/
- **Facebook** : https://www.facebook.com/ensip.helios/
- **Instagram** : https://www.instagram.com/junior.helios/

## Partenariat en cours
- **Archives départementales de la Vienne** — calcul de l'empreinte carbone du bâtiment (méthode ADEME). Affiché dans la section "Ils nous ont fait confiance" sur index.html.

## Assets (dossier `assets/`)
| Fichier | Contenu |
|---|---|
| `logo-helios.webp` | Logo principal Hélios Junior Conseil |
| `logo-ensip.webp` | Logo ENSIP Poitiers |
| `favicon-h.png` | Favicon |
| `anthony-viaux-1.jpg` | Photo Anthony Viaux au pupitre (début de soirée) |
| `anthony-viaux-2.jpg` | Photo Anthony Viaux en présentation (slides SAF visibles) |
| `logo-sg.png` | Société Générale |
| `logo-partner1.png` | ENSIP (partenaire académique) |
| `logo-partner2.png` | Département de la Vienne |
| `logo-partner3.png` | Université de Poitiers |
| `logo-inpb.png` | Bordeaux INP Aquitaine |

## Animations (JavaScript vanilla, aucune librairie)
- **Scroll-reveal** : Intersection Observer, classe `.reveal` / `.reveal-left` / `.reveal-right` / `.reveal-scale` → `.visible`
- **Stagger** : classes `.reveal-d1` à `.reveal-d9` (délais 0.1s à 0.9s)
- **Hero** : entrée CSS au chargement (`@keyframes heroIn`)
- **Parallaxe** : scroll listener sur l'image hero
- **Compteurs** : `data-target` + `data-suffix` sur `.stat-number`
- **Header** : ombre au scroll (classe `.scrolled`)
- **Ripple** : effet vague sur `.ripple-btn` au clic
- **Particules** : canvas animé dans le hero (55 points reliés par des lignes)

## Mobile — points d'attention
- Menu hamburger : `.nav-toggle` + `.nav-links` + `.nav-overlay`
- Le bouton Contact dans le menu mobile utilise `box-shadow: inset 0 0 0 1.5px var(--bleu-encre)` au lieu de `border` pour que le `border-bottom` séparateur reste indépendant
- `overflow-x: hidden` doit être sur **html ET body** pour bloquer le scroll horizontal
- Breakpoints : 1200px, 1024px, 768px, 480px

## Notes techniques
- Site statique : HTML + CSS + JS vanilla, aucun framework JS
- Build via Vite (`npm run build`) — output dans `dist/`
- `node_modules/` et `dist/` ignorés dans `.gitignore`
- Formulaire de contact via FormSubmit (AJAX, pas de rechargement de page)
