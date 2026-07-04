# calculos.py





import tkinter  as tk
import calculos as cl



def run_imc():
    peso_ = float(peso.get() )
    altura_ = float(altura.get())
    resultado = cl.imc(peso_, altura_)
    r  =  round(resultado, 2)
    return mostrar_imc.config(text = r) 




janela  = tk.Tk()
janela.geometry('500x500')



tk.Label(janela, text =  'SISTEMA DE CALCULOS', font=('arial', 15)).pack(pady=20)


tk.Label(janela, text =  'Peso', font=('arial', 15)).pack(pady=20)
peso = tk.Entry(janela,font=('arial', 10))
peso.pack()


tk.Label(janela, text =  'Altura', font=('arial', 15)).pack(pady=20)
altura = tk.Entry(janela,font=('arial', 10))
altura.pack()



bt_imc = tk.Button(janela, text =  'imc', font=('arial', 15), command=run_imc)
bt_imc.pack(pady=20)



mostrar_imc = tk.Label(janela, text = '', font=('arial', 15))
mostrar_imc.pack(pady=20)


janela.mainloop()