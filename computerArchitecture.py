
class Cache: #Memória de alta velocidade que armazena cópias de dados e instruções frequentemente acessados para acelerar o processamento.
    def __init__(self) -> None:
        pass

class UC: #Gerencia e coordena todas as operações da CPU, buscando instruções na memória, interpretando-as e controlando os outros componentes para executá-las.
    def __init__(self, instructions, instruction_list) -> None:
        self.instructions = instructions
        self.instruction_list = instruction_list

    def fetch(self):
        with open(self.instructions, 'r') as file:
            self.instruction_list = []
            content = file.read()
            for instruction in content:
                self.instruction_list.append(instruction)


    def decode(self):
        pass

    def execute(self):
        pass

class ULA(UC): #Responsável por realizar operações aritméticas (soma, subtração, etc.) e lógicas (comparações, operações booleanas) nos dados.
    def __init__(self) -> None:
        pass

class Registradores: #Pequenas unidades de memória ultrarrápidas dentro da CPU que armazenam temporariamente dados e instruções a serem processados.
    def __init__(self) -> None:
        pass

class PC: #Registrador especial que armazena o endereço da próxima instrução a ser executada.
    def __init__(self) -> None:
        pass

""" def fetch():
    pass """

""" def decode():
    pass

def execute():
    pass
 """
def write_back():
    pass