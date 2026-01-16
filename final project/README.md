# Final Project / Undergraduate Thesis Proposal: Modeling Knowledge Transfer with DAPT and PEFT

## Abstract
(This is a research proposal for my undergraduate thesis, also serving as the final project for my self-directed study of CS224n.)
This project aims to investigate the capacity for knowledge transfer in Large Language Models by simulating cross-disciplinary learning scenarios. I propose to employ continued pretraining (DAPT) and parameter-efficient fine-tuning (PEFT) techniques like LoRA and its variants(ReLoRA, FlyLoRA, etc.) on a RoBERTa model, using two related academic sub-disciplines as testbeds.


## 1. Proposed Methodology
- **Base Model**: RoBERTa.
- **Domain-Adaptive Pretraining (DAPT)**: On crawled corpora from two sub-disciplines.
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
[1] RoBERTa: A Robustly Optimized BERT Pretraining Approach

[2] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

[3] EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks

[4] Universal Language Model Fine-tuning for Text Classification

[5] FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts

[6] LoRA: Low-Rank Adaptation of Large Language Models

[7] Don't Stop Pretraining: Adapt Language Models to Domains and Tasks

[8] Domain-Adaptive Continued Pre-Training of Small Language Models
...