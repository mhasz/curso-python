# PyDirb - Ferramenta de Descoberta de Diretórios e Arquivos

O **PyDirb** é uma ferramenta simples e eficaz desenvolvida para realizar a **descoberta de diretórios e arquivos** em servidores web. Ele é projetado para ajudar **pentesters** a identificar diretórios ocultos e arquivos acessíveis, além de fornecer o **status code** das páginas encontradas, facilitando a análise da superfície de ataque de uma aplicação web.

## Funcionalidades

- **Descoberta de Diretórios e Arquivos**: Utiliza uma wordlist para identificar diretórios e arquivos que estão acessíveis no servidor.
- **Detecção de "Index Of"**: Verifica se o diretório listado permite a navegação direta através do recurso "Index Of".
- **Status Code**: Retorna o código de status HTTP para cada URL verificada, indicando se o acesso foi permitido (200), redirecionado (301/302) ou proibido (403).
- **Multithreading**: Usa **multithreading** para aumentar o desempenho da busca, limitando o número de threads a 3 para evitar sobrecarga no servidor ou problemas de desempenho no próprio script.

## Como Funciona

O PyDirb envia requisições HTTP **HEAD** e **GET** para URLs formadas a partir de um domínio e uma **wordlist** de possíveis diretórios ou arquivos. Ele verifica:

- **Códigos de status** das respostas (200, 301, 302, 403, etc.).
- Se o diretório tem um **índice de listagem ("Index Of")**, o que pode indicar diretórios abertos ao público.

A ferramenta utiliza **semaforos** para limitar o número de threads concorrentes a 3, o que melhora o desempenho sem sobrecarregar o servidor nem o próprio sistema de descoberta. Um número maior de threads poderia causar instabilidade ou tornar o processo mais lento.

## Como Usar

### 1. Execução Básica

Para executar o PyDirb, forneça um domínio e uma wordlist contendo os possíveis diretórios ou arquivos que você deseja testar:

```bash
python3 pydirb.py [domínio] [wordlist]
```

- **[domínio]**: O domínio ou IP do servidor web que você deseja escanear.
- **[wordlist]**: Um arquivo de texto com uma lista de possíveis diretórios ou arquivos.

### Exemplo:

```bash
python3 pydirb.py http://exemplo.com /caminho/para/wordlist.txt
```

### Saída:

O PyDirb vai listar os diretórios e arquivos encontrados, além de retornar o **status code** de cada URL verificada. Diretórios com o recurso **"Index Of"** ativado serão destacados, pois isso pode indicar uma possível vulnerabilidade.

Exemplo de saída:

```
http://exemplo.com/admin - CODE:403
http://exemplo.com/uploads - CODE:200
+ DIRETORIO http://exemplo.com/files/
  └ INDEX OF
```

### 2. Multithreading

Por padrão, o PyDirb usa 3 threads para processar as requisições de maneira mais eficiente. Esse número é fixo para evitar que o script se torne instável ou cause sobrecarga no servidor alvo.

## Limitações

- **Número de Threads**: O PyDirb é limitado a 3 threads por vez, controladas por semáforos. Aumentar esse número pode resultar em instabilidade e diminuir o desempenho da ferramenta.
- **Desempenho em Grandes Wordlists**: Em grandes wordlists, o desempenho pode ser afetado devido à quantidade de requisições HTTP. Recomenda-se o uso de wordlists otimizadas e com entradas específicas para evitar um número excessivo de requisições desnecessárias.


## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** O **PyDirb** é uma ferramenta educacional e deve ser usada com autorização prévia em testes de penetração. O uso não autorizado pode violar leis de privacidade e segurança de redes. Utilize esta ferramenta de forma ética e responsável.
