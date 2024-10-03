# Ransomware Educacional - Ferramentas de Encriptação e Decriptação

Este repositório contém duas ferramentas criadas **estritamente para fins educacionais**: um **ransomware** e um **decriptor**. O objetivo dessas ferramentas é ajudar iniciantes na área de **cybersecurity** a entender como funciona o código de ransomware, como esses códigos maliciosos podem ser escritos, e os métodos comuns usados para encriptação e decriptação de arquivos. As ferramentas não devem ser usadas para fins maliciosos e servem apenas como um exemplo prático.

## Ferramentas Incluídas

- **ransomware.py**: Um exemplo educacional de um código ransomware capaz de:
  - Listar arquivos em um sistema Windows.
  - Verificar os tipos de arquivo de forma sofisticada utilizando **MIME types** ao invés de apenas extensões de arquivo.
  - Encriptar arquivos específicos baseados em um filtro de MIME type.
  - Alterar o **background** do sistema operacional após a encriptação.
  - Utilizar **multithreading** para acelerar o processo de encriptação.

- **decriptor.py**: Um script que faz a decriptação dos arquivos encriptados pelo ransomware, revertendo o processo de forma segura.

### Aviso Legal

Este projeto foi criado apenas para fins educacionais e de pesquisa em **cybersecurity**. O uso deste código em sistemas sem a devida permissão é **ilegal**. Certifique-se de usá-lo somente em ambientes de teste controlados.

## ransomware.py - Encriptação de Arquivos

O **ransomware.py** é um exemplo básico de ransomware que percorre o sistema, identificando arquivos específicos com base no tipo MIME, e os encripta utilizando a biblioteca **Fernet** do **Cryptography**.

### Funcionalidades

- **Listagem de Arquivos**: O ransomware percorre o sistema de arquivos (em `/users/` no Windows) e verifica os arquivos com base no **MIME type**.
- **Encriptação**: Arquivos de tipos específicos (como documentos do Word, imagens e vídeos) são encriptados.
- **Multithreading**: A ferramenta utiliza múltiplas threads para acelerar o processo de encriptação.
- **Alteração do Background**: Após a encriptação, a ferramenta altera o background da área de trabalho do Windows para uma imagem pré-definida.

### Como Usar

Para executar o **ransomware.py**, siga o comando abaixo (somente em ambiente de teste controlado!):

```bash
python3 ransomware.py
```

O ransomware irá:

1. Listar e verificar os tipos de arquivos usando **MIME types**.
2. Encriptar arquivos encontrados com base na **whitelist** de tipos MIME:
    - Documentos do Word (`.docx`, `.doc`)
    - Imagens (`.jpeg`, `.png`)
    - Vídeos (`.mp4`)
    - PDFs (`.pdf`)
3. Alterar o **background** do sistema após a encriptação.
4. Imprimir a chave gerada que pode ser usada posteriormente para decriptação.

#### Exemplo de Arquivo Criptografado

Os arquivos encriptados terão a extensão `.enc`, e o conteúdo será inacessível sem a chave de decriptação.

## decriptor.py - Decriptação de Arquivos

O **decriptor.py** é a ferramenta que reverte o processo de encriptação realizado pelo ransomware, restaurando os arquivos encriptados de volta ao estado original.

### Funcionalidades

- **Decriptação de Arquivos**: Percorre o sistema em busca de arquivos encriptados (`.enc`), usando a chave de encriptação gerada pelo ransomware.
- **Multithreading**: Assim como o ransomware, o decriptor também utiliza múltiplas threads para acelerar o processo de decriptação.

### Como Usar

Para decriptar os arquivos, utilize o **decriptor.py** com a chave de encriptação usada no ransomware:

```bash
python3 decriptor.py
```

O script percorrerá os diretórios do sistema, procurando por arquivos com a extensão `.enc`, e os restaurará aos seus formatos originais.

### Configuração da Chave

No código de exemplo, a chave está embutida diretamente no script como uma string codificada em base64. A chave deve ser a mesma que foi gerada pelo **ransomware.py** para que os arquivos possam ser decriptados corretamente.

#### Exemplo de Decriptação

Após a execução, os arquivos anteriormente encriptados terão suas extensões restauradas, e os dados estarão acessíveis novamente.

## Requisitos

Para rodar o **ransomware** e o **decriptor**, você precisará das seguintes bibliotecas:

- **Cryptography**
- **Python-Magic** (para verificação de MIME types)
- **ctypes** (para modificar o background do Windows)

Instale as dependências com o comando:

```bash
pip install cryptography python-magic
```


## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** Este projeto é apenas para fins educacionais e deve ser utilizado em ambientes de teste. O uso não autorizado deste código em sistemas de terceiros é ilegal e pode violar leis de privacidade e segurança.
