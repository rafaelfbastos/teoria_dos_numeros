from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import *
import os

def but_resto(): #função que é chamada ao clicar no botão da aba 1
    #caso valor digitado não for inteiro ou estiver em branco, a função abre messagebox de erro
    try:
        #pegando valores digitados pelos usuarios nos campos da aba 1
        num=entra_dividendo.get()
        den=entra_divisor.get()
        #convertento para inteiro
        num=int(num)
        den=int(den)
        #chamando a função resto
        r_resto=resto(num,den)
        #Fornecendo resposta aos campos da aba 1 
        r_q["text"]=r_resto[0]
        r_r["text"]=r_resto[1]
    except:
        messagebox.showerror("Erro","Digite um número inteiro:")  

def but_converter_base(): #função que é chamada ao clicar no botão da aba 2

  #Chamando a função validar_base e passando como parametro as informações digitadas pelo usuario na aba 2
  condition=validar_base(atual.get(),xnumero.get())
  #pegando valor da base desejada  
  base_desejada=desejada.get()
  
  if condition:
    #chama função conveter_to_10
    base10=converter_to_10(atual.get(),xnumero.get())
    
    if(base_desejada=="10"):
      base_r["text"]=base10
    
    else:
      #chama fução converter_to_n
      y=converter_to_n(base10,base_desejada)
       
      base_r["text"]=y

  else:
    #retorna mensagem no campo resposta da aba 2  
    base_r["text"]="Número não condiz com a base"

def calcular_mdc_bz(): #função que é chamada ao clicar no botão da aba 3
    #Caso valor digitado não seja inteiro a função abre uma menssagebox de erro
    try: 
        dividendo=[]
        divisor=[]
        quociente=[]
        resto=[]
        #pegando valores digitados pelos usuarios na aba 3 convertento em iteiro e absolutos
        a=abs(int(num1.get()))
        b=abs(int(num2.get()))
        
        if(a>b):
            dividendo.append(a)
            divisor.append(b)
            i=0
            q0=int(dividendo[i]/divisor[i])
            #calculando as divisões sucessivas atribuindo as variaveis e tendo i como núnero de divisões significativas
            while(dividendo[i]%divisor[i]!=0):
                resto.append(dividendo[i]%divisor[i])
                quociente.append(int(dividendo[i]/divisor[i]))
                dividendo.append(divisor[i])
                divisor.append(resto[i])
                i+=1
            #Atribuindo resultado no mdc no campo correspontende na aba 3
            mdc["text"]=divisor[i]             
            #chamando função bezout
            rbz=bezout(quociente,int(num1.get()),int(num2.get()),q0,i)
            #Atribuindo os resultado em seus respectivos campos na aba 3
            bez["text"]=str(divisor[i])+" "+"="+" "+"("+str(rbz[0])+")"+"("+ str(num1.get())+")" +" + "+"("+str(rbz[1])+")"+"("+ str(num2.get())+")"
            x0["text"]=rbz[0]
            y0["text"]=rbz[1]
          
        #mesmo algoritimo acima, porém considerando que o modulo do segundo número e maior que o do primeiro   
        elif(a<b):
            dividendo.append(b)
            divisor.append(a)
            i=0
            q0=int(dividendo[i]/divisor[i])
            while(dividendo[i]%divisor[i]!=0):
                resto.append(dividendo[i]%divisor[i])
                quociente.append(int(dividendo[i]/divisor[i]))
                dividendo.append(divisor[i])
                divisor.append(resto[i])
                i+=1
            mdc["text"]=divisor[i]             
            rbz=bezout(quociente,int(num2.get()),int(num1.get()),q0,i)
            bez["text"]=str(divisor[i])+" "+"="+" "+"("+str(rbz[0])+")"+"("+ str(num2.get())+")" +" + "+"("+str(rbz[1])+")"+"("+ str(num1.get())+")"
            x0["text"]=rbz[0]
            y0["text"]=rbz[1]
            
        else: 
            messagebox.showerror("ERROR","Digite números diferentes")
    except:
        messagebox.showerror("ERROR","Digite somente números inteiros")

