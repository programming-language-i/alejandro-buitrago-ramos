
import threading, time

def print_numbers():
    for i in range(1, 6):
        print (f"numeros: {i}")
        time.sleep (1)

def print_letter():
    for letter in "ABCDE":
        print (f"letter: {letter}")
        time.sleep(1)


if __name__ == "__main__" :
    h1 = threading.Thread(target=print_numbers)
    h2 = threading.Thread(target=print_letter)

    h1.start()
    h2.start()

    h1.join()
    h2.join()
