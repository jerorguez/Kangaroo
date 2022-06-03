<div align="center">
    <!-- <h1>Kangaroo</h1> -->
    <h1>Proyecto E-commerce</h1>
    <h6>Francisco Jerobel Rodriguez Niño <br> Siomara de las Nieves Alonso Hernández</h6>
</div>
<hr>

**Kangaroo** es un comercio de distribución de productos para animales basado en el modelo de e-commerce *(comercio online)*. Se dispondrá de una interfaz gráfica hecha con **tkinter** y el lenguaje de programación usado será **python**.
El funcionamiento del programa consistirá en lo siguiente:
* Se mostrará una ventana de logeo en la que el usuarioFrancisco Jerobel Rodriguez Niño podrá introducir sus datos directamente (si ya se encuentra registrado) o, en caso contrario, accederá a un formulario donde podrá registrarse.
    * Aquellos usuarios que son admin podrán acceder a un panel de administración diferente en donde podrán:
        * Añadir proveedores.
        * Añadir productos.
    * El resto de usuarios, o clientes, podrán realizar pedidos; para esto accederan a un nuevo formulario donde podrán seleccionar de la lista de productos, el producto que quieren comprar, la cantidad y, una vez ordenado el pedido, se accederá a una nueva ventana en la que se pedirá el tipo de método de pago y, acto seguido, deberán introducir sus credenciales:
        * Si las credenciales son correctas, únicamente habrá que pulsar el botón de "pagar", este registrará la transacción y se modificará el estado del pedido a "pagado".
        * Si las credenciales no existen deberán ser añadidas al fichero para poder proceder con el pago.
        * Si las credenciales existen pero son incorrectas, únicamente se le pedirá volver a introducirlas.

        
Para el correcto funcionamiento del comercio se ha decidido implementar un sistema de información que almacene los siguientes datos:

* El propio **e-commerce** deberá guardar:
    * NIF
    * Nombre del comercio (Kangaroo)
    * Dirección (diccionario)

* Datos del **cliente** que se registra en la plataforma:
    * ID (Se añade de forma manual)
    * Nombre de usuario
    * Contraseña
    * Email
    * Nombre y apellidos
    * DNI
    * Direccion (diccionario)
    * Teléfono de contacto
    * Si el cliente ha sido recomendado

* Datos de el **proveedor** que suministra el producto:
    * NIF
    * Nombre / Empresa
    * Dirección (diccionario)
    * Contacto

* Información del **producto** de venta:
    * ID (Se añade de forma manual)
    * Nombre del producto
    * Especie asociada al producto
    * Categoria
    * Precio de venta

* Información del **pedido**:
    * ID (Se añade de forma manual)
    * Usuario que hace el pedido
    * Pedido (lista que a su vez contiene sublistas con los datos del propio pedido (nombre del producto, cantidad y precio))
    * Fecha en la que se ordenó el pedido (dia-mes-año)
    * Total (información con la cantidad total del pedido)
    * Estado (si ha sido pagado o no)

* Generar un nuevo **método de pago**:
    * Contiene un diccionario que a su vez tiene un ID de transacción (se añade de forma manual), el método de pago elegido, la fecha y hora de la transacción y el total.

    * Tipo de pago (se crea un objeto del tipo de método de pago cuando se quiera añadir este a su propio fichero de credenciales):
        * Bizum:
            * Teléfono
            * PIN
        * Paypal:
            * Email
            * Contraseña
        * Tarjeta:
            * Número tarjeta
            * Nombre
            * Fecha de caducidad
            * CVV


<hr>
<h6 align="center">IES ANA LUISA BENITEZ - DAW 2021-2022 (ETS / PRO)</h6>