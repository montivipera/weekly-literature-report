#!/usr/bin/env python3
"""Gate checks (brief section 9). Run from ai_tr_diffusion/: python3 drafts/gates_check.py"""
import csv, re, json, collections
inv = list(csv.DictReader(open('inventory.csv', encoding='utf-8')))
src = {r['id']: r for r in csv.DictReader(open('sources.csv', encoding='utf-8'))}
en = open('report_en.md', encoding='utf-8').read()
CL = {'Certain', 'Likely', 'Potential', 'Low'}
print('== (a)')
bad = [r['id'] for r in inv if r['class_1_2y'] not in CL or r['class_3_5y'] not in CL]
nosrc = [r['id'] for r in inv if not re.search(r'S\d{3}', r['source_ids'])]
print(len(inv), 'rows; missing/invalid class:', bad, '; no source id:', nosrc)
print('source-id counts per row min/max:', min(len(re.findall(r'S\d{3}', r['source_ids'])) for r in inv), max(len(re.findall(r'S\d{3}', r['source_ids'])) for r in inv))
print('== (c)')
body, refs = en.split('## 7. References')
cited = set(re.findall(r'\bS\d{3}\b', body))
inv_ids = set(i for r in inv for i in re.findall(r'\bS\d{3}\b', r['source_ids']))
listed = set(re.findall(r'^\[(S\d{3})\]', refs, re.M))
allc = cited | inv_ids
nourl = [i for i in sorted(allc) if i not in src or not re.match(r'https?://\S+', src[i]['url'].strip())]
print('cited in report body', len(cited), '; in inventory source_ids', len(inv_ids), '; union', len(allc), '; listed in section 7', len(listed))
print('cited in body but not in sec 7 list:', sorted(cited - listed)[:20], '; sec 7 not in sources.csv:', sorted(listed - set(src))[:10])
print('without http(s) URL:', nourl)
w = lambda ids: sorted(i for i in ids if i in src and 'weak' in src[i]['verified'])
print('weak among body-cited', len(w(cited)), '; among union', len(w(allc)), '; weak in register', len(w(src)), 'of', len(src))
print('sec-7 URLs without scheme:', [l[:30] for l in refs.splitlines() if l.startswith('[S') and 'http' not in l][:5])
print('verified column values:', collections.Counter(r['verified'] for r in src.values()))
print('== (d)')
ids = {r['id']: (r['class_1_2y'], r['class_3_5y']) for r in inv}
strip = lambda c: c.replace(' (near-Likely)', '').replace(' (lag-based)', '').strip()
tab = {}
for l in en.splitlines():
    m = re.match(r'\| (A\d\d) \|', l)
    if m:
        c = [x.strip() for x in l.split('|')]
        tab[c[1]] = (strip(c[5]), strip(c[6]))
print('Table 3.1 rows', len(tab))
secB = en.split('## 4. Tier B deep focus')[1].split('## 5.')[0]
bcl = {}
for blk in re.split(r'\n\*\*(B\d\d) ', secB)[1:]:
    pass
parts = re.split(r'\n\*\*(B\d\d) \S', '\n' + secB)
for k in range(1, len(parts), 2):
    bid, txt = parts[k], parts[k + 1]
    m = re.search(r'\*Classification\.\* (.*?)(?:\*Deciding|\n)', txt, re.S)
    t = m.group(1)
    t = re.sub(r'\(near-Likely\)|\(lag-based\)', '', t)
    if re.search(r'at both horizons', t):
        c = re.match(r'\s*(Certain|Likely|Potential|Low)', t).group(1); bcl[bid] = (c, c)
    else:
        c1 = re.match(r'\s*(Certain|Likely|Potential|Low)', t).group(1)
        c2 = re.search(r'(Certain|Likely|Potential|Low)\s+at 3.5 years', t).group(1)
        bcl[bid] = (c1, c2)
print('Section 4 items', len(bcl))
en_cls = {**tab, **bcl}
h = open('rapor_tr.html', encoding='utf-8').read()
tr = json.loads(re.search(r'id="classes">(.*?)</script>', h, re.S).group(1))
mism = [(k, en_cls.get(k), tr.get(k), ids.get(k)) for k in sorted(set(ids) | set(en_cls) | set(tr)) if not (tuple(en_cls.get(k, ())) == tuple(tr.get(k, ())) == ids.get(k))]
print('ids', len(ids), 'en', len(en_cls), 'tr', len(tr), 'MISMATCHES:', mism)
print('== words')
body_txt = open('drafts/rapor_tr_body.html', encoding='utf-8').read()
body_txt = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', body_txt, flags=re.S)
body_txt = re.sub(r'@@\w+@@', ' ', body_txt)
vis = re.sub(r'<[^>]+>', ' ', h.split('<body>')[1]); vis = re.sub(r'<script.*', ' ', vis)
print('words in body template (prose only):', len(re.sub(r'<[^>]+>', ' ', body_txt).split()))
hh = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', h, flags=re.S)
hh2 = re.sub(r'<svg.*?</svg>', ' ', hh, flags=re.S)
hh3 = re.sub(r'<details>.*?</details>', ' ', hh2, flags=re.S)
w3 = len(re.sub(r'<[^>]+>', ' ', hh3).split())
print('words visible text excl. SVG labels and collapsed list:', w3, '; at 200 wpm ->', round(w3 / 200, 1), 'min; at 150 wpm ->', round(w3 / 150, 1), 'min')
print('== visuals')
print('matrix', 'id="sekil1"' in h and 'class="mx"' in h, '| timeline', 'id="sekil2"' in h, '| heatmap', 'id="sekil3"' in h, '| Tier B charts', [f'sekil{i}' for i in (4, 5, 6) if f'id="sekil{i}"' in h])
print('emoji check:', re.findall('[\U0001F300-\U0001FAFF☀-➿]', h))
