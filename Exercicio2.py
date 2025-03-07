from tkinter import *
import tkinter as tk

class Pessoa:
    def __init__(self, nome, idade, telefone, cpf):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf

class Paciente(Pessoa):
    def __init__(self, nome, idade, telefone, cpf, dores):
        super().__init__(nome, idade, telefone, cpf)
        self.dores = dores

class Medico(Pessoa):
    def __init__(self, nome, idade, telefone, cpf, especialidade):
        super().__init__(nome, idade, telefone, cpf)
        self.especialidade = especialidade

class Consultas:
    def __init__(self, medico, paciente, data, hora):
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.hora = hora

class Clinica:
    def __init__(self, nome):
        self.nome = nome
        self.medicos = []
        self.pacientes = []
        self.consultas = []

    def cadastrar_medico(self, medico):
        self.medicos.append(medico)

    def cadastrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agendar_consultas(self, medico, paciente, data, hora):
        consulta = Consultas(medico, paciente, data, hora)
        self.consultas.append(consulta)

    def visualizar_consultas(self):
        if not self.consultas:
            print("Não há consultas agendadas.")
        for consulta in self.consultas:
            print(f'Médico: {consulta.medico.nome}, Paciente: {consulta.paciente.nome}, Data: {consulta.data}, Hora: {consulta.hora}')


def limpar_tela():
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_mensagem(mensagem):
    limpar_tela()
    Label(frame, text=mensagem, fg='green', font=('Arial', 14), bg='#f0f0f0').pack(pady=20)
    Button(frame, text="OK", command=limpar_tela, font=('Arial', 12), bg='#4CAF50', fg='white').pack(pady=10)

def validar_campos(campos):
    for campo in campos:
        if not campo.get():
            return False
    return True

def cadastrar_paciente():
    limpar_tela()
    
    nome_entry = Entry(frame, font=('Arial', 12))
    idade_entry = Entry(frame, font=('Arial', 12))
    telefone_entry = Entry(frame, font=('Arial', 12))
    cpf_entry = Entry(frame, font=('Arial', 12))
    dores_entry = Entry(frame, font=('Arial', 12))

    Label(frame, text='Nome:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    nome_entry.pack(pady=5)
    Label(frame, text='Idade:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    idade_entry.pack(pady=5)
    Label(frame, text='Telefone:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    telefone_entry.pack(pady=5)
    Label(frame, text='CPF:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    cpf_entry.pack(pady=5)
    Label(frame, text='Dores:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    dores_entry.pack(pady=5)

    def salvar_paciente():
        campos = [nome_entry, idade_entry, telefone_entry, cpf_entry, dores_entry]
        if validar_campos(campos):
            paciente = Paciente(nome_entry.get(), idade_entry.get(), telefone_entry.get(), cpf_entry.get(), dores_entry.get())
            clinica.cadastrar_paciente(paciente)
            mostrar_mensagem('Paciente cadastrado com sucesso!')
        else:
            mostrar_mensagem('Preencha todos os campos!')

    Button(frame, text="Salvar", command=salvar_paciente, font=('Arial', 12), bg='#4CAF50', fg='white').pack(pady=20)

def cadastrar_medico():
    limpar_tela()

    nome_entry = Entry(frame, font=('Arial', 12))
    idade_entry = Entry(frame, font=('Arial', 12))
    telefone_entry = Entry(frame, font=('Arial', 12))
    cpf_entry = Entry(frame, font=('Arial', 12))
    especialidade_entry = Entry(frame, font=('Arial', 12))

    Label(frame, text='Nome:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    nome_entry.pack(pady=5)
    Label(frame, text='Idade:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    idade_entry.pack(pady=5)
    Label(frame, text='Telefone:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    telefone_entry.pack(pady=5)
    Label(frame, text='CPF:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    cpf_entry.pack(pady=5)
    Label(frame, text='Especialidade:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    especialidade_entry.pack(pady=5)

    def salvar_medico():
        campos = [nome_entry, idade_entry, telefone_entry, cpf_entry, especialidade_entry]
        if validar_campos(campos):
            medico = Medico(nome_entry.get(), idade_entry.get(), telefone_entry.get(), cpf_entry.get(), especialidade_entry.get())
            clinica.cadastrar_medico(medico)
            mostrar_mensagem('Médico cadastrado com sucesso!')
        else:
            mostrar_mensagem('Preencha todos os campos!')

    Button(frame, text="Salvar", command=salvar_medico, font=('Arial', 12), bg='#4CAF50', fg='white').pack(pady=20)

def agendar_consulta():
    limpar_tela()

    medico_entry = Entry(frame, font=('Arial', 12))
    paciente_entry = Entry(frame, font=('Arial', 12))
    data_entry = Entry(frame, font=('Arial', 12))
    hora_entry = Entry(frame, font=('Arial', 12))

    Label(frame, text='Médico:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    medico_entry.pack(pady=5)
    Label(frame, text='Paciente:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    paciente_entry.pack(pady=5)
    Label(frame, text='Data:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    data_entry.pack(pady=5)
    Label(frame, text='Hora:', font=('Arial', 12), bg='#f0f0f0').pack(pady=5)
    hora_entry.pack(pady=5)

    def salvar_consulta():
        campos = [medico_entry, paciente_entry, data_entry, hora_entry]
        if validar_campos(campos):
            medico = next((m for m in clinica.medicos if m.nome == medico_entry.get()), None)
            paciente = next((p for p in clinica.pacientes if p.nome == paciente_entry.get()), None)
            if medico and paciente:
                clinica.agendar_consultas(medico, paciente, data_entry.get(), hora_entry.get())
                mostrar_mensagem('Consulta agendada com sucesso!')
            else:
                mostrar_mensagem('Médico ou Paciente não encontrado!')
        else:
            mostrar_mensagem('Preencha todos os campos!')

    Button(frame, text="Salvar", command=salvar_consulta, font=('Arial', 12), bg='#4CAF50', fg='white').pack(pady=20)

master = tk.Tk()
master.geometry("500x600")
master.title("Clínica Médica")
master.configure(bg="#f0f0f0")

clinica = Clinica("Clínica XYZ")

# Buttons
Button(master, text="Cadastrar Paciente", command=cadastrar_paciente, font=('Arial', 14), bg='#2196F3', fg='white', width=20).pack(pady=10)
Button(master, text="Cadastrar Médico", command=cadastrar_medico, font=('Arial', 14), bg='#2196F3', fg='white', width=20).pack(pady=10)
Button(master, text="Agendar Consulta", command=agendar_consulta, font=('Arial', 14), bg='#2196F3', fg='white', width=20).pack(pady=10)

# Frame
frame = Frame(master, bg="#f0f0f0")
frame.pack(fill=BOTH, expand=True)

master.mainloop()
