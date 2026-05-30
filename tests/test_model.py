import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
import pytest
from model import SimulationConfig, DismantledMindsetSimulation


def run(**kw):
    return DismantledMindsetSimulation(SimulationConfig(**kw)).run()


def test_defaults():
    cfg = SimulationConfig()
    assert cfg.n_nodes == 10 and cfg.n_steps == 50

def test_reproducible():
    assert np.array_equal(run(seed=0).fragmentation_matrix, run(seed=0).fragmentation_matrix)

def test_different_seeds_differ():
    assert not np.allclose(run(seed=1).fragmentation_matrix, run(seed=99).fragmentation_matrix)

def test_history_shape():
    sim = run(n_nodes=5, n_steps=20)
    assert sim.fragmentation_matrix.shape == (21, 5)
    assert sim.power_matrix.shape == (21, 5)

def test_fragmentation_bounded():
    assert np.all(run(n_nodes=15, n_steps=100).fragmentation_matrix <= 1)
    assert np.all(run(n_nodes=15, n_steps=100).fragmentation_matrix >= 0)

def test_metrics_length():
    assert len(run(n_steps=30).metrics["avg_fragmentation"]) == 31

def test_intervention_reduces_fragmentation():
    no_int = run(seed=42, beta=0.0, intervention_value=0.0)
    strong  = run(seed=42, beta=0.2, intervention_value=0.5)
    assert np.mean(strong.metrics["avg_fragmentation"]) < np.mean(no_int.metrics["avg_fragmentation"])

def test_power_convergence():
    P = run(seed=0, gamma=1.0, n_steps=5).power_matrix
    assert np.allclose(P[1], P[1, 0])

def test_custom_intervention_vector():
    iv = np.array([0.0, 0.5, 0.0, 0.5, 0.0, 0.5])
    sim = DismantledMindsetSimulation(SimulationConfig(n_nodes=6, intervention_vector=iv, seed=1)).run()
    assert sim.fragmentation_matrix.shape[1] == 6
