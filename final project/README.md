# Final Project / Undergraduate Thesis Proposal: A Study on Undergraduate Major Similarity and Transferability Based on DACP+SFT

## Abstract
This paper proposes a quantitative analysis method for measuring similarity and knowledge transferability between undergraduate majors based on a masked pre-trained language model. Using RoBERTa as the base model, the method takes E-commerce and Logistics Engineering as examples. Domain-adaptive continual pre-training is conducted separately on the textbook corpus of the two related undergraduate majors, simulating from a computational perspective the outcomes of students’knowledge internalization within a specific disciplinary system. On this basis, two domain-specific major discrimination models are trained by supervised fine-tuning on corresponding true/false question datasets (a binary classification task) for each major......


## 1. Proposed Methodology
- **Base Model**: RoBERTa.
- **Domain-Adaptive Continued Pretraining (DACP)**: On crawled corpora from two sub-disciplines.
- **Parameter-Efficient Fine-Tuning (PEFT)**: Using LoRA or its variants to efficiently adapt the model for a specific task, meanwhile as a analogy to human brains adapting to tasks (e.g., correctness judgment on exam-like questions).
......

## 2. Relation to CS224n
- This project directly builds upon the concepts learned in CS224n, including but not limited to:
    - **Word Vector Representations** (Lecture 1)
    - **Neural Network Training** (Lectures 2 & 3)
    - **Model Efficiency and Adaptation** (related to practical deployment considerations discussed throughout the course)

## 3. Project Timeline
- [✅] Literature Review
- [✅] Data Collection
- [✅] Data Preprocessing
- [ ] Baseline Model Implementation (Planned)
- [ ] ... (Other phases)

## 4. References
[1] VASWANI A, SHAZEER N, PARMAR N, et al. Attention Is All You Need[EB/OL].
2023. https://arxiv.org/abs/1706.03762. arXiv: 1706.03762 [cs.CL].
[2] DEVLIN J, CHANG M W, LEE K, et al. BERT: Pre-training of Deep Bidirectional Trans-
formers for Language Understanding[EB/OL]. 2019. https://arxiv.org/abs/1810.04805.
arXiv: 1810.04805 [cs.CL].
[3] LIU Y, OTT M, GOYAL N, et al. RoBERTa: A Robustly Optimized BERT Pretraining
Approach[EB/OL]. 2019. https://arxiv.org/abs/1907.11692. arXiv: 1907.11692 [cs.CL].
[4] PAN S J, YANG Q. A survey on transfer learning[J]. IEEE Transactions on knowledge
and data engineering, 2009, 22(10): 1345-1359.
[5] GURURANGAN S, MARASOVIĆ A, SWAYAMDIPTA S, et al. Don’t stop pretraining:
Adapt language models to domains and tasks[C]//Proceedings of the 58th annual meeting
of the association for computational linguistics. 2020: 8342-8360.
[6] RADFORD A, NARASIMHAN K, SALIMANS T, et al. Improving language under-
standing by generative pre-training[J]. 2018.
[7] OUYANG L, WU J, JIANG X, et al. Training language models to follow instructions
with human feedback[J]. Advances in neural information processing systems, 2022, 35:
27730-27744.
[8] 李航. 统计学习方法[J]. 2019.
[9] FIRTH J. A synopsis of linguistic theory, 1930-1955[J]. Studies in linguistic analysis,
1957: 10-32.
[10] MIKOLOV T, CHEN K, CORRADO G, et al. Efficient estimation of word representa-
tions in vector space[J]. arXiv preprint arXiv:1301.3781, 2013.
[11] SINHA K, JIA R, HUPKES D, et al. Masked language modeling and the distributional
hypothesis: Order word matters pre-training for little[C]//Proceedings of the 2021 con-
ference on empirical methods in natural language processing. 2021: 2888-2913.
[12] DENG J, DONG W, SOCHER R, et al. Imagenet: A large-scale hierarchical image
database[C]//2009 IEEE conference on computer vision and pattern recognition. 2009:
248-255.
[13] KRIZHEVSKY A, SUTSKEVER I, HINTON G E. Imagenet classification with deep
convolutional neural networks[J]. Advances in neural information processing systems,
2012, 25.
[14] ERHAN D, COURVILLE A, BENGIO Y, et al. Why does unsupervised pre-training help
deep learning?[C]//Proceedings of the thirteenth international conference on artificial in-
telligence and statistics. 2010: 201-208.
[15] LAMPINEN A K, GANGULI S. An analytic theory of generalization dynamics and
transfer learning in deep linear networks[J]. arXiv preprint arXiv:1809.10374, 2018.
[16] KAPLAN J, MCCANDLISH S, HENIGHAN T, et al. Scaling laws for neural language
models[J]. arXiv preprint arXiv:2001.08361, 2020.
[17] HOFFMANN J, BORGEAUD S, MENSCH A, et al. Training compute-optimal large
language models[J]. arXiv preprint arXiv:2203.15556, 2022, 10.
[18] SUN C, QIU X, XU Y, et al. How to fine-tune bert for text classification?[C]//China
national conference on Chinese computational linguistics. 2019: 194-206.
[19] LEE J, YOON W, KIM S, et al. BioBERT: a pre-trained biomedical language represen-
tation model for biomedical text mining[J]. Bioinformatics, 2020, 36(4): 1234-1240.
[20] LibreTexts. LibreTexts[EB/OL]. 2026. https://libretexts.org/.
[21] Docling Team. Docling[CP/OL]. https://github.com/docling-project/docling.
[22] CHEN D, HUANG Y, PAN X, et al. Data-Juicer 2.0: Cloud-Scale Adaptive Data Pro-
cessing for and with Foundation Models[J]. NeurIPS, 2025.
[23] HU E J, SHEN Y, WALLIS P, et al. LoRA: Low-Rank Adaptation of Large Language
Models[EB/OL]. 2021. https://arxiv.org/abs/2106.09685. arXiv: 2106.09685 [cs.CL].
[24] Hugging Face. Adapters on the Hugging Face Hub[Z]. https://huggingface.co/docs/hub
/adapters. Accessed: 2026-04-22. 2024.
[25] MILL R D, COLE M W. Dynamically Shifting from Compositional to Conjunctive
Brain Representations Supports Cognitive Task Learning[J/OL]. Nature Communica-
tions, 2025, 16: 10084. https://doi.org/10.1038/s41467- 025- 65041- 2. DOI: 10.103
8/s41467-025-65041-2.
[26] FLESCH T, JUECHEMS K, DUMBALSKA T, et al. Orthogonal representations for
robust context-dependent task performance in brains and neural networks[J/OL]. Neuron,2022, 110(7): 1258-1270.e11. https://www.sciencedirect.com/science/article/pii/S0896627322000058. DOI: https://doi.org/10.1016/j.neuron.2022.01.005
...