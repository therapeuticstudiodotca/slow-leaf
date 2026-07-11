# Slow Leaf — Therapeutic Studio

Slow Leaf is a small project about tea, built as four connected experiences. It has no build server and no external services at runtime: every page is plain HTML that runs by opening it or by serving the folder with GitHub Pages.

| Experience | File | Status |
| --- | --- | --- |
| **Home** | `index.html` | Ready — hub linking the four experiences |
| **Living Atlas** | `living-atlas.html` | Ready — interactive world map of tea |
| **Knowing Tea** | `knowing-tea.html` | Scaffolded — a conceptual map of why tea matters |
| **Practicing Tea** | `practicing-tea.html` | Scaffolded — guides to preparing each kind of tea |
| **Tea Room** | `tea-room.html` | Scaffolded — a year-long seasonal experience |

## Living Atlas

An interactive world map of the places where tea (*Camellia sinensis*) is grown. It carries 50 markers spanning the major producing nations and the smaller, niche, and emerging growers across Asia, Africa, South America, Europe, and Oceania. The size of each leaf reflects the scale of that country's tea output, from the largest producers down to single-estate operations.

Selecting a leaf opens a card that unfolds in three layers:

- **Quick view** — the characteristic vessel, a one-line flavour summary, and the teas made there.
- **Context** — the *cha / te / native* language-and-migration lineage, terroir, ritual, and social purpose.
- **Deep dive** — trade and migration movement, a short history, current practices, and sources.

The map is a Natural Earth projection, drawn from public-domain [Natural Earth](https://www.naturalearthdata.com/) data via the `world-atlas` package. All geometry is baked into `living-atlas.html`, so it needs no live map service.

Each leaf is shaded along a cool-green ramp by its **principal tea style** — fresh green for green tea, through muted teal for oolong, to a deep pine for black and post-fermented dark tea — which lifts the markers off the grey land and lets the map be read at a glance. The card's leaf drawing is coloured to match. Because a region can make several styles, the colour reflects its signature style, while the filter still matches any style it produces.

A **type filter** above the map lets you select one or more tea styles (Green, White, Oolong, Black, Dark), each shown with its colour so the row doubles as a key. Selecting a style emphasises the regions that produce it and quietly fades the rest; selecting several unions them, and **All** clears the filter. The chips are generated from the `types` field in the data, so they stay in step with whatever the regions describe.

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
  "types": ["green", "black"],
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

