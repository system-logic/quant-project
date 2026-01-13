# Experiment #1: Memory Optimization

## Goal

Understand how many resources are wasted by default and how much memory can be saved by deliberately choosing the correct (minimal sufficient) data type.

## Results  
1,000,000 elements comparison

| Data type   | Memory used | Savings compared to float64 | Relative size |
|-------------|-------------|-------------------------------|---------------|
| float64     | 7.63 MB     | 0% (baseline)                | 100%          |
| float32     | 3.81 MB     | **50%**                       | 50%           |
| int16       | 1.91 MB     | **75%**                       | 25%           |
| int8        | 0.95 MB     | **87.5%**                     | 12.5%         |

## Manifest Conclusion

> In quantum-scale computations we **always** choose the minimally sufficient data type.  
> If 15 decimal digits of precision are not required — **float32 is the rational default**.

## Infrastructure Decisions Log

### Environment & Interpreter

| Component           | Choice              | Rationale                                                                 |
|---------------------|---------------------|---------------------------------------------------------------------------|
| Python version      | **3.11**            | Significant performance improvements in core interpreter + stable scientific stack support (NumPy, Optuna, etc.) |
| Package manager     | **Conda**           | Much better handling of low-level dependencies (MKL, OpenBLAS, BLIS…)     |
| venv / pipenv / poetry | **Not used**      | In a resource-constrained world (Constraint #4) hardware-level optimization of math libraries is non-negotiable |

**Key principle:**  
When every byte and every flop counts — infrastructure choices are **not** aesthetic or convenience decisions.  
They are **performance & survival** decisions.