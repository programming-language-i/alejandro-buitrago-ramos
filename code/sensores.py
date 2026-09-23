import threading, time

def sensor(numero, temperatura):
    for i in range(5):
        print(f"Sensor: {numero}, Temperatura: {temperatura}")
        time.sleep(1)
        for i in range(5):
            print(f"Sensor: - {i+1}, Temperatura: {temperatura} centigrados")

            time.sleep(1)

            print ("Termino")

            if  --__name__== "__main__":
                treads = [              
                threading.Thread(target=sensor, args=("sensor 1", 30)),
                threading.Thread(target=sensor, args=("sensor 2", 40)),
                threading.Thread(target=sensor, args=("sensor 3", 50)),
                threading.Thread(target=sensor, args=("sensor 4", 60)),
                threading.Thread(target=sensor, args=("sensor 5", 70)),
                ]

                
                for thread in treads:
                    thread.start()
                

                
                for thread in treads:
                    thread.join()

                print("Finalizaron todos los hilos")