# RAT Educacional - Trojan de Acesso Remoto

Este repositório contém um exemplo prático de um **RAT (Remote Access Trojan)**, projetado **estritamente para fins educacionais**. O objetivo é ajudar iniciantes em **cybersecurity** a compreenderem como funcionam os trojans de acesso remoto, como eles são desenvolvidos e as técnicas comuns utilizadas para controle remoto de sistemas. **Este código não deve ser usado para fins maliciosos**.

## Ferramentas Incluídas

- **server.py**: Atua como o servidor controlador do RAT. Ele é responsável por se comunicar com o cliente (máquina infectada), executar comandos remotamente e receber dados.
  
- **rat.py**: O cliente que é executado na máquina-alvo. Este script permite a execução remota de comandos, transferência de arquivos, captura de tela, uso da webcam e monitoramento de teclado (keylogger).

### Aviso Legal

Este projeto foi criado apenas para fins educacionais e de pesquisa. O uso deste código em sistemas sem a devida permissão é **ilegal**. Certifique-se de usá-lo apenas em ambientes de teste controlados, com total permissão dos proprietários dos sistemas.

## Funcionalidades

### rat.py (Cliente)

- **Execução de Comandos Remotos**: Permite a execução de comandos diretamente no sistema operacional da máquina-alvo através de um shell interativo.
- **Download de Arquivos**: O cliente pode enviar arquivos da máquina infectada para o servidor de controle.
- **Upload de Arquivos**: O servidor pode enviar arquivos para a máquina infectada.
- **Captura de Tela**: O cliente pode tirar screenshots da máquina infectada e enviar ao servidor.
- **Acesso à Webcam**: Captura uma imagem da webcam (caso exista) e envia ao servidor.
- **Keylogger**: Registra as teclas pressionadas em tempo real e as envia ao servidor.
- **Persistência**: Configura o RAT para ser executado automaticamente após a reinicialização do sistema operacional.
- **Criptografia**: Todas as comunicações entre o servidor e o cliente são encriptadas usando **Fernet (AES)**, garantindo que dados sensíveis não sejam facilmente detectados por sistemas de detecção de intrusão.

### server.py (Servidor)

- **Controle Remoto**: Permite o envio de comandos e o controle completo da máquina infectada.
- **Gerenciamento de Arquivos**: Recebe e envia arquivos para a máquina infectada.
- **Captura de Dados**: Armazena as teclas pressionadas pelo keylogger em um arquivo de log.
- **Execução de Tarefas**: Envia comandos para iniciar captura de tela, capturar imagens da webcam e muito mais.
- **Criptografia de Comunicação**: Todos os dados enviados entre o servidor e o cliente são criptografados.

## Como Funciona

### 1. Execução do Servidor (Controlador)

O **server.py** é a interface de controle que se conecta à máquina infectada. Para iniciar o servidor, execute o comando:

```bash
python3 server.py [porta]
```

- **[porta]**: A porta que o servidor usará para escutar conexões do cliente.

#### Exemplo:

```bash
python3 server.py 8080
```

### 2. Execução do Cliente (RAT)

O **rat.py** deve ser executado na máquina-alvo (ou máquina de teste). Ele se conecta ao servidor e aguarda comandos para executar remotamente.

Após a execução, o cliente tentará conectar-se ao servidor, utilizando o IP e a porta fornecidos.

## Comandos Disponíveis no Servidor

Depois de estabelecer uma conexão com o cliente, o servidor permite executar diversos comandos:

- **start keylogger**: Inicia o keylogger, que captura e envia as teclas pressionadas.
- **stop keylogger**: Para o keylogger.
- **download [nome do arquivo]**: Baixa um arquivo da máquina infectada.
- **upload [caminho do arquivo]**: Envia um arquivo do servidor para a máquina infectada.
- **screenshot**: Captura uma screenshot da máquina infectada.
- **webcam**: Captura uma imagem da webcam (se disponível).
- **exit**: Encerra a conexão com o cliente.

Para ver todos os comandos disponíveis, utilize o comando **help** no servidor.

### Exemplo de Uso

No servidor:

```bash
python3 server.py 8080
```

No cliente:

```bash
python3 rat.py
```

Comandos no servidor:

```bash
Comando > start keylogger
Comando > screenshot
Comando > download /path/to/file
Comando > whoami
Comando > webcam
Comando > exit
```

## Segurança e Criptografia

Toda comunicação entre o **server.py** e o **rat.py** é criptografada usando **Fernet (AES)**, garantindo que os dados trafegados pela rede (como comandos, capturas de tela, keylogger, etc.) sejam protegidos contra inspeção por sistemas de detecção de intrusão (IDS).

## Requisitos

Para rodar o servidor e o cliente, você precisará das seguintes bibliotecas:

- **Cryptography** (para criptografia de dados)
- **Socket** (para comunicação entre cliente/servidor)
- **Pillow** (para captura de tela)
- **OpenCV** (para captura de imagens da webcam)
- **Keyboard** (para o keylogger)

Instale as dependências com o comando:

```bash
pip install cryptography pillow opencv-python keyboard
```


## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** Este projeto é apenas para fins educacionais e deve ser utilizado em ambientes de teste. O uso não autorizado deste código em sistemas de terceiros é ilegal e pode violar leis de privacidade e segurança.
