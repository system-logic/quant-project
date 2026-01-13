## Experiment #1: Memory Optimization

**Goal:**  
Understand how many resources are wasted by default and how much memory can be saved by choosing the correct data type.

**Results for 1,000,000 elements:**

- **float64** — 7.63 MB *(default standard)*
- **float32** — 3.81 MB *(50% memory savings)*
- **int16** — 1.91 MB *(75% memory savings)*
- **int8** — 0.95 MB *(87.5% memory savings)*

**Manifest Conclusion:**  
In quantum-scale computations, we always choose the minimally sufficient data type.  
If 15 decimal digits of precision are not required, `float32` is the rational choice.
