import tkinter as tk

메인창 = tk.Tk()
메인창.title('계산기')

입력1 = tk.Entry(메인창, width=10)
입력1.pack(side=tk.LEFT)

연산자 = tk.Label(메인창, text='+')
연산자.pack(side=tk.LEFT)

입력2 = tk.Entry(메인창, width=10)
입력2.pack(side=tk.LEFT)

계산 = tk.Button(메인창, text='계산')
계산.pack(side=tk.LEFT)

결과 = tk.Label(메인창, text='결과: ', width=20, anchor='w')
결과.pack(side=tk.LEFT)

메인창.mainloop()
