"""Gera o cabeçalho e o cartão de contribuições do perfil (SVG claro e escuro).

Lê o calendário de contribuições pela API GraphQL do GitHub e escreve
dist/cartao*.svg e dist/cabecalho*.svg. Só usa a biblioteca padrão.
Uso: GITHUB_TOKEN=... python scripts/cartao.py [usuario]
"""
import json
import os
import sys
import urllib.request
from collections import OrderedDict
from datetime import date, datetime, timezone
from pathlib import Path

USUARIO = sys.argv[1] if len(sys.argv) > 1 else "davispecia"
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

TEMAS = {
    "cartao": {"fundo": "#ffffff", "borda": "#d0d7de", "texto": "#1f2328", "suave": "#59636e",
               "grade": "#eaeef2", "barra": "#2a78d6"},
    "cartao-escuro": {"fundo": "#0d1117", "borda": "#30363d", "texto": "#f0f6fc", "suave": "#9198a1",
                      "grade": "#21262d", "barra": "#3987e5"},
}

CONSULTA = """query($login: String!) { user(login: $login) { contributionsCollection {
  contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }"""


def buscar_dias():
    corpo = json.dumps({"query": CONSULTA, "variables": {"login": USUARIO}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=corpo, headers={
        "Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "User-Agent": "cartao-perfil"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        dados = json.load(resp)
    if "errors" in dados:
        raise SystemExit(dados["errors"])
    cal = dados["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    dias = [(date.fromisoformat(d["date"]), d["contributionCount"])
            for s in cal["weeks"] for d in s["contributionDays"]]
    return sorted(dias), cal["totalContributions"]


def sequencias(dias):
    maior = atual = 0
    for _, n in dias:
        atual = atual + 1 if n else 0
        maior = max(maior, atual)
    corrente, inicio = 0, len(dias) - 1
    if dias and dias[-1][1] == 0:  # o dia de hoje ainda não acabou
        inicio -= 1
    for i in range(inicio, -1, -1):
        if not dias[i][1]:
            break
        corrente += 1
    return corrente, maior


def por_mes(dias):
    meses = OrderedDict()
    for d, n in dias:
        meses[(d.year, d.month)] = meses.get((d.year, d.month), 0) + n
    return list(meses.items())[-12:]


def dias_txt(n):
    return f"{n} dia" if n == 1 else f"{n} dias"


def num(n):
    return f"{n:,}".replace(",", ".")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;")


def svg(cores, total, ativos, corrente, maior, meses, dia_forte, hoje):
    W, H = 840, 346
    fonte = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
    p = [(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'role="img" aria-labelledby="t d" font-family="{fonte}">'),
         f'<title id="t">Contribuições de {USUARIO} no GitHub</title>',
         f'<desc id="d">{num(total)} contribuições nos últimos 12 meses, {ativos} dias ativos, '
         f'maior sequência de {dias_txt(maior)}. Por mês: '
         + ", ".join(f"{MESES[m-1]}/{a}: {n}" for (a, m), n in meses) + '.</desc>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{cores["fundo"]}" stroke="{cores["borda"]}"/>']
    # Indicadores
    (a_top, m_top), n_top = max(meses, key=lambda x: x[1])
    media = f"{total / ativos:.1f}".replace(".", ",") if ativos else "0"
    blocos = [("Contribuições em 12 meses", num(total)), ("Dias com contribuição", num(ativos)),
              ("Mês mais ativo", f"{MESES[m_top-1]}/{str(a_top)[2:]} · {num(n_top)}"),
              ("Média por dia ativo", media)]
    larg = (W - 48) / 4
    for i, (rot, val) in enumerate(blocos):
        x = 24 + i * larg
        p.append(f'<text x="{x:.0f}" y="44" font-size="13" fill="{cores["suave"]}">{rot}</text>')
        p.append(f'<text x="{x:.0f}" y="76" font-size="26" font-weight="600" fill="{cores["texto"]}">{val}</text>')
    # Gráfico de barras por mês
    p.append(f'<text x="24" y="124" font-size="14" font-weight="600" fill="{cores["texto"]}">Contribuições por mês</text>')
    topo, base, esq, dir_ = 150, 280, 24, W - 24
    maximo = max(n for _, n in meses) or 1
    passo = (dir_ - esq) / len(meses)
    barra = passo * 0.62
    for frac in (0.5, 1.0):
        y = base - (base - topo) * frac
        p.append(f'<line x1="{esq}" x2="{dir_}" y1="{y:.1f}" y2="{y:.1f}" stroke="{cores["grade"]}"/>')
    p.append(f'<line x1="{esq}" x2="{dir_}" y1="{base}" y2="{base}" stroke="{cores["borda"]}"/>')
    i_max = max(range(len(meses)), key=lambda i: meses[i][1])
    for i, ((a, m), n) in enumerate(meses):
        x = esq + i * passo + (passo - barra) / 2
        h = (base - topo) * n / maximo
        if n:
            r = min(4, h)
            p.append(f'<path d="M{x:.1f},{base} V{base-h+r:.1f} Q{x:.1f},{base-h:.1f} {x+r:.1f},{base-h:.1f} '
                     f'H{x+barra-r:.1f} Q{x+barra:.1f},{base-h:.1f} {x+barra:.1f},{base-h+r:.1f} V{base} Z" '
                     f'fill="{cores["barra"]}"><title>{MESES[m-1]}/{a}: {n}</title></path>')
        cx = x + barra / 2
        rot = MESES[m-1] + (f"/{str(a)[2:]}" if m == 1 or i == 0 else "")
        p.append(f'<text x="{cx:.1f}" y="{base+18}" font-size="12" text-anchor="middle" fill="{cores["suave"]}">{rot}</text>')
        if i in (i_max, len(meses) - 1) and n:
            p.append(f'<text x="{cx:.1f}" y="{base-h-6:.1f}" font-size="12" font-weight="600" '
                     f'text-anchor="middle" fill="{cores["texto"]}">{num(n)}</text>')
    nota = (f"Dia mais ativo: {dia_forte}. Maior sequência: {dias_txt(maior)}. Mês atual até {hoje.day:02d}/{hoje.month:02d}. "
            f"Inclui contribuições em repositórios privados. Atualizado em {hoje:%d/%m/%Y}.")
    p.append(f'<text x="24" y="{H-18}" font-size="11.5" fill="{cores["suave"]}">{esc(nota)}</text>')
    p.append("</svg>")
    return "\n".join(p)


MARCA = ('<rect width="48" height="48" rx="12" fill="#0F172A"/>'
         '<path d="m8 17 16-9 16 9-16 9Z" fill="#3B82F6"/>'
         '<path d="m8 25 16 9 16-9M8 33l16 9 16-9" fill="none" stroke="#22D3EE" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/>')


def cabecalho(cores, verde):
    W, H = 840, 150
    fonte = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
    fatos = ["Ex-sócio-fundador da Alugaix", "2 artigos científicos", "2 prêmios em hackathons"]
    p = [(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'role="img" aria-labelledby="t" font-family="{fonte}">'),
         '<title id="t">Davi Specia, analista de dados, Palotina, PR. Disponível para contratação.</title>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{cores["fundo"]}" stroke="{cores["borda"]}"/>',
         f'<g transform="translate(24 43) scale(1.333)">{MARCA}</g>',
         f'<text x="108" y="62" font-size="30" font-weight="600" fill="{cores["texto"]}">Davi Specia</text>',
         f'<text x="108" y="88" font-size="16" fill="{cores["suave"]}">Analista de dados · Engenharia de dados e IA</text>',
         f'<circle cx="113" cy="113" r="5" fill="{verde}"/>',
         f'<text x="125" y="118" font-size="14" fill="{cores["texto"]}">Disponível para contratação · Palotina, PR</text>',
         f'<line x1="540" x2="540" y1="34" y2="{H-34}" stroke="{cores["borda"]}"/>']
    for i, f in enumerate(fatos):
        y = 58 + i * 26
        p.append(f'<rect x="566" y="{y-9}" width="8" height="8" rx="2" fill="{cores["barra"]}"/>')
        p.append(f'<text x="582" y="{y}" font-size="13.5" fill="{cores["suave"]}">{esc(f)}</text>')
    p.append("</svg>")
    return "\n".join(p)


def main():
    dias, total = buscar_dias()
    corrente, maior = sequencias(dias)
    ativos = sum(1 for _, n in dias if n)
    soma = [0] * 7
    for d, n in dias:
        soma[d.weekday()] += n
    dia_forte = DIAS[soma.index(max(soma))]
    hoje = dias[-1][0] if dias else datetime.now(timezone.utc).date()
    meses = por_mes(dias)
    saida = Path("dist")
    saida.mkdir(exist_ok=True)
    for nome, cores in TEMAS.items():
        verde = "#1a7f37" if nome == "cartao" else "#3fb950"
        (saida / f"{nome.replace('cartao', 'cabecalho')}.svg").write_text(cabecalho(cores, verde), encoding="utf-8")
        (saida / f"{nome}.svg").write_text(svg(cores, total, ativos, corrente, maior, meses, dia_forte, hoje), encoding="utf-8")
    print(f"{total} contribuições, {ativos} dias ativos, sequência {corrente}/{maior}, {len(meses)} meses")


if __name__ == "__main__":
    main()
