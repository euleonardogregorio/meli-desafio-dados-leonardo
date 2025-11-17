# 📮 Automação – Envio Automático do Dashboard via Looker (por e-mail)

Objetivo:  
Configurar o **envio automático do dashboard** por e-mail, toda **segunda-feira às 9:00 a.m.**, diretamente pelo Looker / Looker Studio.

---

## 1. Pré-requisitos

- Dashboard pronto e publicado no Looker / Looker Studio.
- Lista de e-mails dos destinatários (ex.: operação, gestão, coordenadores).
- Permissões de acesso ao dashboard para todos os envolvidos.

---

## 2. Passo a passo no Looker / Looker Studio

1. Abra o **dashboard** que você quer enviar automaticamente.
2. Clique em **Compartilhar**.
3. Selecione a opção **Agendar envio por e-mail** (Schedule email).
4. Preencha os campos:
   - **Destinatários:** e-mails separados por vírgula  
     `ex.: operacao@empresa.com, gestao@empresa.com`
   - **Assunto:**  
     `Dashboard ICQA – Atualização Semanal`
   - **Mensagem do e-mail:**  
     Texto curto explicando o que é o dashboard e qual período está sendo analisado.
   - **Formato:** escolha **PDF** (mais comum) ou **link de acesso**.

---

## 3. Configurar o horário e a recorrência

Na parte de agendamento:

- **Frequência:** `Semanal (Weekly)`
- **Dia:** `Segunda-feira`
- **Horário:** `09:00`
- **Fuso horário:** `America/Sao_Paulo` (ou equivalente)

Clique em **Salvar**.

---

## 4. Resultado da automação

- Toda **segunda-feira às 9:00 a.m.**, o Looker / Looker Studio:
  - Atualiza o dashboard com os dados mais recentes.
  - Gera o PDF (ou link).
  - Envia automaticamente o e-mail para os destinatários configurados.

Nenhuma ação manual é necessária após a configuração.

---
