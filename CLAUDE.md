# Hélios Junior Conseil — Site Web

## Contexte projet
Refonte du site de la junior-entreprise de l'ENSIP (École Nationale Supérieure d'Ingénieurs de Poitiers), spécialisée en résilience climatique, bilan carbone et conseil environnemental.

- **Site original (Wix)** : https://www.helios-juniorconseil.com/
- **Repo GitHub** : https://github.com/marcdenizot1-max/helios
- **Fichier principal** : `index.html` (site one-page, zéro dépendance)

## Design choisi : Design 5
Le design de référence est `design5.html`. Style éditorial minimaliste inspiré des grands cabinets de conseil.

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

## Structure du site (sections dans l'ordre)
1. **Header** sticky — logo + nav (Expertises, Méthode, Équipe, Références, Contact)
2. **Hero** — titre animé + description + image Unsplash (parallaxe)
3. **Stats bar** — 4 chiffres clés avec compteurs animés
4. **Quote** — Mot du Président sur fond bleu encre
5. **Expertises** — liste éditoriale (hover slide)
6. **Méthodologie** — 4 étapes en grille
7. **Équipe** — photos de groupe par pôle (alternées photo/texte)
8. **Partenaires** — logos en grayscale (colorisés au hover)
9. **Footer** — CTA email + logos + réseaux sociaux

## Assets (dossier `assets/`)
| Fichier | Contenu |
|---|---|
| `logo-helios.png` | Logo principal Hélios Junior Conseil (bleu) |
| `logo-ensip.webp` | Logo ENSIP Poitiers |
| `team-photo1.png` | Photo groupe Pôle Bureau |
| `team-photo2.png` | Photo groupe Pôle Technico-Commercial |
| `team-photo3.png` | Photo groupe Pôle Communication |
| `team-photo4.png` | Photo groupe Pôle Évènementiel |
| `logo-sg.png` | Société Générale |
| `logo-partner2.png` | Département de la Vienne |
| `logo-partner3.png` | Université de Poitiers |
| `logo-inpb.png` | Bordeaux INP Aquitaine |
| `logo-partner1.png` | Université (partenaire académique) |

Tous les assets viennent de `static.wixstatic.com` (site Wix original).

## Équipe actuelle
### Pôle Bureau
- Raphaël Herraïz — Président
- Lilian Coupet — Secrétaire
- Tom Catalao — Trésorier

### Études Carbone & Synthèse
- Raphaël Herraïz — Chargé d'étude carbone
- Thomas Damiron — Chargé d'étude carbone · Coordinateur évènementiel
- Cléa Joassard — Chargée de synthèse

### Pôle Communication
- Baptiste Pamies — Site internet
- Tom Catalao — Site internet
- Line Le Rudulier — Compte Instagram

> Pas de photos disponibles pour l'instant — la section équipe utilise des avatars avec initiales.

## Contenu clé
- **Citation président** : *"Une junior entreprise reflète bien souvent l'identité de son école..."* — Thomas Candau
- **Expertise principale** : Bilan Carbone (méthode BASE EMPREINTE ADEME)
- **Fondée en** : 2024
- **Contact** : contact@helios-juniorconseil.com
- **LinkedIn** : https://www.linkedin.com/company/helios-jconseil/
- **Facebook** : https://www.facebook.com/ensip.helios/
- **Instagram** : https://www.instagram.com/junior.helios/

## Animations (JavaScript vanilla, pas de librairie)
- **Scroll-reveal** : Intersection Observer, classe `.reveal` → `.visible`
- **Stagger** : classes `.reveal-d1` à `.reveal-d9` (délais 0.1s à 0.9s)
- **Hero** : entrée CSS au chargement (`@keyframes heroIn`)
- **Parallaxe** : scroll listener sur l'image hero
- **Compteurs** : `data-target` + `data-suffix` sur `.stat-number`
- **Header** : ombre au scroll (classe `.scrolled`)

## Pages du site original (pour référence future)
- `/` — Accueil
- `/expertises` — Détail des prestations
- `/notre-equipe` — Équipe
- `/contact` — Contact
- `/blog` — Actualités
- `/members` — Espace membres

## Notes techniques
- Site statique pur : HTML + CSS + JS vanilla, aucun framework
- `node_modules/` est ignoré (`.gitignore`)
- Le site Wix original est dynamique (Thunderbolt), le contenu n'est pas dans le HTML statique — extraction faite via `curl` + parsing Python
