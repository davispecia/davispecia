# Davi Specia

Analista de dados, com foco em engenharia de dados e IA. Python, SQL, Databricks e Power BI.

Bacharelando em Inteligência Artificial na Faculdade Donaduzzi (Biopark). Moro em Palotina, PR, e tenho disponibilidade imediata.

<a href="https://davispecia.com.br/?utm_source=github&utm_medium=perfil&utm_campaign=readme"><img alt="Portfólio · davispecia.com.br" src="https://img.shields.io/badge/Portf%C3%B3lio%20%C2%B7%20davispecia.com.br-2a78d6?style=flat-square"></a>
<a href="https://www.linkedin.com/in/davispecia/"><img alt="LinkedIn · davispecia" src="https://img.shields.io/badge/LinkedIn%20%C2%B7%20davispecia-0A66C2?style=flat-square"></a>
<a href="mailto:davi.specia@gmail.com"><img alt="davi.specia@gmail.com" src="https://img.shields.io/badge/davi.specia%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white"></a>

<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="SQL" src="https://img.shields.io/badge/SQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="Rust" src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white"> <img alt="Databricks" src="https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white"> <img alt="PySpark" src="https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white"> <img alt="Airflow" src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white"> <img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"> <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white"> <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"> <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/davispecia/davispecia/output/cartao-escuro.svg">
  <img alt="Contribuições no GitHub nos últimos 12 meses, por mês" src="https://raw.githubusercontent.com/davispecia/davispecia/output/cartao.svg" width="100%">
</picture>

## Experiência

**Alugaix, sócio-fundador e analista de dados (out/2023 a nov/2026).** Fui responsável pela área de dados de uma gestora de 60 imóveis por temporada em Toledo e região. Construí a camada analítica (ingestão via API do PMS, indicadores de ocupação, ADR e RevPAR), os painéis de BI da empresa e o Compacta, ferramenta interna que monta anúncios a partir das fotos e dos documentos do imóvel.

## Projetos

**[Cinerd](https://cinerd.davispecia.com.br)**: busca de filmes por descrição, em produção. Catálogo de 22.029 títulos, busca híbrida com 8 sinais (BM25, embeddings multilíngues e5-large, nome de personagem, popularidade) normalizados por z-score. No conjunto de teste, nDCG@10 de 0,829 contra 0,360 do BM25 sozinho. Testei um cross-encoder e tirei da produção, porque o ganho ficou dentro do ruído e a latência aumentou cerca de 40 vezes. Deploy na Oracle Cloud, com DVC, CI e métricas em Prometheus.
`Python` `sentence-transformers` `ONNX Runtime` `DVC` `Docker` `Prometheus`

**[Pipeline de análise de crédito](https://github.com/davispecia/pipeline-analise-credito)**: arquitetura medalhão no Databricks, job serverless de 6 tarefas com Databricks Asset Bundles, tabelas Delta no Unity Catalog, carga incremental com MERGE INTO e quality gate com 20 regras. A mesma lógica roda localmente com PostgreSQL e Airflow, com mais de 40 testes.
`Databricks` `PySpark` `Delta Lake` `Airflow` `PostgreSQL`

**[Rede neural guiada por física para Itaipu](https://github.com/davispecia/PGNN_itaipu)**: implementada do zero em Rust, com retropropagação e Adam escritos à mão, sobre dados do ONS de 2015 a 2024. Na ablação, o modelo sem o termo físico errou menos nos dados, mas teve resíduo físico cerca de 33 vezes maior. O cenário operacional chegou a RMSE de 508 MWmed (R² de 0,91) e superou a persistência em todos os anos da validação de 2020 a 2024.
`Rust` `Physics-Guided ML`

## Publicações

- Modelagem da geração hidrelétrica de Itaipu via redes neurais guiadas por física em Rust. Latin.Science 2026, Latinoware (artigo aprovado).
- Estimativa de peso de suínos a partir de imagens RGB utilizando redes neurais convolucionais. [RECIMA21, 2026](https://recima21.com.br/recima21/pt_BR/article/view/8496).

## Prêmios

- 1º lugar no Hackathon da Semana Acadêmica de Tecnologia da Faculdade Donaduzzi, com o MobIA (mai/2026).
- 3º lugar no Hackatour Cataratas, como líder e analista de dados do TripData (abr/2026).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/davispecia/davispecia/output/cobrinha-escura.svg">
  <img alt="Cobrinha percorrendo o gráfico de contribuições" src="https://raw.githubusercontent.com/davispecia/davispecia/output/cobrinha.svg" width="100%">
</picture>

<sub>O cartão e a cobrinha são atualizados todo dia por um workflow deste repositório (<code>scripts/cartao.py</code>), a partir da API do GitHub.</sub>