def btn_primos():#função que é chamada ao clicar no botão da aba 4
    try:
        #resetando a listbox para apagar resultados anteriores
        list_box.delete(0,END)

        lista_de_numeros=[]
        #pegando a quantidade que o usuario informou 
        quantidade=int(p_qtd.get())
        cont=1
        n=0
        
        while n<quantidade:
            #chamando a função que testa se o número é primo
            if(NumeroPrimo(cont)):
                n+=1
                lista_de_numeros.append(str(n)+" º número primo é ---> "+str(cont))
            cont+=1
        for n in lista_de_numeros:
            list_box.insert(END,n)
        if quantidade<0:
            messagebox.showinfo("Número negativo:", "Digite um número inteiro positivo:")           
    except:
        messagebox.showerror("ERRO", "Digite um número inteiro positivo:")

def btn_marsenne():#função que é chamada ao clicar no botão da aba 4
    try:
        list_box.delete(0,END)
        #lista que vai receber os n primeiros numeros primos
        lista=[]
        #lista que vai receber as repostas que serão passadas para a listbox    
        lista_de_numeros=[]
        quantidade=int(p_qtd.get())
        cont=1
        n=0
        while n<quantidade:
            if(NumeroPrimo(cont)):
                n+=1
                lista.append(cont)
            cont+=1
        
        for i,item in enumerate(lista):
            lista_de_numeros.append(str(i+1)+" º"+" número de Marsenne é ---> " + str(2**item-1))
            
        for (n) in lista_de_numeros:
            list_box.insert(END,n)           
        if quantidade<0:
            messagebox.showinfo("Número negativo","Digite um número inteiro positivo:")
    except:
        messagebox.showerror("ERRO","Digite um número inteiro positivo:")

def btn_fermat():#função que é chamada ao clicar no botão da aba 4
    #essa função calcula até os 20 primeiros numeros de Fermat pois as respostas ficam muito grande já que é uma duplamente exponencial
    try:
        n=int(p_qtd.get())
        n1=n
        lista_de_numeros=[]
        list_box.delete(0,END)
        
        if n1<0:
            messagebox.showinfo("Número negativo","Digite um número inteiro positivo:")
        
        elif n1<=20:  
            for i in range(n):
                lista_de_numeros.append(str(1+i)+" º número de Fermat é ---> "+str((2**(2**i))+1))
                
            for (n) in lista_de_numeros:
                list_box.insert(END,n) 
        else:
            messagebox.showwarning("Aviso!","Resposta muito grande, poderá travar seu programa:")

    except:
        messagebox.showerror("ERRO","Digite um número inteiro positivo:")

def btn_verifique():#função que é chamada ao clicar no botão da aba 4
    #chama a função primo e testa se o número digitado pelo usuario é primo
    try:
        pri=int(np_verificar.get())
        
        if pri>0:
        
            if NumeroPrimo(pri):
                rp_verificar["text"]="O número "+ str(pri)+" é primo:"
                    
            else:
                rp_verificar["text"]="O número "+ str(pri)+" não é primo:"
        else: 
           messagebox.showinfo("Número negativo","Digite um número inteiro positivo:") 

    except:
        messagebox.showerror("ERRO","Digite um número inteiro positivo:")

