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
[1] DAAD. Database on Admission Requirements[EB/OL]. German Academic Exchange
Service. (2024-12-20). https://www.daad.de/en/studying-in-germany/requirements/adm
ission-database/.

[2] European Commission. European Credit Transfer and Accumulation System (ECTS)
[EB/OL]. European Commission. (2024-12-20) [2026-04-24]. https://education.ec.eu
ropa.eu/education-levels/higher-education/inclusive-and-connected-higher-education/e
uropean-credit-transfer-and-accumulation-system.

[3] MONTT G. The Causes and Consequences of Field-of-Study Mismatch: An Analysis
Using PIAAC[R/OL]. OECD Social, Employment and Migration Working Papers 167.
Paris: OECD Publishing, 2015. https://doi.org/10.1787/5jrxm4dhv9r2-en. DOI: 10.178
7/5jrxm4dhv9r2-en.

[4] JIANG S, GUO Y. Reasons for college major-job mismatch and labor market outcomes:
Evidence from China[J/OL]. China Economic Review, 2022, 74: 101822. https://www.s
ciencedirect.com/science/article/pii/S1043951X22000803. DOI: https://doi.org/10.1016
/j.chieco.2022.101822.

[5] HEMELT S W, HERSHBEIN B, MARTIN S, et al. College Majors and Skills: Evidence
from the Universe of Online Job Ads[J/OL]. Labour Economics, 2023, 85: 102429. http
s://doi.org/10.1016/j.labeco.2023.102429. DOI: 10.1016/j.labeco.2023.102429.

[6] Lightcast. Lightcast Data[EB/OL]. Lightcast. (2024-12-20). https://lightcast.io/products
/data/overview.

[7] BERĘSEWICZ M, CHERNIAIEV H, MANTAJ A, et al. Text Analysis of Job Offers for
Mismatch of Educational Characteristics to Labour Market Demands[J/OL]. Quality &
Quantity, 2024, 58: 1799-1825. eprint: 10.1007/s11135-023-01707-7. DOI: 10.1007/s1
1135-023-01707-7.

[8] DEVLIN J, CHANG M W, LEE K, et al. BERT: Pre-training of Deep Bidirectional Trans-
formers for Language Understanding[EB/OL]. 2019. https://arxiv.org/abs/1810.04805.
arXiv: 1810.04805 [cs.CL].

[9] LIU Y, OTT M, GOYAL N, et al. RoBERTa: A Robustly Optimized BERT Pretraining
Approach[EB/OL]. 2019. https://arxiv.org/abs/1907.11692. arXiv: 1907.11692 [cs.CL].

[10] GURURANGAN S, MARASOVIĆ A, SWAYAMDIPTA S, et al. Don’t stop pretraining:
Adapt language models to domains and tasks[C]//Proceedings of the 58th annual meeting
of the association for computational linguistics. 2020: 8342-8360.

[11] VASWANI A, SHAZEER N, PARMAR N, et al. Attention Is All You Need[EB/OL].
2023. https://arxiv.org/abs/1706.03762. arXiv: 1706.03762 [cs.CL].

[12] PAN S J, YANG Q. A survey on transfer learning[J]. IEEE Transactions on knowledge
and data engineering, 2009, 22(10): 1345-1359.

[13] RADFORD A, NARASIMHAN K, SALIMANS T, et al. Improving language under-
standing by generative pre-training[J]. 2018.

[14] OUYANG L, WU J, JIANG X, et al. Training language models to follow instructions
with human feedback[J]. Advances in neural information processing systems, 2022, 35:
27730-27744.

[15] 李航. 统计学习方法[J]. 2019.

[16] FIRTH J. A synopsis of linguistic theory, 1930-1955[J]. Studies in linguistic analysis,
1957: 10-32.

[17] MIKOLOV T, CHEN K, CORRADO G, et al. Efficient estimation of word representa-
tions in vector space[J]. arXiv preprint arXiv:1301.3781, 2013.

[18] SINHA K, JIA R, HUPKES D, et al. Masked language modeling and the distributional
hypothesis: Order word matters pre-training for little[C]//Proceedings of the 2021 conference on empirical methods in natural language processing. 2021: 2888-2913.

[19] DENG J, DONG W, SOCHER R, et al. Imagenet: A large-scale hierarchical image
database[C]//2009 IEEE conference on computer vision and pattern recognition. 2009:
248-255.

[20] KRIZHEVSKY A, SUTSKEVER I, HINTON G E. Imagenet classification with deep
convolutional neural networks[J]. Advances in neural information processing systems,
2012, 25.

[21] ERHAN D, COURVILLE A, BENGIO Y, et al. Why does unsupervised pre-training help
deep learning?[C]//Proceedings of the thirteenth international conference on artificial intelligence and statistics. 2010: 201-208.

...

[49] BENDER E M, KOLLER A. Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data[C/OL]//JURAFSKY D, CHAI J, SCHLUTER N, et al. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics.Online: Association for Computational Linguistics, 2020: 5185-5198. https://aclanthology.org/2020.acl-main.463/. DOI: 10.18653/v1/2020.acl-main.463.

[50] HA D, SCHMIDHUBER J. World Models[J/OL]. CoRR, 2018, abs/1803.10122. arXiv:1803.10122. http://arxiv.org/abs/1803.10122.

[51] HAHN M. Theoretical Limitations of Self-Attention in Neural Sequence Models[J/OL].Transactions of the Association for Computational Linguistics, 2020, 8: 156-171. eprint:https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl_a_00306/1923102/tacl_a_00306.pdf. https://doi.org/10.1162/tacl_a_00306. DOI: 10.1162/tacl_a_00306.