import tkinter as tk

class MyWindow:
    def __init__(self, title="My Window"):
        self.window = tk.Tk()
        self.window.title(title)

        self.label = tk.Label(self.window, text="Hello, World! Vinay Here")
        self.label.pack(pady=20)

        self.button = tk.Button(self.window, text="Close", command=self.close_window)
        self.button.pack(pady=10)

    def close_window(self):
        self.window.destroy()

    def show(self):
        self.window.mainloop()

if __name__ == "__main__":
    my_window = MyWindow("Simple UI Example")
    my_window.show()