def calc_mmc(): #função que é chamada ao clicar no botão da aba 5    
    try:
        #reseta todas a listbox da aba
        list_fatoracao.delete(0,END)
        list_np.delete(0,END)
        list_disores.delete(0,END)
        #pega os dados inserido pelo usuario e os serara em uma lista - separado é o espaço
        entrada=mmc_entry.get()    
        entrada=entrada.split()
        #identifica quantos números o usuario digitou
        ind=len(entrada)
        r_mdc=[]
        r_mmc=[]
        #chama a funçao mdc e mmc 
        r_mdc.append(f_mdc(int(entrada[0]),int(entrada[1])))
        r_mmc.append(f_mmc(int(entrada[0]),int(entrada[1])))
        n=1
        teorema_potencia=[]
        #Caso for digitado mais de dois números o algoritimo continua calculando os mdc e mmc sempre comparando a resposta anterior com o proximo número        
        while n<(ind-1):
            r_mdc.append(f_mdc(r_mdc[n-1],int(entrada[n+1])))
            r_mmc.append(f_mmc(r_mmc[n-1],int(entrada[n+1])))
            n+=1
        #passa resposta para variavel do Label da ABA 
        resp_mdc["text"]="MDC é = "+str(r_mdc[ind-2])
        resp_mmc["text"]="MMC é = "+str(r_mmc[ind-2])

        #zerando a variael de contagem
        n=0
        #Laço que irá calcular a forma fatorada de cada número digitado
        while n<(ind):
            #criando listas de controles vazias 
            teorema_potencia=[]
            teorema_comp=[]
            teorema_bases=[]        
            #chamando a funçao teorema_aritimetica
            teorema_comp=teorema_aritimetica(int(entrada[n]))
            #usando metodo set() para retornar um conjundo de elementos únicos
            teorema_bases=sorted(set(teorema_comp))
            np=1
            #analizando cada elemento do conjunta das bases e usando metodo .count() para saber quantas vezes essa base se repetiu na lista completa
            for i in teorema_bases:
                teorema_potencia.append(teorema_comp.count(i))

            #colocando sinal de negativo caso o número seja negatico
            if int(entrada[n])>0:
                resposta=str(entrada[n])+" = "
            else:
                resposta=str(entrada[n])+" = - "

            for i in range(len(teorema_bases)):
                #calculando o número de divisores positivos pelo teorema
                np=np*(int(teorema_potencia[i])+1)
                #chamando a função que convete os caracteres em sobrescrito
                portencia_up=potencias_carac(teorema_potencia[i])
                #concatenando os valores a variavel resposta
                resposta=resposta+str(teorema_bases[i])+str(portencia_up)+" ∙ "
            #eliminado os dois ultimos caracteres da resposta
            resposta = resposta[:-2]        
            #Criando a variavel de contre resposta
            r_np="#D₊({}) = {}".format(entrada[n],np)
            #adicionado o resultado da variavel de controle a listbox
            list_np.insert(END,r_np)
            #adicionado a variavel resposta a listbox
            list_fatoracao.insert(END,resposta)
            #criando uma variavel de controle que recebera a lista com todos os divisores - retorno da função divisores
            r_divisores="D({}) = {}".format(entrada[n],divisores(int(entrada[n])))
            #adicionado o resultado da variavel de controle a listbox
            list_disores.insert(END,r_divisores)        
            n+=1
    except:
        messagebox.showerror("ERRO","Digite números inteiros separados por espaços")

