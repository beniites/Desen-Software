from tkinter import *
import tkinter as tk


def limpar_tela():
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_mensagem():
    limpar_tela()
    Label(frame, text='Dados salvos!', fg='green', font=('Arial', 14)).pack()
    Button(frame, text="OK", command=limpar_tela).pack()

def cadastrar_paciente():
    limpar_tela()
    Label(frame, text='Nome:').pack()
    Entry(frame).pack()
    Label(frame, text='Idade:').pack()
    Entry(frame).pack()
    Label(frame, text='Telefone:').pack()
    Entry(frame).pack()
    Label(frame, text='CPF:').pack()
    Entry(frame).pack()
    Label(frame, text='Dores:').pack()
    Entry(frame).pack()
    Button(frame, text="Salvar", command=mostrar_mensagem).pack()

def cadastrar_medico():
    limpar_tela()
    Label(frame, text='Nome:').pack()
    Entry(frame).pack()
    Label(frame, text='Idade:').pack()
    Entry(frame).pack()
    Label(frame, text='Telefone:').pack()
    Entry(frame).pack()
    Label(frame, text='CPF:').pack()
    Entry(frame).pack()
    Label(frame, text='Especialidade:').pack()
    Entry(frame).pack()
    Button(frame, text="Salvar", command=mostrar_mensagem).pack()

def agendar_consulta():
    limpar_tela()
    Label(frame, text='Médico:').pack()
    Entry(frame).pack()
    Label(frame, text='Paciente:').pack()
    Entry(frame).pack()
    Label(frame, text='Data:').pack()
    Entry(frame).pack()
    Label(frame, text='Hora:').pack()
    Entry(frame).pack()
    Button(frame, text="Salvar", command=mostrar_mensagem).pack()

master = tk.Tk()
master.geometry("400x500")
master.title("Clínica Médica")

Button(master, text="Cadastrar Paciente", command=cadastrar_paciente).pack()
Button(master, text="Cadastrar Médico", command=cadastrar_medico).pack()
Button(master, text="Agendar Consulta", command=agendar_consulta).pack()

frame = Frame(master)
frame.pack(fill=BOTH, expand=True)

master.mainloop()

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
            print(consulta)

