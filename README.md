# ScrewPY

**Autor:** José Adrián Rodríguez González  

ScrewPY es una librería para el cálculo de **tornillos en la teoría helicoidal**, ampliamente utilizada en **cinemática y dinámica de robots**.  
Proporciona estructuras matemáticas claras y operaciones algebraicas bien definidas para trabajar con:

- Vectores
- Tornillos clásicos
- Tornillos de Plücker
- Matrices de tornillos

---

## Instalación

> ⚠️ La librería se encuentra en desarrollo.  
> El proceso de instalación será documentado cuando se publique oficialmente en PyPI.

Una vez instalada, se importa de la siguiente forma:

```python
import screw as sc
```

---

## Módulos disponibles

ScrewPY está organizado en los siguientes módulos:

- `Vectors`
- `Screw`
- `PluckerScrew`
- `MatrixScrew`

### Forma directa (recomendada)

```python
from screw.vector import Vectors
v1 = Vectors(1, 2, 3)
```

---

## Vectors

### Creación de un vector

```python
from screw.vector import Vectors

v1 = Vectors(1, 2, 3)
v2 = Vectors((1, 2, 3))
v3 = Vectors([1, 2, 3])
```

### Longitud del vector

```python
print(len(v1))
```

Salida:

```
3
```

### Representación

```python
print(v1)
```

```
Vector(1,2,3)
```

---

## Operaciones vectoriales

### Suma

```python
v1 = Vectors(1,2,3)
v2 = Vectors(2,4,6)
v3 = v1 + v2
print(v3)
```

```
Vector(3,6,9)
```

---

## Screw

Un tornillo se define como:

\[
S =
\begin{bmatrix}
\mathbf{W} \\
\mathbf{V}
\end{bmatrix}
\in \mathbb{R}^6
\]

### Definición

```python
from screw.screw import Screw

S1 = Screw([1,2,3], [3,4,5])
```

---

## Plücker Screw

```python
from screw.PluckerScrew import PluckerScrew

Ps = PluckerScrew([1,1,1], [1,2,3], 10, "R")
```

---

## MatrixScrew

```python
from screw.MatrixScrew import MatrixScrew

M = MatrixScrew(6)
```

---

## Licencia

Pendiente de definir.
