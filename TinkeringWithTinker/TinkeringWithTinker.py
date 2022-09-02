import tkinter as tk
from wsgiref import validate

def main():
    window = App()
    window.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Math")

        self.gen_ui()

    def gen_ui(self):
        topFrame = tk.Frame(master=self)
        # create the input boxes
        vcmd = (self.register(self.validate_number), '%P')
        icmd = (self.register(self.invalid_number), '%P')
        self.numOne = tk.Entry(master=topFrame, width=15, validate="key", validatecommand=vcmd, invalidcommand=icmd)
        self.numTwo = tk.Entry(master=topFrame, width=15, validate="key", validatecommand=vcmd, invalidcommand=icmd)

        self.numOne.grid(row=1, column=0, padx=5, pady=5)
        self.numTwo.grid(row=1, column=1, padx=5, pady=5)

        lblOne = tk.Label(master=topFrame, width=15, text="Num 1")
        lblTwo = tk.Label(master=topFrame, width=15, text="Num 2")

        lblOne.grid(row=0, column=0, padx=5, pady=1)
        lblTwo.grid(row=0, column=1, padx=5, pady=1)

        topFrame.pack(fill=tk.BOTH, side=tk.TOP, padx=20, pady=10)

        btnAdd = tk.Button(text="ADD", background="green", master=topFrame, width=10, foreground="white",
                           command=self.on_add)
        btnMultiply = tk.Button(text="MUL", background="pink", master=topFrame, width=10,
                                command=self.on_mul)

        btnAdd.grid(row=2, column=0, padx=5, pady=10)
        btnMultiply.grid(row=2, column=1, padx=5, pady=10)

        botFrame = tk.Frame(master=self)
        # create the dispaly label

        self.lblOut = tk.Label(text="Result: ", master=botFrame)
        self.lblOut.pack(fill=tk.BOTH, side=tk.TOP)

        botFrame.pack(fill=tk.BOTH, side=tk.TOP, padx=20, pady=10)

    def validate_number(self, val):
        if val == "" or val is None or val == "-":
            return True

        try:
            float(val)
            return True
        except:
            return False

    def invalid_number(self, val):
        # TODO if time
        pass

    def on_add(self):
        one = self.numOne.get()
        two = self.numTwo.get()
        if (one != "" and two != ""):
            self.lblOut["text"] = "ADD Result: {}".format(float(one) + float(two))
            self.numOne["text"] = ""
            self.numTwo["text"] = ""
        else:
            self.lblOut["text"] = "Enter two numbers first!"

    def on_mul(self):
        one = self.numOne.get()
        two = self.numTwo.get()
        if (one != "" and two != ""):
            self.lblOut["text"] = "MUL Result: {}".format(float(one) * float(two))
            self.numOne["text"] = ""
            self.numTwo["text"] = ""
        else:
            self.lblOut["text"] = "Enter two numbers first!"

if __name__ == "__main__":
    main()