# AGENTS.md — aulas-programacao

Este arquivo orienta agentes de código (especialmente Codex) ao trabalhar neste repositório.

## 1. Objetivo do repositório

Este repositório reúne materiais de **Programação Aplicada** do Prof. Claudio Cesar Amado para o **3º A do curso Técnico em Informática para Internet do CEPEF — Centro de Educação Profissional Ezequiel Ferreira Lima**, em 2026.

O repositório deve funcionar como uma **central simples de acesso para os estudantes**, contendo páginas HTML de aula, roteiros de laboratório, códigos de apoio e arquivos `.py` quando necessário.

O objetivo não é apenas publicar código pronto. O material deve apoiar uma sequência pedagógica em que o estudante:

**problema → raciocínio → algoritmo → código → execução → teste → correção → explicação**.

---

## 2. Regra principal

Ao receber uma tarefa para criar ou atualizar uma aula:

1. **Leia primeiro este `AGENTS.md`.**
2. **Inspecione o `index.html` e os materiais recentes do repositório antes de editar.**
3. Preserve o padrão visual, estrutural e pedagógico já existente.
4. Não introduza conteúdo novo apenas para deixar a página mais completa.
5. Se o conteúdo previsto para a data não estiver claramente informado pelo professor ou pelos arquivos disponíveis, **pare e sinalize a falta de informação em vez de inventar**.
6. Não altere silenciosamente decisões pedagógicas já aprovadas.
7. Sempre trate o nível da turma como **Ensino Médio Técnico**, evitando tanto simplificação infantil quanto abstração excessiva.

---

## 3. Disciplina e turma

Contexto principal deste repositório:

- Escola: CEPEF — Centro de Educação Profissional Ezequiel Ferreira Lima
- Curso: Técnico em Informática para Internet
- Turma: 3º A
- Professor: Claudio Cesar Amado
- Disciplina: Programação Aplicada
- Linguagem principal: Python
- Ano: 2026

No 2º semestre, as aulas presenciais de Programação Aplicada do 3º A acontecem às quintas-feiras em dois tempos consecutivos:

- **1º tempo: 07:00–07:50**
- **2º tempo: 07:50–08:40**

Os dois tempos formam um bloco pedagógico de 100 minutos, mas quando o professor solicitar materiais separados, cada tempo deve ter **objetivo e entrega próprios**, preservando continuidade entre eles.

---

## 4. Projeto integrador do semestre

O projeto integrador é a **Central de Avisos**.

Objetivo geral: desenvolver progressivamente um sistema em Python para cadastrar, organizar, consultar e controlar avisos importantes, como provas, manutenções programadas, reuniões e alterações de horário.

O projeto deve crescer conforme os conteúdos forem ensinados. **Não antecipar recursos para completar o sistema.**

Exemplos de evolução curricular esperada:

- estruturas de dados já conhecidas → representação dos avisos;
- funções → organização das ações;
- `while` → menu contínuo;
- `for` → percorrer avisos;
- classes e objetos → somente quando esse conteúdo tiver sido formalmente introduzido;
- persistência/banco de dados → somente quando chegar a etapa prevista no planejamento.

---

## 5. Continuidade pedagógica obrigatória

Antes de produzir material novo, procure evidências no próprio repositório sobre o que já foi trabalhado.

Não considere um conteúdo como ensinado apenas porque ele faz parte da ementa geral.

Dê preferência ao histórico real do repositório, incluindo páginas como:

- `aula_07maio_slides.html`
- `aula_14maio_slides.html`
- `aula_21maio_slides.html`
- `aula_28maio_slides.html`
- `roteiro_lab_28maio.html`
- `aula_11junho_slides.html`
- `roteiro_lab_11junho.html`
- `aula_18junho_slides.html`
- `roteiro_lab_18junho.html`
- `aula_09julho_slides.html`
- `roteiro_lab_09julho.html`

Conteúdos já consolidados no histórico anterior incluem, em diferentes níveis:

- variáveis;
- entrada e saída;
- operadores;
- `if/else` e decisões;
- funções;
- parâmetros e retorno;
- listas;
- `append()`;
- `for`;
- dicionários;
- modularização básica;
- bibliotecas padrão já trabalhadas em aulas específicas.

No 3º bimestre de 2026, a Central de Avisos passa a integrar esses conhecimentos progressivamente.

