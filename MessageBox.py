from CTkMessagebox import CTkMessagebox
from customtkinter import CTkInputDialog

def show_info(title: str, message: str):
    msg = CTkMessagebox(title=title, message=message)
    return msg.get()


def show_error(title: str, message: str):
    CTkMessagebox(title=title, message=message, icon="cancel", option_1='Continuar')


def show_success(message: str):
    msg = CTkMessagebox(title='Sucesso', message=message, icon="check", option_1="Continuar")
    return msg.get()


def show_warning(title: str, message: str, **kwargs):
    msg = CTkMessagebox(title=title, message=message,
                        icon="warning", **kwargs)
    return msg.get()


def ask_question(title: str, question: str, **options):
    msg = CTkMessagebox(title=title, message=question,
                        icon="question", **options)
    return msg.get()
