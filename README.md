# DIO Agent - Especializado em Ciberseguranca

> DIO Agent customizado com skill de analise de vulnerabilidades, atuando como mentor de AppSec.

## Sobre o Projeto

Este projeto e uma evolucao do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) original, especializado em **ciberseguranca**. O agente foi transformado num mentor de seguranca da informacao que conduz analises de vulnerabilidades como um profissional de AppSec faria: perguntando o contexto, avaliando severidade e orientando a correcao.

### Por que essa especializacao?

Um profissional de seguranca nao chega e diz "isso esta errado". Ele:
1. **Entende o contexto** — onde roda, quem acessa, o que protege
2. **Classifica o risco** — nem toda falha e critica
3. **Documenta com padrao** — CWE, MITRE ATT&CK, OWASP
4. **Orienta a correcao** — e valida depois

O agente ensina esse processo, nao apenas aponta falhas.

---

## O que foi criado e alterado

### Arquivos criados

| Arquivo | Descricao |
|---------|-----------|
| `skills/vulnerability-analysis/SKILL.md` | Skill de analise de vulnerabilidades — o roteiro que o agente segue |
| `skills/vulnerability-analysis/README.md` | Explicacao da skill para pessoas |
| `agent/knowledge/security-basics.md` | Base de conhecimento: triade CIA, OWASP Top 10, MITRE ATT&CK, CWEs, boas praticas |
| `app.py` | Aplicacao vulneravel a SQL Injection (para demonstracao) |
| `app_seguro.py` | Versao corrigida com consultas parametrizadas e hash de senhas |

### Arquivos alterados

| Arquivo | O que mudou |
|---------|-------------|
| `agent/persona.md` | Adicionada secao "Especialidade em Ciberseguranca" com o perfil de analista AppSec |
| `AGENTS.md` | Adicionada a skill "Analise de vulnerabilidades" na tabela de skills e o knowledge de seguranca na base de conhecimento |

---

## Estrutura do Projeto

```
dio-agent-security/
├── README.md                    Este guia
├── AGENTS.md                    Definicao do agente (alterado)
├── CLAUDE.md                    Atalho para o Claude Code
├── app.py                       App vulneravel (SQL Injection) - NOVO
├── app_seguro.py                App corrigido (parametrizado) - NOVO
├── agent/
│   ├── persona.md               Personalidade do agente (alterado)
│   └── knowledge/
│       ├── dio-platform.md      Conhecimento sobre a DIO
│       ├── learning-experiences.md  Experiencias educacionais
│       └── security-basics.md   Fundamentos de seguranca - NOVO
├── skills/
│   ├── README.md                Como criar skills
│   ├── vulnerability-analysis/  Skill de seguranca - NOVA
│   │   ├── SKILL.md             Roteiro do agente
│   │   └── README.md            Explicacao para pessoas
│   ├── study-plan/              (original)
│   ├── explain-concept/         (original)
│   ├── unblock-challenge/       (original)
│   ├── web-search/              (original)
│   ├── portfolio-review/        (original)
│   └── ai-builder-path/         (original)
└── docs/
    ├── glossary.md              Glossario
    └── youcom-mcp.md            Configuracao You.com
```

---

## Como rodar o agente

### 1. Instale um harness

O agente funciona em qualquer harness compativel com `AGENTS.md`:

| Harness | Documentacao |
|---------|--------------|
| Hermes (usado nas aulas) | https://hermes-agent.nousresearch.com/docs |
| Claude Code | https://code.claude.com/docs |
| Google Antigravity | https://antigravity.google/docs |

### 2. Abra o projeto no harness

```bash
git clone https://github.com/BrunoVieiraMendes/dio-agent-security.git
cd dio-agent-security
```

No Hermes, abra o terminal **dentro da pasta do projeto** e rode:

```bash
hermes
```

**Importante:** o terminal precisa estar na pasta que contem o `AGENTS.md`. Se abrir em outro lugar, o harness nao encontra os arquivos.

