class Singleton(type):      #Constructor de clases, conocido como metaclase
    __instances = {}
    def __call__(cls, *args, **kwargs):     #Cada vez que se llama a la clase se ejecuta el metodo
        if cls not in cls.__instances:      #Si la clase no esta incluido en instances (donde se guardan las clases), la guardara
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]