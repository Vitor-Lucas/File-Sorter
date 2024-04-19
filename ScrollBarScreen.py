from customtkinter import CTkProgressBar, CTkButton, CTkLabel, CTkToplevel


class ProgressBarScreen(CTkToplevel):
    def __init__(self, title: str, size: int):
        super().__init__()
        self.size = size

        width = 600
        height = 300
        self.configure(width=width, height=height)
        self.resizable(True, True)
        self.title(title)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.focus()
        self.after(2000, lambda: self.focus())

        self.progressBar = CTkProgressBar(self, orientation='horizontal', width=375, height=22)
        self.progressBar.place(x=5, y=height/4)
        self.progressBar.configure(progress_color='#3D9140')
        self.progressBar.grid(row=1, column=0, sticky="ew", columnspan=2)

        self.progressCount = 0
        self.progressBar.set(self.progressCount)

    def increase(self):
        self.progressCount += float(1/self.size)
        if self.check_ended():
            self.destroy()
        else:
            self.progressBar.set(self.progressCount)
        self.update()

    def check_ended(self):
        return self.progressCount >= 1 or self.progressCount >= 1-(1/self.size)


if __name__ == '__main__':
    pg = ProgressBarScreen('Teste', 10)
    pg.bind("<Button-1>", lambda event: pg.increase())
    pg.mainloop()
