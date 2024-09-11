import customtkinter
from cryptography.fernet import Fernet
from CTkMessagebox import CTkMessagebox

listaPessoas = []

#Função de cadastro, vai abrir uma janela nova a partir da principal, realizar o cadastro do usuario de acordo com os requesitos principais, futuramente realizar dentroi da função um calculo de imc e atribuição de exercicios e alimentação.
def cadastro():

    #Abre uma nova janela para a realização do cadastro
    janelaCadastro = customtkinter.CTkToplevel()
    janelaCadastro.title("Cadastro")
    janelaCadastro.geometry("500x600")
    janelaCadastro.resizable(False,False)

    def trazerAFrente():
        janelaCadastro.lift()
        janelaCadastro.focus_force()

    trazerAFrente()
    #função para verificar se as senhas do usuario no cadastro estão iguais, estou tendo erros nessa parte
    def verificaSenhasIguais(senha1, senha2):
        if senha1 == senha2:
            chaveSecreta = Fernet.generate_key()
            fernet = Fernet(chaveSecreta)

            def criptografarSenha(senhaUsuario):
                return fernet.encrypt(senhaUsuario.encode()).decode()

            return criptografarSenha(senha1)
        else:
            CTkMessagebox(title="Atenção", message="Insira Senhas iguais!!")
            return None

    #Função para capturar valores dos inputs e passar para as variaveis necessarias
    def valorCadastro():
        nomePessoa = inputNomePessoa.get()
        idadePessoa = inputIdadePessoa.get()
        telefonePessoa = inputTelefonePessoa.get()
        pesoPessoa = inputPesoPessoa.get()
        alturaPessoa = inputAlturaPessoa.get()
        
        #Metodo para inserir os dados do usuario na listaPessoas
        listaPessoas.append({
            'Nome': nomePessoa,
            'Idade': idadePessoa,
            'Telefone': telefonePessoa,
            'Peso': pesoPessoa,
            'Altura': alturaPessoa,
        })
        print("Pessoa Cadastrada: ",listaPessoas)
        verificaSenhasIguais(senha1,senha2)
        janelaCadastro.destroy()


    #Elementos da Biblioteca customtkinter que vão receber os dados do usuario
    labelJanelaCadastro = customtkinter.CTkLabel(janelaCadastro,text="Preencha os campos abaixo de acordo com as especificações.")
    inputNomePessoa = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Nome Completo")
    inputNomeDeUsuarioPessoa = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Defina Um nome de Usuario")
    inputIdadePessoa = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Idade")
    inputTelefonePessoa = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Telefone")
    inputPesoPessoa = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Peso Atual")
    inputAlturaPessoa = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Altura")
    inputSenhaUsuario = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Insira sua Senha")
    inputSenhaUsuarioNovamente = customtkinter.CTkEntry(janelaCadastro,placeholder_text="Insira sua Senha Novamente")

    botaoSalvar = customtkinter.CTkButton(janelaCadastro, text="Salvar", command=valorCadastro)

    labelJanelaCadastro.pack(padx=10,pady=10)
    inputNomePessoa.pack(padx=10,pady=10)
    inputNomeDeUsuarioPessoa.pack(padx=10,pady=10)
    inputIdadePessoa.pack(padx=10,pady=10)
    inputTelefonePessoa.pack(padx=10,pady=10)
    inputPesoPessoa.pack(padx=10,pady=10)
    inputAlturaPessoa.pack(padx=10,pady=10)
    inputSenhaUsuario.pack(padx=10,pady=10)
    inputSenhaUsuarioNovamente.pack(padx=10,pady=10)

    botaoSalvar.pack(padx=10,pady=10)



#Função responsavel por exibir a janela principal do usuario, essa janela vai mostrar dados de usuario, recomendação de treino baseados nas informações descritas(Lesões do usuario,Alimentação baseada em dieta,treino recomendados e suplementação recomendada.) 
def janelaDashboard():
    janelaDashboardPrincipal = customtkinter.CTkToplevel()
    janelaDashboardPrincipal.geometry("600x500")
    janelaDashboardPrincipal.title("Dashboard")
    janela.destroy()
    janelaDashboardPrincipal.resizable(False,False)

    caixaDeTexto = customtkinter.CTkTextbox(janelaDashboardPrincipal,width=200,height=200,)
    caixaDeTexto.pack()
    caixaDeTexto.insert("Bem Vindo\n\n","Olá, Bem vindo DevMonsterHealth, Aqui você vai ter informações detalhadas sobre seu Treino,Alimentação e recomendação de treinos para  sua condição fisica.\n\n","Está é nossa tela de Dashboard principal, aqui você vai ficar por dentro das informações mais importantes do seu treino e condição atual.")



#Janela De login do app, onde o app uma função ira verificar se o usuario está ou não cadastrado na plataforma
janela = customtkinter.CTk()
janela.geometry("600x500")
janela.title("Login")

labelLogin = customtkinter.CTkLabel(janela,text="Login")

inputUsername = customtkinter.CTkEntry(janela,placeholder_text="Nome de usuario")
inputSenha = customtkinter.CTkEntry(janela,placeholder_text="Senha")
botaoLogin = customtkinter.CTkButton(janela,text="Conectar",fg_color="green")
botaoCadastro = customtkinter.CTkButton(janela,text="Cadastro",command=cadastro)
labelLogin.pack(padx=10,pady=10)
inputUsername.pack(padx=10,pady=10)
inputSenha.pack(padx=10,pady=10)
botaoLogin.pack(padx=10,pady=10)
botaoCadastro.pack(padx=10,pady=10)

janela.mainloop()