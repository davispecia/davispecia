# Davi Specia

**Machine Learning Engineer** — pipelines, serving e avaliação rigorosa.
Python e Rust.

Bacharelando em Inteligência Artificial. Trabalho com o ciclo completo: dado versionado,
treino reproduzível, modelo servido e monitorado.

📍 Toledo, Paraná — Brasil
🎓 Bacharelado em Inteligência Artificial — em andamento
📧 [davi.specia@gmail.com](mailto:davi.specia@gmail.com)

---

## Projetos

**[Busca semântica de filmes](<link>)** — recuperação por conceito
("filme onde o cara acorda sem memória"), sobre dataset próprio de
<N> títulos construído via scraping do IMDB e reconciliado com a
API do TMDB (<X>% de match). Busca híbrida BM25 + vetorial,
nDCG@10 de <valor> contra <valor> do baseline. Servido em FastAPI,
p99 de <N>ms. [Demo ao vivo](<link>)
`Python` `Rust` `FastAPI` `DVC` `Prometheus` `Docker`

**[Classificação de mamografias](<link>)** — suspeito vs. normal em
DICOM, treino no RSNA-2023 com validação externa no VinDr-Mammo.
Ablação de <N> configurações. AUC interno <valor>, externo <valor>.
Não é dispositivo médico.
`Python` `PyTorch` `MONAI` `MLflow` `DICOM`

**[PGNN para geração hidrelétrica — Itaipu](<link>)** — rede guiada por
física implementada do zero em Rust, com backprop e Adam manuais.
Ablação do termo físico mostrou que o modelo sem restrição obteve o
menor erro de dados e o maior resíduo físico: MSE menor não significa
modelo fisicamente melhor.
`Rust` `Physics-Guided ML` `ONS 2015–2024`

**[Estimativa de peso de suínos](<link>)** — visão computacional em
condição de granja, erro médio de <valor>. Publicado na RECIMA21.
`Python` `Computer Vision`

**[Decisão de crédito sob custo assimétrico](<link>)** — threshold
otimizado por matriz de custo em vez de F1, validação temporal,
calibração (Brier <valor>) e auditoria de disparidade por subgrupo.
`Python` `XGBoost` `Scikit-learn`

---

## Publicações

- Estimativa de peso de suínos por visão computacional — **RECIMA21**,
  <2026>. [ESTIMATIVA DE PESO DE SUÍNOS A PARTIR DE IMAGENS RGB UTILIZANDO REDES NEURAIS CONVOLUCIONAIS E O DATASET PIGRGB-WEIGHT](<https://recima21.com.br/recima21/pt_BR/article/view/8496>)
- Physics-Guided Neural Network para geração hidrelétrica —
  **Latinoware <2026>**, submetido.

---

## Stack

Python, Rust, SQL · PyTorch, scikit-learn, DVC, ·
MLflow, Pandera · FastAPI, Docker, GitHub Actions ·
Prometheus, Grafana

## 📊 GitHub

<p align="left">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=davidogral&theme=transparent&hide_border=true&date_format=M%20j%5B%2C%20Y%5D&card_width=340" alt="GitHub Streak" height="170">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=davidogral&theme=github_dark" alt="GitHub Stats" height="170">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=davidogral&theme=github_dark" alt="Most Used Languages" height="170">
</p>

## 📫 Contato

📧 **[davi.specia@gmail.com](mailto:davi.specia@gmail.com)**
