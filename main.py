# Import modules

import numpy
import sympy as sy
import colorama
import os
import string
from colorama import Fore, Back, Style
from sympy.solvers import solve
from sympy import Symbol
import sympy as sym
from fractions import Fraction
sym.init_printing()

def inputswitch():
  print(Fore.YELLOW + "1 for Arithmetic | 2 for Algebra | 3 for Indices | 4 for Fraction, Decimal & Percentage Converter | 5 for HCF Calculator | 6 for LCM Calculator | 7 for Prime Number Checker | 8 for help")
  maininput = input(Fore.WHITE + "[>] ")
  if maininput == "1":
    maininput1()
  elif maininput == "2":
    maininput2()
  elif maininput == "3":
    maininput3()
  elif maininput == "4":
    maininput4()
  elif maininput == "5":
    maininput5()
  elif maininput == "6":
    maininput6()
  elif maininput == "7":
    maininput7()
  elif maininput == "8":
    maininput8()
  else:
    print("Enter enter a number from 1-8")
    inputswitch()
def helpinputswitch():
  print("1 For Arithmetic Help | 2 For Algebraic Help | 3 For Indice Help | 4 for Fraction, Decimal And Percentage Converter | 5 For Main Menu")
  helpmaininput = input(Fore.WHITE + "[>] ")
  if helpmaininput == "1":
    helpmaininput1()
  elif helpmaininput == "2":
    helpmaininput2()
  elif helpmaininput == "3":
    helpmaininput3()
  elif helpmaininput == "4":
    helpmaininput4()
  elif helpmaininput == "5":
    mainmenu()
  else:
    print("Enter 1,2,3,4 or 5")
    helpinputswitch()
# Start of actual code

def clearConsole():
    command = "clear"
    os.system(command)
# End of setup



