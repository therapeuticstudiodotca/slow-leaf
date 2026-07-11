# Slow Leaf — Therapeutic Studio

Slow Leaf is a small project about tea, built as four connected experiences. It has no build server and no external services at runtime: every page is plain HTML that runs by opening it or by serving the folder with GitHub Pages.

| Experience | File | Status |
| --- | --- | --- |
| **Home** | `index.html` | Ready — hub linking the four experiences |
| **Living Atlas** | `living-atlas.html` | Ready — interactive world map of tea |
| **Knowing Tea** | `knowing-tea.html` | Scaffolded — a conceptual map of why tea matters |
| **Practicing Tea** | `practicing-tea.html` | Ready — guides to preparing each kind of tea |
| **Tea Room** | `tea-room.html` | Scaffolded — a year-long seasonal experience |


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

