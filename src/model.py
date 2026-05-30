"""
Dismantled Mindset Theory — Network Simulation Model
Reference: Castro Quiles, F. (2025). SSRN 5824582.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional


@dataclass
class SimulationConfig:
    n_nodes: int = 10
    seed: int = 42
    alpha: float = 0.1
    beta: float = 0.05
    gamma: float = 0.3
    intervention_value: float = 0.1
    intervention_vector: Optional[object] = None
    n_steps: int = 50


class DismantledMindsetSimulation:
    """
    Fragmentation dynamics (Section 2.3):
        df_i/dt = alpha * (A^T @ (p * f)) - beta * I_i

    Power redistribution (Section 2.4):
        p_i(t+1) = (1 - gamma) * p_i(t) + gamma * mean(p(t))
    """

    def __init__(self, config: SimulationConfig = SimulationConfig()):
        self.config = config
        self._rng = np.random.default_rng(config.seed)
        self._init_state()
        self.history = []
        self.power_history = []
        self.metrics = {"avg_fragmentation": [], "avg_coherence": []}

    def _init_state(self):
        N = self.config.n_nodes
        self.p = self._rng.random(N)
        self.f = self._rng.random(N)
        self.A = self._rng.random((N, N))
        np.fill_diagonal(self.A, 0)

    @property
    def coherence(self):
        return 1.0 - self.f

    @property
    def avg_fragmentation(self):
        return float(np.mean(self.f))

    @property
    def avg_coherence(self):
        return float(np.mean(self.coherence))

    def _get_intervention(self):
        cfg = self.config
        if cfg.intervention_vector is not None:
            return np.asarray(cfg.intervention_vector, dtype=float)
        return np.full(cfg.n_nodes, cfg.intervention_value)

    def step(self):
        I = self._get_intervention()
        df = self.config.alpha * (self.A.T @ (self.p * self.f)) - self.config.beta * I
        self.f = np.clip(self.f + df, 0.0, 1.0)
        self.p = (1 - self.config.gamma) * self.p + self.config.gamma * np.mean(self.p)

    def run(self):
        for _ in range(self.config.n_steps):
            self.history.append(self.f.copy())
            self.power_history.append(self.p.copy())
            self.metrics["avg_fragmentation"].append(self.avg_fragmentation)
            self.metrics["avg_coherence"].append(self.avg_coherence)
            self.step()
        self.history.append(self.f.copy())
        self.power_history.append(self.p.copy())
        self.metrics["avg_fragmentation"].append(self.avg_fragmentation)
        self.metrics["avg_coherence"].append(self.avg_coherence)
        return self

    @property
    def fragmentation_matrix(self):
        return np.array(self.history)

    @property
    def power_matrix(self):
        return np.array(self.power_history)
