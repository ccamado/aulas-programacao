import tkinter as tk
from tkinter import ttk
from datetime import datetime
class Aviso:
    def __init__(self, codigo, dados):
        self.codigo, self.dados = codigo, dados.copy()
avisos, proximo_id, selecionado = [], 1, None
AZUL, FUNDO, BRANCO = '#18365B', '#EAF1F9', '#FFFFFF'
filtro_titulo, filtro_categoria = '', 'Todas'
janela = tk.Tk()
janela.title('CEPEF | Central de Avisos'); janela.geometry('1000x710')
janela.configure(bg=FUNDO)
tk.Label(janela, text='CENTRAL DE AVISOS  |  CEPEF', bg=AZUL,
         fg=BRANCO, font=('Arial', 18, 'bold'), pady=15).pack(fill='x')
painel = tk.LabelFrame(janela, text=' Dados do aviso ', bg=BRANCO,
                      fg=AZUL, padx=12, pady=8)
painel.pack(fill='x', padx=15, pady=10)
nomes = ['Titulo', 'Categoria', 'Prioridade', 'Publico-alvo',
         'Responsavel', 'Data (dd/mm/aaaa)', 'Situacao', 'Descricao']
valores = {nome: tk.StringVar() for nome in nomes}
opcoes = {'Categoria': ['Evento', 'Atividade', 'Comunicado'],
          'Prioridade': ['Normal', 'Alta', 'Urgente'],
          'Publico-alvo': ['Alunos', 'Professores', 'Comunidade', 'Todos'],
          'Situacao': ['Rascunho', 'Publicado']}
for i, nome in enumerate(nomes):
    linha, coluna = divmod(i, 3)
    tk.Label(painel, text=nome, bg=BRANCO, fg=AZUL).grid(
        row=linha * 2, column=coluna, sticky='w', padx=5)
    if nome in opcoes:
        campo = ttk.Combobox(painel, textvariable=valores[nome],
                             values=opcoes[nome], state='readonly')
    else:
        campo = tk.Entry(painel, textvariable=valores[nome])
    campo.grid(row=linha * 2 + 1, column=coluna, padx=5, pady=5, sticky='ew')
for i in range(3):
    painel.columnconfigure(i, weight=1)  # Compativel com Pyroom.
mensagem = tk.StringVar(value='Novo cadastro: preencha os campos.')
tk.Label(janela, textvariable=mensagem, bg=FUNDO, fg=AZUL).pack(anchor='w', padx=20)
def modo_edicao(editar):
    botoes['CADASTRAR'].configure(state='disabled' if editar else 'normal')
    for nome in ('ALTERAR', 'EXCLUIR'):
        botoes[nome].configure(state='normal' if editar else 'disabled')
    botoes['LIMPAR'].configure(state='normal' if editar else 'disabled')
def atualizar():
    for item in tabela.get_children():
        tabela.delete(item)
    for aviso in avisos:
        d = aviso.dados
        if filtro_titulo.lower() not in d['Titulo'].lower():
            continue
        if filtro_categoria != 'Todas' and d['Categoria'] != filtro_categoria:
            continue
        tabela.insert('', 'end', iid=str(aviso.codigo), values=(
            aviso.codigo, d['Titulo'], d['Categoria'], d['Prioridade'],
            d['Publico-alvo'], d['Situacao']))
def limpar():
    global selecionado
    selecionado = None
    for var in valores.values():
        var.set('')
    for campo, padrao in [('Categoria', 'Evento'), ('Prioridade', 'Normal'),
                          ('Publico-alvo', 'Alunos'), ('Situacao', 'Rascunho')]:
        valores[campo].set(padrao)
    for item in tabela.selection():
        tabela.selection_remove(item)
    modo_edicao(False)
    mensagem.set('Modo cadastro: CADASTRAR habilitado.')
def ler():
    d = {nome: var.get().strip() for nome, var in valores.items()}
    if not d['Titulo'] or not d['Responsavel']:
        mensagem.set('Titulo e Responsavel sao obrigatorios.'); return None
    if d['Data (dd/mm/aaaa)']:
        try:
            datetime.strptime(d['Data (dd/mm/aaaa)'], '%d/%m/%Y')
        except ValueError:
            mensagem.set('Data invalida: use dd/mm/aaaa.'); return None
    return d
