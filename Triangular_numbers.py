from tkinter import *			
from tkinter.ttk import Combobox
from tkinter import messagebox  
from tkinter import Canvas      
import Library_of_defasification_functions                 
from pathlib import *          

class ToolTip(object):                      #Всплывающая подсказка (Tooltip)    

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):                #Показать подсказку (Show hint)
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):             #Создаем всплывающую подсказку (Create a tooltip)
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def callbackFunc3(event):                   #Включаем уровень значимости Alfa (Turning on the significance level of Alfa)
    if combo4.get() == "Для метода 'Адамо'":
        txt = Entry(window,width=23, textvariable=Alfa) 
        txt.grid(column=2, row=4)
    else:
        txt = Entry(window,width=23, textvariable=Alfa, state='disabled') 
        txt.grid(column=2, row=4)

def View_check(a, b, c, A, B, C):           #Проверка чисел (Checking numbers)
    I=0
    if a>=b or a>=c or b>=c:
        messagebox.showerror('Ошибка', 'Левое треугольное число не является нечетким.\nЧисла должны располагаться по возрастанию.')
        I+=1

    if A>=B or A>=C or B>=C:
        messagebox.showerror('Ошибка', 'Правое треугольное число не является нечетким.\nЧисла должны располагаться по возрастанию.')
        I+=1
    return I
def Checking_skip(a, b, c, A, B, C):        #Проверка на пропуски чисел (Checking for missing numbers)
    i=0
    if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(A) == 0 or len(B) == 0 or len(C) == 0:
        messagebox.showerror('Ошибка', 'Пропуск числа.')
        i+=1
    if combo3.get() == "Адамо":
        alfa=Alfa.get()
        if len(alfa) == 0:
            messagebox.showerror('Ошибка', 'Пропуск числа Alfa у для метода Адамо.')
            i+=1
        else:
            alfa=float(Alfa.get())
            if alfa<=0 or alfa>1:
               messagebox.showerror('Ошибка', 'Уровень значимости Alfa должно быть > 0 и <= 1.')
               i+=1
    if combo4.get() == "Ур. значимости \u03B1" and len(Alfa.get()) != 0 and combo3.get() == "Адамо":
        messagebox.showerror('Ошибка', 'Активируйте строку с числом Alfa для метода Адамо.')
        i+=1
    return i

