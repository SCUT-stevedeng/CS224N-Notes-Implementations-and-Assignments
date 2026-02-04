# Final Project / Undergraduate Thesis Proposal: A Study on Undergraduate Knowledge Transfer Based on DACP+SFT

## Abstract
(This is a research proposal for my undergraduate thesis, also serving as the final project for my self-directed study of CS224n.)
This project aims to investigate the capacity for knowledge transfer in Large Language Models by simulating cross-disciplinary learning scenarios. I propose to employ domain adaptive continued pretraining (DACP) and parameter-efficient fine-tuning (PEFT) techniques like LoRA and its variants(ReLoRA, FlyLoRA, etc.) on a RoBERTa model, using two related academic sub-disciplines as testbeds.


## 1. Proposed Methodology
- **Base Model**: RoBERTa.
- **Domain-Adaptive Continued Pretraining (DACP)**: On crawled corpora from two sub-disciplines.
- **Parameter-Efficient Fine-Tuning (PEFT)**: Using LoRA or its variants to efficiently adapt the model for a specific task (e.g., correctness judgment on exam-like questions).
- **Evaluation**: Analyze performance improvement on the target domain after training on the source domain, and probe the model's internal representations.

## 2. Expected Outcomes & Relation to CS224n
- I expect to demonstrate a measurable knowledge transfer effect.
- This project directly builds upon the concepts learned in CS224n, including but not limited to:
    - **Word Vector Representations** (Lecture 1)
    - **Neural Network Training** (Lectures 2 & 3)
    - **Model Efficiency and Adaptation** (related to practical deployment considerations discussed throughout the course)

## 3. Project Timeline
- [ ] Literature Review (In Progress)
- [ ] Data Collection (In Progress)
- [ ] Baseline Model Implementation (Planned)
- [ ] ... (Other phases)

## 4. References
[1] Petroni F, Rocktäschel T, Riedel S, et al. Language models as knowledge bases?[C]//Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP). 2019: 2463-2473.

[2] Zhang N, Li Q, Wu S X, et al. A Novel Influence Analysis-Based University Major Similarity Study[J]. Education Sciences, 2024, 14(3): 337.

[3] Kornblith S, Norouzi M, Lee H, et al. Similarity of neural network representations revisited[C]//International conference on machine learning. PMlR, 2019: 3519-3529.

[4] Sung C, Dhamecha T, Saha S, et al. Pre-training BERT on domain resources for short answer grading[C]//Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP). 2019: 6071-6075.

[5] Ke Z, Shao Y, Lin H, et al. Continual pre-training of language models[J]. arXiv preprint arXiv:2302.03241, 2023.

[6] Xie Y, Aggarwal K, Ahmad A. Efficient continual pre-training for building domain specific large language models[C]//Findings of the Association for Computational Linguistics ACL 2024. 2024: 10184-10201.

[7] Pan S J, Yang Q. A survey on transfer learning[J]. IEEE Transactions on knowledge and data engineering, 2009, 22(10): 1345-1359.

[8] Ruder S, Peters M E, Swayamdipta S, et al. Transfer learning in natural language processing[C]//Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: Tutorials. 2019: 15-18.

[9] Gururangan S, Marasović A, Swayamdipta S, et al. Don't stop pretraining: Adapt language models to domains and tasks[J]. arXiv preprint arXiv:2004.10964, 2020.

[10] Liu Y, Ott M, Goyal N, et al. Roberta: A robustly optimized bert pretraining approach[J]. arXiv preprint arXiv:1907.11692, 2019.

[11] Wei J, Zou K. EDA: Easy data augmentation techniques for boosting performance on text classification tasks[J]. arXiv preprint arXiv:1901.11196, 2019.

[12] Howard J, Ruder S. Universal language model fine-tuning for text classification[J]. arXiv preprint arXiv:1801.06146, 2018.

[13] Sun C, Qiu X, Xu Y, et al. How to fine-tune bert for text classification?[C]//China national conference on Chinese computational linguistics. Cham: Springer International Publishing, 2019: 194-206.

[14] Hu E J, Shen Y, Wallis P, et al. Lora: Low-rank adaptation of large language models[J]. ICLR, 2022, 1(2): 3.

[15] Bender E M, Koller A. Climbing towards NLU: On meaning, form, and understanding in the age of data[C]//Proceedings of the 58th annual meeting of the association for computational linguistics. 2020: 5185-5198.
...