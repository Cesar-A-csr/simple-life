# Manual Técnico Simple Life

## Arquitectura General del Sistema

El código implementa un juego de simulación en bucle continuo (Game Loop) mediante consola en Python. Maneja el estado mediante variables globales simples (diccionarios para atributos mutables) e interacciones mediante entrada/salida estándar (input() / print()).

El flujo general se resume en:

- Inicialización: Lectura y validación del nombre del personaje; inicialización de estado de jugador y tiempo.
- Ciclo Principal (while True):
- Generación de inventario del mercado (valores dinámicos usando random).
- Mapeo y presentación de datos.
- Captura de decisiones de compra con validación estricta de tipos y rangos.
- Recálculo de atributos (dinero, hambre, tiempo).
- Verificación de condiciones de fin de juego o de parada opcional.

## Estructuras de Datos

dict_jugador:   
Almacena el estado persistente de las variables financieras y físicas del personaje.

```
dict_jugador = {    
    "nombre": str,        # Identificador ingresado por el usuario   
    "dinero": float,      # Saldo disponible (inicia en 365)  
    "hambre": float,      # Acumulador de déficit nutricional (0 a 100)  
    "renta": int,         # Gasto fijo mensual aleatorio [100, 300]  
    "salario": int        # Ingreso quincenal aleatorio [275, 365]   
}
```

dict_tiempo:    
Controla el avance temporal dentro de la simulación.

```
dict_tiempo = {     
    "dia": int,                    # Día dentro del mes actual (1 a 30)   
    "dias transcurridos": int,     # Contador total acumulativo de días   
    "semanas transcurridas": int,  # Truncamiento entero: días // 7   
    "meses trancurridos": int      # Truncamiento entero: días // 30  
}
```

dict_producto (Generado por iteración):     
Estructura anidada recalculada dinámicamente al inicio de cada día para variar la oferta del mercado.

```
dict_producto = {   
    "<nombre_producto>": {  
        "cantidad": int,   # Disponibilidad aleatoria   
        "precio": float,   # Costo unitario en rango con decimales redondeados  
        "saciedad": float, # Unidades de energía recuperable por unidad     
        "tipo": str        # Categoría ("fruta" | "verdura")    
    }   
}
```

## Lógica de Funciones y Algoritmos clave

Validación de Entrada (Nombre del Jugador)  
Utiliza .strip() para descartar espacios en blanco y el operador not para forzar un nombre válido antes de avanzar.

```
nombre_jugador = input("Ingresa el nombre de tu personaje: ").strip()
while not nombre_jugador:
    nombre_jugador = input("...").strip()
```

Modificación de Parámetros de Hambre    
El hambre se calcula restando la energía recuperada a la energía gastada aleatoriamente en el día, previniendo valores negativos mediante max():

```
hambre = max(0, hambre + energia_gastada − energia_recuperada)
```

Actualización Económica     
Día 1: gasto = renta + total_compra     
Días 15 y 30: dinero = dinero + salario     
Redondeo sistemático: Se emplea `round(val, 2)` en operaciones numéricas con punto flotante para prevenir imprecisiones de representación de coma flotante.

## Manejo de Excepciones
El sistema incluye bloques try-except especificando ValueError en dos momentos críticos:

Selección del Producto:     
Captura entradas no numéricas (ej. texto).  
Valida el rango permitido: 1 <= opcion <= len(ls_claves_producto).

Cantidad a Comprar:     
Previene valores menor o iguales a 0 (cantidad_elegida <= 0).   
Evita sobrecompra comparando contra la cantidad disponible en el mercado (cantidad_elegida > cantidad_disponible).

## Condiciones de Fin de Juego (Game Over)
El ciclo while principal rompe la ejecución bajo tres circunstancias:

- Decision voluntaria: seguir != 's' al completar el día 30 (un mes).     
- Bancarrota: dict_jugador["dinero"] <= 0.    
- Colapso físico: dict_jugador["hambre"] >= 100.