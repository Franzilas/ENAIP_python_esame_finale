def funzione1(x, y):
    """Questa funzione restituisce l'area di un retangolo"""
    return x*y 

def funzione2(y):
    """
    Questa funzione accetta un nome e restituisce un saluto personalizzato alla persona.
    """
    return f"Buona serata {y}"

def funzione3(y, z):
    """
    Questa funzione trova e restituisce il massimo dei due numeri.
    """
    return max(y ,z)



class classeDaFinire:
    def __init__(self, nome, età, città):
        self.nome = nome
        self.età = età
        self.città = città

    def metodo1(self):
        """
        Questo metodo dovrebbe restituire un'introduzione della persona (restituendo
        una stringa con nome, età e città di provenienza).
        """
        return f"Ciao, sono {self.nome}, ho {self.età} anni e vengo da {self.città}!"

    def metodo2(self, x):
        """
        Questo metodo dovrebbe aggiungere un argomento numerico all'età dell'oggetto.
        """
        y = self.età + x
        return f"Ciao, il mio numero fortunato è {y} !"