def callbackFunc2(event):                   #Методы (Methods)

    if combo3.get() == "Адамо":             #Создаем всплывающую подсказку для каждого метода (Create a tooltip for each method)
        CreateToolTip(combo3, text = 'Ранжирование происходит с помощью сравнения только правых концов альфа срезов, для определенного значения альфа.\nАльфа (α) при этом является мерой риска неправильного решения, т. е. чем больше альфа, тем меньше риск неправильного решения.')
    elif combo3.get() == "Центр максимумов":
        CreateToolTip(combo3, text = 'Центр максимумов нечеткого числа вычисляется как среднее значение конечных точек модальных интервалов (максимальных значений принадлежности)')
    elif combo3.get() == "Центра масс":
        CreateToolTip(combo3, text = 'Выделяет значение, которое является центром масс нечеткого множества.')
    elif combo3.get() == "Медианы":
        CreateToolTip(combo3, text = 'Находит центр области нечеткого числа, деля кривую функции принадлежности на две равные части.')
    elif combo3.get() == "Индекс Чанга":
        CreateToolTip(combo3, text = 'Метод основан на предложенном Чангам индексе.')
    elif combo3.get() == "Возможное среднее":
        CreateToolTip(combo3, text = 'Средневзвешенное значение средних точек альфа разрезов нечеткого числа.')
    elif combo3.get() == "Индекс Ягера":
        CreateToolTip(combo3, text = 'Этот индекс можно рассмотреть, как обобщение метода ранжирования на основе центра тяжести.')
    elif combo3.get() == "USt1":
        CreateToolTip(combo3, text = 'Ухоботов В.И., Стабулит И.С., Кудрявцев К.Н.\nСравнение нечетких чисел треугольного вида, Вестник Удмуртского университета.\nМатематика. Механика. Компьютерные науки, 2019, т. 29, вып. 2, с. 197-210')
    elif combo3.get() == "USt2":
        CreateToolTip(combo3, text = 'Ухоботов В.И., Стабулит И.С., Кудрявцев К.Н.\nСравнение нечетких чисел треугольного вида, Вестник Удмуртского университета.\nМатематика. Механика. Компьютерные науки, 2019, т. 29, вып. 2, с. 197-210')
    elif combo3.get() == "USt3":
        CreateToolTip(combo3, text = 'Conference Paper On the Issue of Comparison of Fuzzy Numbers\nUkhobotov, V., Stabulit, I., Kudryavtsev, K.\nCommunications in Computer and Information Science, 2019, 1090 CCIS, page 590–603')
    elif combo3.get() == "USt4":
        CreateToolTip(combo3, text = 'Conference Paper On the Issue of Comparison of Fuzzy Numbers\nUkhobotov, V., Stabulit, I., Kudryavtsev, K.\nCommunications in Computer and Information Science, 2019, 1090 CCIS, page 590–603')
    else:
        CreateToolTip(combo3, text = '')

    i=Checking_skip(name.get(),name1.get(),name2.get(),Name.get(),Name1.get(),Name2.get())
    if (i==0):                              #Все правильно (Everything is correct)
        a=float(name.get())
        b=float(name1.get())
        c=float(name2.get())

        A=float(Name.get())
        B=float(Name1.get())
        C=float(Name2.get())

        I=View_check(a, b, c, A, B, C)
        if I==0:                            #Все правильно (Everything is correct)
            if combo3.get() == "Метод сравнения":         
                messagebox.showerror('Ошибка', 'Выберите метод.')
            else:
                if combo3.get() == "Адамо":               ##Метод Адамо (Adamo method) 
                    alfa=float(Alfa.get())
                    o, O = Library_of_defasification_functions.Adamo(a, b, c, A, B, C, alfa)

                elif combo3.get() == "Центр максимумов":  #Метод центра максимумов (Center maxima method)
                    o, O = Library_of_defasification_functions.CofMax(a, b, c, A, B, C)

                elif combo3.get() == "Центра масс":       #Метод Центра масс (Center of Mass Method)
                    o, O = Library_of_defasification_functions.CofMass(a, b, c, A, B, C)

                elif combo3.get() == "Медианы":           #Метод Медианы (Median Method)
                    o, O = Library_of_defasification_functions.Medians(a, b, c, A, B, C)

                elif combo3.get() == "Индекс Чанга":      #Метод - индекс Чанга (Method - Chang Index)
                    o, O = Library_of_defasification_functions.Chang(a, b, c, A, B, C)
                        
                elif combo3.get() == "Возможное среднее": #Метод - возможное среднее (Method - Possible Average)
                    o, O = Library_of_defasification_functions.PAv(a, b, c, A, B, C)

                elif combo3.get() == "Индекс Ягера":      #Метод - индекс Ягера (Method - Yager index)
                    o, O = Library_of_defasification_functions.Jager(a, b, c, A, B, C)

                elif combo3.get() == "USt1":              #Метод - USt1 (Method - USt1)
                    o, O = Library_of_defasification_functions.USt1(a, b, c, A, B, C)

                elif combo3.get() == "USt2":              #Метод - USt2 (Method - USt2) 
                    o, O, myA = Library_of_defasification_functions.USt2(a, b, c, A, B, C)

                elif combo3.get() == "USt3":              #Метод - USt3 (Method - USt3) 
                    o, O = Library_of_defasification_functions.Medians(a, b, c, A, B, C)

                elif combo3.get() == "USt4":              #Метод - USt4 (Method - USt4) 
                    o, O, dAB, dBA = Library_of_defasification_functions.USt4(a, b, c, A, B, C)

                window1 = Tk()				              #Отображение результата (Displaying the result)
                window1.title("Результат")  
                window1.geometry('390x200')
                window1.iconbitmap(Path.cwd() / '1.ico')  

                if o<O:
                    lbl = Label(window1, text="Правое число больше")	
                    lbl.grid(column=2, row=7)
                elif o>O:
                    lbl = Label(window1, text="Левое число больше")	
                    lbl.grid(column=2, row=7)
                else:
                    lbl = Label(window1, text="Числа равны")	
                    lbl.grid(column=2, row=7)

                lbl = Label(window1, text=combo3.get())               
                lbl.grid(column=2, row=0)

                lbl = Label(window1, text="Треугольная форма числа")   
                lbl.grid(column=1, row=1)

                lbl = Label(window1, text="Треугольная форма числа")   
                lbl.grid(column=3, row=1)

                lbl = Label(window1, text=a)                           
                lbl.grid(column=1, row=2)
                lbl = Label(window1, text=b)
                lbl.grid(column=1, row=3)
                lbl = Label(window1, text=c)
                lbl.grid(column=1, row=4)
                lbl = Label(window1, text=A, fg="Blue")
                lbl.grid(column=3, row=2)
                lbl = Label(window1, text=B, fg="Blue")
                lbl.grid(column=3, row=3)
                lbl = Label(window1, text=C, fg="Blue")
                lbl.grid(column=3, row=4)

                lbl = Label(window1, text="Результат")
                lbl.grid(column=2, row=6)

                if combo3.get() == "USt2":
                    if  myA == 777:
                        lbl = Label(window1, text="d(A>=B) не считалось")   
                        lbl.grid(column=1, row=8)
                        lbl = Label(window1, text="d(B>=A) не считалось")
                        lbl.grid(column=3, row=8)
                    else:
                        lbl = Label(window1, text=myA)                      
                        lbl.grid(column=1, row=8)
                        lbl = Label(window1, text="d(A>=B)")              
                        lbl.grid(column=1, row=9)
                        lbl = Label(window1, text=1-myA)
                        lbl.grid(column=3, row=8)
                        lbl = Label(window1, text="d(B>=A)") 
                        lbl.grid(column=3, row=9)
                elif combo3.get() == "USt4":
                    lbl = Label(window1, text=dAB)                         
                    lbl.grid(column=1, row=8)
                    lbl = Label(window1, text="d(A>=B)")    
                    lbl.grid(column=1, row=9)
                    lbl = Label(window1, text=dBA)
                    lbl.grid(column=3, row=8)
                    lbl = Label(window1, text="d(B>=A)") 
                    lbl.grid(column=3, row=9)
                else:
                    lbl = Label(window1, text=o)                            
                    lbl.grid(column=1, row=8)
                    lbl = Label(window1, text=O, fg="Blue")
                    lbl.grid(column=3, row=8)
