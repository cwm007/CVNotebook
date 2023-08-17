import tkinter as tk
import tkinter.filedialog as tkf
import tkinter.colorchooser as tkc
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        # 创建主菜单栏
        menubar = tk.Menu(self.master)

        # 创建子菜单
        menuFile = tk.Menu(menubar)
        menuEdit = tk.Menu(menubar)
        menuHelp = tk.Menu(menubar)

        # 将子菜单加入到主菜单栏中
        menubar.add_cascade(label='文件', menu=menuFile)
        menubar.add_cascade(label='编辑', menu=menuEdit)
        menubar.add_cascade(label='帮助', menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label='新建', accelerator='ctrl+n', command=self.newFile)
        menuFile.add_command(label='打开', accelerator='ctrl+o', command=self.openFile)
        menuFile.add_command(label='保存', accelerator='ctrl+s', command=self.saveFile)
        menuFile.add_separator()
        menuFile.add_command(label='退出', accelerator='ctrl+q', command=self.exit)

        # 将主菜单栏添加到根窗口
        self.master['menu'] = menubar

        # 增加文本编辑区
        self.text = tk.Text(self.master, width=500, height=400)
        self.text.pack()

        # 创建子菜单
        self.contextMenu = tk.Menu(self.master)
        self.contextMenu.add_command(label='背景颜色', command=self.changeColor)

        self.master.bind("<Button-3>", self.createContextMenu)

        # 增加快捷键的处理
        self.master.bind('<Control-n>', lambda event:self.newFile())
        self.master.bind('<Control-o>', lambda event:self.openFile())
        self.master.bind('<Control-s>', lambda event:self.saveFile())
        self.master.bind('<Control-q>', lambda event:self.quit())

    def test(self):
        pass

    def createContextMenu(self, event):
        self.contextMenu.post(event.x, event.y)

    def openFile(self):
        self.text.delete(1.0, tk.END)
        with tkf.askopenfile(title='打开文本文件') as f:
            self.text.insert(tk.INSERT, f.read())
            self.filename = f.name

    def saveFile(self):
        c = self.text.get(1.0, tk.END)
        with open(self.filename, 'w') as f:
            f.write(c)

    def exit(self):
        self.master.quit()

    def newFile(self):
        tkf.asksaveasfile(title='另存为', initialfile='未命名.txt', filetypes=[("文本文档", '.txt')], defaultextension='.txt')
        self.saveFile()

    def changeColor(self):
        c = tkc.askcolor(color='red', title='选择背景色')
        self.text.config(bg=c[1])


if __name__ == '__main__':
    root = tk.Tk()
    root.title('菜单栏')
    root.geometry('500x400')

    app = Application(root)

    root.mainloop()
