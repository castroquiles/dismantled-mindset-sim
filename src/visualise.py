"""Visualisation utilities for the Dismantled Mindset simulation."""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plot_fragmentation_lines(sim, save_path=None, show=True):
    F = sim.fragmentation_matrix
    T, N = F.shape
    fig, ax = plt.subplots(figsize=(10, 5))
    colours = cm.get_cmap("tab10", N)
    for i in range(N):
        ax.plot(np.arange(T), F[:, i], label=f"Node {i}", color=colours(i), linewidth=1.8)
    ax.set_xlabel("Time Step"); ax.set_ylabel("Fragmentation $f_i$")
    ax.set_title("Node Fragmentation Dynamics over Time")
    ax.legend(loc="upper right", fontsize=8, ncol=2); ax.set_ylim(0, 1); ax.grid(alpha=0.3)
    fig.tight_layout()
    if save_path: fig.savefig(save_path, dpi=150)
    if show: plt.show()
    return fig


def plot_fragmentation_heatmap(sim, save_path=None, show=True):
    F = sim.fragmentation_matrix
    fig, ax = plt.subplots(figsize=(10, 6))
    img = ax.imshow(F.T, aspect="auto", cmap="viridis", origin="lower", vmin=0, vmax=1)
    fig.colorbar(img, ax=ax).set_label("Fragmentation $f_i$")
    ax.set_xlabel("Time Step"); ax.set_ylabel("Node")
    ax.set_title("Heatmap of Node Fragmentation over Time")
    ax.set_yticks(range(F.shape[1]))
    ax.set_yticklabels([f"Node {i}" for i in range(F.shape[1])], fontsize=8)
    fig.tight_layout()
    if save_path: fig.savefig(save_path, dpi=150)
    if show: plt.show()
    return fig


def plot_global_metrics(sim, save_path=None, show=True):
    m = sim.metrics
    steps = np.arange(len(m["avg_fragmentation"]))
    fig, ax1 = plt.subplots(figsize=(10, 4))
    ax2 = ax1.twinx()
    ax1.plot(steps, m["avg_fragmentation"], color="#e74c3c", linewidth=2, label="Avg Fragmentation")
    ax2.plot(steps, m["avg_coherence"], color="#2ecc71", linewidth=2, linestyle="--", label="Avg Coherence")
    ax1.set_xlabel("Time Step"); ax1.set_ylabel("Avg Fragmentation", color="#e74c3c")
    ax2.set_ylabel("Avg Coherence", color="#2ecc71")
    ax1.set_ylim(0, 1); ax2.set_ylim(0, 1); ax1.grid(alpha=0.3)
    lines = ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
    labels = ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
    ax1.legend(lines, labels, loc="upper right")
    fig.suptitle("Global Network Metrics over Time"); fig.tight_layout()
    if save_path: fig.savefig(save_path, dpi=150)
    if show: plt.show()
    return fig


def plot_power_redistribution(sim, save_path=None, show=True):
    P = sim.power_matrix
    T, N = P.shape
    fig, ax = plt.subplots(figsize=(10, 5))
    colours = cm.get_cmap("tab10", N)
    for i in range(N):
        ax.plot(np.arange(T), P[:, i], label=f"Node {i}", color=colours(i), linewidth=1.8)
    ax.axhline(np.mean(P[0]), color="black", linewidth=1.5, linestyle=":", label="Initial mean")
    ax.set_xlabel("Time Step"); ax.set_ylabel("Power $p_i$")
    ax.set_title("Power Redistribution over Time")
    ax.legend(loc="upper right", fontsize=8, ncol=2); ax.set_ylim(0, 1); ax.grid(alpha=0.3)
    fig.tight_layout()
    if save_path: fig.savefig(save_path, dpi=150)
    if show: plt.show()
    return fig


def save_all(sim, out_dir="results"):
    os.makedirs(out_dir, exist_ok=True)
    plot_fragmentation_lines(sim,   save_path=f"{out_dir}/fragmentation_lines.png",  show=False)
    plot_fragmentation_heatmap(sim, save_path=f"{out_dir}/fragmentation_heatmap.png", show=False)
    plot_global_metrics(sim,        save_path=f"{out_dir}/global_metrics.png",        show=False)
    plot_power_redistribution(sim,  save_path=f"{out_dir}/power_redistribution.png",  show=False)
    print(f"All figures saved to '{out_dir}/'")