def calcular_diofan(): #função que é chamada ao clicar no botão da aba 6
    #primeiro try qua valida a entrada do usuario, caso a returna da função a_b_C_Diofante for "false" exibira mensagem de erro 
    try:
        #chamando a função que trata a entrada do usuario e recebe os coeficientes
        a_b_c=a_b_C_Diofante(diof_entry.get())
        dividendo=[]
        divisor=[]
        quociente=[]
        resto=[]
        #atribuindo valores absolutos para o calculo de bezout
        a=abs(a_b_c[0])
        b=abs(a_b_c[1])
        #calculando o mdc
        mdc_d=f_mdc(a,b)
        #Divisões sucessivas para o calculo de bezout sempre dividindo maior número pelo menor    
        if(a>b):
            dividendo.append(a)
            divisor.append(b)
            i=0
            q0=int(dividendo[i]/divisor[i])
            while(dividendo[i]%divisor[i]!=0):
                resto.append(dividendo[i]%divisor[i])
                quociente.append(int(dividendo[i]/divisor[i]))
                dividendo.append(divisor[i])
                divisor.append(resto[i])
                i+=1
            rbz=bezout(quociente,a_b_c[0],a_b_c[1],q0,i)
           #Parte que identifica se o usuario digitou primeiro a varielvel x ou Y
            if(a_b_c[3]=="xy"):
                d_x0=rbz[0]*(a_b_c[2]/mdc_d)
                d_y0=rbz[1]*(a_b_c[2]/mdc_d)
            else:
                d_y0=rbz[0]*(a_b_c[2]/mdc_d)
                d_x0=rbz[1]*(a_b_c[2]/mdc_d)
                    
        elif(a<b):
            dividendo.append(b)
            divisor.append(a)
            i=0
            q0=int(dividendo[i]/divisor[i])
            while(dividendo[i]%divisor[i]!=0):
                resto.append(dividendo[i]%divisor[i])
                quociente.append(int(dividendo[i]/divisor[i]))
                dividendo.append(divisor[i])
                divisor.append(resto[i])
                i+=1         
            rbz=bezout(quociente,a_b_c[1],a_b_c[0],q0,i)
            if(a_b_c[3]=="xy"):
                d_x0=rbz[1]*(a_b_c[2]/mdc_d)
                d_y0=rbz[0]*(a_b_c[2]/mdc_d)
            else:
                d_y0=rbz[1]*(a_b_c[2]/mdc_d)
                d_x0=rbz[0]*(a_b_c[2]/mdc_d)
        
        #verifição se a equação tem soluções inteira, caso positivo apresentar na janela     
        if(a_b_c[0]%mdc_d==0 and a_b_c[1]%mdc_d==0 and a_b_c[2]%mdc_d==0):
            resp_x0["text"]="X₀ = {}".format(int(d_x0))
            resp_y0["text"]="Y₀ = {}".format(int(d_y0))
            #exibe as equações de todas as possiveis respostas
            if(a_b_c[3]=="xy"):
                resp_ex["text"]="X = {} + ({}) ∙ t".format(int(d_x0),int(a_b_c[1]/mdc_d))
                resp_ey["text"]="Y = {} - ({}) ∙ t".format(int(d_y0),int(a_b_c[0]/mdc_d))
                cxk=a_b_c[1]/mdc_d
                cyk=a_b_c[0]/mdc_d
            else:
                resp_ex["text"]="X = {} + ({}) ∙ t".format(int(d_x0),int(a_b_c[0]/mdc_d))
                resp_ey["text"]="Y = {} - ({}) ∙ t".format(int(d_y0),int(a_b_c[1]/mdc_d))
                cxk=a_b_c[0]/mdc_d
                cyk=a_b_c[1]/mdc_d
            
        else:#caso falso mensagem informando que não existe soluções
            messagebox.showinfo("","Equação não possui solução inteira")
        
        #limpa a listbox 
        list_k.delete(0,END)
        #parque que será executada caso usuario defina um intervalo de t 
        if len(k1_entry.get())==0 and len(k2_entry.get())==0:
           pass
        
        else:
            try:
                #calculando todas as respostas de x e y para "ts" definidos no intervalo e adicionado a listbox
                k1=int(k1_entry.get())
                k2=int(k2_entry.get())
                if k1<=k2:
                   while k1<=k2:
                       xk=d_x0+(cxk*k1)
                       yk=d_y0-(cyk*k1)
                       resp_k="t({})---> X = {}  e  Y = {}".format(int(k1),int(xk),int(yk))
                       list_k.insert(END,resp_k)
                       k1+=1 
                
                else:#messagem caso usuario não digite um intervalo valido
                   messagebox.showerror("ERRO","Digite um intervalo válido:") 
            
            except:
                messagebox.showerror("ERRO","Digite um intervalo válido:")
        
    except:
        messagebox.showerror("ERRO","Digite a equação seguindo o modelo ----> AX+BY=C")
            
