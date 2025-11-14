🟩 ICQA – Solução Completa de Dados

Pipeline moderno, inteligente e automatizado, desenvolvido para transformar dados brutos em insights acionáveis.
Este projeto demonstra domínio em SQL, qualidade de dados, arquitetura, análise exploratória, dashboards e automação.

🧭 Sumário

Visão Geral

Arquitetura da Solução

Etapa 1 — Correção e Otimização da Query

Etapa 2 — Processamento e Tabela Final no-BigQuery

Etapa 3 — Análise Exploratória com IA

Etapa 4 — Dashboard Analítico

Etapa 5 — Automação Semanal

Estrutura do Repositório

Tecnologias Utilizadas

Autor

🚀 Visão Geral

Este projeto apresenta uma solução completa de dados (end-to-end) criada para resolver um desafio técnico que envolve:

Problema em uma query SQL

Qualidade, limpeza e validação dos dados

Processamento e criação de tabela final no BigQuery

Identificação dos piores desempenhos semanais

Análise exploratória com IA

Construção de dashboard

Automação semanal de relatórios

A entrega vai além do código: traz clareza, arquitetura, inteligência analítica e storytelling técnico como esperado em times de dados modernos.

🏗 Arquitetura da Solução
📥 Entrada de Dados
    - CSV original
    - Query inicial com problemas
        ↓
🔧 Tratamento e Correção de Query (SQL)
    - Limpeza
    - Normalização
    - CTEs
        ↓
🗄 BigQuery – Tabela Final Particionada
    - KPIs calculados
    - Ranking semanal
        ↓
🤖 Análise Exploratória com IA
    - Padrões
    - Outliers
    - Tendências
        ↓
📊 Dashboard Analítico
    - Filtros
    - Tendências
    - Ranking de pior desempenho
        ↓
📨 Automação Semanal
    - Scheduled Query
    - Envio de e-mail automático


Versão visual:
➡ /arquitetura/arquitetura.png

🛠 Etapa 1 — Correção e Otimização da Query

Nesta etapa foram aplicadas boas práticas de engenharia e análise:

Revisão de todos os JOINs

Tratamento de duplicidades

Normalização de KPIs

Criação de CTEs organizadas

Cálculo seguro da taxa com SAFE_DIVIDE

Identificação de piores desempenhos com ROW_NUMBER()

Documentação completa:
➡ /consultas/explicacao_query.md

SQL disponibilizado em:

query_original.sql

query_corrigida.sql

🗃 Etapa 2 — Processamento e Tabela Final no BigQuery

Criada a tabela:

dataset.kpi_piores_sites_semana


Com:

Particionamento por semana

Clustering por KPI

Campos calculados

Otimização para dashboards

Recarga semanal automática

Script utilizado:
➡ /scripts/consulta_agendada.sql

🤖 Etapa 3 — Análise Exploratória com IA

A IA foi utilizada como ferramenta de análise de alto nível:

Identificação de outliers

Padrões e recorrências

Hipóteses operacionais

Recomendações práticas

Resumo executivo para tomada de decisão

Documentos:

prompt.md → comando enviado

insights.md → análise gerada

📊 Etapa 4 — Dashboard Analítico

O dashboard possibilita:

Investigação por KPI

Comparação semanal

Identificação rápida dos piores desempenhos

Drill-down por site

Tendência temporal

Screenshots:
➡ /dashboard/screenshots/

Descrição:
➡ /dashboard/descricao_dashboard.md

Ferramentas possíveis:
Looker Studio, Power BI, Streamlit ou Dash.

🔁 Etapa 5 — Automação Semanal

Foi implementada uma automação completa:

BigQuery Scheduled Query para atualizar a tabela

Script Python para:

gerar resumo

anexar prints

enviar e-mail

adicionar link do dashboard

Código em:
➡ /scripts/envio_email.py

📁 Estrutura do Repositório
icqa-dados-leonardo/
│
├── README.md
├── arquitetura/
├── consultas/
├── dados/
├── analise_ia/
├── dashboard/
├── scripts/
└── notebooks/


Cada pasta contém arquivos específicos para manter o projeto limpo, modular e escalável.

🧰 Tecnologias Utilizadas

SQL (BigQuery)

Python

AI – Large Language Models (ChatGPT / Gemini)

Power BI / Looker Studio

GitHub & GitHub Pages

Miro (Design da Arquitetura)

👤 Autor

Leonardo Gregorio
Engenheiro de Tecnologia | Dados & Analytics
Transformando problemas complexos em soluções inteligentes e práticas.
