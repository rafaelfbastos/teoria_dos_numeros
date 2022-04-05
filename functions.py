# Esse arquivo onde estão as funções de cálculos matématicos

def NumeroPrimo (n): #função que recebe um paremetro int n e verifica se é primo e retorna uma booleana
    #atibuiçao de uma variel cont
    cont=0 

    for i in range(n+1): #repitição que irá verificar o resto da divisão ente n e i , sendo i variando de 0 a n
        if i==0:
            continue
        if n%i==0:      #sempre irá incrementar 1 ao contador caso resto for zero
            cont+=1
    if cont==2:         #verificar se o contador foi igual a dois para dizer se o numéro e primo ou não 
        return True;
    else:
        return False;

def validar_base(base_atual,numero):  #função que recebe dois paremetro str e verifica se a base digitada corresponde ao número e retorna uma booleana
  #atribuiçao de uma lista com os caractreres permitidos
  lista_caracteres=["2","3","4","5","6","7","8","9","0","1","A","B","C","D","E","F"]  
  # método para tranformar todos caracteres em maiúsculas e minimizar erro de digitação
  numero=numero.upper() 
  # método para restirar espaços caso for digitado
  numero=numero.replace(" ","") 
  #atibuindo a variavel de saiada o valor verdadeiro
  validador=True 
  #verificando para base Hexadeciamal
  if(base_atual=="HEX"): 
    #for que pecorre cada caracter na string atibuindo a variavel ch
    for ch in numero:
      #verifiucar se a variavel ch está presente na lista de cacteres permitido
      if ch in lista_caracteres: 
        continue
      #Caso falso a variavel de retorno recebe falso
      else: 
        validador=False
  #verificação para qualquer base númerica   
  else: 
    #Caso oque doi digitado não for "HEX" ele vericia se é um número
    if numero.isnumeric(): 
    #for que pecorre cada caracter na string atibuindo a variavel ch
      for ch in numero: 
        #Variavies temporarias que tranforma o caracter em int para fazer as comparações
        i=int(ch)       
        b=int(base_atual)
        if(i<b):        
          continue
        else:
          validador=False
          break
    else:
      validador=False
  return validador;

def converter_to_10(base_atual,numero): #função que recebe dois paremetro str converter o numero para base 10

  numero=numero.upper()
  numero=numero.replace(" ","") 
  #metodo para saber a quantidade de algarismos o número tem, pelo tramnha da string
  n=len(numero) 
  x=n-1 
  resultado=0

  if(base_atual=="HEX"): 
    #criando uma lista vazia
    vnum=[] 
    b=16
    #Preencendo essa lista com valores convertidos para int fazendo a conversão do valores hexadecimal correspondente
    for ch in numero:
      if (ch=="A"):
        vnum.append(10)
      elif(ch=="B"):
        vnum.append(11)
      elif(ch=="C"):
        vnum.append(12)
      elif(ch=="D"):
        vnum.append(13)
      elif(ch=="E"):
        vnum.append(14)
      elif(ch=="F"):
        vnum.append(15)
      else:
        vnum.append(int(ch))  
    #convertendo a lista em um numero na base 10
    for i in range(n):  
      resultado=resultado+vnum[x]*b**i
      x-=1
  #convertendo a string digitada em um numero na base 10  
  else:
    b=int(base_atual)
    for i in range(n):
      resultado=resultado+int(numero[x])*b**i
      x-=1 
  
  return resultado;

def converter_to_n(inteiro,base): #função que recebe um número inteiro na base 10 e un str com valor da base desejada e retorna uma lista com os valores
  #criando um lista para receber a resposta
  resposta=[]
  
  #convertento a str da base em uma variel int
  if(base=="HEX"):
    b=16
  else:
    b=int(base)
  
  #divisões sucessivas para conversao da base
  while(inteiro>=b):
    resposta.append(inteiro%b)
    inteiro=int(inteiro/b)
  #atribuindo o ultimo valor a resposta: porém ela está invertida
  resposta.append(int(inteiro))
  #chamando função que inverte a lista e substitui os numeros inteiros para caracteres do HEX
  resultado=inverter(resposta)
  
  return resultado;
   
