import tkinter as tk

메인창 = tk.Tk()
메인창.title('안녕하세요')

버튼 = tk.Button(메인창, text='버튼입니다')
버튼.pack()

메인창.mainloop()