import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=20)
        self.create_widgets()
        self.image_path = ""

    def create_widgets(self):
        self.winfo_toplevel().title("Watermarking app")

        self.file = tk.Button(self, text="Select the image file", command=self.select_file)
        self.file.grid(row=0, column=0, columnspan=2)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=3, column=0, columnspan=2)

    def select_file(self):
        self.image_path = filedialog.askopenfilename()

        if len(self.image_path) > 0:
            print(self.image_path)

            tk.Label(self, text="Enter your watermark").grid(row=2, column=0)
            self.user_watermark = tk.Entry(self)
            self.user_watermark.grid(row=2, column=1)
            tk.Button(self, text="OK", command=self.add_watermark).grid(row=2, column=2)

    def add_watermark(self):
        self.image = Image.open(self.image_path)
        print(self.image)
        width, height = self.image.size
        watermark = self.user_watermark.get()

        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(watermark, font)
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), watermark, font=font)
        self.image.show()

        tk.Button(self, text="Download the file", fg="blue",
                  command=self.save_file).grid(row=1, column=0, pady=2, columnspan=2, padx=2)

    def save_file(self):
        self.image.save(f"{self.image_path.rsplit('/', 1)[0]}/watermark.jpg")
        tk.Label(self, text="Saved the file in the same directory as the original one").grid(row=4, column=0, columnspan=2)


root = tk.Tk()
root.minsize(350, 300)
app = Application(master=root)
app.mainloop()
