'''
Universidade Federal de Pernambuco - (UFPE) - (https://www.ufpe.br/)
Centro de Informática (CIn) - (https://www2.cin.ufpe.br/site/index.php)
Graduando - Sistemas de Informação
Programação 1 - IF968

Autor: Aslay Clevisson Soares Santos - (acss3)
E-mail: acss3@cin.ufpe.br
Data: 26-08-2019
Copyright(c) 2019 Aslay Clevisson Soares Santos
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import csv


dic_admin = {'admin':'admin'}
class escolinha():
    def __init__(self):
        '''
        Janela principal do programa.
        Recolhe informações de entrada de login e senha para abrir os demais painéis
        '''
        self.janela = Tk()
        self.janela['bg']='#B8D6F0'
        self.janela.title('Login')
        self.janela.geometry('450x250+500+250')
        
        Label(self.janela,text='Entre como admin',bg='#B8D6F0').place(x=170,y=40)
        Label(self.janela,text='Login:',bg='#B8D6F0').place(x=125,y=70)
        self.login = Entry(self.janela, width = 20)
        self.login.place(x=165,y=70)
        
        Label(self.janela,text='Senha:',bg='#B8D6F0').place(x=125,y=95)
        self.senha = Entry(self.janela, show='*')
        self.senha.place(x=165,y=95)
        
        self.label_conf_login = Label(self.janela,text=' ',bg='#B8D6F0')
        self.label_conf_login.place(x=112,y=150)
        
        self.janela.resizable(False,False)
        #botões de comando
        Button(self.janela, text='Entrar',width=15, command=self.autenticacaoLogin, bg='#22467D', fg='white').place(x=170,y=120)
        self.janela.mainloop()


    def autenticacaoLogin(self):
        '''
        Verifica se o login do Prof/Administrador, pode ser autenticado
        '''
        login = self.login.get()
        senha = self.senha.get()
        for key,value in dic_admin.items():
            if login == key and senha == value:
                messagebox.showinfo('login','Você foi autenticado!')
                self.painelProf()

    
    def painelProf(self):
        '''
        Painel com configurações de professor
        - busca
        - lista
        - cadastro
        '''
        self.janela.destroy()
        self.janela = Tk()
        self.janela.geometry('600x350+500+300')
        self.janela['bg']='#B8D6F0'
        self.janela.title('Painel professor')
        self.painel = 1
        self.busca = 0

        Label(self.janela,text='Aluno Matrícula N°: ',bg='#B8D6F0',font='negrito').place(x=10,y=50)
        self.aluno = Entry(self.janela, width = 35,font="arial")
        self.aluno.place(x=150,y=50)
        Button(self.janela,text='Buscar Aluno', command=self.buscarAluno, bg='#22467D', fg='white').place(x=475,y=48)
        Button(self.janela,text='Listar alunos',command=self.alunosListados, bg='#22467D', fg='white').place(x=220,y=75)
        Button(self.janela,text='Cadastrar aluno',command=self.cadastroAluno, bg='#22467D', fg='white').place(x=315,y=75)
        Button(self.janela,text='Sair',command=self.voltar, bg='#22467D', fg='white',width=15).place(x=482,y=322)

        self.janela.mainloop()
    
    def buscarAluno(self):
        '''
        Verifica a matrícula do aluno se encontra no arquivo.csv, es estiver, abre uma janela com configurações do mesmo
        '''
        self.alunoProcurado = str(self.aluno.get())
        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            for linha in leitura:
                if str(linha[0]) == self.alunoProcurado:
                    self.busca = 1
                    self.alunosListados()
            #else:
            #    messagebox.showinfo('','Aluno não encontrado.')

                    
    
    def alunosListados(self):
        '''
        Lista todos os alunos encontrados no banco de dados ou lista apenas o aluno buscado
        - remover a
        - editar notas
        '''
        self.janela.destroy()
        self.janela = Tk ()
        self.janela['bg']='#B8D6F0'
        self.janela.title('Jan. Alunos')
        self.janela.geometry('+500+250')
        self.painel = 2

        self.treeAlunos = ttk.Treeview(self.janela,selectmode='browse',column=('column1','column2'), show='headings')
        
        self.treeAlunos.column('column1', width=100,minwidth=200,stretch=NO)
        self.treeAlunos.heading('#1', text='Matrícula')

        self.treeAlunos.column('column2', width=100,minwidth=200,stretch=NO)
        self.treeAlunos.heading('#2', text='Aluno') 

        self.treeAlunos.grid(row=1, column=1,padx=4,pady=4,rowspan=6,columnspan=2)

        
        Button(self.janela,text='Remover aluno', command=self.removerAluno, bg='#22467D', fg='white', width=15).grid(row=3,column=3,padx=3,pady=3)
        Button(self.janela,text='Ver aluno', command=self.alunoInfo, bg='#22467D', fg='white', width=15).grid(row=4,column=3,padx=3,pady=3)
        Button(self.janela,text='Voltar', command=self.voltar, bg='#22467D', fg='white', width=15).grid(row=6,column=3,padx=3,pady=3,sticky=E+S)


        if self.busca == 1:
            with open('programacao_1-20192.csv','r') as alunos:
                leitura = csv.reader(alunos)
                next(leitura)
                linhaADD=[]
                for a in leitura:
                    if str(a[0]) == self.alunoProcurado:
                        linhaADD=[a[0],a[1]]
                        print(linhaADD)
                        self.treeAlunos.insert("", END, values=linhaADD, iid=a[0], tag='1')
                alunos.close()
        else:
            if self.busca != 1:
                with open('programacao_1-20192.csv','r') as alunos:
                    todosA = csv.reader(alunos)
                    next(todosA)
                    linhasADD=[]

                    for a in todosA:
                        linhasADD=[a[0],a[1]]
                        self.treeAlunos.insert("", END, values=linhasADD, iid=a[0], tag='1')
                    alunos.close()
        self.janela.mainloop()


    def cadastroAluno(self):
        '''
        Recebe as informações do aluno que será cadastrado
        '''
        self.janelinha = Tk()
        self.janelinha['bg']='#B8D6F0'
        self.janelinha.title('Jan. cad.')
        self.janelinha.geometry('380x200+500+250')

        Label(self.janelinha,text='Aluno: ',bg='#B8D6F0',font='negrito').grid(row=1,column=1,sticky=E,padx=3,pady=3)
        self.aluno = Entry(self.janelinha, width = 25,font="arial")
        self.aluno.grid(row=1,column=2,padx=3,pady=3)


        Label(self.janelinha,text='Matrícula: ',bg='#B8D6F0',font='negrito').grid(row=2,column=1,sticky=E,padx=3,pady=3)
        self.matricula = Entry(self.janelinha, width = 25,font="arial")
        self.matricula.grid(row=2,column=2,padx=3,pady=3)

        Button(self.janelinha,text='Cadastrar aluno', command=self.cadastroFeito, bg='#22467D', fg='white').grid(row=3,column=2,padx=3,pady=3)

        self.janelinha.mainloop()

    def cadastroFeito(self):
        '''
        Armazena as informações recebidas no cadastro do aluno, num arquivo.csv
        '''
        if messagebox.askokcancel('','Confirmar cadastro?'):
            matricula = self.matricula.get()
            aluno = self.aluno.get()
            self.janelinha.destroy()
            with open('programacao_1-20192.csv',mode='a', encoding='utf-8', newline='') as adicionar:
                add = csv.writer(adicionar)
                add.writerow([matricula,aluno,0,0,0,0,0,0])
                adicionar.close()

                messagebox.showinfo('concluído','Aluno adicionado a disciplina')


    def removerAluno(self):
        '''
        Faz a busca do aluno pela Matrícula e o remove do arquivo.csv
        '''
        if messagebox.askokcancel('','Tem certeza que deseja remover esse aluno?'):
            matriculaAluno = int(self.treeAlunos.selection()[0])
            try:
                with open('programacao_1-20192.csv','r') as alunos:
                    leitura = csv.reader(alunos)
                    next(leitura)
                    lista_alunos=[['Matrícula','Nome','Nota1','Nota2','Nota3','Nota4','Media','Faltas']]
                    flag = 0
                    for linha in leitura:
                        if int(linha[0]) == matriculaAluno:
                            flag=1
                            continue
                        else:
                            lista_alunos.append(linha)
                    alunos.close()        
                    if flag == 1:
                        with open('programacao_1-20192.csv', mode='w', encoding='utf-8', newline='') as alunos:
                            escrita = csv.writer(alunos)
                            for linha in lista_alunos:
                                escrita.writerow(linha)
                            alunos.close()
                    messagebox.showinfo('Remoção','Usuário removido.')
                    
                    self.janela.destroy()
                    self.painelProf()
                    self.alunosListados()

            except:
                    print('errei')    

    def alunoInfo(self):
        '''
        Painel das notas e informações sobre o aluno que foi selecionado pela matrícula
        '''
        matriculaAluno = int(self.treeAlunos.selection()[0])

        self.janela = Tk()
        self.janela['bg']='#B8D6F0'
        self.janela.title('Jan. Info.')
        self.janela.geometry('550x253+500+250')
        self.painel = 3

        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            for linha in leitura:
                if int(linha[0]) == matriculaAluno:
                    Label(self.janela, text=f'N° de matrícula: {linha[0]}',bg='#B8D6F0',font='negrito').grid(row=1,column=1)
                    Label(self.janela, text=f'{linha[1]}',bg='#B8D6F0',font='negrito').grid(row=2,column=1,sticky=W)
                    Label(self.janela, text=f'Nota 1: {linha[2]}',bg='#B8D6F0',font='negrito').grid(row=3,column=1,sticky=E)
                    Label(self.janela, text=f'Nota 2: {linha[3]}',bg='#B8D6F0',font='negrito').grid(row=4,column=1,sticky=E)
                    Label(self.janela, text=f'Nota 3: {linha[4]}',bg='#B8D6F0',font='negrito').grid(row=5,column=1,sticky=E)
                    Label(self.janela, text=f'Nota 4: {linha[5]}',bg='#B8D6F0',font='negrito').grid(row=6,column=1,sticky=E)
                    Label(self.janela, text=f'Média: {linha[6]}',bg='#B8D6F0',font='negrito').grid(row=7,column=1,sticky=E)
                    Label(self.janela, text=f'Faltas: {linha[7]}',bg='#B8D6F0',font='negrito').grid(row=8, rowspan=3, column=1,sticky=E) 
                
                    if float(linha[6]) >= 7 and int(linha[7]) <= 8:
                        Label(self.janela, text='Aprovado por média',bg='#B8D6F0',font='negrito').grid(row=7,column=3,sticky=E)
                    else:
                        if int(linha[7]) <= 8 and float(linha[6]) < 7:
                            Label(self.janela, text='Reprovado por média',bg='#B8D6F0',font='negrito').grid(row=7,column=3,sticky=E)
                        
                        elif int(linha[7]) > 8 and float(linha[6]) < 7:
                            Label(self.janela, text='Reprovado faltas',bg='#B8D6F0',font='negrito').grid(row=8,column=4,sticky=E)

                        else:
                             Label(self.janela, text='REPROVADO',bg='#B8D6F0',font='negrito').grid(row=11,column=3,sticky=E)                               

        
        self.n1 = Entry(self.janela)
        self.n1.grid(row=3,padx=2,pady=2,column=2)

        self.n2 = Entry(self.janela)
        self.n2.grid(row=4,column=2,padx=2,pady=2,sticky=E)

        self.n3 = Entry(self.janela)
        self.n3.grid(row=5,column=2,padx=2,pady=2,sticky=E)

        self.n4 = Entry(self.janela)
        self.n4.grid(row=6,column=2,padx=2,pady=2,sticky=E)

        self.faltas = Entry(self.janela)
        self.faltas.grid(row=8,rowspan=3,column=2,padx=2,pady=2,sticky=E)
        
        Button(self.janela, text='Editar N1',width=15, command=self.atualizarNota1, bg='#22467D', fg='white').grid(row=3,column=3,padx=2,pady=2,sticky=E)
        Button(self.janela, text='Editar N2',width=15, command=self.atualizarNota2, bg='#22467D', fg='white').grid(row=4,column=3,padx=2,pady=2,sticky=E)
        Button(self.janela, text='Editar N3',width=15, command=self.atualizarNota3, bg='#22467D', fg='white').grid(row=5,column=3,padx=2,pady=2,sticky=E)
        Button(self.janela, text='Editar N4',width=15, command=self.atualizarNota4, bg='#22467D', fg='white').grid(row=6,column=3,padx=2,pady=2,sticky=E)
        Button(self.janela, text='Adicionar falta',width=15, command=self.atualizarFaltas, bg='#22467D', fg='white').grid(row=8,rowspan=3,column=3,padx=2,pady=2,sticky=E)
        Button(self.janela, text='Voltar',width=15, command=self.voltar, bg='#22467D', fg='white').grid(row=11,column=1,padx=2,pady=2,sticky=W+S)
            
        self.janela.mainloop()

    def atualizarNota1(self):
        '''
        Atualiza a nota do aluno selecionado, sendo declarada pelo professor, no arquivo.csv
        '''
        matriculaAluno = int(self.treeAlunos.selection()[0])
        print(matriculaAluno)

        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            lista_alunos=[['Matrícula','Nome','Nota1','Nota2','Nota3','Nota4','Media','Faltas']]
            for elem in leitura:
                if int(elem[0]) == matriculaAluno:
                    aux = elem
                    aux[6] = (float(self.n1.get())+float(elem[3])+float(elem[4])+float(elem[5]))/4
                    aux[2] = float(self.n1.get())
                    lista_alunos.append(aux)
                else:
                    lista_alunos.append(elem)
            alunos.close()

            with open('programacao_1-20192.csv',mode='w', encoding='utf-8', newline='') as alunos:
                escrita = csv.writer(alunos)
                for lista in lista_alunos:
                    escrita.writerow(lista)
                alunos.close()
        messagebox.showinfo('atualização','Nota atualizada.')
        self.janela.destroy()
        self.alunoInfo()

    def atualizarNota2(self):
        '''
        Atualiza a nota do aluno selecionado, sendo declarada pelo professor, no arquivo.csv
        '''
        matriculaAluno = int(self.treeAlunos.selection()[0])
        print(matriculaAluno)

        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            lista_alunos=[['Matrícula','Nome','Nota1','Nota2','Nota3','Nota4','Media','Faltas']]
            for elem in leitura:
                if int(elem[0]) == matriculaAluno:
                    aux = elem
                    aux[6] = (float(self.n2.get())+float(elem[2])+float(elem[4])+float(elem[5]))/4
                    aux[3] = float(self.n2.get())
                    lista_alunos.append(aux)
                else:
                    lista_alunos.append(elem)
            alunos.close()

            with open('programacao_1-20192.csv',mode='w', encoding='utf-8', newline='') as alunos:
                escrita = csv.writer(alunos)
                for lista in lista_alunos:
                    escrita.writerow(lista)
                alunos.close()
        messagebox.showinfo('atualização','Nota atualizada.')
        self.janela.destroy()
        self.alunoInfo()

    def atualizarNota3(self):
        '''
        Atualiza a nota do aluno selecionado, sendo declarada pelo professor, no arquivo.csv
        '''
        matriculaAluno = int(self.treeAlunos.selection()[0])
        print(matriculaAluno)

        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            lista_alunos=[['Matrícula','Nome','Nota1','Nota2','Nota3','Nota4','Media','Faltas']]
            for elem in leitura:
                if int(elem[0]) == matriculaAluno:
                    aux = elem
                    aux[6] = (float(self.n3.get())+float(elem[2])+float(elem[3])+float(elem[5]))/4
                    aux[4] = float(self.n3.get())
                    lista_alunos.append(aux)
                else:
                    lista_alunos.append(elem)
            alunos.close()

            with open('programacao_1-20192.csv',mode='w', encoding='utf-8', newline='') as alunos:
                escrita = csv.writer(alunos)
                for lista in lista_alunos:
                    escrita.writerow(lista)
                alunos.close()
        messagebox.showinfo('atualização','Nota atualizada.')
        self.janela.destroy()
        self.alunoInfo()  

    def atualizarNota4(self):
        '''
        Atualiza a nota do aluno selecionado, sendo declarada pelo professor, no arquivo.csv
        '''
        matriculaAluno = int(self.treeAlunos.selection()[0])
        print(matriculaAluno)

        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            lista_alunos=[['Matrícula','Nome','Nota1','Nota2','Nota3','Nota4','Media','Faltas']]
            for elem in leitura:
                if int(elem[0]) == matriculaAluno:
                    aux = elem
                    print((float(self.n4.get())+float(elem[3])+float(elem[4])+float(elem[2]))/4)
                    aux[6] = (float(self.n4.get())+float(elem[3])+float(elem[4])+float(elem[2]))/4
                    aux[5] = float(self.n4.get())
                    lista_alunos.append(aux)
                else:
                    lista_alunos.append(elem)
            alunos.close()

            with open('programacao_1-20192.csv',mode='w', encoding='utf-8', newline='') as alunos:
                escrita = csv.writer(alunos)
                for lista in lista_alunos:
                    escrita.writerow(lista)
                alunos.close()
        messagebox.showinfo('atualização','Nota atualizada.')
        self.janela.destroy()
        self.alunoInfo()

    def atualizarFaltas(self):
        '''
        Atualiza as faltas do aluno selecionado, sendo declarada pelo professor, no arquivo.csv
        '''
        matriculaAluno = int(self.treeAlunos.selection()[0])
        print(matriculaAluno)

        with open('programacao_1-20192.csv','r') as alunos:
            leitura = csv.reader(alunos)
            next(leitura)
            lista_alunos=[['Matrícula','Nome','Nota1','Nota2','Nota3','Nota4','Media','Faltas']]
            for elem in leitura:
                if int(elem[0]) == matriculaAluno:
                    aux = elem
                    aux[7] = int(self.faltas.get())
                    lista_alunos.append(aux)
                else:
                    lista_alunos.append(elem)
            alunos.close()

            with open('programacao_1-20192.csv',mode='w', encoding='utf-8', newline='') as alunos:
                escrita = csv.writer(alunos)
                for lista in lista_alunos:
                    escrita.writerow(lista)
                alunos.close()
        messagebox.showinfo('atualização','Faltas atualizada.')
        self.janela.destroy()
        self.alunoInfo()

    def voltar(self):
        if self.painel == 3:
            self.alunosListados()
        elif self.painel == 2:
            self.painelProf()
        elif self.painel == 1:
            self.janela.destroy()
            self.__init__()






escolinha()