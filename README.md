# 🐍 Exercícios de Python - Funções Básicas

Este repositório contém uma coleção de exercícios práticos em Python focados no desenvolvimento de funções básicas e interação com o usuário.

## 📋 Exercícios Incluídos

### 1. 🧾 Calculadora de Gorjeta
**Arquivo:** `calculadora_gorjeta.py`

Função que calcula a gorjeta a ser deixada em um restaurante baseada no valor total da conta e na porcentagem desejada.

**Funcionalidades:**
- Calcula o valor da gorjeta baseado no total da conta
- Aplica porcentagem personalizada
- Formatação em reais (R$)

**Exemplo de uso:**
```
Digite o valor total da conta: 100.00
Digite a porcentagem da gorjeta: 10
A gorjeta a ser deixada é: R$ 10.00
```

### 2. 🔄 Verificador de Palíndromo
**Arquivo:** `verificador_palindromo.py`

Função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente).

**Funcionalidades:**
- Remove espaços e pontuação
- Ignora diferenças entre maiúsculas e minúsculas
- Implementação manual de inversão de string
- Retorna resposta em português ("Sim" ou "Não")

**Exemplo de uso:**
```
Digite uma palavra ou frase: A man a plan a canal Panama
É um palíndromo? Sim
```

### 3. 💰 Calculadora de Desconto
**Arquivo:** `calculadora_desconto.py`

Programa que calcula o preço final de um produto após aplicar um desconto percentual.

**Funcionalidades:**
- Calcula valor do desconto
- Determina preço final
- Arredonda para 2 casas decimais
- Formatação em reais (R$)

**Exemplo de uso:**
```
Digite o preço original do produto: 150.00
Digite o percentual de desconto: 20
O preço final do produto é: R$ 120.00
```

### 4. 📅 Calculadora de Dias de Vida
**Arquivo:** `calculadora_dias_vida.py`

Programa que calcula quantos dias uma pessoa está viva baseado na data exata de nascimento.

**Funcionalidades:**
- Calcula dias de vida usando data de nascimento real
- Utiliza a biblioteca `datetime` para cálculos precisos
- Considera anos bissextos e variações mensais
- Formatação de data brasileira (DD/MM/AAAA)

**Exemplo de uso:**
```
Digite sua data de nascimento (DD/MM/AAAA): 15/03/1998
Você está vivo há 9661 dias.
```

**Versão alternativa:** Também disponível versão simplificada que usa aproximação de anos, meses e dias.

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/exercicios-python.git
   cd exercicios-python
   ```

2. **Execute qualquer exercício:**
   ```bash
   python calculadora_gorjeta.py
   python verificador_palindromo.py
   python calculadora_desconto.py
   python calculadora_dias_vida.py
   ```

**Nota:** O exercício 4 possui duas versões:
- Versão com `datetime` (mais precisa, usa data exata)
- Versão simplificada (aproximação com anos/meses/dias)

## 📚 Conceitos Abordados

- **Funções:** Definição, parâmetros e valores de retorno
- **Entrada do usuário:** `input()` e conversões de tipo
- **Formatação de strings:** f-strings e formatação de números
- **Manipulação de strings:** Remoção de espaços, conversão de caso
- **Estruturas condicionais:** `if/else`
- **Operações matemáticas:** Cálculos percentuais e arredondamento
- **Loops:** Implementação manual de algoritmos
- **Biblioteca datetime:** Manipulação e cálculos com datas
- **Formatação de datas:** Parsing de strings para objetos datetime

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca datetime** (nativa do Python)
- Demais funcionalidades usam apenas bibliotecas nativas

## 📝 Observações

- Todos os programas incluem interação com o usuário via terminal
- Os valores monetários são formatados em Real (R$)
- O verificador de palíndromo implementa inversão de string de forma manual para fins educativos
- A calculadora de dias de vida possui duas versões: uma com cálculos precisos usando `datetime` e outra com aproximações simples

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias, correções ou novos exercícios!

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ Se este repositório foi útil para você, não esqueça de dar uma estrela!
