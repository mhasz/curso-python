# PyroDump - Ferramenta de Captura e Ataque para Redes WPA

O **PyroDump** é um conjunto de duas ferramentas desenvolvidas para realizar testes de segurança em redes Wi-Fi, especialmente em redes WPA. As ferramentas foram projetadas para trabalhar em conjunto, permitindo tanto a **captura de pacotes** quanto a **injeção de pacotes de desautenticação**.

## Ferramentas Incluídas

- **pyrodump.py**: Ferramenta capaz de capturar pacotes Wi-Fi em modo monitor, identificar redes próximas, extrair informações como **BSSID**, **ESSID**, **canal** e **tipo de criptografia**. Além disso, identifica e captura pacotes **EAPOL** com o objetivo de realizar ataques de força bruta no handshake WPA, salvando as capturas em arquivos PCAP.
  
- **pyreplay.py**: Ferramenta que envia pacotes de **desautenticação** para forçar dispositivos conectados a redes Wi-Fi a se desconectarem, o que pode ser útil para forçar a geração de novos handshakes WPA.

### Aviso Legal

Essas ferramentas foram desenvolvidas **estritamente para uso educacional**. Utilizá-las sem a devida autorização é ilegal e pode violar leis de privacidade e segurança de redes. Use-as com responsabilidade e somente em redes para as quais você tenha autorização.

## pyrodump.py - Captura de Pacotes Wi-Fi

O **pyrodump.py** foi projetado para usar uma interface Wi-Fi em modo monitor e capturar pacotes **BEACON** e **EAPOL**, fornecendo informações sobre as redes próximas, como:

- **BSSID**: Endereço MAC da rede.
- **ESSID**: Nome da rede.
- **Canal**: Canal de comunicação utilizado pela rede.
- **Criptografia**: Tipo de segurança da rede (WPA, WPA2, WEP, ou rede aberta).
- **EAPOL**: Identifica e captura pacotes EAPOL para tentar obter o handshake WPA.

### Funcionalidades Principais

- Captura pacotes BEACON para identificar redes Wi-Fi próximas.
- Extrai detalhes sobre a rede, como BSSID, ESSID, canal, e tipo de criptografia.
- Detecta pacotes EAPOL para capturar o handshake WPA.
- Salva a captura em arquivos **PCAP**, que podem ser usados posteriormente para ataques de força bruta de handshakes WPA.

### Como Usar

Para usar o **pyrodump.py**, sua interface Wi-Fi deve estar configurada em **modo monitor**. O comando básico é o seguinte:

```bash
python3 pyrodump.py -i [interface] [-c canal] [-bssid bssid] [-w arquivo]
```

- **-i**: Define a interface de rede em modo monitor.
- **-c**: (Opcional) Define um canal específico para escanear.
- **--bssid**: (Opcional) Filtra os pacotes capturados por um BSSID específico.
- **-w**: (Opcional) Salva a captura em um arquivo PCAP para análise posterior.

#### Exemplo de uso:

Capturar todas as redes no canal 6 e salvar os resultados em um arquivo PCAP:

```bash
python3 pyrodump.py -i wlan0mon -c 6 -w captura.pcap
```

### Saída

Durante a execução, a ferramenta exibirá informações sobre as redes encontradas:

```
BSSID                   CANAL   CIFRA           ESSID
00:11:22:33:44:55       6       WPA2/RSN        MinhaRedeWiFi
66:77:88:99:AA:BB       11      WPA             OutraRede
```

Se o handshake for capturado, você verá a seguinte mensagem:

```
Handshake capturado
```

## pyreplay.py - Injeção de Pacotes de Desautenticação

O **pyreplay.py** é uma ferramenta que envia pacotes de **desautenticação** para uma rede Wi-Fi específica, o que força os dispositivos conectados a se desconectar. Isso é útil para forçar um novo handshake WPA, que pode ser capturado com o **pyrodump.py**.

### Como Usar

Para enviar pacotes de desautenticação, use o seguinte comando:

```bash
python3 pyreplay.py -a [BSSID] -i [interface] -c [número de pacotes]
```

- **-a**: BSSID do ponto de acesso (rede alvo).
- **-i**: Interface de rede em modo monitor.
- **-c**: Número de pacotes de desautenticação a serem enviados.

#### Exemplo de uso:

Enviar 10 pacotes de desautenticação para a rede com BSSID **00:11:22:33:44:55** usando a interface **wlan0**:

```bash
python3 pyreplay.py -a 00:11:22:33:44:55 -i wlan0mon -c 10
```

### Importante

Enviar pacotes de desautenticação sem autorização é **ilegal** em muitos países. Utilize essa ferramenta somente em redes para as quais você tenha permissão para testar.

## Requisitos

- **Python 3.x**
- **Pyshark** e **Scapy** (para captura e manipulação de pacotes):
  
  Instale as dependências necessárias com:

  ```bash
  pip install pyshark scapy
  ```

## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** Este projeto foi criado para fins educacionais e de pesquisa. O uso de ferramentas como o **PyroDump** sem autorização pode ser ilegal e violar leis de privacidade e segurança de redes. Certifique-se de ter permissão antes de realizar testes em qualquer rede.
