import os
import re

d = r'e:\Downloads\lab112-uict.github.io-main\lab112-uict.github.io-main'
files = [f for f in os.listdir(d) if f.endswith('.html') and f != 'HomePage.html']

root_new = """    :root {
      /* New Premium Palette */
      --galaxy: #081F5C;
      --galaxy-rgb: 8, 31, 92;
      --planetary: #334EAC;
      --planetary-rgb: 51, 78, 172;
      --universe: #7096D1;
      --universe-rgb: 112, 150, 209;
      --venus: #BAD6EB;
      --venus-rgb: 186, 214, 235;
      --sky: #D0E3FF;
      --sky-rgb: 208, 227, 255;
      --milky-way: #FFF9F0;
      --meteor: #F7F2EB;

      /* Mapping to semantic usage */
      --navy: var(--galaxy);
      --navy-mid: var(--planetary);
      --navy-light: var(--universe);
      --amber: var(--sky); /* Primary Accent */
      --amber-light: var(--milky-way); /* Hover state */
      --cream: var(--milky-way);
      --cream-dim: var(--meteor);
      --teal: var(--venus); /* Secondary Accent */
      --teal-light: var(--universe);
      --white: #ffffff;
      --text-dim: var(--venus);
      
      --card-bg: rgba(var(--planetary-rgb), 0.3);
      --border: rgba(var(--sky-rgb), 0.2);
      
      --font-display: 'Syne', sans-serif;
      --font-mono: 'Space Mono', monospace;
      --font-body: 'Inter', sans-serif;
    }"""

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Theme color
    content = re.sub(r'<meta name="theme-color" content="#[a-fA-F0-9]{6}" />', '<meta name="theme-color" content="#081F5C" />', content)
    
    # Root CSS
    # Since the root block might be compressed or formatted differently, we use a regex to match it
    content = re.sub(r':root\s*\{.*?(?:--font-body:\'Inter\',sans-serif;).*?\}', root_new, content, flags=re.DOTALL)
    
    # RGBA replacements
    content = content.replace('rgba(13,148,136,0.12)', 'rgba(var(--venus-rgb), 0.15)')
    content = content.replace('rgba(240,165,0,0.08)', 'rgba(var(--sky-rgb), 0.12)')
    content = content.replace('rgba(240,165,0,0.04)', 'rgba(var(--sky-rgb), 0.06)')
    content = content.replace('rgba(10,22,40,0.85)', 'rgba(var(--galaxy-rgb), 0.85)')
    content = content.replace('rgba(10, 22, 40, 0.85)', 'rgba(var(--galaxy-rgb), 0.85)')
    content = content.replace('rgba(10,22,40,0.97)', 'rgba(var(--galaxy-rgb), 0.97)')
    content = content.replace('rgba(10, 22, 40, 0.97)', 'rgba(var(--galaxy-rgb), 0.97)')
    
    content = content.replace('rgba(240,165,0,0.06)', 'rgba(var(--sky-rgb), 0.08)')
    content = content.replace('rgba(240,165,0,0.5)', 'rgba(var(--sky-rgb), 0.5)')
    content = content.replace('rgba(240,165,0,0.1)', 'rgba(var(--sky-rgb), 0.15)')
    content = content.replace('rgba(240,165,0,0.25)', 'rgba(var(--sky-rgb), 0.3)')
    content = content.replace('rgba(20,184,166,0.2)', 'rgba(var(--venus-rgb), 0.2)')
    content = content.replace('rgba(13,148,136,0.05)', 'rgba(var(--venus-rgb), 0.05)')
    content = content.replace('rgba(240,165,0,0.12)', 'rgba(var(--sky-rgb), 0.15)')
    content = content.replace('rgba(240,165,0,0.2)', 'rgba(var(--sky-rgb), 0.25)')
    content = content.replace('rgba(20,184,166,0.1)', 'rgba(var(--venus-rgb), 0.15)')
    content = content.replace('rgba(240,165,0,0.15)', 'rgba(var(--sky-rgb), 0.2)')
    content = content.replace('rgba(20,184,166,0.06)', 'rgba(var(--venus-rgb), 0.1)')
    content = content.replace('rgba(240,165,0,0.05)', 'rgba(var(--sky-rgb), 0.08)')
    content = content.replace('rgba(251,113,133,0.1)', 'rgba(var(--universe-rgb), 0.15)')
    content = content.replace('rgba(251,113,133,0.12)', 'rgba(var(--universe-rgb), 0.15)')
    content = content.replace('rgba(251,113,133,0.25)', 'rgba(var(--universe-rgb), 0.3)')
    content = content.replace('rgba(13,148,136,0.1)', 'rgba(var(--venus-rgb), 0.15)')
    content = content.replace('rgba(13,148,136,0.2)', 'rgba(var(--venus-rgb), 0.3)')
    content = content.replace('rgba(75,85,99,0.2)', 'rgba(112, 150, 209, 0.2)')
    content = content.replace('rgba(75,85,99,0.3)', 'rgba(112, 150, 209, 0.3)')
    
    content = content.replace('rgba(13,148,136,0.15)', 'rgba(var(--venus-rgb), 0.15)')
    content = content.replace('rgba(240,165,0,0.07)', 'rgba(var(--sky-rgb), 0.1)')
    content = content.replace('rgba(10,22,40,0.3)', 'rgba(var(--galaxy-rgb), 0.5)')
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done updating html files')