def bezout(quociente,x,y,q0,i): #funçao que calcula indentidade de bezout: 
  #recebendo como parametros uma lista com todos os quocientes o valor de x e y  o quociente da primeira divisão e o numero de diviões revelantes e retorna uma lista com os dois coeficientes
    bz=[]
  #calculo baseando no algoritimo da divisão sucessivas  
    if(i==0):
        a=[]
        b=[]
        a.append(1)
        b.append(1-q0)
        if(x>0):
            
            bz.append(a[0])
        else:
            
            bz.append(-a[0])
        if(y>0): 
            
            bz.append(b[0])
        else:
            
            bz.append(-b[0])
    
    elif(i==1):
        a=[]
        b=[]
        a.append(1)
        b.append(-quociente[0])
        if(x>0):
           
            bz.append(a[0])
        else:
           
            bz.append(-a[0])
        if(y>0): 
          
            bz.append(b[0])
        else:
           
            bz.append(-b[0])

    elif(i==2):
        a=[]
        b=[]
        a.append(1)
        b.append(-quociente[0])
        a.append(-quociente[1]*a[0])
        b.append(1-b[0]*quociente[1])
        
        if(x>0):
           
            bz.append(a[1])
        else:
            
            bz.append(-a[1])
        if(y>0): 
           
            bz.append(b[1])
        else:
           
            bz.append(-b[1])

    else:
        a=[]
        b=[]
        count=i-2
        idx=0
        a.append(1)
        b.append(-quociente[0])
        a.append(-quociente[1]*a[0])
        b.append(1-b[0]*quociente[1])
        
        while count>0:

            a.append(a[idx]-quociente[2+idx]*a[1+idx])
            b.append(b[idx]-quociente[2+idx]*b[1+idx])
            count-=1
            idx+=1
                
        if(x>0):
            
            bz.append(a[1+idx])
        else:
            
            bz.append(-a[1+idx])
        if(y>0): 
           
            bz.append(b[1+idx])
        else:
            
            bz.append(-b[1+idx])
    #retorno dos coeficientes de bezout sempre será com o coeficiente na posição bz[0] relatico ao coeficente do maior número em modulo digitado pelo usuario e não pela ordem digitada
    return bz;

def resto(num,den):#funcão que recebe dois números inteiros e calcula o resto da divisão segundo algoritmo da teoria dos números
  resposta_da_divisao=[]
  numerador=num
  denominador=den
  q=0

  #esse algorimo leva em considerção que o resto da divisão sempre será um numero inteiro >=0  e satisfaz a equação (dividendo = divisor*quociente + resto ) 
  if numerador>=0 and denominador>0:
     
    r=numerador%denominador
    q=int(numerador/denominador)
    resposta_da_divisao.append(q)
    resposta_da_divisao.append(r)
  
  elif numerador>=0 and denominador<0:

    while q*denominador<=numerador:
        q-=1
    r=numerador-(q+1)*denominador    
    resposta_da_divisao.append(q+1)
    resposta_da_divisao.append(r)  
       
  elif numerador<=0 and denominador>0:   
    while q*denominador>numerador:
        q-=1
    r=numerador-q*denominador    
    resposta_da_divisao.append(q)
    resposta_da_divisao.append(r)  
    
  elif numerador<=0 and denominador<0:
    while q*denominador>numerador:
        q+=1
    r=numerador-q*denominador    
    resposta_da_divisao.append(q)
    resposta_da_divisao.append(r)
  return resposta_da_divisao;

def f_mdc(num1,num2): # função que recebe dois números e calcula o mdc entre eles pelo método das divisões sucessivas
  
  dividendo=[]
  divisor=[]
  quociente=[]
  resto=[]
  #Para calculo do mdc utiliza-se os valores absolutos 
  a=abs(int(num1))
  b=abs(int(num2))
    
  if(a>b):
    dividendo.append(a)
    divisor.append(b)
    i=0
    while(dividendo[i]%divisor[i]!=0):
      resto.append(dividendo[i]%divisor[i])
      quociente.append(int(dividendo[i]/divisor[i]))
      dividendo.append(divisor[i])
      divisor.append(resto[i])
      i+=1
    c_mdc=divisor[i]             
     
  elif(a<b):
    dividendo.append(b)
    divisor.append(a)
    i=0  
    while(dividendo[i]%divisor[i]!=0):
      resto.append(dividendo[i]%divisor[i])
      quociente.append(int(dividendo[i]/divisor[i]))
      dividendo.append(divisor[i])
      divisor.append(resto[i])
      i+=1
    c_mdc=divisor[i]
  return c_mdc;             
 
