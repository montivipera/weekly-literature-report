#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds rapor_tr.html (single self-contained file) from inventory.csv.
All classes, counts, charts and the hidden JSON block are generated from the CSV."""
import csv, json, collections, html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, 'inventory.csv'), encoding='utf-8')))
assert len(rows) == 73
by_id = {r['id']: r for r in rows}

CLS_TR = {'Certain': 'Kesin', 'Likely': 'Olası', 'Potential': 'Potansiyel', 'Low': 'Düşük olasılık'}
CLS_KEY = {'Certain': 'k', 'Likely': 'o', 'Potential': 'p', 'Low': 'd'}
H1, H2 = '1–2 yıl (2026–2028)', '3–5 yıl (2028–2031)'

SHORT = {
 'A01':'Muayene notu asistanı','A02':'Tıbbi görüntüleme yazılımı','A03':'Hasta randevu sesli asistanı','A04':'YZ ile ilaç keşfi',
 'A05':'Ajanla dolandırıcılık tespiti','A06':'YZ ile kredi skorlama','A07':'Ajanla ödeme ve ticaret','A08':'YZ özel öğretmenleri',
 'A09':'Okullarda ölçme ve YZ kuralları','A10':'Öğretmen asistanları','A11':'Kamu YZ asistanları','A12':'Kamuda vaka ve risk ayıklama',
 'A13':'Kamu iş akışında ajanlar','A14':'Uydu ile ürün izleme','A15':'Çiftçi danışman sohbet botu','A16':'Hassas ilaçlama, otonom makine',
 'A17':'Şebeke tahmini ve arıza','A18':'Veri merkezi esnekliği','A19':'Bina ve sanayi enerji tasarrufu','A20':'YZ’li sanayi robotları',
 'A21':'İnsansı robotlar','A22':'Kestirimci bakım, görsel kalite','A23':'Depo robotları','A24':'Otonom tır',
 'A25':'Rota ve talep tahmini','A26':'Üretken içerik üretimi','A27':'YZ cevap motorları (haber)','A28':'Yayıncı–YZ lisans anlaşmaları',
 'A29':'İçerik kökeni ve etiketleme','A30':'Hukuki taslak ve sözleşme YZ’si','A32':'Mahkeme ve adli yardım YZ’si','A34':'Kişiselleştirme, dinamik fiyat',
 'A35':'Müşteri hizmetleri ajanları','A36':'Yeni YZ meslekleri','A37':'Gerileyen büro işleri','A38':'YZ’li serbest çalışma',
 'A39':'AB YZ Yasası yükümlülükleri','A40':'Türkçe, yerli dil modelleri','A41':'Kurumsal YZ ajanları','A42':'YZ hesaplama ve veri merkezi',
 'A44':'Siber saldırı ve savunmada YZ','A45':'Deepfake ve kimlik doğrulama','A46':'Sigortada YZ','A47':'Akıllı sulama',
 'A48':'Afet hasar tespiti','A49':'Sağlık verisinin ikincil kullanımı','A50':'YZ okuryazarlığı ve beceri','A51':'İşe alımda algoritma',
 'B01':'Ses kaydıyla tür izleme','B02':'Foto-kapan analizi','B03':'eDNA analizi','B04':'Sulak alan haritalama (uydu)',
 'B05':'Yer gözlemi temel modelleri','B06':'Restorasyon sonuç ölçümü (MRV)','B07':'Doğa riski raporlama araçları','B09':'Ulusal biyoçeşitlilik göstergeleri',
 'B10':'Literatür tarama asistanları','B11':'Sistematik derlemede YZ','B12':'Canlı kanıt veri tabanları','B13':'Araştırmacı kodlama ajanları',
 'B14':'Yayın ve fon YZ kuralları','B15':'Sahte makale tespiti','B17':'Vatandaş bilimi tür tanıma','B18':'Hibe yazımında YZ',
 'B19':'Belediye personeli YZ asistanı','B20':'Belediye vatandaş sohbet botu','B21':'STK’lara gönüllü YZ desteği','B22':'Kanıttan politika notu',
 'B23':'Dron ile habitat haritalama','B24':'Doğa kredisi piyasaları','B25':'YZ “ortak bilim insanı”','B26':'Halk görüşü analizi',
 'B27':'Kentsel doğa haritası, dijital ikiz'}
assert set(SHORT) == set(by_id), set(by_id) ^ set(SHORT)

SECT = {'health':'Sağlık','finance':'Finans','education':'Eğitim','public_administration':'Kamu yönetimi','agriculture':'Tarım',
        'energy':'Enerji','manufacturing':'İmalat','logistics':'Lojistik','media':'Medya','law':'Hukuk','retail':'Perakende',
        'labour_market':'İş gücü','cross_cutting':'Kesişen konular','ecology_environment':'Ekoloji ve çevre',
        'academia_research':'Akademi','civil_society':'Sivil toplum'}
TIERB = ['ecology_environment', 'academia_research', 'civil_society']

def is_lag(r):  # Potential 1-2y, Likely 3-5y = reached through the lag assumption
    return r['class_1_2y'] == 'Potential' and r['class_3_5y'] == 'Likely'
LAG = [r['id'] for r in rows if is_lag(r)]
assert sorted(LAG) == sorted(['A11','A16','A32','A41','A42','A44','A46','B27']), LAG

def esc(s): return html.escape(s, quote=True)
def fmt(x): return format(x, '.1f').replace('.', ',')
def cnt(key, cls): return sum(1 for r in rows if r[key] == cls)
C1 = {c: cnt('class_1_2y', c) for c in CLS_TR}
C2 = {c: cnt('class_3_5y', c) for c in CLS_TR}

# ---------------------------------------------------------------- shapes
def marker(cls, cx, cy, lag=False, title=None):
    k = CLS_KEY[cls]
    t = f'<title>{esc(title)}</title>' if title else ''
    if cls == 'Certain':
        s = f'<circle class="m{k}" cx="{cx}" cy="{cy}" r="6">{t}</circle>'
    elif cls == 'Likely':
        pts = f'{cx},{cy-8} {cx+8},{cy} {cx},{cy+8} {cx-8},{cy}'
        if lag:
            s = f'<polygon class="mo-lag" points="{pts}">{t}</polygon>'
        else:
            s = f'<polygon class="m{k}" points="{pts}">{t}</polygon>'
    else:
        s = f'<rect class="m{k}" x="{cx-5.5}" y="{cy-5.5}" width="11" height="11" rx="2">{t}</rect>'
    return s

def legend_html(with_lag=True):
    def sv(inner): return f'<svg class="lg" width="20" height="20" viewBox="0 0 20 20" aria-hidden="true">{inner}</svg>'
    out = ['<ul class="legend" aria-label="Gösterge">']
    out.append('<li>' + sv(marker('Certain', 10, 10)) + 'Kesin</li>')
    out.append('<li>' + sv(marker('Likely', 10, 10)) + 'Olası</li>')
    if with_lag:
        out.append('<li>' + sv(marker('Likely', 10, 10, lag=True)) + 'Olası (gecikme temelli)</li>')
    out.append('<li>' + sv(marker('Potential', 10, 10)) + 'Potansiyel</li>')
    out.append('<li>' + sv('<polygon class="md" points="10,2 18,10 10,18 2,10"/>') + 'Düşük olasılık (bu görüntüde 0)</li>')
    out.append('</ul>')
    return ''.join(out)

# ---------------------------------------------------------------- (a) diffusion matrix (HTML/CSS)
def chip_list(ids, lag=False):
    li = []
    for i in ids:
        li.append(f'<li class="{"lag" if lag else ""}" title="{i}">{esc(SHORT[i])} <span class="id">{i}</span></li>')
    return '<ul class="chips">' + ''.join(li) + '</ul>'

def matrix_html():
    def ids(key, cls, extra=None):
        return [r['id'] for r in rows if r[key] == cls and (extra is None or extra(r))]
    desc = {'Certain': 'Bağlayıcı kural ya da Türkiye’de pilotun ötesinde kullanım',
            'Likely': 'Güçlü fon ya da maliyet çekişi, en az iki benzer ülkede var',
            'Potential': 'Önce lider ülkelerde; sonuç tek bir koşula bağlı',
            'Low': 'Yapısal engel var'}
    h = ['<table class="mx"><caption class="sr">Yayılım matrisi: kesinlik sınıfı ve zaman ufku</caption>',
         f'<thead><tr><th scope="col"><span class="sr">Sınıf</span></th><th scope="col">{H1}</th><th scope="col">{H2}</th></tr></thead><tbody>']
    for cls in ['Certain', 'Likely', 'Potential', 'Low']:
        k = CLS_KEY[cls]
        low_shape = '<polygon class="md" points="10,2 18,10 10,18 2,10"/>'
        shape = marker(cls, 10, 10) if cls != 'Low' else low_shape
        rowh = ('<th scope="row" class="rh rh-' + k + '"><svg class="lg" width="20" height="20" viewBox="0 0 20 20" aria-hidden="true">'
                + shape + '</svg><b>' + CLS_TR[cls] + '</b><span class="rd">' + desc[cls] + '</span></th>')
        tds = []
        for key, hd, counts in (('class_1_2y', H1, C1), ('class_3_5y', H2, C2)):
            n = counts[cls]
            all_ids = ids(key, cls)
            inner = f'<div class="big">{n}</div>'
            if cls == 'Low':
                inner += '<p class="note">Bu anlık görüntüde hiçbir gelişme bu sınıfa girmedi (nedenini “Yöntem ve sınırlar” bölümünde açıklıyoruz).</p>'
            elif cls == 'Potential':
                inner += (f'<details><summary>{n} gelişmeyi listele</summary>{chip_list(all_ids)}</details>')
            elif cls == 'Likely' and key == 'class_3_5y':
                a = [i for i in all_ids if i not in LAG]; b = [i for i in all_ids if i in LAG]
                inner += (f'<p class="sub">Fon ya da maliyet çekişiyle ({len(a)})</p>{chip_list(a)}'
                          f'<p class="sub">Olası (gecikme temelli) ({len(b)})</p>{chip_list(b, True)}')
            else:
                inner += chip_list(all_ids)
            tds.append(f'<td data-h="{esc(hd)}" class="cell cell-{k}">{inner}</td>')
        h.append(f'<tr>{rowh}{"".join(tds)}</tr>')
    h.append('</tbody></table>')
    return ''.join(h)

# ---------------------------------------------------------------- ordering of sectors
sec_items = collections.defaultdict(list)
for r in rows: sec_items[r['sector']].append(r)
def share(v, key): return sum(1 for r in v if r[key] in ('Certain', 'Likely')) / len(v)
tierA = [s for s in sec_items if s not in TIERB]
tierA.sort(key=lambda s: (-share(sec_items[s], 'class_3_5y'), -share(sec_items[s], 'class_1_2y'), s))
SECT_ORDER = tierA + TIERB

# ---------------------------------------------------------------- (b) timeline (SVG)
def arrival(r):
    if r['class_1_2y'] in ('Certain', 'Likely'): return 0
    if r['class_3_5y'] in ('Certain', 'Likely'): return 1
    return 2

def timeline_svg():
    W = 430; LX = 4; LW = 96; CX0 = 104; CW = 108; HDR = 46; PER = 6; SP = 17
    cols = {s: [[], [], []] for s in SECT_ORDER}
    for r in rows: cols[r['sector']][arrival(r)].append(r)
    order = {'Certain': 0, 'Likely': 1, 'Potential': 2}
    heights = {}
    for s in SECT_ORDER:
        mx = 0
        for c in cols[s]:
            c.sort(key=lambda r: (order[r['class_1_2y'] if arrival(r) == 0 else r['class_3_5y']], r['id']))
            mx = max(mx, -(-len(c) // PER))
        heights[s] = max(30, mx * SP + 14)
    H = HDR + sum(heights.values()) + 8
    o = [f'<svg class="viz" viewBox="0 0 {W} {H}" role="img" aria-labelledby="tl-t tl-d">'
         '<title id="tl-t">Türkiye’ye beklenen varış zamanı çizelgesi</title>'
         '<desc id="tl-d">Her işaret bir gelişmeyi gösterir; sektöre göre satırlara, beklenen varış ufkuna göre sütunlara yerleşmiştir.</desc>']
    heads = [('2026–2028', '1–2 yıl'), ('2028–2031', '3–5 yıl'), ('Koşula bağlı', 'tarih öngörülmüyor')]
    for i, (a, b) in enumerate(heads):
        x = CX0 + i * CW
        o.append(f'<rect class="band{i%2}" x="{x}" y="0" width="{CW}" height="{H-4}" rx="4"/>')
        o.append(f'<text class="labb" x="{x+CW/2}" y="19" text-anchor="middle">{a}</text>')
        o.append(f'<text class="lab s" x="{x+CW/2}" y="35" text-anchor="middle">{b}</text>')
    y = HDR
    for s in SECT_ORDER:
        hh = heights[s]
        if s == TIERB[0]:
            o.append(f'<line class="axis" x1="{LX}" x2="{W-4}" y1="{y}" y2="{y}"/>')
        else:
            o.append(f'<line class="grid" x1="{LX}" x2="{W-4}" y1="{y}" y2="{y}"/>')
        o.append(f'<text class="lab" x="{LX}" y="{y+hh/2+4}">{esc(SECT[s])}</text>')
        for ci, c in enumerate(cols[s]):
            for j, r in enumerate(c):
                cls = r['class_1_2y'] if ci == 0 else r['class_3_5y']
                cx = CX0 + ci * CW + 13 + (j % PER) * 16.5
                cy = y + 14 + (j // PER) * SP
                lag = is_lag(r) and ci == 1
                lbl = CLS_TR[cls] + (' (gecikme temelli)' if lag else '')
                o.append(marker(cls, round(cx, 1), cy, lag, f'{r["id"]} · {SHORT[r["id"]]} · {lbl}'))
        y += hh
    o.append('</svg>')
    return ''.join(o)

def timeline_table():
    t = ['<table class="tv"><thead><tr><th>Sektör</th><th>2026–2028</th><th>2028–2031</th><th>Koşula bağlı</th></tr></thead><tbody>']
    for s in SECT_ORDER:
        cells = [[], [], []]
        for r in sorted(sec_items[s], key=lambda r: r['id']):
            a = arrival(r)
            cls = r['class_1_2y'] if a == 0 else r['class_3_5y']
            lag = is_lag(r) and a == 1
            cells[a].append(f'{esc(SHORT[r["id"]])} ({r["id"]}, {CLS_TR[cls]}{", gecikme temelli" if lag else ""})')
        t.append(f'<tr><th scope="row">{esc(SECT[s])}</th>' + ''.join(f'<td data-h="{h}">{"; ".join(c) if c else "–"}</td>' for h, c in zip(["2026–2028","2028–2031","Koşula bağlı"], cells)) + '</tr>')
    t.append('</tbody></table>')
    return ''.join(t)

# ---------------------------------------------------------------- (c) heatmap (SVG)
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def contrast(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb); return (hi + .05) / (lo + .05)
BINS_L = ['#ebeae5', '#cde2fb', '#86b6ef', '#3987e5', '#1c5cab', '#0d366b']
BINS_D = ['#2c2c2a', '#104281', '#1c5cab', '#3987e5', '#6da7ec', '#9ec5f4']
BIN_LAB = ['%0', '%1–19', '%20–39', '%40–59', '%60–79', '%80–100']
def binof(f):
    if f == 0: return 0
    return 1 if f < .2 else 2 if f < .4 else 3 if f < .6 else 4 if f < .8 else 5
def ink(bg):
    return '#0b0b0b' if contrast(bg, '#0b0b0b') >= contrast(bg, '#ffffff') else '#ffffff'
MIN_CONTRAST = min(min(max(contrast(b, '#0b0b0b'), contrast(b, '#ffffff')) for b in BINS_L),
                   min(max(contrast(b, '#0b0b0b'), contrast(b, '#ffffff')) for b in BINS_D))

def heatmap_svg():
    W = 460; LX = 6; LW = 150; NX = 160; X0 = 190; CW = 132; RH = 27; HDR = 40
    H = HDR + RH * len(SECT_ORDER) + 6
    o = [f'<svg class="viz" viewBox="0 0 {W} {H}" role="img" aria-labelledby="hm-t hm-d">'
         '<title id="hm-t">Sektör ısı haritası</title>'
         '<desc id="hm-d">Her sektör için, iki zaman ufkunda Kesin ve Olası sınıfındaki gelişmelerin payı.</desc>']
    for i, hd in enumerate(['1–2 yıl', '3–5 yıl']):
        x = X0 + i * (CW + 2)
        o.append(f'<text class="labb" x="{x+CW/2}" y="16" text-anchor="middle">{hd}</text>')
        o.append(f'<text class="lab s" x="{x+CW/2}" y="31" text-anchor="middle">{["2026–2028","2028–2031"][i]}</text>')
    o.append(f'<text class="lab s" x="{NX}" y="31" text-anchor="start">n</text>')
    y = HDR
    for s in SECT_ORDER:
        v = sec_items[s]; n = len(v)
        if s == TIERB[0]:
            o.append(f'<line class="axis" x1="{LX}" x2="{W-4}" y1="{y-1}" y2="{y-1}"/>')
        o.append(f'<text class="lab" x="{LX}" y="{y+RH/2+4}">{esc(SECT[s])}</text>')
        o.append(f'<text class="lab s" x="{NX}" y="{y+RH/2+4}">{n}</text>')
        for i, key in enumerate(['class_1_2y', 'class_3_5y']):
            ids = [r['id'] for r in v if r[key] in ('Certain', 'Likely')]
            f = len(ids) / n; b = binof(f)
            x = X0 + i * (CW + 2)
            tip = (f'{SECT[s]} · {[H1, H2][i]} · Kesin+Olası: {len(ids)}/{n} (%{round(f*100)})'
                   + (' · ' + ', '.join(ids) if ids else ''))
            o.append(f'<g><title>{esc(tip)}</title><rect class="hb{b}" x="{x}" y="{y+1}" width="{CW}" height="{RH-2}" rx="3"/>'
                     f'<text class="hv hb{b}t" x="{x+CW/2}" y="{y+RH/2+4}" text-anchor="middle">{len(ids)}/{n} · %{round(f*100)}</text></g>')
        y += RH
    o.append('</svg>')
    return ''.join(o)

def heat_legend():
    return '<ul class="legend hl" aria-label="Renk ölçeği">' + ''.join(
        f'<li><svg class="lg" width="22" height="16" viewBox="0 0 22 16" aria-hidden="true"><rect class="hb{i}" x="1" y="1" width="20" height="14" rx="3"/></svg>{BIN_LAB[i]}</li>' for i in range(6)) + '</ul>'

# ---------------------------------------------------------------- (d) Tier B charts (SVG)
DRV = [('d1_regulatory', 'Mevzuat'), ('d2_funding', 'Fon'), ('d3_cost', 'Maliyet'),
       ('d4_infra_data', 'Altyapı'), ('d5_workforce', 'İşgücü'), ('d6_local_activity', 'Yerel')]
def wrap(s, n=18):
    words = s.split(); lines = []; cur = ''
    for w in words:
        if len(cur) + len(w) + 1 <= n or not cur: cur = (cur + ' ' + w).strip()
        else: lines.append(cur); cur = w
    lines.append(cur); return lines[:3]

def tierb_svg(sector, sid):
    items = [r for r in rows if r['sector'] == sector]
    order = {'Certain': 0, 'Likely': 1, 'Potential': 2}
    items.sort(key=lambda r: (order[r['class_1_2y']], order[r['class_3_5y']], r['id']))
    W = 442; LX = 4; X0 = 128; CW = 44; MX0 = X0 + 6 * CW + 10; HDR = 44; RH = 40
    H = HDR + RH * len(items) + 44
    o = [f'<svg class="viz" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{sid}-t {sid}-d">'
         f'<title id="{sid}-t">{esc(SECT[sector])}: altı itici güç puanı</title>'
         f'<desc id="{sid}-d">Her satır bir gelişme; çubuk uzunluğu 1 ile 5 arasındaki puanı, renk ve şekil 1–2 yıllık sınıfı gösterir.</desc>']
    for j, (_, nm) in enumerate(DRV):
        o.append(f'<text class="lab s" x="{X0+j*CW+CW/2-2}" y="30" text-anchor="middle">{nm}</text>')
    o.append(f'<text class="lab s" x="{MX0+12}" y="18" text-anchor="middle">Sınıf (yıl)</text>')
    o.append(f'<text class="lab s" x="{MX0}" y="34" text-anchor="middle">1–2</text><text class="lab s" x="{MX0+24}" y="34" text-anchor="middle">3–5</text>')
    y = HDR
    o.append(f'<line class="axis" x1="{LX}" x2="{W-4}" y1="{y-2}" y2="{y-2}"/>')
    for r in items:
        ls = wrap(SHORT[r['id']])
        ty = y + RH / 2 - (len(ls) - 1) * 6.2 + 4
        tsp = ''.join(f'<tspan x="{LX}" dy="{0 if k==0 else 12.4}">{esc(t)}</tspan>' for k, t in enumerate(ls))
        o.append(f'<text class="lab tl" x="{LX}" y="{ty}">{tsp}</text>')
        k1 = CLS_KEY[r['class_1_2y']]
        for j, (col, nm) in enumerate(DRV):
            v = int(r[col]); x = X0 + j * CW
            tip = f'{r["id"]} · {SHORT[r["id"]]} · {nm}: {v}/5'
            o.append(f'<g><title>{esc(tip)}</title><rect class="trk" x="{x+2}" y="{y+RH/2-4}" width="24" height="8" rx="2"/>'
                     f'<rect class="m{k1}" x="{x+2}" y="{y+RH/2-4}" width="{v*4.8:.1f}" height="8" rx="2"/>'
                     f'<text class="lab n{" w" if v<=2 else ""}" x="{x+28}" y="{y+RH/2+4}">{v}</text></g>')
        o.append(marker(r['class_1_2y'], MX0, y + RH / 2, False, f'{r["id"]} · 1–2 yıl: {CLS_TR[r["class_1_2y"]]}'))
        o.append(marker(r['class_3_5y'], MX0 + 24, y + RH / 2, is_lag(r), f'{r["id"]} · 3–5 yıl: {CLS_TR[r["class_3_5y"]]}' + (' (gecikme temelli)' if is_lag(r) else '')))
        y += RH
        o.append(f'<line class="grid" x1="{LX}" x2="{W-4}" y1="{y}" y2="{y}"/>')
    # mean row
    o.append(f'<text class="labb" x="{LX}" y="{y+RH/2+4}">Alan ortalaması</text>')
    means = []
    for j, (col, nm) in enumerate(DRV):
        m = sum(int(r[col]) for r in items) / len(items); means.append(m); x = X0 + j * CW
        o.append(f'<g><title>{esc(SECT[sector]+" · "+nm+" ortalaması: "+format(m,".1f").replace(".",","))}</title><rect class="trk" x="{x+2}" y="{y+RH/2-4}" width="24" height="8" rx="2"/>'
                 f'<rect class="mean" x="{x+2}" y="{y+RH/2-4}" width="{m*4.8:.1f}" height="8" rx="2"/>'
                 f'<text class="lab n" x="{x+28}" y="{y+RH/2+4}">{fmt(m)}</text></g>')
    o.append('</svg>')
    s = ''.join(o)
    return s, means, len(items)

# ---------------------------------------------------------------- numbers for text
def fmt(x): return format(x, '.1f').replace('.', ',')
chartB = {}
for sec, sid in zip(TIERB, ['eco', 'aka', 'sto']):
    svg, means, n = tierb_svg(sec, sid)
    chartB[sec] = (svg, means, n)
def weakest(sec):
    m = chartB[sec][1]; i = sorted(range(6), key=lambda k: m[k]); return [DRV[k][1] for k in i[:2]], [DRV[k][1] for k in i[-2:]]

ids_cert = [r['id'] for r in rows if r['class_1_2y'] == 'Certain']
ids_lik1 = [r['id'] for r in rows if r['class_1_2y'] == 'Likely']
ids_lik2 = [r['id'] for r in rows if r['class_3_5y'] == 'Likely']

classes_json = json.dumps({r['id']: [r['class_1_2y'], r['class_3_5y']] for r in rows}, ensure_ascii=False, separators=(',', ':'))

# ---------------------------------------------------------------- CSS
def bin_css():
    l = ''.join(f'--hb{i}:{BINS_L[i]};--hb{i}t:{ink(BINS_L[i])};' for i in range(6))
    d = ''.join(f'--hb{i}:{BINS_D[i]};--hb{i}t:{ink(BINS_D[i])};' for i in range(6))
    return l, d
BL, BD = bin_css()

CSS = '''
:root{color-scheme:light;
--bg:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--grid:#e1e0d9;--axis:#c3c2b7;--hair:rgba(11,11,11,.12);
--ck:#2a78d6;--co:#eb6834;--cp:#1baf7a;--cd:#4a3aa7;--mean:#898781;--trk:#ecebe6;
--tint:#eaf2fc;--tint2:#fdf1ea;--link:#1c5cab;--band0:#f4f3ef;--band1:#fcfcfb;
@@BL@@}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
--bg:#0d0d0d;--surface:#1a1a19;--ink:#ffffff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--hair:rgba(255,255,255,.14);
--ck:#3987e5;--co:#d95926;--cp:#199e70;--cd:#9085e9;--mean:#898781;--trk:#2c2c2a;
--tint:#14263d;--tint2:#33211a;--link:#86b6ef;--band0:#202020;--band1:#1a1a19;
@@BD@@}}
:root[data-theme="dark"]{color-scheme:dark;
--bg:#0d0d0d;--surface:#1a1a19;--ink:#ffffff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--hair:rgba(255,255,255,.14);
--ck:#3987e5;--co:#d95926;--cp:#199e70;--cd:#9085e9;--mean:#898781;--trk:#2c2c2a;
--tint:#14263d;--tint2:#33211a;--link:#86b6ef;--band0:#202020;--band1:#1a1a19;
@@BD@@}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow-wrap:break-word}
.wrap{max-width:760px;margin:0 auto;padding:0 16px 48px}
header.top{padding:36px 0 8px}
.eyebrow{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);margin:0 0 8px}
h1{font-size:clamp(26px,6vw,38px);line-height:1.15;margin:0 0 12px;letter-spacing:-.01em}
h2{font-size:clamp(22px,4.6vw,28px);line-height:1.2;margin:48px 0 12px;padding-top:8px;border-top:1px solid var(--hair)}
h3{font-size:19px;line-height:1.3;margin:28px 0 8px}
p{margin:0 0 14px}
.lede{font-size:19px;color:var(--ink2)}
.meta{font-size:14px;color:var(--ink2)}
a{color:var(--link)}
.box{background:var(--surface);border:1px solid var(--hair);border-radius:10px;padding:16px 18px;margin:20px 0}
.box.blue{background:var(--tint)}.box.orange{background:var(--tint2)}
.box h3{margin-top:0}
.box ul,.box ol{margin:0;padding-left:20px}.box li{margin:0 0 6px}
ul.bul,ol.bul{padding-left:22px;margin:0 0 14px}ul.bul li,ol.bul li{margin-bottom:7px}
.classes{list-style:none;margin:0;padding:0}.classes li{display:flex;gap:10px;align-items:flex-start;margin:0 0 10px}
.classes svg{flex:none;margin-top:3px}
figure{margin:24px 0;background:var(--surface);border:1px solid var(--hair);border-radius:10px;padding:14px 12px 12px}
figure .ft{font-weight:650;font-size:16px;margin:0 4px 8px}
figcaption{font-size:14.5px;color:var(--ink2);margin:10px 4px 0;line-height:1.5}
svg.viz{display:block;width:100%;height:auto;max-width:560px;margin:0 auto}
svg.viz text{font-family:inherit;font-size:12.5px;fill:var(--ink2)}
svg.viz text.labb{fill:var(--ink);font-weight:650}svg.viz text.s{font-size:11.5px}svg.viz text.tl{font-size:12px}svg.viz text.n{font-size:11.5px}svg.viz text.n.w{font-weight:700;fill:var(--ink)}
svg.viz text.hv{font-size:12.5px;font-weight:650}
.grid{stroke:var(--grid);stroke-width:1}.axis{stroke:var(--axis);stroke-width:1}
.band0{fill:var(--band0)}.band1{fill:var(--band1)}
.mk{fill:var(--ck);stroke:var(--surface);stroke-width:1.5}.mo{fill:var(--co);stroke:var(--surface);stroke-width:1.5}
.mp{fill:var(--cp);stroke:var(--surface);stroke-width:1.5}.md{fill:none;stroke:var(--cd);stroke-width:2}
.mo-lag{fill:var(--surface);stroke:var(--co);stroke-width:2.2}
rect.mk,rect.mo,rect.mp{stroke:none}
.trk{fill:var(--trk)}.mean{fill:var(--mean)}
@@HB@@
ul.legend{list-style:none;margin:8px 4px 0;padding:0;display:flex;flex-wrap:wrap;gap:6px 16px;font-size:14px;color:var(--ink2)}
ul.legend li{display:flex;align-items:center;gap:6px}svg.lg{flex:none}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
table{border-collapse:collapse;width:100%}
table.mx{margin:0;table-layout:fixed;font-size:14.5px}
table.mx th,table.mx td{vertical-align:top;border-top:1px solid var(--grid);padding:10px 8px;text-align:left}
table.mx thead th{border-top:0;font-size:13.5px;color:var(--ink);padding-bottom:6px}
table.mx th.rh{width:26%}table.mx th.rh b{display:block;font-size:16px}
.rd{display:block;font-weight:400;font-size:13px;color:var(--ink2);line-height:1.4;margin-top:2px}
table.mx th.rh svg{display:block;margin-bottom:4px}
.big{font-size:34px;font-weight:700;line-height:1;margin-bottom:6px;letter-spacing:-.02em}
.cell-k .big{color:var(--ink)}
.cell-k{box-shadow:inset 3px 0 0 var(--ck)}.cell-o{box-shadow:inset 3px 0 0 var(--co)}.cell-p{box-shadow:inset 3px 0 0 var(--cp)}.cell-d{box-shadow:inset 3px 0 0 var(--cd)}
ul.chips{list-style:none;margin:0;padding:0}ul.chips li{font-size:13.5px;line-height:1.35;padding:2px 0;cursor:default}
ul.chips li.lag{font-style:italic}
.id{font-size:11.5px;color:var(--ink2);white-space:nowrap}
.sub{font-size:12.5px;font-weight:650;color:var(--ink);margin:8px 0 2px}
.note{font-size:13px;color:var(--ink2);margin:0}
details{margin-top:6px}summary{cursor:pointer;font-size:14px;color:var(--link);padding:4px 0}
table.tv{font-size:13.5px;margin-top:8px}table.tv th,table.tv td{border-top:1px solid var(--grid);padding:6px 6px;text-align:left;vertical-align:top}
.steps{counter-reset:s;list-style:none;margin:0;padding:0}
.steps li{counter-increment:s;position:relative;padding-left:34px;margin:0 0 10px}
.steps li::before{content:counter(s);position:absolute;left:0;top:1px;width:24px;height:24px;border-radius:50%;background:var(--ck);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.rec{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--ck);border-radius:10px;padding:14px 18px 6px;margin:20px 0}
.rec:nth-of-type(2){border-left-color:var(--co)}.rec:nth-of-type(3){border-left-color:var(--cp)}
.rec h3{margin-top:0}
dl.r{margin:0}dl.r dt{font-weight:700;margin-top:10px;font-size:15px;text-transform:uppercase;letter-spacing:.03em;color:var(--ink2)}dl.r dd{margin:2px 0 10px}
.warn{border-left:4px solid var(--co)}
footer{margin-top:44px;padding-top:16px;border-top:1px solid var(--hair);font-size:14.5px;color:var(--ink2)}
footer .box{color:var(--ink)}
@media (max-width:640px){
 body{font-size:16.5px}
 table.mx,table.mx tbody,table.mx tr,table.mx th,table.mx td{display:block;width:100%}
 table.mx thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
 table.mx tr{margin-bottom:12px;border:1px solid var(--grid);border-radius:8px;overflow:hidden}
 table.mx th.rh{width:100%;background:var(--band0)}
 table.mx td::before{content:attr(data-h);display:block;font-size:12.5px;font-weight:700;color:var(--ink2);margin-bottom:4px}
 table.tv,table.tv tbody,table.tv tr,table.tv th,table.tv td{display:block;width:100%}table.tv thead{display:none}
 table.tv td::before{content:attr(data-h);display:block;font-weight:700;font-size:12px;color:var(--ink2)}
}
@media print{body{background:#fff}details>*{display:block}}
'''.replace('@@BL@@', BL).replace('@@BD@@', BD).replace('@@HB@@', ''.join(f'.hb{i}{{fill:var(--hb{i})}}svg.viz text.hb{i}t{{fill:var(--hb{i}t)}}' for i in range(6)))

# ---------------------------------------------------------------- text
ew, aw, sw = weakest('ecology_environment'), weakest('academia_research'), weakest('civil_society')

BODY = open(os.path.join(HERE, 'rapor_tr_body.html'), encoding='utf-8').read()
tok = {
 '@@K1@@': C1['Certain'], '@@L1@@': C1['Likely'], '@@P1@@': C1['Potential'], '@@D1@@': C1['Low'],
 '@@K2@@': C2['Certain'], '@@L2@@': C2['Likely'], '@@P2@@': C2['Potential'], '@@D2@@': C2['Low'],
 '@@LAGN@@': len(LAG), '@@LAGN2@@': C2['Likely'] - len(LAG),
 '@@MATRIX@@': matrix_html(), '@@LEGEND@@': legend_html(), '@@LEGEND_NOLAG@@': legend_html(),
 '@@TIMELINE@@': timeline_svg(), '@@TLTABLE@@': timeline_table(),
 '@@HEATMAP@@': heatmap_svg(), '@@HEATLEG@@': heat_legend(),
 '@@ECO@@': chartB['ecology_environment'][0], '@@AKA@@': chartB['academia_research'][0], '@@STO@@': chartB['civil_society'][0],
 '@@ECOM@@': ' · '.join(f'{nm} {fmt(m)}' for (c, nm), m in zip(DRV, chartB['ecology_environment'][1])),
 '@@AKAM@@': ' · '.join(f'{nm} {fmt(m)}' for (c, nm), m in zip(DRV, chartB['academia_research'][1])),
 '@@STOM@@': ' · '.join(f'{nm} {fmt(m)}' for (c, nm), m in zip(DRV, chartB['civil_society'][1])),
 '@@CLASSES@@': classes_json, '@@CSS@@': CSS,
}
for k, v in tok.items():
    BODY = BODY.replace(k, str(v))
assert '@@' not in BODY, re.findall(r'@@\w+@@', BODY)
open(os.path.join(HERE, 'rapor_tr.html'), 'w', encoding='utf-8').write(BODY)
print('ok', len(BODY.encode('utf-8')), 'min text contrast on heat bins', round(MIN_CONTRAST, 2))
