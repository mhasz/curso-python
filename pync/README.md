# PyNC - Ferramenta para Conexões TCP/UDP

O **PyNC** é uma ferramenta educacional desenvolvida para demonstrar na prática como funcionam as ferramentas de rede como o **NetCat**. Ele permite iniciar **servidores** e **clientes** TCP e UDP, além de estabelecer conexões com servidores. A ferramenta foi criada com o objetivo de ser simples, sem o uso de threads, o que gera algumas limitações no envio e recebimento simultâneo de pacotes.

## Funcionalidades

- **Servidor TCP**: Inicia um servidor TCP que aguarda conexões na porta especificada.
- **Servidor UDP**: Inicia um servidor UDP que aguarda mensagens de clientes.
- **Cliente TCP**: Conecta a um servidor TCP e permite o envio de mensagens.
- **Cliente UDP**: Conecta a um servidor UDP e permite o envio de mensagens.

### Limitações

Uma das limitações do **PyNC** é a ausência de threads, o que significa que ele não lida bem com múltiplas conexões simultâneas. Isso afeta o desempenho ao tentar enviar e receber pacotes ao mesmo tempo, especialmente em protocolos como o TCP, que exigem um fluxo contínuo de comunicação.

## Como Funciona

O **PyNC** permite tanto o funcionamento como **servidor** quanto como **cliente**, suportando os protocolos **TCP** e **UDP**. Ele é útil para aprender como o NetCat e ferramentas semelhantes operam, servindo de base para a criação de ferramentas de rede personalizadas.

### 1. Servidor

- **TCP**: Inicia um servidor TCP que aguarda conexões de clientes. Após uma conexão, o servidor solicita uma senha e, se correta, a comunicação pode continuar.
- **UDP**: Inicia um servidor UDP que recebe mensagens de clientes e envia respostas de volta.

### 2. Cliente

- **TCP**: Conecta-se a um servidor TCP e envia/recebe mensagens de forma interativa.
- **UDP**: Conecta-se a um servidor UDP e envia/recebe pacotes de dados de forma contínua.

## Como Usar

O **PyNC** pode ser utilizado tanto como **servidor** quanto como **cliente**. Aqui estão os comandos básicos para cada caso:

### 1. Modo Servidor

Para iniciar um servidor TCP ou UDP, use a seguinte sintaxe:

```bash
python3 ncpy.py -s [tcp/udp] [porta]
```

- **[tcp/udp]**: Escolha entre TCP ou UDP para o servidor.
- **[porta]**: A porta que o servidor irá escutar.

#### Exemplo de uso como servidor TCP:

```bash
python3 ncpy.py -s tcp 4444
```

Isso irá iniciar um servidor TCP na porta **4444**.

#### Exemplo de uso como servidor UDP:

```bash
python3 ncpy.py -s udp 4444
```

Isso irá iniciar um servidor UDP na porta **4444**.

### 2. Modo Cliente

Para conectar a um servidor TCP ou UDP, use a seguinte sintaxe:

```bash
python3 ncpy.py -c [tcp/udp] [ip] [porta]
```

- **[tcp/udp]**: Escolha entre TCP ou UDP para a conexão.
- **[ip]**: O endereço IP do servidor ao qual deseja se conectar.
- **[porta]**: A porta na qual o servidor está escutando.

#### Exemplo de uso como cliente TCP:

```bash
python3 ncpy.py -c tcp 127.0.0.1 4444
```

Isso conecta a um servidor TCP no **localhost** (127.0.0.1) na porta **4444**.

#### Exemplo de uso como cliente UDP:

```bash
python3 ncpy.py -c udp 127.0.0.1 4444
```

Isso conecta a um servidor UDP no **localhost** (127.0.0.1) na porta **4444**.

## Limitações e Avisos

- **Sem Threads**: O PyNC não utiliza threads, o que significa que o envio e recebimento de pacotes pode não ocorrer simultaneamente. Essa característica limita o desempenho da ferramenta em comparações com outras ferramentas de rede mais avançadas, como o NetCat.
- **Senha Fixa no Servidor TCP**: No servidor TCP, a senha esperada para autenticação é fixa (`senhafoda123`), o que deve ser alterado caso deseje usar o script em situações diferentes.


## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.
