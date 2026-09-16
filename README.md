# Davi Specia

**Cientista de dados** — NLP, recuperação de informação e modelos em
produção. Python.

Bacharelando em Inteligência Artificial.

📍 Toledo, PR · 📧 davi.specia@gmail.com · [LinkedIn](https://www.linkedin.com/in/davi-specia-7b60962a2/)

---

## Projetos

**[Cinerd](https://cinerd.davispecia.com.br)** — busca semântica de filmes,
no ar. Recuperação híbrida sobre 22.029 títulos: BM25 + embeddings
multilíngues (e5, 1024 dim) + sinal temático, fundidos por z-score, com
reranking por cross-encoder. nDCG@10 de <valor> contra <valor> do baseline.
Recomendação por SVD (RMSE 0,80 em ~2,9M avaliações) fundida por RRF com
perfil multi-interesse.
→ [Números de ablação, latência e protocolo de avaliação](https://cinerd.davispecia.com.br/engineering)
(aba Engenharia, com p99 ao vivo do tráfego real)
`Python` `sentence-transformers` `ONNX` `DVC` `Prometheus` `Docker`

**[PGNN para geração hidrelétrica — Itaipu](https://github.com/davidogral/PGNN_itaipu)** — rede guiada por
física escrita do zero em Rust, com retropropagação e Adam manuais, sobre
séries do ONS (2015–2024). A ablação do termo físico mostrou que o modelo
sem restrição teve o menor erro de dados e o maior resíduo físico: MSE
menor não significa modelo fisicamente melhor. Aceito no **Latinoware**.
`Rust` `Physics-Guided ML`

**[Estimativa de peso de suínos]** — visão computacional em condição
de granja, erro médio de <valor>. Publicado na RECIMA21.
`Python` `Computer Vision`

---

## Publicações

- **Latinoware** — Physics-Guided Neural Network para geração hidrelétrica.
  Aceito para publicação.
- **RECIMA21** — Estimativa de peso de suínos por visão computacional.
  [Artigo](https://recima21.com.br/recima21/pt_BR/article/view/8496)

---

## Experiência

**Alugaix** — sócio-fundador e CTO desde 2024. Camada analítica de uma
operação de locação por temporada: ingestão via API de PMS, indicadores de
ocupação, ADR e RevPAR, e reconstrução de receita após migração de sistema.

---

## Stack

Python, Rust, SQL · pandas, scikit-learn, XGBoost, PyTorch ·
sentence-transformers, BM25, cross-encoder · DVC, MLflow, Docker,
GitHub Actions, Prometheus · FastAPI, Power BI
