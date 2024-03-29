from LineaTelefonica import LineaTelefonica

class Empresa:
    
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Línea telefónica número 1.
    linea1 = 0
    # Línea telefónica número 2.
    linea2 = 0 
    # Línea telefónica número 3.
    linea3 = 0 

    # 1.	Agregar los atributos que modelen la cantidad y el costo de minutos de llamadas a celular.
    cantidadDeMinutosACelular = 0 
    costoDeMinutosACelular = 0 
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def __init__(self):
        self.linea1 = LineaTelefonica()
        self.linea2 = LineaTelefonica()
        self.linea3 = LineaTelefonica ()
        self.linea1.definirEstrato(2) 
        self.linea2.definirEstrato(5) 
        self.linea3.definirEstrato(6) 
        
        # TODO Parte3 PuntoA: Construir linea2 y linea3.
        # agergar al final del metodo constructor tres instrucciones con llamadas al método del punto anterior, para que la línea 1 sea de estrato 2, la línea 2 de estrato 5 y la línea 3 de estrato 
        
    # Retorna la l�nea 1.
    def darLinea1(self):
        return self.linea1
        # TODO Parte3 PuntoB: Completar el m�todo seg�n la documentaci�n dada.

    # Retorna la l�nea 2.
    def darLinea2(self):
        return self.linea2
        # // TODO Parte3 PuntoC: Completar el m�todo seg�n la documentaci�n dada.

    # Retorna la l�nea 3.
    def darLinea3(self):
        return self.linea3
        # // TODO Parte3 PuntoD: Completar el m�todo seg�n la documentaci�n dada.

    '''
	    # Retorna el n�mero total de llamadas realizadas.
	    # @return Total de llamadas de las tres l�neas.
	'''

    def darTotalNumeroLlamadas(self):
        # TODO Parte3 PuntoE: Completar el m�todo seg�n la documentaci�n dada.
        return self.linea1.darNumeroLlamadas() + self.linea2.darNumeroLlamadas() + self.linea3.darNumeroLlamadas()
        
    
    '''
	    # Retorna el total de minutos consumidos.
	    # @return Total de minutos de las tres l�neas.
	 '''
    def darTotalMinutos(self):
        # TODO Parte3 PuntoF: Completar el m�todo seg�n la documentaci�n dada.
        return self.linea1.darNumeroLlamadas() + self.linea2.darNumeroLlamadas() + self.linea2.darNumeroLlamadas()
    
    def darTotalCostoLlamadas(self):
        # TODO Parte3 PuntoG: Completar el m�todo seg�n la documentaci�n dada.
        return self.linea1.darCostoLlamadas() + self.linea2.darCostoLlamadas() + self.linea3.darCostoLlamadas()
    '''
        # Retorna el costo promedio de un minuto, seg�n los minutos consumidos. <br>
	    # @return Costo promedio por minuto.
    '''
    def darCostoPromedioMinuto(self):
        # TODO Parte3 PuntoH: Completar el m�todo seg�n la documentaci�n dad
        return self.darTotalMinutos() / self.darTotalMinutos() 

    '''
        # Agrega una llamada local a la l�nea telef�nica 1 <br>
        # <b>post: </b> Se agreg� la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea1(self, pMinutos):
        self.linea1.agregarLlamadaLocal(pMinutos > 0)

    '''
        # Agrega una llamada local a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agreg� la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea2(self, pMinutos ):
        self.linea2.agregarLlamadaLocal(pMinutos > 0 )
        # TODO Parte3 PuntoI: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada local a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea3(self, pMinutos ):
        self.linea3.agregarLlamadaLocal(pMinutos > 0 )
        # TODO Parte3 PuntoJ: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 1. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea1(self, pMinutos):
        self.linea1.agregarLlamadaLargaDistancia(pMinutos > 0 )

    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea2(self, pMinutos):
        self.linea2.agregarLlamadaLargaDistancia(pMinutos > 0 )
        # TODO Parte3 PuntoK: Completar el m�todo seg�n la documentaci�n dada.
    
    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea3(self, pMinutos):
        self.linea3.agregarLlamadaLargaDistancia(pMinutos > 0 )
        # TODO Parte3 PuntoL: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada a celular a la l�nea telef�nica 1. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea1(self, pMinutos):
        self.linea1.agregarLlamadaCelular(pMinutos)

    '''
        # Agrega una llamada a celular a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea2(self, pMinutos):
        self.linea2.agregarLlamadaCelular(pMinutos > 0 )
        # TODO Parte3 PuntoM: Completar el m�todo seg�n la documentaci�n dada.
    
    '''
        # Agrega una llamada a celular a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea3(self, pMinutos):
        self.linea3.agregarLlamadaCelular(pMinutos > 0 )
        #TODO Parte3 PuntoN: Completar el m�todo seg�n la documentaci�n dada.
    
    '''
        # Reinicia todas las l�neas telef�nicas.
        # <b>post: </b> Se reinici� la llamada a la l�nea 1, 2 y 3. 
    '''
    def reiniciar(self):
        self.linea1.reiniciar()
        # // TODO Parte3 PuntoB: Completar el m�todo para reiniciar las lineas 2 y 3.
        self.linea2.reiniciar()
        self.linea3.reiniciar()

    # retorna el total calculado de sumar lo que retorna el método anterior (darMinutosPorEstrato) para cada línea.
    def darTotalMinutosPorEstrato(self):
        return self.linea1.darMinutosPorEstrato() + self.linea2.darMinutosPorEstrato() + self.linea3.darMinutosPorEstrato()

    '''----------------------------------------------------------------
    # Puntos de Extensi�n
    ----------------------------------------------------------------'''

    # M�todo para la extensi�n 1.
    # @return Respuesta 1. 
    def metodo1(self):
        return  "El total de minutos a celular es " + self.linea1.consultarCantodadMinutosCelular + self.linea2.consultarCantodadMinutosCelular + self.linea3.consultarCantodadMinutosCelular 
    
    

    # M�todo para la extensi�n 2.
    # @return Respuesta 2.
    def metodo2(self):
        bono = 0.2
        return "Valor del bono es " + self.linea1*bono + self.linea2*bono + self.linea3*bono # posible solucion o cambiar el * por un . 
    

