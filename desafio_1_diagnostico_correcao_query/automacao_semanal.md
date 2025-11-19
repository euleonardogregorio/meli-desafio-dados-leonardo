# 🔄 Como Configurar a Atualização Automática Semanal no BigQuery

Abaixo está um passo a passo simples para criar uma atualização semanal automática dos dados usando **Scheduled Queries** no BigQuery. Esse processo garante que sua tabela final seja renovada toda semana com os dados mais recentes.

---

## 🟦 1. Criar a tabela final que será atualizada

Primeiro, execute sua query final (aquela que consolida todos os CTEs e gera o resultado completo).  
Depois, salve o resultado em uma tabela:

**Caminho:**
1. Rodar a query
2. `Salvar resultado` → `Salvar na tabela`
3. Definir:
   - Dataset: `meli_dataset`
   - Tabela: `resultado_icqa_semana`
   - Modo: **Overwrite**

---

## 🟩 2. Criar a Scheduled Query

1. No menu lateral do BigQuery, vá em **Consultas Programadas** (Scheduled Queries).
2. Clique em **Criar Tarefa**.
3. Dê um nome simples, por exemplo:
   - **Nome:** `update_icqa_semanal`
4. Cole sua **query final completa** na caixa de edição.
5. Em *Configurações de destino*, selecione:
   - **Overwrite table**
   - **Dataset:** `meli_dataset`
   - **Tabela:** `resultado_icqa_semana`

Assim, toda execução substituirá a tabela com dados atualizados.

---

## 🟧 3. Definir o agendamento semanal

Na área de agendamento:

- **Frequência:** Weekly  
- **Dia:** Monday  
- **Horário:** 08:00  
- **Timezone:** America/Sao_Paulo  

Isso garante que a atualização sempre aconteça antes do início da operação da semana.

---

## 🟨 4. (Opcional) Ativar alerta por falha

Nas opções avançadas:

- Ativar: **Notify on failure**  
- Inserir seu e-mail  

Assim você recebe aviso se a atualização falhar.
