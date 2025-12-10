// story.js - load a story from data/stories.json and render narrative sections with inline visuals.
// Usage: open story.html?story=story-id

async function fetchJSON(path){
  const r = await fetch(path);
  if(!r.ok) throw new Error(`Failed to fetch ${path}: ${r.status}`);
  return r.json();
}

function q(name){
  const params = new URLSearchParams(location.search);
  return params.get(name);
}

function createEl(tag, attrs = {}, children = []) {
  const el = document.createElement(tag);
  for (const k in attrs) {
    if (k === 'class') el.className = attrs[k];
    else if (k === 'text') el.textContent = attrs[k];
    else el.setAttribute(k, attrs[k]);
  }
  children.forEach(c => el.appendChild(c));
  return el;
}

function clear(el){ el.innerHTML = ''; }

async function renderPlotlyInto(container, path){
  try{
    const spec = await fetchJSON(path);
    // spec: { data: [...], layout: {...}, config?: {...} }
    const div = document.createElement('div');
    div.style.width = '100%';
    div.style.height = '100%';
    container.appendChild(div);
    Plotly.newPlot(div, spec.data || [], spec.layout || {}, spec.config || {});
  }catch(err){
    container.textContent = 'Error loading plot: ' + err.message;
  }
}

async function renderD3CsvInto(container, path){
  try{
    const svg = d3.create("svg").attr("width","100%").attr("height",420);
    container.appendChild(svg.node());
    const data = await d3.csv(path, d3.autoType);
    // Simple scatter if columns x and y exist
    const margin = {top:10,right:10,bottom:40,left:50};
    const width = container.clientWidth - margin.left - margin.right;
    const height = 360 - margin.top - margin.bottom;

    const x = d3.scaleLinear()
      .domain(d3.extent(data, d => d.x)).nice()
      .range([margin.left, margin.left + width]);

    const y = d3.scaleLinear()
      .domain(d3.extent(data, d => d.y)).nice()
      .range([margin.top + height, margin.top]);

    const g = d3.select(svg.node());
    g.append("g")
      .attr("transform", `translate(0,${margin.top + height})`)
      .call(d3.axisBottom(x));
    g.append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y));
    g.selectAll("circle")
      .data(data)
      .join("circle")
      .attr("cx", d => x(d.x))
      .attr("cy", d => y(d.y))
      .attr("r", 4)
      .attr("fill", "#67e8f9")
      .attr("opacity", 0.95);

  }catch(err){
    container.textContent = 'Error loading D3 CSV: ' + err.message;
  }
}

function renderImageInto(container, path){
  const img = document.createElement('img');
  img.src = path;
  img.alt = '';
  img.style.width = '100%';
  img.style.height = 'auto';
  img.style.borderRadius = '6px';
  container.appendChild(img);
}

const renderers = {
  'plotly': renderPlotlyInto,
  'd3-csv': renderD3CsvInto,
  'image': renderImageInto
};

function makeDownloadLink(url, label = 'Download') {
  const a = document.createElement('a');
  a.href = url;
  a.className = 'btn';
  a.textContent = label;
  a.download = '';
  return a;
}

async function renderStory(id){
  const manifest = await fetchJSON('data/stories.json');
  const story = manifest.find(s => s.id === id);
  if(!story){
    document.getElementById('story-title').textContent = 'Story not found';
    return;
  }

  document.getElementById('story-title').textContent = story.title || '';
  document.getElementById('story-subtitle').textContent = story.subtitle || '';
  if(story.meta) {
    document.getElementById('story-meta').textContent = story.meta;
  }

  const body = document.getElementById('story-body');
  clear(body);

  (story.sections || []).forEach((sec, idx) => {
    const section = createEl('section', { class: 'section' });
    if(sec.title) section.appendChild(createEl('h2', { text: sec.title }));
    if(sec.text) section.appendChild(createEl('p', { text: sec.text }));

    if(sec.viz){
      const fig = createEl('figure', { class: 'figure' });
      const vizContainer = createEl('div', { class: 'viz' });
      fig.appendChild(vizContainer);
      if(sec.viz.caption) fig.appendChild(createEl('figcaption', { class: 'caption', text: sec.viz.caption }));
      section.appendChild(fig);

      const r = renderers[sec.viz.type];
      if(r){
        r(vizContainer, sec.viz.path);
      } else {
        vizContainer.textContent = `No renderer for type: ${sec.viz.type}`;
      }

      // actions (download / source)
      const actions = createEl('div', { class: 'actions' });
      if(sec.viz.download) actions.appendChild(makeDownloadLink(sec.viz.download, 'Download data'));
      if(sec.viz.source) {
        const s = document.createElement('a');
        s.className = 'btn';
        s.href = sec.viz.source;
        s.textContent = 'Source';
        s.target = '_blank';
        actions.appendChild(s);
      }
      section.appendChild(actions);
    }

    // optional notes/citation
    if(sec.note) section.appendChild(createEl('p', { class: 'muted', text: sec.note }));

    body.appendChild(section);
  });

  // optional footer citation
  if(story.citation){
    const foot = createEl('div', { class: 'meta muted', text: 'Citation: ' + story.citation });
    body.appendChild(foot);
  }
}

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
  const storyId = q('story') || 'sample-breach';
  try{
    await renderStory(storyId);
  }catch(err){
    document.getElementById('story-title').textContent = 'Error loading story';
    const body = document.getElementById('story-body');
    body.textContent = String(err);
  }
});