# Defino los atributos que va a tener el cliente de una pizzeria

class Cliente:

    def __init__(self, nombre, fecha_nacimiento, alergias, alimentacion):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.alergias = alergias
        self.alimentacion = alimentacion

    # Defino las funcionalidades o metodos que mi cliente va a tener

    def reservar(self, fecha, horario):
        print(f"Tu reserva fue realizada con exito el dia {fecha} a la hora {horario}")

    def pagar(self, medio_de_pago, descuento):
        print(f"El pago se ha realizado con {medio_de_pago} y recibiras un descuento de {descuento}")

    def __str__(self):
        return f"{self.nombre} ha realizado una reserva, este cliente posee alergia a:{self.alergias} y tiene su alimenciacion es {self.alimentacion}"


# Creo Clase secundaria

class Cliente_Pet(Cliente):
    def __init__(self, nombre, fecha_nacimiento, alergias, alimentacion, tipo_mascota, nombre_mascota):
        super().__init__(nombre, fecha_nacimiento, alergias, alimentacion)
        self.tipo_mascota = tipo_mascota
        self.nombre_mascota = nombre_mascota

    def reservar(self, fecha, horario, tipo_mascota, nombre_mascota):
        super().reservar(self)
        print(f"La reserva con tu {tipo_mascota} llamada {nombre_mascota} fue registrada con exito!")

    def __str__(self):
        return f"La Reserva con su mascota {self.nombre_mascota} fue registrada con exito!"