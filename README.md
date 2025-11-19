# Desafio de Dados – ICQA (Mercado Livre)

Este repositório contém minha solução completa para o desafio de dados da área de ICQA, cobrindo:

- Diagnóstico e correção de uma query SQL  
- Criação de tabela final no BigQuery com atualização semanal  
- Análise exploratória com IA (prompt + insights)  
- Dashboard semanal com automação de envio  

---

## 📂 Estrutura do repositório

### 🔎 [Desafio 1 – Diagnóstico e Correção de Query](https://github.com/euleonardogregorio/meli-desafio-dados-leonardo/tree/main/desafio_1_diagnostico_correcao_query)

Nesta pasta você encontra:

- Query original e query corrigida  
- Documento explicando:
  - Três erros ou más práticas da query original  
  - Como a query corrigida retorna apenas colunas válidas  
  - Por que o resultado final é relevante
- Pseudocódigo e instruções para:
  - Criar tabela final no BigQuery  
  - Programar atualização semanal via *scheduled queries*  

---

### 🤖 [Desafio 2 – Análise Exploratória com IA](https://github.com/euleonardogregorio/meli-desafio-dados-leonardo/tree/main/desafio_2_analise_exploratoria/analise_ia)

Nesta pasta estão:

- O **prompt elaborado** para IA  
- O **resultado resumido da IA**, incluindo:
  - Padrões anormais  
  - Categorias com maior participação  
  - Tendências semanais  
  - Relação entre numerador, processos críticos e insights acionáveis  

---

### 📊 [Desafio 3 – Dashboard e Automação](https://github.com/euleonardogregorio/meli-desafio-dados-leonardo/tree/main/desafio_3_dashboard_automacao)

### [LookerSudio | ICQA – Indicadores Semanais de Performance](https://lookerstudio.google.com/reporting/885543ab-aa97-4163-b590-7b5b0c28e236)

Aqui você encontra:

- Prints ou link do dashboard  
- KPIs entregues: vendas totais, ticket médio, ranking, evolução semanal, baixa performance  
- Documento técnico do fluxo de automação:
  - Ferramenta usada (Looker Studio, Power BI etc.)  
  - Como os dados são consumidos  
  - Como ocorre o envio automático toda segunda-feira às 9h  

---

### 🧩 [Desenho da Solução (Arquitetura)](https://github.com/euleonardogregorio/meli-desafio-dados-leonardo/tree/main/desenho_solucao)

Inclui:

- Fluxo completo da solução:  
  CSV → Correção SQL → BigQuery → Scheduled Query → IA (ChatGPT/NotebookLM) → Python para explosão → Google Sheets → Looker Dashboard → Automação por e-mail
- Diagramas do pipeline de dados  
- Descrição das decisões técnicas  
- Documentação end-to-end 

---

## ✔ Como a solução atende ao desafio

- Correção detalhada da query original com documentação técnica  
- Criação de tabela final no BigQuery com atualização semanal  
- Análise exploratória com IA, usando prompting estruturado  
- Dashboard completo no Looker Studio com:
- KPIs  
- gráficos semanais  
- ranking de vendas  
- avaliação de baixo desempenho  
- filtro global por semana  
- Automação total (query + envio do dashboard)

---

## 🛠 Tecnologias e Ferramentas Utilizadas

- **BigQuery** (SQL, Scheduled Queries)
- **Python** (Explosão e transformação dos dados)
- **Google Sheets** (dataset consumido no Looker)
- **Looker Studio** (dashboard + automação de envio)
- **ChatGPT / NotebookLM** (Análise exploratória e documentação)
- **GitHub** (versionamento e documentação do desafio)