---

## 6. Marcos atuais da Central de Avisos

Use estes marcos somente como referência de continuidade. Se o professor fornecer planejamento mais recente, ele prevalece.

### 13/08/2026

Revisão aplicada de conteúdos conhecidos e início da Central de Avisos com listas, dicionários, funções, `for` e decisões.

### 20/08/2026

Novo conteúdo principal: `while`.

Objetivo: compreender condição, repetição, atualização da variável de controle e uso de `while` para manter um menu funcionando.

Menu-base:

```python
opcao = ""

while opcao != "0":
    print("1 - Cadastrar aviso")
    print("2 - Listar avisos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastrar aviso")
    elif opcao == "2":
        print("Listar avisos")
    elif opcao == "0":
        print("Encerrando...")
    else:
        print("Opção inválida")
```

Evitar `while True` e `break` nessa etapa.

### 27/08/2026 — objetivo do bloco de 100 minutos

Concluir a **Central de Avisos v0.1** integrando apenas conteúdos já estudados:

```text
Central v0.1
├── lista de avisos
├── dicionários
├── funções
├── if/elif/else
├── for
├── while
└── menu
```

Funcionalidades mínimas:

1. Cadastrar aviso
2. Listar avisos
0. Sair

Entrega final esperada do bloco: uma primeira versão funcional que possa cadastrar vários avisos, listar os cadastrados, manter o menu com `while` e encerrar corretamente.

#### Divisão pedagógica aprovada para 27/08

**1º tempo — Cadastro funcionando**

Foco:

- `cadastrar_aviso()`;
- `input()`;
- criação de um dicionário para representar um aviso;
- `append()` para adicionar o aviso à lista;
- integração com a opção 1 do menu;
- execução e teste com pelo menos dois avisos.

O código inicial disponibilizado aos alunos **não deve trazer a solução completa**. O aluno deve construir a função durante a aula.

**2º tempo — Listagem e integração da v0.1**

Foco:

- `listar_avisos()`;
- `for` para percorrer a lista;
- acesso às chaves do dicionário;
- integração com a opção 2 do menu;
- teste do fluxo completo;
- correção de erros;
- conclusão da Central v0.1.

Não antecipar filtros, busca avançada, classes, persistência ou banco de dados.

---

## 7. Ambiente de execução dos estudantes

Ambiente padrão atual:

**Trinket — Python 3**

Link:

`https://trinket.io/python3`

O material deve favorecer execução simples no navegador, sem exigir instalação local.

Quando houver botão de execução externa, usar preferencialmente Trinket, a menos que o professor determine outro ambiente.

Evitar dependências que não funcionem naturalmente nesse ambiente.

Evitar transformar limpeza de terminal (`os.system`, ANSI etc.) em requisito pedagógico.

---

## 8. Padrão de materiais por aula

Quando viável, uma aula prática pode possuir:

```text
aula_<data>_<tempo>_slides.html
roteiro_lab_<data>_<tempo>.html
codigos_<data>_<tempo>.html
<arquivo_python_correspondente>.py
```

Exemplo para 27/08, 1º tempo:

```text
aula_27agosto_1tempo_slides.html
roteiro_lab_27agosto_1tempo.html
codigos_27agosto_1tempo.html
central_avisos_27agosto_1tempo_inicio.py
```

Não criar arquivos extras sem valor pedagógico claro.

---

## 9. Diferença entre cada tipo de arquivo

### `aula_*_slides.html`

Material de apresentação/condução da aula.

Deve:

- ter navegação simples;
- usar pouco texto por tela;
- apresentar exemplos progressivos;
- conter perguntas para a turma;
- prever prática;
- terminar, quando solicitado, com **resumo para o caderno**;
- evitar entregar de uma vez a solução que o estudante precisa construir.

### `roteiro_lab_*.html`

Material de execução prática do estudante.

Deve seguir uma progressão como:

```text
abrir ambiente
→ copiar/digitar código inicial
→ executar
→ observar
→ implementar uma parte
→ executar novamente
→ testar
→ corrigir
→ explicar
```

Deve conter:

- objetivo da prática;
- passos claros;
- checkpoints;
- dados de teste;
- evidências esperadas;
- erros comuns quando útil.

### `codigos_*.html`

