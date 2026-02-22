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

    def start_game():
        nonlocal words, index, mistakes
        words = words_list.copy()
        random.shuffle(words)
        index = 0
        mistakes = 0

        word_label.value = words[index]
        status_label.value = ""
        accuracy_label.value = ""
        progress_label.value = f"0/{total}"
        input_box.value = ""
        input_box.disabled = False
        page.update()

    def check_word(e):
        nonlocal index, mistakes

        if input_box.value == words[index]:
            status_label.value = "Correcto"
            status_label.color = "green"
        else:
            status_label.value = "Incorrecto"
            status_label.color = "red"
            mistakes += 1

        index += 1
        input_box.value = ""

        if index < total:
            word_label.value = words[index]
            progress_label.value = f"{index}/{total}"
        else:
            word_label.value = "Terminado"
            accuracy = round((total - mistakes) / total * 100, 2)
            accuracy_label.value = f"Precisión: {accuracy}%"
            input_box.disabled = True

        page.update()
        
    start_button = ft.ElevatedButton("Reiniciar", on_click=lambda e: start_game())
    submit_button = ft.ElevatedButton("Enviar", on_click=check_word)

    page.add(
        word_label,
        input_box,
        submit_button,
        start_button,
        status_label,
        progress_label,
        accuracy_label
    )

    start_game()
ft.app(target=main)