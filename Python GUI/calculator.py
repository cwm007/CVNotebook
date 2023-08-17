"""
利用表格工具实现计算器页面设计
"""
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.grid()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        btnText = [
            ['MC', 'M+', 'M-', 'MR'],
            ['C', '±', '÷', '×'],
            [7,8,9,'-'],
            [4,5,6,'+'],
            [1,2,3,"="],
            [0,"."]
        ]
        tk.Entry().grid(row=0,column=0,columnspan=4, sticky=tk.E, padx=20, pady=10)
        for i, row in enumerate(btnText):
            for j, c in enumerate(row):
                if c == '=':
                    tk.Button(text=c, width=2).grid(row=i+1,column=j, rowspan=2)
                elif c == '.':
                    tk.Button(text=c, width=2).grid(row=i + 1, column=j+1)
                elif c == 0:
                    tk.Button(text=c, width=4).grid(row=i + 1, column=j, columnspan=2)
                else:
                    tk.Button(text=c, width=2).grid(row=i+1, column=j)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('计算器')
    root.geometry("200x250")

    app = Application(master=root)

    root.mainloop()
