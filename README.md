## Citation & Related Publications

If you use this simulation in your research, please cite:

**Primary paper (2026):**
Castro Quiles, F. (2026). The Dismantled Mindset in the Age of Artificial Intelligence: Identity Fragmentation, Algorithmic Power, and a Framework for Collective Restoration. SSRN 6853702. DOI: https://doi.org/10.5281/zenodo.20466800

**Mathematical formalization (2025):**
Castro Quiles, F. (2025). A Mathematical Formalization and Simulation of the Dismantled Mindset Theory. SSRN 5824582. https://ssrn.com/abstract=5824582

**Original theory (2024):**
Castro Quiles, F. (2024). Exploring the Theory of a Dismantled Mindset: A Call for Collective Empowerment. SSRN 5040267. https://ssrn.com/abstract=5040267

**Book:**
Castro Quiles, F. (2025). Dismantled: A Theory of Broken Mindsets, A Blueprint of Infinite Futures. FC Quiles Books.

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20466800.svg)](https://doi.org/10.5281/zenodo.20466800)

# Dismantled Mindset Theory: Mathematical Simulation

Python implementation of the network model from:

Castro Quiles, F. (2025). A Mathematical Formalization and Simulation of the Dismantled Mindset Theory. SSRN 5824582.

## Overview

This repository provides a quantitative simulation of the Dismantled Mindset Theory, modeling fragmentation dynamics, influence propagation, and power redistribution in directed weighted social networks.

## Installation

    pip install -r requirements.txt

## Usage

    # Run with paper defaults (N=10, T=50)
    python run_simulation.py

    # Custom parameters
    python run_simulation.py --nodes 20 --steps 100 --gamma 0.5

    # Include scenario comparison
    python run_simulation.py --scenarios

## Mathematical Model

Symbol      Meaning
p_i         Power of node i, in [0,1]
f_i         Fragmentation of node i, in [0,1]
c_i=1-f_i   Coherence of node i
A_ij        Influence weight from node i to node j

Fragmentation dynamics:
    df_i/dt = alpha * (A^T @ (p * f)) - beta * I_i

Power redistribution:
    p_i(t+1) = (1 - gamma) * p_i(t) + gamma * mean(p(t))

## Repository Structure

    src/model.py         Core simulation logic
    src/visualise.py     Plot generation
    src/scenarios.py     Intervention scenario comparison
    tests/test_model.py  Unit tests
    run_simulation.py    Command-line entry point

## Tests

    pytest tests/ -v

## CLI Options

    --nodes        Number of nodes N          (default: 10)
    --steps        Time steps T               (default: 50)
    --alpha        Fragmentation rate         (default: 0.1)
    --beta         Intervention damping       (default: 0.05)
    --gamma        Power redistribution rate  (default: 0.3)
    --intervention Uniform intervention value (default: 0.1)
    --seed         Random seed                (default: 42)
    --out          Output directory           (default: results/)
    --show         Display figures interactively
    --scenarios    Run scenario comparison

## References

1. Castro Quiles, F. (2025). Exploring the Theory of a Dismantled Mindset: A Call for Collective Empowerment. SSRN 5040267.
2. Newman, M.E.J. Networks: An Introduction. Oxford University Press, 2010.
3. Barabasi, A.-L. Network Science. Cambridge University Press, 2016.

## License

MIT

## Related paper: 

https://doi.org/10.5281/zenodo.20466800

Add citation and publication references
