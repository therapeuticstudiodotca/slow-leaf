# Slow Leaf — Therapeutic Studio

Slow Leaf is a small, self-contained website about tea, built as four connected experiences. It has no build server and no external services at runtime: every page is plain HTML that runs by opening it or by serving the folder with GitHub Pages.

| Experience | File | Status |
| --- | --- | --- |
| **Home** | `index.html` | Ready — hub linking the four experiences |
| **Living Atlas** | `living-atlas.html` | Ready — interactive world map of tea |
| **Knowing Tea** | `knowing-tea.html` | Scaffolded — a conceptual map of why tea matters |
| **Practicing Tea** | `practicing-tea.html` | Scaffolded — guides to preparing each kind of tea |
| **Tea Room** | `tea-room.html` | Scaffolded — a year-long seasonal experience |

The three scaffolded pages are branded, navigable placeholders that describe what each will hold; they are built out one at a time.

## Living Atlas

An interactive world map of the places where tea (*Camellia sinensis*) is grown. It carries 50 markers spanning the major producing nations and the smaller, niche, and emerging growers across Asia, Africa, South America, Europe, and Oceania. The size of each leaf reflects the scale of that country's tea output, from the largest producers down to single-estate operations.

Selecting a leaf opens a card that unfolds in three layers:

- **Quick view** — the characteristic vessel, a one-line flavour summary, and the teas made there.
- **Context** — the *cha / te / native* language-and-migration lineage, terroir, ritual, and social purpose.
- **Deep dive** — trade and migration movement, a short history, current practices, and sources.

The map is a Natural Earth projection, drawn from public-domain [Natural Earth](https://www.naturalearthdata.com/) data via the `world-atlas` package. All geometry is baked into `living-atlas.html`, so it needs no live map service.

### Data and build

| File | Purpose |
| --- | --- |
| `regions.json` | One entry per growing region — the content behind the atlas cards. |
| `index.template.html` | The atlas source, with placeholders for map geometry and region data. |
| `build.mjs` | Projects the world map and injects `regions.json` into the template to produce `living-atlas.html`. |
| `build-pages.mjs` | Generates the three scaffolded companion pages. |

Each region entry looks like this:

```json
{
  "id": "unique-slug",
  "name": "Region name",
  "country": "Country",
  "coords": [latitude, longitude],
  "leaf": "sinensis",
  "tier": "major",
  "teaword": "chá",
  "wordfamily": "cha",
  "language": "The cha / te / native lineage and how the word travelled.",
  "place": "Elevation, climate, soil, harvest season.",
  "vessel": "The characteristic vessel and what it means.",
  "ritual": "How the tea is made and shared.",
  "social": "Hospitality, ceremony, daily life, trade, and so on.",
  "flavor": "Three to five tasting notes.",
  "movement": "Trade route or migration pathway.",
  "history": "Two or three sentences.",
  "practices": "Two or three sentences.",
  "sources": ["Author, Title, Year", "Governing body"]
}
```

`coords` are `[latitude, longitude]` in decimal degrees. `leaf` is one of `sinensis`, `assamica`, `needle`, `flat`. `tier` is one of `major`, `large`, `medium`, `small`, `niche` and sets the leaf's size. Any of the descriptive fields may be omitted; the card hides what is absent.

To rebuild after editing `regions.json`:

```bash
npm install        # first time only
node build.mjs     # regenerates living-atlas.html
```

## Publishing

Enable **GitHub Pages** on the repository (Settings → Pages → deploy from the default branch). `index.html` is served at the root, with the four experiences linked from it.

## Sources

Atlas content is attributed to independent, recognised authorities — including the Tea Boards of India, Kenya, Sri Lanka, and Tanzania; the National Tea and Coffee Development Board of Nepal; ÇAYKUR; the Taiwan Tea Research and Extension Station; the Global Japanese Tea Association; the Food and Agriculture Organization (FAO); and classical texts including *The Classic of Tea* (Lu Yu), *Kissa Yōjōki* (Eisai), and the *Samguk Sagi*. Sources are listed on each region's card.
