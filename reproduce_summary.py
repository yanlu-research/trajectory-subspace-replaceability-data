"""Recompute archived summary contrasts from saved endpoints; no ML dependencies.

Run: python3 reproduce_summary.py
This does not train models, read datasets, or validate the original experiment.
"""
from pathlib import Path
import csv
import math
from statistics import mean

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data/results/reuse-history-optimizer-20261026'


def read(path):
    with path.open(newline='') as handle:
        return list(csv.DictReader(handle))


def save(path, rows):
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    endpoints = read(DATA / 'archive-20261030/endpoint-extract.csv')
    assert len(endpoints) == 366
    assert all(r['status'] == 'complete' for r in endpoints)
    contrasts = []
    partial_vs_original = []
    for target in ('kmnist', 'mnist'):
        for condition in ('A0', 'Astar', 'Sstar', 'Cstar'):
            histories = []
            partial_differences = []
            for history in ('H1', 'H2', 'H3'):
                arms = [r for r in endpoints if (r['target'], r['condition'], r['history']) == (target, condition, history)]
                assert len(arms) == 15
                acc = {r['space']: float(r['target_accuracy']) for r in arms}
                h, ht = acc['H20'], acc['HT60']
                p = [acc[f'P{i:02}'] for i in range(1, 4)]
                w = [acc[f'W{i:02}'] for i in range(1, 11)]
                histories.append({'HT_minus_H': ht-h, 'P_mean_minus_H': mean(p)-h,
                                  'HT_minus_W_mean': ht-mean(w), 'P_mean_minus_W_mean': mean(p)-mean(w)})
                partial_differences.append(mean(p)-ht)
            for name in histories[0]:
                values = [h[name] for h in histories]
                contrasts.append({'target': target, 'condition': condition, 'contrast': name,
                                  'mean_if_all_histories_complete': mean(values), 'min': min(values),
                                  'max': max(values), 'positive_histories': sum(v > 0 for v in values)})
            partial_vs_original.append({'target': target, 'condition': condition,
                                        'partial_mean_minus_HT60_pp': mean(partial_differences)})
    expected = {(r['target'], r['condition'], r['contrast']): r for r in read(DATA / 'history_summary.csv')}
    assert len(expected) == len(contrasts) == 32
    checked = 0
    for row in contrasts:
        old = expected[row['target'], row['condition'], row['contrast']]
        for name in ('mean_if_all_histories_complete', 'min', 'max', 'positive_histories'):
            assert math.isclose(float(row[name]), float(old[name]), rel_tol=0, abs_tol=1e-9), (row, old)
            checked += 1
    out = ROOT / 'reproduced'
    out.mkdir(exist_ok=True)
    save(out / 'history_summary_recomputed.csv', contrasts)
    save(out / 'partial_vs_original_recomputed.csv', partial_vs_original)
    print(f'PASS: {len(endpoints)} saved endpoints; {len(contrasts)} contrasts; {checked} archived summary values agree.')
    print('Scope: consistency of saved scalar records only; not independent scientific reproduction.')


if __name__ == '__main__':
    main()