#path do caminho do arquivo para adicão da logo e do icone        
caminho=os.path.dirname(__file__)

#abertura da janela pricipal GUI tikinter
app=Tk()

#Titulo da janela
app.title("Teoria dos Números")

#Adicinando icone a janela
ico=PhotoImage(file=caminho+"\\icone.png")
app.iconphoto(False,ico)

#Criando o primeiro quadro a esquerda da janela
fr_l=Frame(app)
fr_l.pack(side=LEFT)



#Colocando os texto do quadro a esquerda

Label(fr_l,text="Indice:",font="Arial 10 bold").pack(pady=(0,5))
Label(fr_l,text="ABA 1 ---> Algoritmo da Divisão: ").pack(pady=5,anchor=W,padx=10)
Label(fr_l,text="ABA 2 ---> Conversor de Base: ").pack(pady=5,anchor=W,padx=10)
Label(fr_l,text="ABA 3 ---> Identidade de Bezout: ").pack(pady=5,anchor=W,padx=10)
Label(fr_l,text="ABA 4 ---> Nº Primo, Marsenne e Fermat: ").pack(pady=5,anchor=W,padx=10)
Label(fr_l,text="ABA 5 ---> MMC e MDC ").pack(pady=5,anchor=W,padx=10)
Label(fr_l,text="ABA 6 ---> Equação Diofantinas ").pack(pady=5,anchor=W,padx=10)

#Criando quadro a direita
fr_2=Frame(app)
fr_2.pack(side=RIGHT)

#Criando um noteboook e colocando no quadro a esquerda
nb=ttk.Notebook(fr_2)
nb.pack(pady=5)

#Criando os as abas e adionando ao notebook  
fr_divisao=Frame(nb)
fr_divisao.pack(fill=BOTH)
nb.add(fr_divisao,text=" ABA 1 ")

fr_conversor=Frame(nb)
nb.add(fr_conversor,text=" ABA 2 ")

fr_mdc_bz=Frame(nb)
nb.add(fr_mdc_bz,text=" ABA 3 ")

fr_primo=Frame(nb)
nb.add(fr_primo,text=" ABA 4 ")

fr_mmc=Frame(nb)
nb.add(fr_mmc,text=" ABA 5")

fr_diof=Frame(nb)
nb.add(fr_diof,text=" ABA 6")

#########   Construindo as ABAS ###########

#-------- aba algoritimo da divisão-----------


l_txt1=Label(fr_divisao,text="Digite o dividendo:")
l_txt1.grid(column=1,row=0,pady=10,sticky="nswe",padx=(50,10))
   
entra_dividendo=Entry(fr_divisao,width="25")
entra_dividendo.grid(column=2,row=0,pady=10,sticky="nswe",padx=10)

l_txt2=Label(fr_divisao,text="Digite o divisor:")
l_txt2.grid(column=1,row=2,pady=10,sticky="nswe",padx=(50,10))

entra_divisor=Entry(fr_divisao)
entra_divisor.grid(column=2,row=2,pady=10,sticky="nswe",padx=10)

calcular_resto=Button(fr_divisao,text="Calcular",command=but_resto)
calcular_resto.grid(column=1,row=3,columnspan=2,pady=30)
  
txt_q=Label(fr_divisao,text="Quociente:")
txt_q.grid(row=4,column=1,sticky="nswe",pady=10,padx=(50,10))

txt_r=Label(fr_divisao,text="Resto:")
txt_r.grid(row=5,column=1,sticky="nswe",padx=(50,10),pady=10)

r_q=Label(fr_divisao,text="",bg="#000",fg="white")
r_q.grid(row=4,column=2,sticky="nswe",padx=10,pady=10)