Página de apoio com código(s) relevantes da aula.

Pode incluir:

- botão para copiar código;
- link para Trinket;
- link para `.py`;
- explicação breve do estágio do código.

**Não usar a página de códigos para entregar antecipadamente toda a solução quando a construção faz parte da aprendizagem.**

### Arquivos `.py`

Use nomes descritivos e consistentes.

Se for código inicial, deixar isso explícito no nome, por exemplo:

`central_avisos_27agosto_1tempo_inicio.py`

Se for versão consolidada:

`central_avisos_v01.py`

---

## 10. Padrão visual dos HTMLs

Antes de criar uma página, inspecione as páginas recentes para reutilizar o padrão.

Características atuais:

- fundo escuro;
- cartões em tons escuros;
- bordas discretas;
- cor de destaque por tipo de material;
- tipografia **Nunito** para texto;
- **Fira Code** para código;
- responsividade simples;
- conteúdo legível em projetor e notebook;
- botões visualmente consistentes com o `index.html`.

Não introduzir frameworks grandes sem necessidade.

Preferir HTML + CSS + JavaScript simples e autocontido.

Não adicionar dependências que compliquem o uso escolar.

---

## 11. Padrão do `index.html`

O `index.html` é a entrada principal dos estudantes.

Ao adicionar nova aula:

1. preservar as aulas anteriores;
2. adicionar a nova aula no bimestre correto;
3. usar card no padrão existente;
4. mostrar data, título e descrição curta;
5. adicionar somente botões para arquivos realmente existentes;
6. verificar todos os `href` antes de concluir;
7. manter o link para Trinket quando apropriado;
8. não remover histórico antigo apenas para simplificar a página.

Ao iniciar novo bimestre, criar nova seção em vez de sobrescrever a anterior.

---

## 12. Código Python: regras didáticas

O Python deve priorizar clareza para estudantes.

Preferir código simples, legível e diretamente relacionado ao conteúdo atual.

### Fazer

- nomes de variáveis em português quando isso ajudar a leitura;
- funções pequenas e com propósito claro;
- exemplos próximos da realidade dos alunos;
- execução com entradas previsíveis;
- testes simples;
- comentários somente quando ajudam a compreensão;
- mostrar estados intermediários quando forem úteis para investigação.

### Evitar sem autorização pedagógica

- `while True` + `break` antes de esse padrão ser ensinado;
- comprehensions como atalho para conteúdo ainda não trabalhado;
- `lambda`;
- tratamento de exceções sofisticado;
- programação funcional avançada;
- classes antes da aula de POO;
- decorators;
- type hints como conteúdo obrigatório;
- bibliotecas externas;
- GUI;
- web framework;
- banco de dados antes da etapa prevista;
- abstrações que escondam o raciocínio que o estudante precisa aprender.

---

## 13. Progressão em vez de cópia

A regra pedagógica central é:

**não transformar a aula em copiar e colar código pronto.**

Quando o estudante precisa construir uma funcionalidade, disponibilize um **código inicial funcional o suficiente para começar**, mas deixe a parte-alvo para ser desenvolvida durante a aula.

Exemplo correto para 27/08, 1º tempo:

```python
avisos = []

opcao = ""

while opcao != "0":
    print("1 - Cadastrar aviso")
    print("2 - Listar avisos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastro ainda será implementado.")
```

O estudante deve construir depois:

```python
def cadastrar_aviso():
    ...
```

---

## 14. Teste e evidência de aprendizagem

Toda prática relevante deve gerar evidência observável.

Exemplos:

- programa executa sem erro grave;
- aluno consegue explicar uma parte do código;
- aluno realiza entradas definidas e confere a saída;
- aluno identifica e corrige um erro;
- aluno altera um valor e prevê o efeito;
- aluno demonstra que a funcionalidade solicitada funciona.

Para a Central de Avisos, sempre que possível fornecer um roteiro de teste.

Exemplo de teste da v0.1:

```text
1 → cadastrar primeiro aviso
1 → cadastrar segundo aviso
2 → conferir se ambos aparecem
9 → conferir tratamento de opção inválida
0 → conferir encerramento
```

---

## 15. Erros como recurso pedagógico

Quando apropriado, usar erros previsíveis como oportunidade de aprendizagem.

Erros comuns na Central de Avisos:

