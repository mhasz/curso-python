# PyPort - Ferramenta de Descoberta de Portas para Pentesters

O **PyPort** é uma ferramenta desenvolvida para auxiliar **pentesters** na descoberta de portas abertas em servidores ou serviços. Ela foi projetada para ser altamente eficiente, utilizando **multithreading** e técnicas como o **SYN Scan**, com foco em evitar detecção e acelerar o processo de escaneamento, comparado a ferramentas como o Nmap, apesar de ser escrita em **Python puro**.

## Funcionalidades

- **Scan TCP padrão**: Realiza testes básicos de portas via protocolo TCP, estabelecendo uma conexão completa com a porta alvo.
- **SYN Scan (Stealth Scan)**: Envia pacotes SYN sem completar o **three-way handshake**, permitindo identificar portas abertas com menor risco de detecção.
- **Modo rápido**: Foca nas **1.000 portas mais comuns**, baseado na lista oficial do Nmap, para um escaneamento otimizado.
- **Escaneamento completo**: Permite escanear todas as **65.535 portas** de um alvo, verificando tanto portas comuns quanto incomuns.

## Como Funciona

O **PyPort** utiliza threads para otimizar o processo de escaneamento, limitando o número de threads para evitar sobrecarga e garantir maior estabilidade durante o processo de descoberta de portas. Ele também otimiza a resolução de DNS, buscando o endereço IP diretamente antes de iniciar o escaneamento, o que evita atrasos causados por múltiplas resoluções DNS.

### Modos de Operação

1. **SYN Scan (Stealth Scan)**:
   - Evita completar o handshake TCP, sendo mais discreto e menos detectável por firewalls e sistemas de monitoramento.
   
2. **Scan TCP Padrão**:
   - Realiza um teste completo de conexão TCP, garantindo a verificação de portas abertas com precisão.

3. **Scan Rápido**:
   - Escaneia as **1.000 portas mais comuns** (baseado na lista do Nmap), permitindo uma descoberta rápida de serviços principais.

4. **Escaneamento Completo**:
   - Permite escanear **todas as 65.535 portas** de um alvo para garantir uma cobertura completa.


## Como Usar

O **PyPort** oferece dois tipos principais de escaneamento: o **SYN Scan** e o **Scan TCP Padrão**. Você também pode escolher entre escanear as **1.000 portas principais** ou **todas as portas** de um serviço.

### Sintaxe de Comando

```bash
python3 pyport.py [domínio ou IP] [tipo de scan=s/n] [-p- (opcional)]
```

- **[domínio ou IP]**: O domínio ou IP que você deseja escanear.
- **[tipo de scan=s/n]**: `s` para **SYN Scan**, `n` para **Scan TCP Padrão**.
- **-p-** (opcional): Realiza o escaneamento de **todas as 65.535 portas**. Se omitido, o PyPort escaneará apenas as 1.000 portas mais comuns.

### Exemplos de Uso

#### 1. Escanear as 1.000 portas mais comuns com SYN Scan:

```bash
python3 pyport.py exemplo.com s
```

#### 2. Escanear todas as 65.535 portas com TCP Scan:

```bash
python3 pyport.py 192.168.1.1 n -p-
```

#### 3. Escanear um domínio com TCP Scan, verificando apenas as 1.000 portas mais comuns:

```bash
python3 pyport.py exemplo.com n
```

### Saída

O PyPort retorna as portas abertas e os serviços associados, com base nas informações conhecidas:

```
PORTA           SERVIÇO
80/tcp          http
443/tcp         https
22/tcp          ssh
```

## Limitações

- **Multithreading**: Embora o uso de threads otimize o escaneamento, o número de threads é limitado para evitar sobrecarga e problemas de estabilidade.
- **Resolução de DNS**: O PyPort resolve o endereço IP do alvo apenas uma vez, evitando múltiplas consultas DNS, o que melhora a velocidade em testes com domínios.
- **Sem suporte a UDP**: O PyPort, no momento, é limitado a escaneamentos TCP e não oferece suporte para testes de portas UDP.

## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** O **PyPort** é uma ferramenta educacional e deve ser usada de forma ética e responsável, com autorização prévia em testes de penetração. O uso não autorizado pode violar leis de privacidade e segurança de redes.
