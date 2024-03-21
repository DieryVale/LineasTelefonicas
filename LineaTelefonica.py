class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas = 0    
    
    # Numero de minutos consumidos
    numeroMinutos = 0
    
    # Costo total de las llamadas
    costoLlamadas = 0

    # modelar el estrato 
    estrato = 0 

    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.
        self.numeroLlamadas = 0 
        self.numeroMinutos =  0 
        self.costoLlamadas = 0
        self.costoDeMinutosACelular = 0 
        self.cantidadDeMinutosACelular = 0 
        
    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.

        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numeroMinutos
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroLlamadas = 0 
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        self.costoDeMinutosACelular = 0 
        self.cantidadDeMinutosACelular = 0 

        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
        
    def llamadaLocal (self, pminutos):
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
        self.numeroLlamadas += 1 
        self.numeroMinutos += pminutos
        self.costoLlamadas += pminutos * 35

    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 999
        self.cantidadDeMinutosACelular  = 0 
        self.costoDeMinutosACelular = 999


        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
    
    #Cambiar el estrato de una linea, no retorna nada 
    
    def definirEstrato(self, pEstrato):
        self.estrato = pEstrato



    # Retorna el estrato de la linea 
    def darEstrato(self):
        return self.estrato


    # darMinutosPorEstrato( ) sin parámetros, que retorna el resultado de multiplicar el número de minutos consumidos en la línea por el estrato de la línea.
    def darMinutosPorEstrato(self):
        return self.numeroMinutos * self.estrato  
       
    def consultarCantodadMinutosCelular(self):
        return self.consultarCantodadMinutosCelular
    
    def consultarCostoMinutosCelular(self):
        return self.consultarCostoMinutosCelular