r_r=Label(fr_divisao,text="",bg="#000",fg="white")
r_r.grid(row=5,column=2,sticky="nswe",padx=10,pady=10)

#-------- aba conversor de Base -----------

#lista de bases que será exibida na Combobox
lista_bases=["2","3","4","5","6","7","8","9","10","HEX"]

base_txt1=Label(fr_conversor,text="Digite o número a ser convertido:")
base_txt1.grid(row=0,column=0,pady=10,sticky="nswe",padx=(20,0))
xnumero=Entry(fr_conversor,width=26)
xnumero.grid(row=0,column=1,pady=10,sticky="nswe",padx=(0,10))

base_txt2=Label(fr_conversor,text="Qual a base atual desse número: ")
base_txt2.grid(row=1,column=0,pady=10,sticky="nswe",padx=(20,0))
atual=ttk.Combobox(fr_conversor,values=lista_bases,width=17)
atual.grid(row=1,column=1,pady=10,sticky="nswe",padx=(0,10))

base_txt3=Label(fr_conversor,text="Digite a base desejada:")
base_txt3.grid(row=2,column=0,sticky="nswe",pady=10,padx=(20,0))
desejada=ttk.Combobox(fr_conversor,values=lista_bases,width=17)
desejada.grid(row=2,column=1,sticky="nswe",pady=10,padx=(0,10))
  
base_txt4=Label(fr_conversor,text="Resposta:",font="Segoeui 10 bold")
base_txt4.grid(row=3,column=0,sticky="nswe",pady=10,columnspan=2,padx=10)

base_btn=Button(fr_conversor,text="Converter",command=but_converter_base)
base_btn.grid(row=5,column=0,pady=10,columnspan=2)

base_r=Label(fr_conversor, text="",bg="#000",fg="#fff",font="Segoe 10 bold")
base_r.grid(row=4,column=0,pady=10,columnspan=2,sticky="nswe",ipady=10,padx=(20,10))

#-------- aba Mdc e Bezout -----------

txt1=Label(fr_mdc_bz,text="Digite o 1º número:",width="25")
txt1.grid(column=0,row=0,pady=10,sticky="nswe")
   
num1=Entry(fr_mdc_bz,width="25")
num1.grid(column=1,row=0,pady=10,sticky="nswe")

txt2=Label(fr_mdc_bz,text="Digite o 2º número:")
txt2.grid(column=0,row=2,pady=10,sticky="nswe")

num2=Entry(fr_mdc_bz)
num2.grid(column=1,row=2,pady=10,sticky="nswe")

txt3=Label(fr_mdc_bz,text="MDC = ")
txt3.grid(row=3,column=0,pady=10,sticky="e")

mdc=Label(fr_mdc_bz,text="",bg="#000",fg="#fff")
mdc.grid(row=3,column=1,sticky="nswe",pady=10)

calc=Button(fr_mdc_bz,text="Calcular",command=calcular_mdc_bz)
calc.grid(row=8,column=0,columnspan=2,pady=10)

txt4=Label(fr_mdc_bz,text="Identidade de Bezout",fg="black")
txt4.grid(row=4,column=0,columnspan=2,sticky="nswe",pady=10)

txt5=Label(fr_mdc_bz,text="X0")
txt5.grid(row=5,column=0,sticky="nswe")

txt6=Label(fr_mdc_bz,text="Y0")
txt6.grid(row=5,column=1,sticky="nswe",padx=10)

x0=Label(fr_mdc_bz,text="",bg="#000",fg="white")
x0.grid(row=6,column=0,sticky="nswe",padx=(10,30))

y0=Label(fr_mdc_bz,text="",bg="#000",fg="white")
y0.grid(row=6,column=1,sticky="nswe",padx=10)

bez=Label(fr_mdc_bz,text="",bg="black",fg="white")
bez.grid(row=7,column=0,columnspan=2,sticky="nswe",pady=10,padx=10)

