# DNSScan - Ferramenta de Automação de Análises DNS para Pentesters

O **DNSScan** é uma ferramenta voltada para **pentesters** que visa automatizar uma série de análises que podem ser realizadas através de consultas DNS. A ferramenta foi projetada para ser uma aliada durante um processo de pentest, permitindo verificar informações de WHOIS, realizar ataques de força bruta para descoberta de subdomínios, e verificar possíveis vulnerabilidades de **subdomain takeover** por meio de registros **CNAME**.

## Funcionalidades

- **Consulta WHOIS**: Recupera informações WHOIS sobre o domínio-alvo.
- **Força Bruta de Subdomínios**: Usa uma wordlist para realizar força bruta em subdomínios e verifica se eles estão ativos (IPv4/IPv6).
- **Verificação de CNAME**: Realiza consultas de registro CNAME nos subdomínios descobertos, verificando se algum deles está apontando para serviços que possam ser vulneráveis a **subdomain takeover**.

## Como Funciona

O **DNSScan** possui três principais funcionalidades:

1. **Verificação WHOIS**:
   - Conecta-se aos servidores WHOIS para obter informações detalhadas sobre o domínio-alvo.
   - Salva o resultado da consulta WHOIS em um arquivo para análise posterior.

2. **Brute Force de Subdomínios**:
   - Utiliza uma wordlist de subdomínios comuns para realizar consultas DNS e identificar subdomínios válidos.
   - Suporta consultas tanto para **IPv4** quanto **IPv6**.
   - Os subdomínios identificados são armazenados em um arquivo JSON.

3. **Verificação de CNAME**:
   - Realiza consultas de CNAME em subdomínios para identificar possíveis vulnerabilidades de **subdomain takeover**.
   - Salva os resultados em um arquivo JSON para futura referência.


## Como Usar

Existem dois modos principais de operação: **execução direta** e **menu interativo**.

### 1. Execução Direta

Para realizar um scan completo em um domínio, incluindo **WHOIS**, **força bruta de subdomínios** e **verificação de CNAME**, execute o seguinte comando:

```bash
python3 dnsscan.py [domínio] [wordlist]
```

Exemplo:

```bash
python3 dnsscan.py exemplo.com wordlist.txt
```

### 2. Menu Interativo

Após realizar um ou mais scans, você pode visualizar os resultados usando o menu interativo:

```bash
python3 dnsscan.py menu
```

No menu interativo, você poderá visualizar informações detalhadas como:

- Subdomínios encontrados (IPv4 e IPv6).
- Registros CNAME.
- Informações WHOIS.

### Exemplo de Saída

Após rodar o script com um domínio e uma wordlist, a saída no terminal mostrará as descobertas, e os resultados serão salvos em arquivos para análise posterior. Os arquivos gerados estarão na pasta `scans/[dominio]`:

- WHOIS: `scans/[dominio]/[dominio].whois`
- Subdomínios: `scans/[dominio]/[dominio]-subdomains.json`
- CNAME: `scans/[dominio]/[dominio]-cname.json`

## Estrutura dos Arquivos

- **dnsclass.py**: Contém as classes principais para realizar consultas WHOIS, força bruta de subdomínios e verificação de CNAME.
- **dnsmenu.py**: Implementa o menu interativo para visualização dos resultados dos scans.
- **dnsscan.py**: Script principal que integra as funcionalidades e oferece a interface de linha de comando.


## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** O **DNSScan** é uma ferramenta educacional e deve ser usada apenas em ambientes autorizados. O uso não autorizado pode violar leis de privacidade e segurança de redes. Use esta ferramenta de forma ética e responsável.