- comparar a opção de `input()` com número em vez de string;
- esquecer `()` ao chamar uma função;
- colocar a lista dentro da função e reiniciá-la a cada chamada;
- errar indentação;
- usar chave de dicionário com nome diferente;
- confundir o dicionário individual com a lista de avisos;
- tentar acessar `avisos["titulo"]` quando o correto é acessar o dicionário atual;
- colocar código da função dentro do `while` por engano.

Não corrija silenciosamente todos os erros do material sem preservar o objetivo didático.

---

## 16. Resumo para o caderno

Quando o professor solicitar que a última tela seja “resumo para o caderno”:

- ela deve ser obrigatoriamente a última tela;
- deve conter somente os conceitos essenciais;
- deve ser copiável em poucos minutos;
- deve incluir sintaxe mínima ou pequeno exemplo;
- não deve introduzir conteúdo novo.

Para Programação Aplicada, registrar geralmente:

**conceito + sintaxe essencial + exemplo curto**.

---

## 17. Conteúdo novo versus integração

Antes de adicionar qualquer construção Python, pergunte implicitamente:

> “Este recurso já foi ensinado ou está explicitamente previsto para esta aula?”

Se a resposta não estiver sustentada pelo histórico ou pela instrução do professor, não o adicione como requisito.

Não usar um recurso tecnicamente melhor se ele prejudicar a sequência curricular.

Exemplo: uma solução profissional com exceções, classes e persistência pode ser tecnicamente superior, mas é inadequada se a turma ainda está consolidando listas, dicionários, funções, `for` e `while`.

---

## 18. Relação com Projeto e Desenvolvimento de Sistemas (PDS)

A Central de Avisos é integrada com PDS, mas este repositório é prioritariamente de **Programação Aplicada**.

Quando mencionar PDS, manter a distinção:

- PDS → problema, requisitos, modelagem, documentação;
- PA → implementação, execução, testes e correções em Python.

Não transformar páginas de Programação Aplicada em aula de UML ou requisitos, salvo quando o professor pedir uma referência breve de integração.

---

## 19. Validação antes de concluir uma alteração

Antes de finalizar uma tarefa, verificar:

- [ ] conteúdo corresponde ao que o professor pediu;
- [ ] não há conteúdo novo antecipado;
- [ ] arquivos seguem padrão de nomes;
- [ ] links internos funcionam;
- [ ] link para Trinket está correto quando utilizado;
- [ ] HTML abre sem erro evidente;
- [ ] JavaScript não quebra navegação;
- [ ] código Python tem sintaxe válida;
- [ ] código é compatível com o nível da turma;
- [ ] existe uma atividade ou ação do estudante;
- [ ] existe alguma evidência de aprendizagem;
- [ ] solução completa não foi liberada cedo demais;
- [ ] `index.html` preserva materiais anteriores;
- [ ] a nova aula está na seção correta do bimestre;
- [ ] não há botão apontando para arquivo inexistente;
- [ ] textos estão em português do Brasil;
- [ ] nomes institucionais e da turma estão corretos.

---

## 20. Como responder ao professor ao final de uma tarefa

Ao concluir mudanças no repositório, responder de forma objetiva informando:

1. quais arquivos foram criados;
2. quais arquivos foram alterados;
3. qual é o código inicial ou entrega disponibilizada aos alunos;
4. o que ficou propositalmente para ser construído em sala;
5. se houve qualquer inconsistência ou decisão que precise de confirmação;
6. se possível, o link do repositório/página para conferência.

Não afirmar que algo foi validado se não foi realmente verificado.

---

## 21. Regra para tarefas ambíguas

Se o pedido for algo como:

> “gere a aula da próxima quinta”

mas não houver conteúdo da data claramente disponível, **não inventar a sequência**.

Primeiro verificar os arquivos, o histórico e a orientação fornecida. Se ainda faltar informação, pedir ao professor o conteúdo/planejamento correspondente.

Se o professor já forneceu explicitamente a divisão entre os tempos, manter essa divisão.

---

## 22. Princípio final

O repositório deve ajudar o aluno a aprender programação, não apenas entregar respostas.

Em qualquer dúvida entre:

**mais recursos técnicos**

ou

**mais clareza, continuidade, teste e compreensão**, 

priorize a segunda opção.