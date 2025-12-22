# Kabosu

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Aridoge13/Kabosu)

---

## Overview

**Kabosu** is a research framework for studying **robust disease risk modeling across heterogeneous public datasets**, with a long-term goal of **biologically grounded, multi-modal integration**.

The project deliberately prioritizes:
- data understanding over premature modeling  
- cross-dataset synthesis over single-dataset performance  
- biological constraints over metric chasing  

**Kabosu** is a research framework for studying **robust disease risk modeling across heterogeneous public datasets**, with a long-term goal of **biologically grounded, multi-modal integration**.

The project deliberately prioritizes:
- data understanding over premature modeling  
- cross-dataset synthesis over single-dataset performance  
- biological constraints over metric chasing  

Kabosu is **not a clinical or diagnostic tool** and makes **no diagnostic or therapeutic claims**.  

Its long-term research objective is to inform the development of **transparent, biologically constrained decision-support methodologies** that could, in the future, contribute to clinician-facing systems after appropriate validation.


---

## Project Philosophy

**Do Only Good Everyday**: a commitment to methodological rigor, transparency, and harm minimization in computational health research.

Most ML-for-health projects fail because they:
- overfit single datasets
- ignore dataset shift
- treat genomics as feature concatenation
- optimize metrics instead of understanding failure modes

Kabosu is explicitly designed to avoid these traps.

Core principles:
- **Analysis before models**
- **Synthesis before integration**
- **Ablation before expansion**
- **Biology as constraint, not decoration**


---

## Versioned Roadmap (Authoritative)

### v0.1 – v0.6: Dataset-local analysis (Tabular only)
Each public dataset is analyzed **in isolation** to identify:
- signal vs noise
- label instability
- feature fragility
- dataset-specific artefacts

No cross-dataset modeling.  
No genomics.

Deliverables:
- dataset reports
- negative results
- failure characterizations

---

### v0.7 – v0.8: Cross-dataset synthesis
Insights from multiple tabular datasets are synthesized to study:
- feature equivalence classes
- stability across populations
- agreement / disagreement in direction of effect
- domain shift behavior

This phase is **analysis**, not model building.

---

### v0.9: Unified tabular abstraction
A single tabular model is constructed **only after synthesis** to test:
- whether abstractions generalize
- which signals survive dataset shift

This model is diagnostic, not final.

---

### v1.0 – v1.9: Progressive genomic integration
Genomic data is integrated **incrementally**, not all at once.

Each genomic modality is admitted **only if it addresses a documented failure** from earlier versions.

Planned progression:
- Genetic risk layers (e.g. GWAS-level summaries)
- Expression / regulatory signals
- Pathway and network constraints
- Interaction-aware biological structure

Every layer is stress-tested and ablated.

---

### v2.0: Consolidated system
v2.0 is a **minimal, biologically constrained framework** containing:
- only components that survived ablation
- documented contributions and failure modes
- explicit limits of validity

---

## Current Status

**Status:** Active research development  
**Current focus:** v0.x dataset-local analysis and synthesis

What Kabosu currently does:
- exploratory and confirmatory analysis of public tabular health datasets
- investigation of feature stability and dataset shift
- controlled experiments on synthetic adversarial test data

What Kabosu does **not** yet do:
- clinical prediction
- multi-omics integration
- deployment-facing inference

---

## Synthetic Testing Strategy

Synthetic data is used **only** for adversarial testing:
- covariate shift
- label noise injection
- missing-not-at-random simulation
- spurious correlation stress tests

Synthetic agreement alone is **not considered validation**.

---

## Technical Stack (subject to change)

| Component | Tools |
|---------|------|
| Data analysis | pandas, numpy |
| ML (experimental) | scikit-learn, lightgbm |
| Visualization | matplotlib, seaborn |
| Workflow (planned) | Snakemake |
| Genomics (future) | biopython, pysam |

Dependencies evolve with project phases.

---

## Installation (Development)

```bash
git clone https://github.com/Aridoge13/Kabosu
cd Kabosu

conda create -n kabosu python=3.9
conda activate kabosu

pip install pandas numpy matplotlib seaborn scikit-learn
```

## Contributions

This is a research-driven project.

Contributions are welcome **if they align with the project philosophy**:
- reproducibility over novelty
- analysis over hype
- clarity over performance claims

Open an issue before major contributions.

## License

MIT License: [LICENSE](License.md)

## Contact
Email: aritra.mukherjee98@gmail.com
Linkedin: www.linkedin.com/in/aritra-mukherjee-82b070125
ORCID: https://orcid.org/0000-0002-6061-611X