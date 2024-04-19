from customtkinter import CTk, CTkButton, CTkLabel, CTkInputDialog
from tkinter import filedialog
from ProgressBarScreen import ProgressBarScreen
import file_processing
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

        self.output_Label = CTkLabel(self, text=self.output_path)
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

        self.create_year_and_months_dirs(start_year, end_year)
        MessageBox.show_success(message='Pastas dos anos e meses criados com sucesso!')
        self.organize()

    def organize(self):  # TODO adicionar as extensões certas
        allowed_extensions = []
        for file_path in file_processing.get_all_file_paths(self.input_path, allowed_extensions):
            print(f'Arquivo {file_path} sendo processado')

            date = file_processing.get_creation_date(file_path)
            _, month, year = date.split('/')
            print(file_path.split('\\')[-1])
            new_path = os.path.join(self.output_path, str(year), str(month), file_path.split('\\')[-1])
            print('Foi do caminho : ' + file_path)
            print('Pro caminho: ' + new_path)
            file_processing.rename_file(file_path, new_path)

        file_processing.delete_empty_dirs(self.output_path)

    def create_year_and_months_dirs(self, start, end):
        progressBar = ProgressBarScreen(title='Criando arquivos', size=(end - start) * 12)
        for year in range(start, end + 1):
            year_path = str(year)
            file_processing.create_dir(self.output_path, year_path)

            # creates each month's dir inside the year dir
            months = [str(i).zfill(2) for i in range(1, 13)]
            for month in months:
                file_processing.create_dir(self.output_path, os.path.join(year_path, month))
                progressBar.increase()
        print('Pastas criadas com sucesso!\n\n\n\n\n')

    def get_input_path(self):
        self.input_path = filedialog.askdirectory()
        text = 'Pasta a ser organizada: ' + self.input_path
        self.input_Label.configure(text=text)
        print(f'Input path: {self.input_path}')

    def get_output_path(self):
        self.output_path = filedialog.askdirectory()
        text = 'Pasta final: ' + self.output_path
        self.output_Label.configure(text=text)
        print(f'Output path: {self.output_path}')

