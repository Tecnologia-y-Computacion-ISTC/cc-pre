
# Semana 1 - Dia 1: Lógica Proporsional

## Que Hice

en este ejercicio, he completado las siguientes tareas relacionadas con la logica proporciobnal:

- Creee un alista de 10 proposiones del mundo real e identifique su valor de verdad.
- Construi las tablas de verdad para la conjucion ( `p ∧ q` ), disyuncion ( `p ∨ q` ) , implicacion ( `p → q` ) y la bicondicional ( `p ↔ q` ), y prueba de Ley morgan ( `¬(p ∧ q) ≡ ¬p ∨ ¬q` y `¬(p ∨ q) ≡ ¬p ∧ ¬q` ).
- Desarrolle un programa en python `truth_tables.py` para generar y mostrar automaticamente la tablas de verdad  para las operaciones logicas principales

## Cómo correr el Código

Para ejecutar el programa, asegúrate de tener Python instalado. Luego, abre una terminal, navega hasta el directorio del archivo y ejecuta el siguiente comando:
`python truth_tables.py`

## Ejemplo de Salida

La ejecución del script `truth_tables.py` produce la siguiente salida en la consola:

  p       q     p AND q  p OR q  p -> q
False - False - False  - False - True
False - True  - False  - True  - True
True  - False - False  - True  - False
True  - True  - True   - True  - True
