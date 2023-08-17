"""
利用place设计扑克牌游戏界面
"""
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.photos = [tk.PhotoImage(file='poke_images/%s.gif' % f) for f in range(1, 11)]
        self.labels = [tk.Label(self.master, image=f, width=200, height=300) for f in self.photos]
        for i in range(len(self.labels)):
            self.labels[i].place(x=20 + 80 * i, y=50)

        # 为所有label增加事件处理
        self.labels[0].bind_class('Label', "<Button-1>", self.chupai)

    def chupai(self, event):
        # 获取坐标信息
        print(event.widget.winfo_geometry())
        if event.widget.winfo_y() > 30:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('扑克牌')
    root.geometry("1000x400")

    app = Application(root)

    root.mainloop()