def clicked():                              #Рисуем (Draw)
    i=0
    i=Checking_skip(name.get(),name1.get(),name2.get(),Name.get(),Name1.get(),Name2.get())
    if (i==0):
        root = Tk()                                                     
        root.title("Графическое отображение")
        root.iconbitmap(Path.cwd() / '4.ico')                          

        c = Canvas(root, width=470, height=300, bg='white')             
        c.pack()                                                      
        c.create_line(name.get(), 85, name2.get(), 85, name1.get(), 10, name.get(), 85)
        c.create_line(Name.get(), 85, Name2.get(), 85, Name1.get(), 10, Name.get(), 85, fill='Blue') 
    
#Начало программы (Start of the program)
window = Tk()				           
window.title("Сравнение нечетких чисел")  
window.geometry('477x157')
window.iconbitmap(Path.cwd() / '2.ico') 

name = StringVar()                      
name1 = StringVar()
name2 = StringVar()
name3 = StringVar()

Name = StringVar()
Name1 = StringVar()
Name2 = StringVar()
Name3 = StringVar()

Alfa = StringVar()

lbl = Label(window, text="Треугольная форма числа")                      
lbl.grid(column=1, row=0)

lbl = Label(window, text="Треугольная форма числа")                      
lbl.grid(column=4, row=0)

lbl = Label(window, text="A")                        
lbl.grid(column=0, row=1)             

txt = Entry(window,width=23, textvariable=name)        
txt.grid(column=1, row=1)

lbl = Label(window, text="B") 
lbl.grid(column=0, row=2)

txt = Entry(window,width=23, textvariable=name1)  
txt.grid(column=1, row=2)

lbl = Label(window, text="C")
lbl.grid(column=0, row=3)

txt = Entry(window,width=23, textvariable=name2)
txt.grid(column=1, row=3)		

lbl = Label(window, text="A") 
lbl.grid(column=3, row=1)

txt = Entry(window,width=23, textvariable=Name, fg="Blue")
txt.grid(column=4, row=1)	

lbl = Label(window, text="B") 
lbl.grid(column=3, row=2)

txt = Entry(window,width=23, textvariable=Name1, fg="Blue") 
txt.grid(column=4, row=2)	

lbl = Label(window, text="C")  
lbl.grid(column=3, row=3)

txt = Entry(window,width=23, textvariable=Name2, fg="Blue")
txt.grid(column=4, row=3)	

combo4 = Combobox(window)
combo4['values'] = ("Ур. значимости \u03B1", "Для метода 'Адамо'")  
combo4.current(0)			
combo4.grid(column=1, row=4)
combo4.bind("<<ComboboxSelected>>", callbackFunc3)

txt = Entry(window,width=23, textvariable=Alfa, state='disabled') 
txt.grid(column=2, row=4)

combo3 = Combobox(window)	                                        
combo3['values'] = ("Метод сравнения", "Адамо", "Центр максимумов", "Центра масс", "Медианы", "Индекс Чанга", "Возможное среднее", "Индекс Ягера", "USt1", "USt2", "USt3", "USt4")  
combo3.current(0)			 
combo3.grid(column=2, row=5)
combo3.bind("<<ComboboxSelected>>", callbackFunc2)

btn = Button(window, text="Сравнить", command=clicked)              
btn.grid(column=2, row=6)

window.mainloop()