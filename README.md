# Planificador Inteligente Hendry C111
# Dominio elegido y razon
 Elegí hacer mi proyecto basado en un taller de reparación de motherboards de computadora
 debido a que trabajé en uno durante bastante tiempo y entiendo las complejidades y como funciona,
 por lo tanto puedo realizar el proyecto con mayor claridad sobre los que voy a hacer
# Eventos                            Duracion
 0- Defectacion                       | 1h
 1- Reparacion de tarjeta de video    | 5h
 2- Reparacion de socket              | 12h
 3- Reparacion de los 15 segundos     | 1h
 4- Reparacion del 12v del procesador | 5h
 5- Cambio de Pastilla de audio       | 3h
 6- Sustitucion de puerto usb         | 2h
 7- Sustitucion de puerto de video    | 2h
 8- Reparacion de chipset de video    | 9h
 9- Mantenimiento(bajo, medio, alto)  | 1h , 2h , 4h
10- Reparacion sencilla               | 2h
# Recursos
 Estos son los recursos que existen en mi dominio
 Herramientas y recursos:                    Personal:
1- Osciloscopio                           3 Tecnicos
2- Cautin                                 
3- Estacion de Calor                      
4- Multimetro
5- Estaño
6- Flux
7- Pasta termica
8- Alcohol Isopropilico
9- Goma de borrar
10- Monitor con Boardview
11- Lupa con lámpara
12- Fuente de Poder
13- Regulador de voltaje
14- Tester de fuente de poder
15- Maquina de Reballing
16- Sopladora/Aspiradora de aire
17- Brocha
18- Cepillo
# Eventos + Recursos + Restricciones
0- Defectacion (Osciloscopio, Multimetro, Alcohol isopropilico, Goma de borrar, Monitor con Boardview, Fuente de Poder, Regulador de voltaje, Lupa con lampara) (Osciloscopio != Multimetro, Fuente de Poder!= Regulador de voltaje) (Osciloscopio = Monitor con Boardview, Multimetro = Monitor con Boardview) 
1- Reparacion de tarjeta de video (Estacion de Calor,Cautin, Estaño, Flux, Pasta termica, Lupa con lampara, Maquina de Reballing) (Estacion de Calor != Cautin) 
2- Reparacion de Socket (Maquina de reballing)
3- Reparacion de los 15 seg (Flux, Estacion de Calor, Cautin) (Estacion de Calor != Cautin) (Flux = Estacion de Calor, Flux = Cautin)
4- Reparacion del 12v del procesador (Flux, Osciloscopio, Multimetro, Monitor con Boardview, Cautin, Estacion de Calor,Fuente de Poder, Tester de fuente de poder) (Estacion de Calor != Cautin, Osciloscopio != Multimetro) (Tester de fuente de poder = Fuente de poder, Flux = Estacion de Calor, Flux = Cautin, Multimetro = Monitor con Boardview, Osciloscopio = Monitor con Boardview)
5- Cambio de pastilla de audio (Flux, Estacion de Calor, Cautin) (Estaicon de Calor != Cautin) (Flux = Estacion de Calor, Flux = Cautin)
6- Sustitucion de puerto usb (Flux, Estacion de Calor, Cautin) (Estaicon de Calor != Cautin) (Flux = Estacion de Calor, Flux = Cautin)
7- Sustitucion de puerto de video (Flux, Estacion de Calor, Cautin) (Estaicon de Calor != Cautin) (Flux = Estacion de Calor, Flux = Cautin)
8- Reparacion de chipset de video (Multimetro ,Osciloscopio, Monitor con Boardview, Estacion de Calor, Cautin, Flux, Regulador de Voltaje) (Estaicon de Calor != Cautin, Multimetro != Osciloscopio) (Flux = Estacion de Calor, Flux = Cautin, Multimetro = Monitor con Boardview, Osciloscopio = Monitor con Boardview)
9- Mantenimiento: Bajo(Pasta Termica) Medio(Pasta Termica, Goma de borrar, Brocha) Alto(Pasta Termica, Goma de Borrar, Alcohol isopropilico, Brocha, Cepillo, Sopladora/Aspiradora de aire) 
10- Reparacion Sencilla (Cautin, Flux) (Cautin = Flux)