### 3. Teste a skill de seguranca

Envie ao agente:

```
Analise o arquivo app.py como especialista em AppSec.
Identifique as vulnerabilidades, classifique a severidade,
cite a tecnica do MITRE ATT&CK e me oriente a corrigir.
```

O agente vai:
1. Perguntar o contexto (onde roda, quem acessa)
2. Identificar o SQL Injection (CWE-89)
3. Classificar como severidade Critica
4. Explicar como seria explorado
5. Pedir para voce corrigir
6. Validar a correcao

---

## Demonstracao: SQL Injection

### O codigo vulneravel (`app.py`)

A funcao de login concatena a entrada do usuario direto na query SQL:

```python
query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
```

Um atacante usa `' OR '1'='1` como username e password, e a query vira:

```sql
SELECT * FROM usuarios WHERE username = '' OR '1'='1' AND password = '' OR '1'='1'
```

Resultado: acesso sem saber a senha.

### A correcao (`app_seguro.py`)

Usa consulta parametrizada — o `?` impede que a entrada do usuario seja interpretada como SQL:

```python
cursor.execute(
    "SELECT * FROM usuarios WHERE username = ?",
    (username,)
)
```

Alem disso:
- Senhas armazenadas com **hash SHA-256 + salt** (nao em texto puro)
- Mensagem de erro generica (nao revela se o usuario existe)

### Rodando os testes

```bash
python app.py          # mostra a vulnerabilidade sendo explorada
python app_seguro.py   # mostra as tentativas sendo bloqueadas
```

---

## A skill em detalhes

A skill `vulnerability-analysis` segue um processo de 7 etapas:

1. **Entender o contexto** — perguntar antes de analisar
2. **Identificar vulnerabilidades** — com CWE e MITRE ATT&CK
3. **Avaliar severidade** — impacto x probabilidade
4. **Demonstrar a exploracao** — apenas em laboratorio
5. **Orientar a correcao** — ensinar, nao entregar pronto
6. **Validar a correcao** — confirmar que a falha foi mitigada
7. **Resumir no formato padrao** — tabela com severidade e status

### Formato padrao de saida

Toda analise termina com um resumo estruturado, permitindo comparar diferentes cenarios:

```
| # | Vulnerabilidade | Severidade | Status |
|---|----------------|-----------|--------|
| 1 | SQL Injection   | Critica   | Corrigida |
```

---

## Melhoria escolhida: formato padronizado de analise

A melhoria implementada foi **padronizar a saida da analise** com impacto, probabilidade e severidade em formato tabular. Isso permite:

- Comparar analises de diferentes cenarios
- Priorizar correcoes por severidade
- Documentar o estado das vulnerabilidades (corrigida/pendente)
- Integrar com fluxos de DevSecOps (cada alteracao pode ser analisada antes de ir para producao)

---

## Teste com outro cenario

Alem do SQL Injection, voce pode testar com cenarios como:

```
Tenho um servidor Ubuntu de laboratorio exposto na internet,
rodando Apache com a pagina padrao. O SSH esta aberto na porta 22
com autenticacao por senha. Me ajude a avaliar os riscos.
```

O agente deve **perguntar o contexto** antes de sugerir qualquer comando.

---

## Aviso Legal

- Todo codigo vulneravel e para **fins educacionais** em ambiente controlado
- Testes de seguranca so devem ser feitos em sistemas proprios ou com autorizacao
- Lei 12.737/2012 (Lei Carolina Dieckmann) tipifica acesso nao autorizado como crime
- Sempre pratique **divulgacao responsavel**

---

## Creditos

- Projeto base: [DIO Agent](https://github.com/digitalinnovationone/dio-agent) por [DIO](https://dio.me)
- Especializacao em seguranca: Bruno Vieira Mendes
- Desafio do curso de Ciberseguranca da DIO
