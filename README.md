Práctica 3 - Indirect Group Communication
Joan Pascual Alcaraz

En una estructura de comunicación basada en sockets de pub/sub, el objetivo era 
modificar el código para permitir conexiones de multiples clientes.

En un primer intento, quería que fuera el broker quien comprobara si el puerto 
al que el cliente se quiere conectar ya estaba en uso, y en tal caso enviar al 
cliente el siguiente puerto disponible para que se conectara a éste. Aquí he 
tenido problemas a la hora de transmitir dicho puerto desde el broker y al 
leerlo desde el cliente, así que he hecho otro enfoque quizá un poco más simple. 
He dejado esta implementación comentada en el broker.

Así como está definido el código del cliente suscriptor, siempre intenta conectarse 
al puerto 10001. El primer cliente lo conseguirá, pero al próximo le saltará 
un error de dirección en uso. Para ello, he implementado un tratamiento de este 
error, de modo que cuando salta, el cliente cambia al siguiente puerto, en este 
caso 10002, y así hasta que encuentra uno disponible.