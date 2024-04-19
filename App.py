from customtkinter import CTk, CTkButton, CTkLabel, CTkInputDialog
from tkinter import filedialog
from ScrollBarScreen import ProgressBarScreen
import MessageBox
import os


class App(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('400x300')
        self.resizable(False, False)
        self.input_path = ''
        self.output_path = ''

        self.input_Button = CTkButton(self, text="Pasta para ser organizada", command=self.get_input_path)
        self.input_Button.pack()

        self.input_Label = CTkLabel(self, text=self.input_path)
        self.input_Label.pack()

        self.output_Button = CTkButton(self, text="Pasta para ficar os arquivos organizados",
                                       command=self.get_output_path)
        self.output_Button.pack()

        self.output_Label = CTkLabel(self, text=self.input_path)
        self.output_Label.pack()

        self.organize_Button = CTkButton(self, text='Organizar', command=self.prepare_organization)
        self.organize_Button.pack()

    def prepare_organization(self):
        year_range = CTkInputDialog(text="Digite de que ano até que ano você gostaria que as pastas fossem criadas:\n"
                                         "Ex: 1990 - 2024",
                                    title="Range de arquivos")
        separated_years = year_range.get_input().split('-')
        start_year = int(separated_years[0].strip())
        end_year = int(separated_years[1].strip())
        print(f'Start year: {start_year}')
        print(f'End year: {end_year}')
        #TODO acabar a barra de progresso
        progressBar = ProgressBarScreen()
        self.create_year_and_months_dirs(start_year, end_year)
        MessageBox.show_success(message='Pastas dos anos e meses criados com sucesso!')
        # TODO criar uma função que pega a data de criação de um arquivo

    def organize(self):  # TODO acabar essa função
        pass

    def create_year_and_months_dirs(self, start, end):
        for year in range(start, end + 1):
            year_path = str(year)
            self.create_dir(year_path)

            # creates each month's dir inside the year dir
            months = [_ for _ in range(1, 13)]
            for month in months:
                self.create_dir(os.path.join(year_path, str(month)))

    def create_dir(self, path):
        full_path = os.path.join(self.output_path, path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Directory '{full_path}' created successfully.")
        else:
            print(f"Directory '{full_path}' already exists.")

    def get_input_path(self):
        self.input_path = filedialog.askdirectory()
        text = 'Pasta a ser organizada: ' + self.input_path
        self.input_Label.configure(text=text)
        print(f'Input path: {self.input_path}')

    def get_output_path(self):
        self.output_path = filedialog.askdirectory()
        text = 'Pasta final: ' + self.output_path
        self.output_Label.configure(text=text)
        print(f'Input path: {self.output_path}')
