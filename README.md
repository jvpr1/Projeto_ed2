# Heap: Min Heap, Max Heap e Heap Sort

## Introdução

Este repositório foi desenvolvido como material de apoio para o seminário da disciplina **Estruturas de Dados II**, abordando a estrutura de dados Heap, seus fundamentos teóricos, operações principais, análise de complexidade e aplicações práticas em algoritmos de ordenação e filas de prioridade.

---

## Conceitos Fundamentais

### O que é uma Heap?

Heap é uma estrutura de dados baseada em uma árvore binária completa que segue uma propriedade de ordenação específica entre os nós pais e seus filhos.

Uma árvore binária completa é aquela em que todos os níveis são preenchidos da esquerda para a direita, exceto possivelmente o último nível.

A principal característica da estrutura é a **Propriedade Heap**, que garante uma relação de prioridade entre os elementos.

### Tipos de Heap

#### Max Heap

Em uma Max Heap, o valor armazenado em cada nó pai é sempre maior ou igual ao valor de seus filhos.

```text
        90
       /  \
      70   60
     / \   / \
    40 50 20 10
```

O maior elemento da estrutura permanece na raiz.

#### Min Heap

Em uma Min Heap, o valor armazenado em cada nó pai é sempre menor ou igual ao valor de seus filhos.

```text
        10
       /  \
      20   30
     / \   / \
    40 50 60 70
```

O menor elemento da estrutura permanece na raiz.

---

## Características

- Estrutura baseada em árvore binária completa;
- Inserção eficiente;
- Remoção eficiente;
- Acesso imediato ao elemento de maior ou menor prioridade;
- Implementação frequentemente realizada por meio de vetores;
- Amplamente utilizada em filas de prioridade e algoritmos de ordenação.

---

## Representação em Vetor

Apesar de ser conceitualmente uma árvore, a Heap normalmente é armazenada em um vetor, eliminando a necessidade de ponteiros entre os nós.

Exemplo:

```text
        50
       /  \
      30   40
     / \   /
    10 20 35
```

Representação em vetor:

```python
heap = [50, 30, 40, 10, 20, 35]
```

Relações entre índices:

```python
pai = (i - 1) // 2
filho_esquerdo = 2 * i + 1
filho_direito = 2 * i + 2
```

---

## Operações Fundamentais

### Inserção

A inserção consiste em adicionar um novo elemento ao final da estrutura e restaurar a propriedade Heap através do processo denominado **Up-Heapify**.

Etapas:

1. Inserir o elemento no final do vetor.
2. Comparar o elemento com seu pai.
3. Realizar trocas quando necessário.
4. Repetir até que a propriedade Heap seja restaurada.

### Remoção

A remoção ocorre sempre sobre o elemento da raiz.

Etapas:

1. Remover a raiz.
2. Mover o último elemento para a raiz.
3. Aplicar o processo **Down-Heapify**.
4. Restaurar a propriedade Heap.

---

## Heapify

Heapify é o processo responsável por construir ou restaurar uma Heap válida.

### Up-Heapify

Utilizado após inserções.

```text
Inserir elemento
      ↓
Comparar com o pai
      ↓
Trocar se necessário
      ↓
Repetir até a posição correta
```

### Down-Heapify

Utilizado após remoções.

```text
Mover último elemento para a raiz
                ↓
Comparar com os filhos
                ↓
Trocar se necessário
                ↓
Repetir até restaurar a Heap
```

---

## Complexidade das Operações

| Operação | Complexidade |
|-----------|-------------|
| Inserção | O(log n) |
| Remoção da raiz | O(log n) |
| Acesso ao maior/menor elemento | O(1) |
| Busca de elemento específico | O(n) |
| Construção da Heap | O(n) |
| Heap Sort | O(n log n) |

---

## Heap Sort

Heap Sort é um algoritmo de ordenação baseado na estrutura Heap.

Seu funcionamento pode ser dividido em duas etapas principais:

1. Construção de uma Max Heap a partir dos elementos do vetor.
2. Troca sucessiva da raiz pelo último elemento da estrutura, seguida da aplicação de Heapify para restaurar a propriedade Heap.

### Complexidade

| Caso | Complexidade |
|--------|------------|
| Melhor caso | O(n log n) |
| Caso médio | O(n log n) |
| Pior caso | O(n log n) |

### Vantagens

- Desempenho previsível em todos os cenários;
- Não requer memória auxiliar significativa;
- Adequado para grandes volumes de dados.

### Desvantagens

- Implementação mais complexa quando comparada a algoritmos simples de ordenação;
- Não é estável por padrão.

---

## Aplicações

A estrutura Heap é utilizada em diversas áreas da computação:

- Filas de prioridade;
- Escalonamento de processos em sistemas operacionais;
- Algoritmo de Dijkstra;
- Sistemas de recomendação e inteligência artificial;
- Bancos de dados;
- Jogos e sistemas de ranking;
- Redes de computadores;
- Algoritmos de ordenação.

---

## Referências Bibliográficas

- CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.; STEIN, Clifford. *Algoritmos: Teoria e Prática*. 3. ed. Rio de Janeiro: Elsevier, 2012.
- GOODRICH, Michael T.; TAMASSIA, Roberto. *Estruturas de Dados e Algoritmos em Java*. Porto Alegre: Bookman, 2013.
- ZIVIANI, Nivio. *Projeto de Algoritmos com Implementações em Java e C++*. São Paulo: Cengage Learning, 2011.
- LEITE, Thiago et al. *Estruturas de Dados: Domine as práticas essenciais em C, Java, C#, Python e JavaScript*. Casa do Código, 2023.
