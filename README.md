# Training trajectory subspace replaceability numerical evidence

Supporting numerical records for **Partial Replaceability of Training-Trajectory Subspaces for Cross-Task Adaptation**, by Yan Lu and Jiaqi Gong. Release 0.1.0 covers the manuscript snapshot exported on 2026-11-13. This release accompanies a manuscript in preparation and is not a peer-reviewed publication. The release scope is frozen to that manuscript snapshot.

## Scope

This release contains saved scalar result tables and selected scientific metadata for the original rank/core/whole/partial comparisons, the three-history × target-update extension, and the exploratory diagnostics described in that manuscript's appendices. Included files retain all result rows, including negative outcomes and the KMNIST high-learning-rate reversal.

This is a **numerical evidence release**, not the complete development repository or an end-to-end reproduction package. Training code, datasets, model checkpoints, source trajectories, basis tensors and fixed batch schedules are not included. These omissions limit independent reproduction of training; no claim of complete reproducibility is made. Subsequent experiments outside the stated manuscript snapshot are outside this release and may be added in a versioned update.

## Layout

- `data/results/`: original experiment directory names, CSV result tables and selected JSON scientific metadata.
- `reproduce_summary.py`: a standalone Python standard-library script for recomputing the main extension summary from archived endpoints.
- `reproduced/`: outputs of that saved-record calculation.
- `DATA_FILES.csv`: per-file byte count, CSV row count and SHA-256.
- `SHA256SUMS`: checksums of all release files except this checksum file itself.

## Verify the main extension summary

```sh
python3 reproduce_summary.py
```

This reads all 366 formal epoch-60 endpoints and recomputes 32 accuracy contrasts, checking 128 archived mean/range/sign-count values. It also outputs the partial-family-minus-original-space comparison. The check concerns internal consistency of saved scalar records; it does not retrain or independently validate the experiments. The summary utility was prepared with assistance from OpenAI Codex and checked against the archived endpoint records.

Three source histories are the replication units. The two target tasks share those histories, and replacement draws are nested within each history. Calibration history C0 is separate from production histories H1–H3. A0 and Astar use the same ambient Adam procedure at different rates. Accuracy is a percentage; accuracy differences are percentage points. Cross-entropy units follow the original records.

## Metadata processing

Scalar CSV values are retained. Original local machine path prefixes in text metadata are replaced with `RESEARCH_REPO` and `LOCAL_HOME`; these are display placeholders, not executable paths. The two preflight records and the experiment plan retain scientific fields, while internal workflow/authorization/session metadata is omitted. Metadata preserves historical planning statements as historical records, not as statements of this release's current publication or review status.

## Dataset sources

The experiments use MNIST, Fashion-MNIST and Kuzushiji-MNIST. Dataset images are not redistributed here. Consult the original projects and their respective terms:

- MNIST: https://yann.lecun.org/exdb/mnist/
- Fashion-MNIST: https://github.com/zalandoresearch/fashion-mnist
- Kuzushiji-MNIST: https://github.com/rois-codh/kmnist

## Citation and licensing

Authors: Yan Lu (ORCID https://orcid.org/0009-0004-0940-0024) and Jiaqi Gong. A journal reference, preprint identifier or archival DOI will be added when available. No journal acceptance is implied.

No additional reuse license has been selected for this initial release. Public availability should not be interpreted as an unrestricted reuse grant. Authors can add a data/code license in a subsequent update.

## Research collection

This public numerical evidence package is maintained in [Yan Lu Research](https://github.com/yanlu-research). Each paper has its own repository as needed; the scope of this repository remains the selected results and metadata described above.

## Maintaining this release

Numerical and selected metadata files are exported from recorded internal experiment sources. Corrections should be made in the maintained source and released as a reviewed version; this public package is not an independently edited numerical database. Internal source and export hashes are checked before packaging. Repository documentation and citation metadata are maintained here.