def f_mmc(num1,num2):#Calcula o mmc pelo teorema mmc=(|a|*|b|)/mdc
  
  a=abs(int(num1))
  b=abs(int(num2))

  #calcunado mmc chamando a função mdc

  c_mmc=int((a*b)/f_mdc(num1,num2)) 
 
  return c_mmc;      

def divisores(num): #retorna uma lista com todos os divisores de um número
  num=abs(num)
  divisor=[]
  divisor_negativo=[]
  #pega os divisores positivos
  for i in range(num+1):
    if i==0:
      continue
    if num%i==0:
      divisor.append(i)
  #pega os divores positivos e converter para negativos
  for i in divisor:
    divisor_negativo.append(-i)    
  #junta as duas lista e organiza em ordem crescente
  divisor.extend(divisor_negativo)
  divisor=sorted(divisor)
  return divisor;  

def teorema_aritimetica(num): #função que recebe um número e ela retorna uma lista com resultado da fotorção por fatores primos podendo ter repetições
  num=abs(num)
  i=1
  base=[]
  #chama a funcão n_primo
  while num!=1:
    if num%n_primo(i)==0:
      base.append(n_primo(i))
      num/=n_primo(i)
    else:
      i+=1
  return base;

def n_primo(n): #função que o numero primo da posição n 
  i=0
  primo=0
  cont=2
  
  while i<n:
    if(NumeroPrimo(cont)):
      i+=1
      primo=cont
    cont+=1
  return primo;

def potencias_carac(potencias):#funcão que que metodos de tranlate da string para substituir caracteres numericos em seus respectivos valores sobrescrito 
  result=str(potencias)
  carac="0123456789"
  change="⁰¹²³⁴⁵⁶⁷⁸⁹"
  tab_trans=result.maketrans(carac, change )
  
  return result.translate(tab_trans);

def a_b_C_Diofante(string): #funcão que recebe a entrada do usuario e retira os coeficientes a b e c da as equaçoes diofantinas 
  
  resposta=[]
  string=string.lower()
  string=string.replace(" ","") 
  #essa função ira tratar a string se o usuario digitar ax+by=c ou ax-by=c serve para troca da ordem das letras x e y
  
  try:
    if(string.find("x")<string.find("y")):
      string=string.split("x",1)
      resposta.append(int(string[0]))
      string=string[1]
      string=string.split("y",1)
      resposta.append(int(string[0]))
      string=string[1]
      string=string.replace("=","")
      resposta.append(int(string))
      resposta.append("xy")  
    
    else:
      string=string.split("y",1)
      resposta.append(int(string[0]))
      string=string[1]
      string=string.split("x",1)
      resposta.append(int(string[0]))
      string=string[1]
      string=string.replace("=","")
      resposta.append(int(string))
      resposta.append("yx")  
  except:
    resposta="false"

  return resposta;

def inverter(lista): #função que trata a lista da conversão de base: ela recebe uma lista invertida e com valores interiros e retorna uma lista com a resposta correta para usuario 
  n=len(lista)
  x=n-1
  invertido=""
  for i in range(n):
    if(lista[x]==10):
      invertido=invertido+"A"
    elif(lista[x]==11):
      invertido=invertido+"B"
    elif(lista[x]==12):
      invertido=invertido+"C"
    elif(lista[x]==13):
      invertido=invertido+"D"
    elif(lista[x]==14):
      invertido=invertido+"E"
    elif(lista[x]==15):
      invertido=invertido+"F"
    else:
      invertido=invertido+str(lista[x])
    x-=1  
  return invertido;
