import re, sys
src, css_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
css = open(css_path, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a[:70], c)
    s = s.replace(a, b)

# head: title + fonts
rep('<title>PASUL 3 - SITE_prototip_1</title>', '<title>PASUL 3 - SITE_prototip_2</title>')
i, j = s.index('<link href="https://fonts.googleapis.com/css2'), s.index('rel="stylesheet">') + len('rel="stylesheet">')
s = s[:i] + '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700;800&family=Cormorant+Garamond:ital,wght@0,600;1,500&display=swap" rel="stylesheet">' + s[j:]

# stylesheet
i, j = s.index('<style'), s.index('</style>')
s = s[:i] + '<style>' + css + s[j:]

# body shell
i, j = s.index('<body>') + 6, s.index('<nav class="tabbar"')
LOGO = '<span class="w">ANNA<svg viewBox="0 0 100 8" preserveAspectRatio="none" aria-hidden="true"><path d="M0 5 Q50 -1 100 2 Q50 2 4 8 Z" fill="#e8322e"/></svg></span><span class="s">Business Club</span>'
shell = '''
<header class="top-banner"><div class="wrap">
  <a class="logo" href="#acasa" aria-label="ANNA Business Club, pagina de start">''' + LOGO + '''</a>
  <div class="demo">
    <b>DEMO</b>
    <div class="seg" id="roles" role="group" aria-label="Rol în demo"></div>
    <div class="seg" id="junior" role="group" aria-label="Tip de membru" hidden>
      <button type="button" data-junior="0">Senior</button><button type="button" data-junior="1">Junior</button>
    </div>
    <div class="seg" role="group" aria-label="Temă"><button type="button" data-theme-set="light">Deschisă</button><button type="button" data-theme-set="dark">Întunecată</button></div>
  </div>
</div></header>

<div class="shell">
  <aside class="rail">
    <div class="rail-top"><span class="rail-title">Meniu</span><button type="button" class="btn sm quiet menu-btn" id="menu" aria-expanded="false" aria-controls="nav">Meniu</button></div>
    <nav class="main" id="nav" aria-label="Meniu principal"></nav>
    <div class="zone" id="zone" hidden><div class="wrap"></div></div>
    <a class="btn sm cta" href="#invitatie" id="cta">Am o invitație</a>
  </aside>
  <main><div id="view" aria-live="polite"></div></main>
</div>

'''
s = s[:i] + shell + s[j:]

# script: storage keys, page header builder, per-route colour, entrance motion
rep("localStorage.getItem('anna-'+k)", "localStorage.getItem('anna2-'+k)")
rep("localStorage.setItem('anna-'+k,v)", "localStorage.setItem('anna2-'+k,v)")
rep("""return '<div class="stack"><div class="eyebrow">'+eb+'</div><h1 style="font-size:clamp(32px,5vw,48px)">'+t+'</h1>'+(lead?'<p class="lead">'+lead+'</p>':'')+'</div>'}""",
    """return '<div class="vhead"><div class="left"><span class="sec-badge">'+eb+'</span><h1>'+t+'</h1></div>'+(lead?'<p class="lead">'+lead+'</p>':'')+'</div>'}""")
rep("""$('#view').innerHTML=ok?V[r]():gate(need);decorate();""",
    """var vw=$('#view');vw.innerHTML=ok?V[r]():gate(need);vw.setAttribute('data-c',COL[r]||'gold');vw.setAttribute('data-r',r);decorate();""")
rep("function route(){", """var COL={acces:'blue',regulament:'blue',autentificare:'blue',invitatie:'blue',cerere:'blue',chestionar:'blue',rezultat:'blue',candidatura:'blue',tipuri:'blue',evenimente:'teal',servicii:'teal',anunturi:'teal',concurs:'rose',panou:'emerald',cartela:'emerald',invitatii:'emerald',rezervari:'emerald',forum:'emerald',automatizare:'emerald',voluntariat:'emerald',admin:'purple',candidaturi:'purple',membri:'purple',avertismente:'purple',buget:'purple',echipe:'purple'};
function kick(){var v=$('#view');v.classList.remove('in');void v.offsetWidth;v.classList.add('in')}
function route(){""")
rep("render();window.scrollTo(0,0)});", "render();kick();window.scrollTo(0,0)});")
rep("""'<div class="hero"><div class="stack lg"><span class="logo big">""", """'<div class="hero"><div class="club-hero stack lg"><span class="logo big">""")

assert s.lstrip().startswith('<!DOCTYPE html>')
open(out, 'w', encoding='utf-8').write(s)
print('ok', len(s))
