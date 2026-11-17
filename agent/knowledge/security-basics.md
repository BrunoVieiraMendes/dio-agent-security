# Fundamentos de Seguranca da Informacao

Este arquivo e a base de conhecimento do DIO Agent para conversas sobre ciberseguranca. Ele define os conceitos essenciais que o agente usa ao analisar vulnerabilidades.

## Conceitos fundamentais

### Vulnerabilidade

Uma fraqueza num sistema, aplicacao ou processo que pode ser explorada por um atacante. Exemplos: falta de validacao de entrada, senha padrao, porta aberta desnecessariamente.

### Ameaca

Qualquer evento ou acao que pode explorar uma vulnerabilidade e causar dano. Pode ser um atacante humano, um malware, um desastre natural ou ate um erro de configuracao.

### Risco

A combinacao de uma ameaca explorando uma vulnerabilidade e o impacto que isso causa. Risco = Probabilidade x Impacto. Seguranca e sobre gerenciar riscos, nao elimina-los completamente.

### Exploit

Codigo ou tecnica que tira proveito de uma vulnerabilidade para causar um efeito nao intencional no sistema.

### Payload

A carga que o exploit entrega. E o que realmente causa o dano: roubar dados, abrir uma porta dos fundos, criptografar arquivos.

## A triade CIA (Confidencialidade, Integridade, Disponibilidade)

Toda analise de seguranca gira em torno desses tres pilares:

### Confidencialidade

A informacao so pode ser acessada por quem tem autorizacao. Violacao: alguem nao autorizado le dados sensiveis.

**Exemplos de ataque:** SQL Injection para extrair dados, vazamento de credenciais, interceptacao de trafego sem criptografia.

**Defesas:** criptografia em transito (TLS) e em repouso (AES), controle de acesso (RBAC), principio do menor privilegio.

### Integridade

A informacao nao pode ser alterada sem autorizacao. Violacao: alguem modifica dados, codigo ou configuracoes sem permissao.

**Exemplos de ataque:** injecao de SQL para alterar registros, man-in-the-middle para modificar dados em transito, defacement de site.

**Defesas:** hashing (SHA-256), assinaturas digitais, checksums, controle de versao, logs de auditoria.

### Disponibilidade

O sistema precisa estar acessivel quando necessario. Violacao: o sistema fica fora do ar ou inacessivel.

**Exemplos de ataque:** DDoS, ransomware que criptografa dados, destruicao de backups.

**Defesas:** redundancia, backups (regra 3-2-1), balanceamento de carga, plano de recuperacao de desastres.

## OWASP Top 10 (referencia para aplicacoes web)

As 10 vulnerabilidades mais criticas em aplicacoes web segundo a OWASP:

1. **Broken Access Control (A01):** usuarios acessam funcoes ou dados que nao deveriam.
2. **Cryptographic Failures (A02):** falhas na protecao de dados sensiveis (criptografia fraca ou ausente).
3. **Injection (A03):** dados nao confiaveis sao enviados a um interpretador como parte de um comando (SQL, OS, LDAP).
4. **Insecure Design (A04):** falhas de arquitetura e design que nenhum patch corrige.
5. **Security Misconfiguration (A05):** configuracoes padrao inseguras, servicos desnecessarios, permissoes excessivas.
6. **Vulnerable and Outdated Components (A06):** uso de bibliotecas, frameworks ou sistemas com vulnerabilidades conhecidas.
7. **Identification and Authentication Failures (A07):** falhas no login, sessoes, MFA.
8. **Software and Data Integrity Failures (A08):** atualizacoes sem verificacao, pipelines CI/CD inseguros.
9. **Security Logging and Monitoring Failures (A09):** falta de logs, monitoramento ou alertas.
10. **Server-Side Request Forgery - SSRF (A10):** o servidor e enganado para fazer requisicoes a destinos nao intencionais.

## MITRE ATT&CK (referencia para tecnicas de ataque)

O MITRE ATT&CK e uma base de conhecimento de taticas e tecnicas de adversarios observadas no mundo real. As taticas principais:

- **Reconnaissance:** coleta de informacoes sobre o alvo.
- **Initial Access:** como o atacante entra (phishing, exploits publicos).
- **Execution:** como o atacante roda codigo malicioso.
- **Persistence:** como o atacante mantem acesso.
- **Privilege Escalation:** como o atacante ganha mais permissoes.
- **Defense Evasion:** como o atacante evita deteccao.
- **Credential Access:** como o atacante rouba credenciais.
- **Lateral Movement:** como o atacante se move pela rede.
- **Collection:** como o atacante junta dados de interesse.
- **Exfiltration:** como o atacante tira dados do ambiente.
- **Impact:** o dano final (destruicao, ransomware, defacement).

## CWE (Common Weakness Enumeration)

As CWEs mais comuns que o agente encontra em codigo de estudantes:

- **CWE-89:** SQL Injection
- **CWE-79:** Cross-Site Scripting (XSS)
- **CWE-287:** Improper Authentication
- **CWE-862:** Missing Authorization
- **CWE-798:** Use of Hard-Coded Credentials
- **CWE-306:** Missing Authentication for Critical Function
- **CWE-502:** Deserialization of Untrusted Data
- **CWE-78:** OS Command Injection
- **CWE-22:** Path Traversal
- **CWE-352:** Cross-Site Request Forgery (CSRF)

## Boas praticas de seguranca no desenvolvimento

### Validacao de entrada
- Nunca confie em dados que vem do usuario.
- Valide tipo, tamanho, formato e faixa de valores.
- Use listas de permissao (allowlist), nao listas de bloqueio (blocklist).

### Consultas parametrizadas
- Nunca concatene entrada do usuario em queries SQL.
- Use prepared statements ou ORM.

### Autenticacao e sessoes
- Armazene senhas com hash forte (bcrypt, Argon2).
- Implemente MFA quando possivel.
- Use tokens de sessao aleatorios e seguros.
- Configure tempo de expiracao adequado.

### Principio do menor privilegio
- De apenas as permissoes necessarias para a funcao.
- Aplique em usuarios, servicos, APIs e bancos de dados.

### Defesa em profundidade
- Nao confie em uma unica camada de protecao.
- Combine firewall + WAF + validacao + autenticacao + logs + monitoramento.

### Seguranca no ciclo de desenvolvimento (DevSecOps)
- Integre revisao de seguranca no pipeline de desenvolvimento.
- Faca code review focado em seguranca.
- Use ferramentas de analise estatica (SAST) e dinamica (DAST).
- Mantenha dependencias atualizadas.
- Faca testes de penetracao periodicos.

## Resposta a incidentes

Quando uma vulnerabilidade e explorada, a resposta segue etapas:

1. **Identificacao:** detectar que algo aconteceu.
2. **Contencao:** limitar o dano (isolar o sistema).
3. **Erradicacao:** remover a causa (corrigir a vulnerabilidade).
4. **Recuperacao:** restaurar o sistema ao estado normal.
5. **Licoes aprendidas:** documentar e melhorar o processo.

## Etica e legalidade

- **Sempre teste em ambientes proprios ou com autorizacao explicita.**
- No Brasil, acessar sistemas sem autorizacao e crime (Lei 12.737/2012 - Lei Carolina Dieckmann).
- Teste de seguranca so e legal com contrato ou autorizacao por escrito.
- Divulgacao responsavel: ao encontrar uma vulnerabilidade em sistema de terceiro, reporte ao responsavel antes de publicar.