#-------- aba Nº (primo, Marsene e Fermat) -----------

rb=IntVar()

p_txt1=Label(fr_primo,text="Quantos \"n\" primeiros termos deseja obter:")
p_txt1.grid(column=0,row=0,columnspan=2,pady=10,sticky="nswe")

p_qtd=Entry(fr_primo,width=17)
p_qtd.grid(row=0,column=2)

rb_p=Radiobutton(fr_primo,text="Primos",value=1,variable=rb,command=btn_primos)
rb_p.grid(row=1,column=0)

rb_m=Radiobutton(fr_primo,text="Marsenne",value=2,variable=rb,command=btn_marsenne)
rb_m.grid(row=1,column=1)

rb_f=Radiobutton(fr_primo,text="Fermat",value=3,variable=rb,command=btn_fermat)
rb_f.grid(row=1,column=2)

tv_fr=Frame(fr_primo)
tv_fr.grid(row=2,column=0,columnspan=3)
scroll=Scrollbar(tv_fr)
scroll.pack(side=RIGHT,fill=Y)
scroll_bot=Scrollbar(tv_fr,orient=HORIZONTAL)
scroll_bot.pack(side=BOTTOM,fill=X)

list_box=Listbox(tv_fr,bg="black",fg="white",width=50,height=7)
list_box.pack()
 
scroll_bot.config(command=list_box.xview)
scroll.config(command=list_box.yview)

Label(fr_primo,text="Verifique se o número é primo:").grid(row=3,column=0,columnspan=2,pady=10)

np_verificar=Entry(fr_primo,width=17)
np_verificar.grid(row=3,column=2,padx=(0,10))

btn_verificar=Button(fr_primo,text="Verificar",command=btn_verifique)
btn_verificar.grid(row=4,column=0,columnspan=3)

rp_verificar=Label(fr_primo,text="",background="black",foreground="white",width=35,font="Arial 8 bold")
rp_verificar.grid(row=5,column=0,columnspan=3,pady=10,ipady=5,sticky="nswe",padx=20)

#-------- aba MMC E MDC -----------

Label(fr_mmc,text="Digite os números que deseja calcular: (Separe-os por espaço)").grid(row=0,column=0,columnspan=3,sticky="nswe",padx=10)

mmc_entry=Entry(fr_mmc)
mmc_entry.grid(row=1,column=0,columnspan=2,padx=10,sticky="nswe")

btn_mmc=Button(fr_mmc,text="Calcular",command=calc_mmc)
btn_mmc.grid(row=1,column=2, padx=(5,10),sticky="nswe")

resp_mdc=Label(fr_mmc,text="",bg="black",fg="white",width=18)
resp_mdc.grid(row=2,column=0,padx=10,pady=10,sticky="nswe")

resp_mmc=Label(fr_mmc,text="",bg="black",fg="white",width=15)
resp_mmc.grid(row=2,column=2, padx=(5,5),pady=10,sticky="nswe")

Label(fr_mmc,text="Decomposição canônica ").grid(row=3,column=0,columnspan=2,padx=(0,25))

list_box_fat=Frame(fr_mmc)
list_box_fat.grid(row=4,column=0,columnspan=2)

scroll_fat=Scrollbar(list_box_fat)
scroll_fat.pack(fill=Y,side=RIGHT)

list_fatoracao=Listbox(list_box_fat,background="black",fg="white",height=5,font="Arial 11")
list_fatoracao.pack(fill=X)
scroll_fat.config(command=list_fatoracao.yview)
scroll_fat_bot=Scrollbar(list_box_fat,orient=HORIZONTAL)
scroll_fat_bot.pack(side=BOTTOM,fill=X)
scroll_fat_bot.config(command=list_fatoracao.xview)


Label(fr_mmc,text="Nº divisores positivos").grid(row=3,column=2,padx=10)

