# Breach Insights â€” Story pages scaffold

What this is
- A minimal longform story scaffold for embedding interactive visuals in narrative pages.
- story.html loads the stories manifest at data/stories.json and renders the requested story (query param ?story=story-id).
- The renderer supports Plotly JSON specs, D3 CSV scatter (expects numeric x and y columns), and static images.

How to add a story
1. Add a new object to data/stories.json:
   - id: unique id (used with ?story=id)
   - title, subtitle, meta: header text
   - sections: ordered array of sections. Each section may include:
     - title, text, note
     - viz: { type: "plotly"|"d3-csv"|"image", path: "visuals/yourfile", caption, download, source }
   - citation: optional final citation text

2. Place visual files in the visuals/ folder (or update paths accordingly).

3. Preview locally:
   - Open story.html in a static server (or upload to GitHub Pages).
   - Example: story.html?story=sample-breach

Publishing
- Recommended: place these files in /docs and enable GitHub Pages from branch main (/docs).
- Alternatively, place in root or serve from gh-pages branch.

Extensions you might want
- Add a small script to auto-generate data/stories.json entries from visuals/ file names (I can do this).
- Add per-story navigation, permalink, social sharing, and embed code.
- Add more renderers (Vega-Lite, Leaflet for maps, video embeds).
- Add a CI workflow to deploy to Pages automatically.

If you want, I can:
- commit these files into your repo under /docs and open a PR,
- bootstrap stories.json by scanning visuals/ and creating draft sections,
- add an Actions workflow to auto-deploy to Pages.
