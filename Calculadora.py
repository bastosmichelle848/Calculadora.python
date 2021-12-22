#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Print na tela

print("\n ********Python Calculator*************")

#Funções

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

#Print na tela

print("\nSelecione o número da operação desejada: \n")
print('1- Soma')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')

# Definir as variáveis da calculadora

escolha=input("\nDigite sua opção (1/2/3/4): ")

num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número: "))

if escolha =='1':
    print("\n")
    print(num1,"+",num2,"=",add(num1,num2))
    print("\n")
    
elif escolha =='2':
    print("\n")
    print(num1,"-",num2,"=",subtract(x,y))

elif escolha=='3':
    print("\n")
    print(num1,"x",num2,"=",multiply(x,y))

elif escolha =='4':
    print("\n")
    print(num1,"/",num2,"=",divide(x,y))

    
else:
    print("\n Opção Inválida")


# In[ ]:




