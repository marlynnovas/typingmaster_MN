import flet as flet
import random 

def main (page: ft.Page):
    page.title= "Typing Master"

    words_list = [
        "otorrinolaringologo", "electroencefalograma",
        "hipopotomonstrosesquipedaliofobia", "desoxirribonucleico",
        "paralelepipedo", "inconstitucionalidad",
        "esternocleidomastoideo", "anticonstitucional",
        "electrodomestico", "circunferencia",
        "desafortunadamente", "extraordinario",
        "incomprensible", "psicologia",
        "responsabilidad"
    ]

    total = 15

    words = []
    index = 0
    mistakes = 0

    word_label = ft.Text(size=25)
    status_label = ft.Text()
    progress_label = ft.Text()
    accuracy_label = ft.Text()
    input_box = ft.TextField()