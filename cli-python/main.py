from typing import List, Optional, TypeVar 

class Elemento:
    def __init__(self, linha: int, coluna: int, valor: float) -> None:
        self.linha = linha
        self.coluna = coluna
        self.valor = valor
    
    def __str__(self) -> str:
        return str(self.valor)

class Matriz:
    def __init__(self, linhas: int, colunas: int) -> None:
        self.linhas = linhas
        self.colunas = colunas
        self.elementos = self.__preenche_elementos()

    E = TypeVar('E', bound='Elemento') # Criação de um tipo    

    def tipo_de_matriz(self) -> Optional[str]:
        saida = []
        if self.linhas == self.colunas: # identificar se é uma matriz quadrada
            saida.append("matriz quadrada")
        elif self.linhas == 1: # identificar se é uma matriz linha
            saida.append("matriz linha")
        elif self.colunas == 1: # identificar se é uma matriz coluna
            saida.append("matriz coluna") 
        if self.__eh_uma_matriz_nula() == True: # identificar se é uma matriz contendo apenas elementos nulos
            saida.append("matriz nula")
        
        if len(saida) == 0:
            return None
        else:
            return ", ".join(saida)

    def eh_uma_matriz_identidade(self) -> bool:
        tipo_de_matriz = self.tipo_de_matriz().split(',')[0]
        if tipo_de_matriz == "matriz quadrada":
            return True        

    def __eh_uma_matriz_nula(self) -> bool:
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.elementos[i][j].valor != 0:
                    return False
        return True 

    def __preenche_elementos(self) -> List[List[E]]: 
        elementos = []
        for i in range(self.linhas):
            elementos.append([])
            for j in range(self.colunas):
                elementos[i].append(Elemento(i, j, 0))
        return elementos

    def __str__(self) -> str:
        saida = []
        for i in range(self.linhas):
            saida.append([])
            for j in range(self.colunas):
                saida[i].append(self.elementos[i][j].valor)
        return str(saida)

matriz = Matriz(2, 2) # [[0, 0], [0, 0], [0, 0]] 
print(matriz)
matriz.elementos[0][0].valor = 2
print(matriz)
print(matriz.tipo_de_matriz())
print(matriz.eh_uma_matriz_identidade())