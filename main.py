from tkinter import *
import math

def tem_cp(t1,t2,t3):
    t=(t3-t2)/(2.3*math.log10((t1-t2)/(t1-t3)))
    return int(t)

def do_power_win(root):
    power_win=Tk()
    power_win.title("Вычисление расхода пара")
    power_win.geometry("400x500+540+300")
    power_win.resizable(False,False)
    def reopen_main():   
        power_win.destroy()
        root.deiconify()

    def power():
        try:
            t2=float(entry_t2.get())
            t3=float(entry_t3.get())
            G=float(entry_G.get())
            i=float(entry_i.get())
            l=float(entry_l.get())
            P=(G*0.94*(t3-t2))/(i-l)/0.8
            otvet = Tk()
            otvet.title("Ответ")
            Label(otvet, text=f"Расход пара на нагрев молока равен: {P}", padx=10, pady=10, font=("Arial", 15)).pack(anchor=CENTER)
            gb = Button(otvet, text="Назад", command=lambda: otvet.destroy())
            gb.pack(anchor=S)
        except:
            Label(power_win,text="Данные введены неверно,\n попробуйте убрать буквы или заменить запятые на точки",foreground="red").grid(row=2,column=0,columnspan=2)

    frame1 = Frame(power_win, padx=5, pady=5)
    frame1.grid(row=0, column=0)
    Label(frame1, text="Начальная темпрература молока", padx=5, pady=5).pack(anchor=E)
    Label(frame1, text="Конечная температура молока", padx=5, pady=5).pack(anchor=E)
    Label(frame1, text="Поизводительность пастеризатора в час", padx=5, pady=5).pack(anchor=E)
    Label(frame1, text="Теплосодержание пара", padx=5, pady=5).pack(anchor=E)
    Label(frame1, text="Теплосодержание конденсата", padx=5, pady=5).pack(anchor=E)

    frame2 = Frame(power_win, padx=5, pady=5)
    frame2.grid(row=0, column=1)
    entry_t2 = Entry(frame2)
    entry_t2.pack(anchor=W, padx=5, pady=5)
    entry_t3 = Entry(frame2)
    entry_t3.pack(anchor=W, padx=5, pady=5)
    entry_G = Entry(frame2)
    entry_G.pack(anchor=W, padx=5, pady=5)
    entry_i = Entry(frame2)
    entry_i.pack(anchor=W, padx=5, pady=5)
    entry_l=Entry(frame2)
    entry_l.pack(anchor=W, padx=5, pady=5)


    bt = Button(power_win, text="Провести вычисления", command=power)
    bt.grid(row=1, column=1)
    go_back_button = Button(power_win, text="Назад", command=reopen_main)
    go_back_button.grid(row=1, column=0, stick=EW, padx=5)
    root.withdraw()

def do_koef_win(root):
    koef_win=Tk()
    koef_win.title("Вычисление коэфициента")
    koef_win.geometry("350x500+540+300")
    koef_win.resizable(False,False)

    def koef():
        try:
            t1 = float(entry_t1.get())
            t2 = float(entry_t2.get())
            t3 = float(entry_t3.get())
            G = float(entry_G.get())
            T = float(entry_T.get())
            F = float(entry_F.get())
            t = tem_cp(t1, t2, t3)
            K = (0.94 * G * (t3 - t2)) / (F * t * T)

            otvet = Tk()
            otvet.title("Ответ")
            Label(otvet, text=f"Коефициент равен: {K}", padx=10, pady=10, font=("Arial", 15)).pack(anchor=CENTER)
            gb = Button(otvet,text="Назад", command=lambda: otvet.destroy())
            gb.pack(anchor=S)
        except:
            Label(koef_win,text="Данные введены неверно,\n попробуйте убрать буквы или заменить запятые на точки",foreground="red").grid(row=2,column=0,columnspan=2)

    def reopen_main():
        koef_win.destroy()
        root.deiconify()
    frame1=Frame(koef_win,padx=5,pady=5)
    frame1.grid(row=0,column=0)
    Label(frame1,text="Температура пара",padx=5,pady=5).pack(anchor=E)
    Label(frame1,text="Начальная темпрература молока",padx=5,pady=5).pack(anchor=E)
    Label(frame1,text="Конечная температура молока",padx=5,pady=5).pack(anchor=E)
    Label(frame1,text="Колисество молока",padx=5,pady=5).pack(anchor=E)
    Label(frame1,text="Площадь нагрева",padx=5,pady=5).pack(anchor=E)
    Label(frame1,text="Время нагрева",padx=5,pady=5).pack(anchor=E)

    frame2=Frame(koef_win,padx=5,pady=5)
    frame2.grid(row=0,column=1)
    entry_t1=Entry(frame2)
    entry_t1.pack(anchor=W,padx=5,pady=5)
    entry_t2=Entry(frame2)
    entry_t2.pack(anchor=W,padx=5,pady=5)
    entry_t3=Entry(frame2)
    entry_t3.pack(anchor=W,padx=5,pady=5)
    entry_G=Entry(frame2)
    entry_G.pack(anchor=W,padx=5,pady=5)
    entry_F=Entry(frame2)
    entry_F.pack(anchor=W,padx=5,pady=5)
    entry_T=Entry(frame2)
    entry_T.pack(anchor=W,padx=5,pady=5)

    bt=Button(koef_win,text="Провести вычисления",command=koef)
    bt.grid(row=1,column=1)
    go_back_button=Button(koef_win,text="Назад",command=reopen_main)
    go_back_button.grid(row=1,column=0,stick=EW,padx=5)
    root.withdraw()




root = Tk()
root.title("Вычисление")
root.geometry("350x500+540+300")
root.resizable(False,False)

bt1=Button(root,text="Посчитать коефициент",command=lambda : do_koef_win(root))
bt1.grid(row=0,column=0,rowspan=4, ipadx=10, ipady=100, padx=10, pady=25)
bt2=Button(root,text="Посчитать мощность",command=lambda : do_power_win(root))
bt2.grid(row=0,column=1,rowspan=5, ipadx=10, ipady=100, padx=10, pady=25)



root.mainloop()
