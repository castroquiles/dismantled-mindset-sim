"""Scenario comparison: baseline vs. intervention strategies."""

import os
import numpy as np
import matplotlib.pyplot as plt
import sys; sys.path.insert(0, os.path.dirname(__file__))
from model import SimulationConfig, DismantledMindsetSimulation


def run_scenarios(save_path=None, show=True):
    N = 10
    targeted = np.zeros(N); targeted[:N//2] = 0.3

    scenarios = {
        "No intervention":          SimulationConfig(beta=0.0, intervention_value=0.0),
        "Baseline (paper default)": SimulationConfig(beta=0.05, intervention_value=0.1),
        "Strong uniform":           SimulationConfig(beta=0.1,  intervention_value=0.2),
        "Targeted (top-half)":      SimulationConfig(beta=0.1,  intervention_vector=targeted),
        "High redistribution":      SimulationConfig(gamma=0.6, intervention_value=0.1),
    }

    results = {name: DismantledMindsetSimulation(cfg).run() for name, cfg in scenarios.items()}

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    colours = plt.cm.tab10(np.linspace(0, 0.9, len(results)))

    for (name, sim), colour in zip(results.items(), colours):
        steps = np.arange(len(sim.metrics["avg_fragmentation"]))
        axes[0].plot(steps, sim.metrics["avg_fragmentation"], label=name, color=colour, linewidth=1.8)
        axes[1].plot(steps, sim.metrics["avg_coherence"],     label=name, color=colour, linewidth=1.8)

    for ax, title in zip(axes, ["Avg Fragmentation $\\bar{F}$", "Avg Coherence $\\bar{C}$"]):
        ax.set_xlabel("Time Step"); ax.set_title(title)
        ax.set_ylim(0, 1); ax.grid(alpha=0.3); ax.legend(fontsize=8)

    fig.suptitle("Scenario Comparison — Dismantled Mindset Simulation"); fig.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        fig.savefig(save_path, dpi=150)
    if show: plt.show()
    return results


if __name__ == "__main__":
    run_scenarios(save_path="results/scenario_comparison.png", show=False)
    print("Saved to results/scenario_comparison.png")
