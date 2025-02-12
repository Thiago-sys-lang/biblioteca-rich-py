# personalizador/estilo.py
from rich.console import Console # type: ignore

def formatar(texto, isArquivo):
    console = Console()
    if isArquivo:
        with open(texto, "r") as file:
            texto = file.read()
    console.print(texto, style="italic")

def realcar(texto, isArquivo):
    console = Console()
    if isArquivo:
        with open(texto, "r") as file:
            texto = file.read()
    console.print(texto, style="reverse")
