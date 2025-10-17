
#Ejercicio de uso de variables  con funciones 

def get_guess() :
        guess =  int(input('Ingresa un numero: '))
        return guess


def main () :
        guess  = get_guess()
        if guess == 50:
                print('Correcto')
        else: print('Incorrecto')

    
main()