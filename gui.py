import tkinter as tk
import threading


class DrawBoard(tk.Frame):
    def __init__(self):
        super().__init__()
        self.initiateUI()

    def initiateUI(self):
        self.master.title("DATE UI")
        self.pack(fill=tk.BOTH, expand=1)

    def createBox(self, canvas, x, y, w, h, color, message):
        canvas.create_rectangle(x, y, w, h, outline=color, fill=color)
        canvas.create_text((x + w) / 2, y + (h / 2), text=message)


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        canvas = tk.Canvas()
        self.root.geometry("400x100+300+300")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        drawBoard = DrawBoard()
        drawBoard.createBox(canvas, 30, 10, 120, 80, '#fb0', 'Call Doctor')
        drawBoard.createBox(canvas, 150, 10, 240, 80, '#f50', 'Adjust bed')
        drawBoard.createBox(canvas, 270, 10, 370, 80, '#05f', 'Play Music')
        canvas.pack(fill=tk.BOTH, expand=1)
        self.root.mainloop()


app = App()