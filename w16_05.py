import tkinter as tk

메인창 = tk.Tk()
메인창.title('안녕하세요')

입력 = tk.Entry(메인창)
입력.pack(side=tk.LEFT)

설명창 = tk.Label(메인창, text='안녕하세요 파이썬 윈도우입니다')
설명창.pack(side=tk.LEFT)

버튼 = tk.Button(메인창, text='닫기', command=메인창.destroy)
버튼.pack(side=tk.LEFT)

메인창.mainloop()