def mainmenu():
  clearConsole()
  print(Fore.RED + """
░██████╗██╗░░░██╗██████╗░███████╗██████╗░
██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░░██║██████╔╝█████╗░░██████╔╝
░╚═══██╗██║░░░██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██║░░░░░███████╗██║░░██║
╚═════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")

  print("\n")
  print(Fore.GREEN + "Welcome to SuperCalculator! Please select a choice to get started. Note - Install numpy, sympy and colorama.")
  print("\n")
  inputswitch()
def maininput1():
    clearConsole()
    print(Fore.RED + """
░█████╗░██████╗░██╗████████╗██╗░░██╗███╗░░░███╗███████╗████████╗██╗░█████╗░
██╔══██╗██╔══██╗██║╚══██╔══╝██║░░██║████╗░████║██╔════╝╚══██╔══╝██║██╔══██╗
███████║██████╔╝██║░░░██║░░░███████║██╔████╔██║█████╗░░░░░██║░░░██║██║░░╚═╝
██╔══██║██╔══██╗██║░░░██║░░░██╔══██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██║██║░░██╗
██║░░██║██║░░██║██║░░░██║░░░██║░░██║██║░╚═╝░██║███████╗░░░██║░░░██║╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░╚════╝░""")

    print("\n")
    print(Fore.GREEN + "Welcome to the arithmetic calculator, please input a number.")
  
    num1 = float(input(Fore.WHITE + "[>] "))
  
    print(Fore.GREEN + "Please enter an operand.")
  
    operand = input(Fore.WHITE + "[>] ")
  
    print(Fore.GREEN + "Please enter the last number.")
  
    num2 = float(input(Fore.WHITE + "[>] "))
  
    if operand == "+":
     print(num1 + num2)
  
    elif operand == "-":
     print(num1 - num2)
  
    elif operand == "/":
     print(num1 / num2)
  
    elif operand == "*" or "x" or "X":
     print(num1 * num2)
  
    else:
     print("Invalid operand. Only enter +,-,/,*,x or X")

    inputswitch()
  
# Algebraic calculator
  
def maininput2():
  clearConsole()
  
  print(Fore.RED + """
░█████╗░██╗░░░░░░██████╗░███████╗██████╗░██████╗░░█████╗░
██╔══██╗██║░░░░░██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗
███████║██║░░░░░██║░░██╗░█████╗░░██████╦╝██████╔╝███████║
██╔══██║██║░░░░░██║░░╚██╗██╔══╝░░██╔══██╗██╔══██╗██╔══██║
██║░░██║███████╗╚██████╔╝███████╗██████╦╝██║░░██║██║░░██║
╚═╝░░╚═╝╚══════╝░╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")
  
  print("\n")
  print(Fore.GREEN + "Welcome to the Algebraic calculator. Please enter an equation. Replace '=' with ' - '.")
  equation = input(Fore.WHITE + "[>] ")
  print(Fore.GREEN + "What do you want to solve for")
  solvesymbol = input(Fore.WHITE + "[>] ")
  print(solve(equation,solvesymbol))

  inputswitch()
  
# Indice calculator
  
def maininput3():
  clearConsole()
  
  print(Fore.RED + """
██╗███╗░░██╗██████╗░██╗░█████╗░███████╗░██████╗
██║████╗░██║██╔══██╗██║██╔══██╗██╔════╝██╔════╝
██║██╔██╗██║██║░░██║██║██║░░╚═╝█████╗░░╚█████╗░
██║██║╚████║██║░░██║██║██║░░██╗██╔══╝░░░╚═══██╗
██║██║░╚███║██████╔╝██║╚█████╔╝███████╗██████╔╝
╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░╚════╝░╚══════╝╚═════╝░""")
  print("\n")
  print(Fore.GREEN + "Welcome to the Indice Calculator. Please enter the base.")
  indice1 = int(input(Fore.WHITE + "[>] "))
  print(Fore.GREEN + "Enter the indice.")
  indice2 = int(input(Fore.WHITE + "[>] "))
  print(indice1**indice2)
  
  inputswitch()

# Fractions, Decimals and Percentage converter

def maininput4():
  clearConsole()
  
  print(Fore.RED + """
███████╗██████╗░░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
█████╗░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔══╝░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██║░░░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

██████╗░███████╗░█████╗░██╗███╗░░░███╗░█████╗░██╗░░░░░
██╔══██╗██╔════╝██╔══██╗██║████╗░████║██╔══██╗██║░░░░░
██║░░██║█████╗░░██║░░╚═╝██║██╔████╔██║███████║██║░░░░░
██║░░██║██╔══╝░░██║░░██╗██║██║╚██╔╝██║██╔══██║██║░░░░░
██████╔╝███████╗╚█████╔╝██║██║░╚═╝░██║██║░░██║███████╗
╚═════╝░╚══════╝░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝

██████╗░███████╗██████╗░░█████╗░███████╗███╗░░██╗████████╗░█████╗░░██████╗░███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔════╝░██╔════╝
██████╔╝█████╗░░██████╔╝██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░███████║██║░░██╗░█████╗░░
██╔═══╝░██╔══╝░░██╔══██╗██║░░██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██║██║░░╚██╗██╔══╝░░
██║░░░░░███████╗██║░░██║╚█████╔╝███████╗██║░╚███║░░░██║░░░██║░░██║╚██████╔╝███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝


░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝""")

  print("\n")
  print(Fore.GREEN + "Welcome to the Fraction, Decimal And Percentage Converter. Please enter the type of value you want to convert from. 1 for fraction | 2 for decimal | 3 for percentage.")
  fromtype = input(Fore.WHITE + "[>] ")
  if fromtype == "1":
    print(Fore.GREEN + "Please enter numerator")
    numerator = float(input(Fore.WHITE + "[>] "))
    print(Fore.GREEN + "Please enter denominator")
    denominator = float(input(Fore.WHITE + "[>] "))
  else:
    print(Fore.GREEN + "Please enter the value you want to convert from. Do not use %, just use the number.")
    typevalue = float(input(Fore.WHITE + "[>] "))
  
  print(Fore.GREEN + "Please enter the type of value you want to convert to. 1 for fraction | 2 for decimal | 3 for percentage.")
  totype = input(Fore.WHITE + "[>] ")

  if fromtype == "1":
    if totype == "1":
      print("Do not convert to the same value")
    elif totype == "2":
      print(numerator/denominator)
    elif totype == "3":
      print((numerator/denominator)*100)
      print("%")

  elif fromtype == "2":
    if totype == "1":
      print(Fraction(typevalue))
    elif totype == "2":
      print("Do not convert to the same value")
    elif totype == "3":
      print(typevalue*100)
      print("%")

  elif fromtype == "3":
    if totype == "1":
      print(Fraction(typevalue))
    elif totype == "2":
      print(totype/100)
    elif totype == "3":
      print("Do not convert to the same value")
  
  inputswitch()

def maininput5():
  clearConsole()
  print(Fore.RED + """
██╗░░██╗░█████╗░███████╗  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██║░░██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
███████║██║░░╚═╝█████╗░░  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██╔══██║██║░░██╗██╔══╝░░  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░░██║╚█████╔╝██║░░░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")
  def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

  print(Fore.WHITE + "Enter first number.")
  num1 = int(input(Fore.WHITE + "[>] ")) 
  print("Enter second number.")
  num2 = int(input(Fore.WHITE + "[>] "))
  print("The H.C.F. is", compute_hcf(num1, num2))
  inputswitch()
def maininput6():
  clearConsole()
  print(Fore.RED + """
██╗░░░░░░█████╗░███╗░░░███╗  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██║░░░░░██╔══██╗████╗░████║  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░░░░██║░░╚═╝██╔████╔██║  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░░░░██║░░██╗██║╚██╔╝██║  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
███████╗╚█████╔╝██║░╚═╝░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚══════╝░╚════╝░╚═╝░░░░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")
  def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
    
  print(Fore.WHITE + "Enter first number.")
  num1 = int(input(Fore.WHITE + "[>] ")) 
  print("Enter second number.")
  num2 = int(input(Fore.WHITE + "[>] "))
  print("The L.C.M. is", compute_lcm(num1, num2))
  inputswitch()
def maininput7():
  clearConsole()
  print(Fore.RED + """
██████╗░██████╗░██╗███╗░░░███╗███████╗  ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██║████╗░████║██╔════╝  ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║██╔████╔██║█████╗░░  ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══╝░░  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║██║░╚═╝░██║███████╗  ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
  print(Fore.WHITE + "Enter number.")
  num = int(input(Fore.WHITE + "[>] "))
  flag = False
  if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
  if flag:
    print(num, "is not a prime number")
  else:
    print(num, "is a prime number")

  inputswitch()
  
def maininput8():
  
  clearConsole()

# Help book
  
  print(Fore.RED + """
██╗░░██╗███████╗██╗░░░░░██████╗░
██║░░██║██╔════╝██║░░░░░██╔══██╗
███████║█████╗░░██║░░░░░██████╔╝
██╔══██║██╔══╝░░██║░░░░░██╔═══╝░
██║░░██║███████╗███████╗██║░░░░░
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░""")
  print("\n")
  print(Fore.GREEN + "Welcome to the Help part of this program. Here, we will show you all the operands and ways to use this program.")
  print("\n")
  print(Fore.WHITE + "What do you need help with today?")
  print("\n")

  helpinputswitch()
def helpmaininput1():
    print(Fore.WHITE + "Arithmetic Operands")
    print("\n")
    print("Plus = +")
    print("Minus = -")
    print("Multiply = *")
    print("Divide = /")
    print("\n")

    helpinputswitch()
    
def helpmaininput2():
    print(Fore.GREEN + "Algebraic Help Manual")
    print("\n")
    print(Fore.RED + "Note: DO NOT RUN THIS WITH THE ANSWER, as it will not function!")
    print("\n")
    print(Fore.WHITE + "The operands are the same as the Arithmetic calculator. Remember to replace '=' with ' - '.")

    helpinputswitch()

def helpmaininput3():
    print(Fore.GREEN + "Indices Operands")
    print("\n")
    print(Fore.WHITE + "Power = **")
    
    helpinputswitch()

def helpmaininput4():
  print(Fore.WHITE + "Follow all instructions on the converter to use it. Note - Do not use the % symbol.")

  helpinputswitch()

mainmenu()

# End Of Code
