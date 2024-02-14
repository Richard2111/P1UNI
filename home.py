import flet as ft
from flet import *


def main(page):

        page.title = "Pagina Principal"
    def propieb(e):
        propieb = ft.ElevatedButton("Propietario")
        page.add(propieb)
        t = ft.Text(value="Hello, world!", color="green")
        page.controls.append(t)
        page.update()

    def adminb(e):
        adminb = ft.ElevatedButton("Administrador")
        page.add(adminb)
        page.update()

    '''
    t = ft.Text(value="La transparencia genera un ambiente de confianza y garantías de sinceridad entre los "
                      "diferentes actores o agentes que administran los bienes de la comunidad.", color="green")
    page.controls.append(t)
    '''


ft.app(target=main)