def cadastrar():
    global proximo_id
    if selecionado is not None: return  # Dupla protecao contra duplicacao.
    dados = ler()
    if dados is None: return
    avisos.append(Aviso(proximo_id, dados))
    codigo, proximo_id = proximo_id, proximo_id + 1
    atualizar(); limpar()
    mensagem.set('Aviso %s cadastrado!' % codigo)
def escolher(event=None):
    global selecionado
    linhas = tabela.selection()
    if not linhas: return
    codigo = int(linhas[0])
    aviso = next((a for a in avisos if a.codigo == codigo), None)
    if aviso is None: return
    selecionado = codigo
    for nome in nomes:
        valores[nome].set(aviso.dados[nome])
    modo_edicao(True)
    mensagem.set('Aviso %s selecionado: altere, exclua ou limpe.' % codigo)
def alterar():
    if selecionado is None: return
    dados = ler()
    if dados is None: return
    for aviso in avisos:
        if aviso.codigo == selecionado:
            aviso.dados = dados.copy()
            codigo = selecionado
            atualizar(); limpar()
            mensagem.set('Aviso %s alterado!' % codigo)
            return
def excluir():
    global avisos
    if selecionado is None: return
    codigo = selecionado
    avisos = [a for a in avisos if a.codigo != codigo]
    atualizar(); limpar()
    mensagem.set('Aviso %s excluido!' % codigo)
def consultar():
    global filtro_titulo, filtro_categoria
    busca = tk.Toplevel(janela)
    busca.title('Consultar avisos'); busca.geometry('350x210')
    busca.configure(bg=FUNDO)
    titulo = tk.StringVar(value=filtro_titulo); categoria = tk.StringVar(value=filtro_categoria)
    tk.Label(busca, text='Titulo contem:', bg=FUNDO).pack(pady=(12, 2))
    tk.Entry(busca, textvariable=titulo, width=34).pack()
    tk.Label(busca, text='Categoria:', bg=FUNDO).pack(pady=(9, 2))
    ttk.Combobox(busca, textvariable=categoria, state='readonly',
        values=['Todas'] + opcoes['Categoria'], width=31).pack()
    def aplicar(reset=False):
        global filtro_titulo, filtro_categoria
        filtro_titulo = '' if reset else titulo.get().strip()
        filtro_categoria = 'Todas' if reset else categoria.get()
        limpar(); atualizar(); busca.destroy()
        mensagem.set('Consulta aplicada. Registros encontrados: %s' % len(tabela.get_children()))
    tk.Button(busca, text='FILTRAR', bg='#1964A0', fg='white',
              command=aplicar).pack(side='left', padx=35, pady=15)
    tk.Button(busca, text='VER TODOS', bg='#576579', fg='white',
              command=lambda: aplicar(True)).pack(side='left', pady=15)
barra = tk.Frame(janela, bg=FUNDO)
barra.pack(fill='x', padx=16, pady=8)
botoes = {}
for texto, funcao, cor in [('CADASTRAR', cadastrar, '#147D52'),
                           ('CONSULTAR', consultar, '#1964A0'),
                           ('ALTERAR', alterar, '#C47A13'),
                           ('EXCLUIR', excluir, '#B53C48'),
                           ('LIMPAR', limpar, '#576579')]:
    botoes[texto] = tk.Button(barra, text=texto, command=funcao,
        bg=cor, fg='white', padx=12, pady=7, font=('Arial', 10, 'bold'))
    botoes[texto].pack(side='left', padx=4)
tk.Label(janela, text='AVISOS CADASTRADOS', bg=FUNDO,
         fg=AZUL, font=('Arial', 11, 'bold')).pack(anchor='w', padx=18)
colunas = ('ID', 'Titulo', 'Categoria', 'Prioridade', 'Publico', 'Situacao')
tabela = ttk.Treeview(janela, columns=colunas, show='headings', height=8)
for nome, largura in zip(colunas, [45, 300, 140, 110, 150, 120]):
    tabela.heading(nome, text=nome)
    tabela.column(nome, width=largura)
tabela.pack(fill='both', expand=True, padx=18, pady=8)
tabela.bind('<<TreeviewSelect>>', escolher)
limpar()
janela.mainloop()