listbox_np_fr=Frame(fr_mmc)
listbox_np_fr.grid(row=4,column=2)

scroll_np=Scrollbar(listbox_np_fr)
scroll_np.pack(fill=Y,side=RIGHT)

list_np=Listbox(listbox_np_fr,background="black",fg="white",height=5,font="Arial 11")
list_np.pack(fill=X)

scroll_np_bot=Scrollbar(listbox_np_fr,orient=HORIZONTAL)
scroll_np_bot.pack(side=BOTTOM,fill=X)
scroll_np_bot.config(command=list_np.xview)
scroll_np.config(command=list_np.yview)

Label(fr_mmc,text="Divisores").grid(row=5,column=0,columnspan=3,padx=10)

fr_list_divisores=Frame(fr_mmc)
fr_list_divisores.grid(row=6,column=0,columnspan=3)

list_disores=Listbox(fr_list_divisores,background="black",fg="white",height=3,font="Arial 10",width=50)
scroll_divisores=Scrollbar(fr_list_divisores)
scroll_divisores.pack(side=RIGHT,fill=Y)
scroll_divisores.config(command=list_disores.yview)
scroll_divisores_bot=Scrollbar(fr_list_divisores,orient=HORIZONTAL)
scroll_divisores_bot.pack(side=BOTTOM,fill=X)
scroll_divisores_bot.config(command=list_disores.xview)
list_disores.pack()

#-------- aba Equação Diofantina -----------

Label(fr_diof,text="Digite a equação Diofantina no formato --->  AX + BY = C" ).grid(row=0,column=0,columnspan=3,sticky="nswe",padx=10)

diof_entry=Entry(fr_diof)
diof_entry.grid(row=1,column=0,columnspan=2,padx=10,sticky="nswe")

btn_diof=Button(fr_diof,text="Calcular",command=calcular_diofan)
btn_diof.grid(row=1,column=2, padx=(5,10),sticky="nswe")

resp_x0=Label(fr_diof,text="",bg="black",fg="white",width=18)
resp_x0.grid(row=2,column=0,padx=10,pady=10,sticky="nswe")

resp_y0=Label(fr_diof,text="",bg="black",fg="white",width=18)
resp_y0.grid(row=2,column=2, padx=(5,5),pady=10,sticky="nswe")

Label(fr_diof,text="Equação de todas as soluçoes inteiras onde t ∈ Z" ).grid(row=3,column=0,columnspan=3,sticky="nswe",padx=10)

resp_ex=Label(fr_diof,text="",bg="black",fg="white",width=18)
resp_ex.grid(row=4,column=0,padx=10,pady=10,sticky="nswe")

resp_ey=Label(fr_diof,text="",bg="black",fg="white",width=18)
resp_ey.grid(row=4,column=2, padx=(5,5),pady=10,sticky="nswe")

Label(fr_diof,text="Defina um intervalo de t que deseja obter as soluções" ).grid(row=5,column=0,columnspan=3,sticky="nswe",padx=10)

k1_entry=Entry(fr_diof,width=15)
k1_entry.grid(row=6,column=0,padx=10,pady=10,sticky="nswe")

Label(fr_diof,text="≤ t ≤" ).grid(row=6,column=1,sticky="nswe",padx=3)

k2_entry=Entry(fr_diof,width=15)
k2_entry.grid(row=6,column=2, padx=(5,5),pady=10,sticky="nswe")

fr_k=Frame(fr_diof)
fr_k.grid(row=7,column=0,columnspan=3)

list_k=Listbox(fr_k,background="black",fg="white",height=5,font="Arial 10",width=50)
scroll_k=Scrollbar(fr_k)
scroll_k.pack(side=RIGHT,fill=Y)
scroll_k.config(command=list_disores.yview)
list_k.pack(padx=(10,0))

app.mainloop() #metodo para a jenela permanecer aberta