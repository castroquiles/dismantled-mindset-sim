#!/usr/bin/env python3
"""CLI entry point — replicates all figures from SSRN 5824582.

Usage:
  python run_simulation.py
  python run_simulation.py --nodes 20 --steps 100 --gamma 0.5
  python run_simulation.py --scenarios --show
"""

import argparse, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from model import SimulationConfig, DismantledMindsetSimulation
from visualise import save_all
from scenarios import run_scenarios


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--nodes",        type=int,   default=10)
    p.add_argument("--steps",        type=int,   default=50)
    p.add_argument("--alpha",        type=float, default=0.1)
    p.add_argument("--beta",         type=float, default=0.05)
    p.add_argument("--gamma",        type=float, default=0.3)
    p.add_argument("--intervention", type=float, default=0.1)
    p.add_argument("--seed",         type=int,   default=42)
    p.add_argument("--out",          type=str,   default="results")
    p.add_argument("--show",         action="store_true")
    p.add_argument("--scenarios",    action="store_true")
    args = p.parse_args()

    print(f"\n  N={args.nodes}  T={args.steps}  α={args.alpha}  β={args.beta}  γ={args.gamma}\n")

    cfg = SimulationConfig(n_nodes=args.nodes, n_steps=args.steps, alpha=args.alpha,
                           beta=args.beta, gamma=args.gamma,
                           intervention_value=args.intervention, seed=args.seed)
    sim = DismantledMindsetSimulation(cfg).run()

    print(f"  Final avg fragmentation : {sim.metrics['avg_fragmentation'][-1]:.4f}")
    print(f"  Final avg coherence     : {sim.metrics['avg_coherence'][-1]:.4f}\n")

    save_all(sim, out_dir=args.out)

    if args.scenarios:
        run_scenarios(save_path=f"{args.out}/scenario_comparison.png", show=args.show)

    print("Done.")

if __name__ == "__main__":
    main()
