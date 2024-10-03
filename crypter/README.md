# Crypter - Bypass de Antivirus para Executáveis Python

O **Crypter** é uma ferramenta educacional desenvolvida para ensinar como um **crypter** pode funcionar, com foco em bypassar softwares antivírus. A ferramenta foi projetada especificamente para **executáveis Python** e implementa diversas técnicas de evasão para dificultar a análise de comportamento e evitar ambientes de execução controlados, como **Máquinas Virtuais (VMs)**. Além disso, a ferramenta realiza a **ofuscação de variáveis e funções**, tornando mais difícil a leitura e compreensão do código em caso de engenharia reversa.

## Como Funciona

O Crypter funciona basicamente codificando o executável alvo em **base64** e, em seguida, o decodifica no momento da execução. Algumas das principais técnicas utilizadas incluem:

- **Detecção de ambiente de execução**: O Crypter verifica a quantidade de núcleos de CPU e a memória RAM disponível para evitar ser executado em **Máquinas Virtuais** ou sandboxes de análise.
- **Ofuscação de código**: As variáveis e funções do código são renomeadas aleatoriamente durante o processo, dificultando a leitura do código em caso de engenharia reversa.
- **Técnicas de confusão**: Inclui várias rotinas de código inúteis e laços sem propósito que servem para confundir ferramentas de análise automatizada.
- **Execução do código ofuscado**: O Crypter escreve o código na máquina local e o executa diretamente. Apesar de ser uma técnica básica, essa abordagem é eficiente para **executáveis Python**.

## Estrutura do Código

O código é dividido em dois arquivos principais:

- **cripter.py**: Este script principal realiza a ofuscação e a codificação do código original. Ele também cuida da criação de um executável final, utilizando o **PyInstaller**.
- **raw_code.py**: O código-base que será modificado e inserido no executável final. Ele inclui a lógica de verificação de CPU e memória, além da decodificação do código ofuscado.

### Exemplo de Ofuscação

O Crypter altera automaticamente os nomes das variáveis e funções para sequências aleatórias, tornando mais difícil entender o comportamento do código. Por exemplo:

```python
<fcpu> = <psutil>.cpu_count(logical=False)
<lcpu> = <psutil>.cpu_count(logical=True)
<cpu> = <fcpu> + <lcpu>
```

Os nomes de variáveis como `<fcpu>`, `<lcpu>`, e `<cpu>` são gerados aleatoriamente em cada execução, garantindo que o código seja diferente a cada vez que o Crypter for utilizado.


## Como Usar

1. Primeiro, forneça o arquivo Python que deseja ofuscar para o Crypter:

   ```bash
   python3 cripter.py seu_executavel.py
   ```

2. O Crypter irá gerar um novo executável com o nome `codigo.exe`. Esse executável será ofuscado e preparado para execução com as técnicas descritas.

3. Para rodar o executável, simplesmente execute o arquivo gerado:

   ```bash
   ./codigo.exe
   ```

## Limitações

- **Técnica de execução**: Embora o Crypter escreva o código na máquina local antes de executá-lo, o que é um método menos sofisticado, essa abordagem é mais eficiente para executáveis Python. Técnicas mais avançadas, como **injeção de código em memória**, são mais complexas de implementar com Python.
- **Bypass de antivirus**: Embora o Crypter utilize técnicas para evitar a detecção por antivírus, ele não é infalível e não deve ser utilizado para fins maliciosos. O objetivo da ferramenta é educacional.


## Licença

Este projeto está licenciado sob a **GPLv3**. Consulte o arquivo [LICENSE](../LICENSE) para mais detalhes.

---

**Atenção:** Este projeto é estritamente educacional e deve ser utilizado apenas em ambientes de teste ou com a devida autorização. Não nos responsabilizamos pelo uso indevido deste código.
```

