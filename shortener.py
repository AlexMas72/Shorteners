import pyshorteners, sys, colorama
from time import sleep
from colorama import Fore, Back, Style
colorama.init()
print(Fore.YELLOW)
print("░██████╗██╗░░██╗░█████╗░██████╗░████████╗███████╗███╗░░██╗███████╗██████╗░")
print("██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗░██║██╔════╝██╔══██╗")
print("╚█████╗░███████║██║░░██║██████╔╝░░░██║░░░█████╗░░██╔██╗██║█████╗░░██████╔╝")
print("░╚═══██╗██╔══██║██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██║╚████║██╔══╝░░██╔══██╗")
print("██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░███████╗██║░╚███║███████╗██║░░██║")
print("╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝")
print(Style.RESET_ALL)
print(Fore.BLUE + '                                                 By AleksMas72')

sleep(1)
print(Style.RESET_ALL)
def start():
	print("1 : Сократить ссылку")
	print("2 : Расшифровать ссылку")
	print("0 : Exit")
	dei = ""
	print(Fore.GREEN)
	dei = int(input("Выбирите действие: "))
	print(Style.RESET_ALL)
	if dei==1:
		socsilk()
	elif dei==2:
		rassilk()
	elif dei == 0:
		exit()
	else:
		print(Fore.RED + "Неверное значение!")
		print("")
		print(Style.RESET_ALL)
		start()


def socsilk():
	print(Fore.GREEN)
	vd = input("Введите ссылку: ")
	print(Style.RESET_ALL)
	s = pyshorteners.Shortener()
	print(Fore.BLUE)
	print("Сокращённая ссылка: " + s.isgd.short(vd))
	print(Style.RESET_ALL)
	start()

def rassilk():
	print("Рассшифровка ссылки работает только с сайтом https://is.gd/")
	print(Fore.GREEN)
	vdr = input("Введите ссылку: ")
	print(Style.RESET_ALL)
	s = pyshorteners.Shortener()
	print(Fore.BLUE)
	print("Рассшифрованная ссылка: " + s.isgd.expand(vdr))
	print(Style.RESET_ALL)
	start()

def exit():
	print(Fore.RED + "Выход из системы")
	sys.exit()


if __name__ == "__main__":
    start()






