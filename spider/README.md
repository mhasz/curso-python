# Spider - Rastreador de Links e Informações de Contato em Sites

O **Spider** é uma ferramenta desenvolvida para acessar sites e identificar **links** de forma recursiva, varrendo toda a estrutura pública de um site. Além disso, o **Spider** é capaz de detectar **emails** e **números de telefone** utilizando **expressões regulares**. Para melhorar a eficiência, a ferramenta utiliza **multithreading**, mas limita o número de threads a 3, já que o aumento desse valor pode causar instabilidade no script, dada a natureza de ferramentas web.

## Funcionalidades

- **Varrimento de Sites**: Rastreamento recursivo de todas as páginas e links públicos de um domínio.
- **Identificação de Emails**: O Spider busca por padrões de emails usando expressões regulares e exibe todos os emails encontrados ao longo do rastreamento.
- **Identificação de Telefones**: O Spider também busca por padrões de números de telefone, exibindo os números encontrados.
- **Multithreading Controlado**: Utiliza 3 threads simultâneas para melhorar a eficiência do rastreamento, evitando sobrecarga no servidor ou instabilidade no script.

### Expressões Regulares Utilizadas

- **Email**: O script utiliza a seguinte expressão regular para capturar emails: `r"[a-z0-9_-]+@[a-z0-9_-]+\.[a-z\.]+"`
- **Telefone**: A expressão regular para capturar números de telefone é: `r"\+?\d{0,2}\s?\(\d{2}\)\s?\d{4,5}\s?-?\d{4}"`

### Aviso Legal

Este projeto foi desenvolvido para fins **educacionais** e **de pesquisa**. O uso desta ferramenta em sites sem a devida autorização pode ser **ilegal**. Certifique-se de utilizá-la apenas em sites onde você tenha permissão para realizar esse tipo de teste.

## Como Funciona

O **Spider** acessa o site fornecido e começa a identificar **links** em páginas HTML, formulários e iframes, além de verificar o conteúdo HTML em busca de emails e telefones. Toda essa análise é feita de forma recursiva, e o script mantém uma lista dos links que já foram visitados para evitar loops e repetições.

### Execução Básica

Para executar o **Spider**, basta fornecer a URL do site que deseja varrer. Certifique-se de que o endereço começa com `http://` ou `https://`.

```bash
python3 spider.py [URL]
```

- **[URL]**: A URL do site que será rastreado. Exemplo: `https://exemplo.com`

### Exemplo de Uso

```bash
python3 spider.py https://meusite.com
```

Durante a execução, o **Spider** começará a varrer a estrutura pública do site e exibirá os emails e números de telefone encontrados diretamente no terminal, além de visitar todos os links públicos do site.

### Limitação de Threads

Para evitar sobrecarga no site alvo e garantir a estabilidade do script, o número de threads é limitado a 3. O uso de um número maior de threads pode causar instabilidade tanto no servidor quanto na própria execução do script.

## Estrutura de Saída

Durante a execução, a ferramenta irá exibir:

- **Emails**: Todos os emails detectados ao longo do rastreamento.
- **Telefones**: Todos os números de telefone capturados em páginas, formulários e iframes.

### Exemplo de Saída

```
john.doe@example.com
contact@empresa.com
+55 (11) 99999-8888
+44 (20) 1234-5678
```

## Requisitos

Para utilizar o **Spider**, você precisará das seguintes bibliotecas:

- **Requests**: Para fazer requisições HTTP.
- **BeautifulSoup** (via `bs4`): Para análise do HTML.
  
Você pode instalar as dependências executando:

```bash
pip install requests beautifulsoup4
```

## Limitações

- **Recursividade Controlada**: O script varre os links de forma recursiva, mas pode haver limitações no caso de sites com redirecionamentos infinitos ou estruturas HTML extremamente complexas.
- **Multithreading Limitado**: O número de threads é limitado a 3 para garantir que a ferramenta funcione de maneira estável.

## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais informações.

---

**Atenção:** Esta ferramenta foi criada para fins educacionais. Utilize-a de forma ética e responsável, e somente em sites para os quais você tenha permissão de varrimento.
