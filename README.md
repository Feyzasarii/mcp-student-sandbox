# mystery_module.py

`mystery_module.py` is a focused utility module for solving quadratic equations of the form:

```
ax² + bx + c = 0
```

## What it does

The module exposes a single function, `fn_x(a, b, c)`, which calculates the real roots of a quadratic polynomial using the quadratic formula.

If the equation has two real solutions, the function returns a tuple containing both roots. If the discriminant is negative and no real roots exist, the function returns `None`.

## Function signature

```python
fn_x(a, b, c)
```

### Parameters

- `a` (`int | float`): coefficient of `x²`
- `b` (`int | float`): coefficient of `x`
- `c` (`int | float`): constant term

### Returns

- `tuple[float, float]` when the equation has two real solutions
- `None` when no real solutions exist

## Usage example

```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)
if roots is None:
    print("No real roots available.")
else:
    x1, x2 = roots
    print(f"Roots: {x1}, {x2}")
```

## Behavior details

- Computes the discriminant: `d = b**2 - 4*a*c`
- If `d < 0`, returns `None`
- Otherwise, returns:

```python
((-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a))
```

## Notes

- The function assumes `a` is non-zero for a valid quadratic equation.
- This module is intentionally small and purpose-built for quadratic root calculation.

## Dependencies

- Python standard library: `math`
