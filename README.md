# Quantized Legal Tagger Monitor

[![Built with askThili](https://msrit.ask.thili.ai/api/v1/public/projects/bn32yzz366/badge.svg)](https://msrit.ask.thili.ai/b/bn32yzz366)

This project, the Quantized Legal Tagger Monitor, helps legal aid workers evaluate the efficiency of a legal clause tagger. You will fine-tune a GPT-2 model to tag legal clauses, then apply quantization to reduce its size and improve inference speed. The final output will be a dashboard-like display comparing the original and quantized models' performance.

## What you are building

**Goal.** You will build a monitoring tool for legal aid workers to evaluate the efficiency of a quantized legal clause tagger, comparing its size and simulated inference speed against the original model for efficient document processing.

**Done when.** You have successfully fine-tuned a GPT-2 model for legal clause classification, applied dynamic and static post-training quantization, and presented a dashboard-like output comparing the original and quantized models' sizes, simulated inference times, and tagging accuracy.

## Milestones

Tick these off as you go, and commit after each one.

- [x] **1. Prepare a subset of the LEDGAR dataset for legal clause tagging.**  
      Hint: Data preparation.
- [ ] **2. Fine-tune a GPT-2 model to tag legal clauses using the classification as generation approach.**  
      Hint: Use the `Fine-Tune GPT-2 to Tag Legal Contract Clauses` technique.
- [x] **3. Evaluate the tagging accuracy of the fine-tuned model.**  
      Hint: Evaluate model performance.
- [ ] **4. Apply dynamic and static post-training quantization to the trained model.**  
      Hint: Apply the `Shrink a Neural Network with Quantisation` technique.
- [x] **5. Compare the original and quantized model sizes and measure simulated inference times.**  
      Hint: Compare model size and simulated inference speed.
- [x] **6. Present a dashboard-like output of model efficiency metrics.**  
      Hint: Visualize efficiency metrics.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- Provide a more granular breakdown of tagging accuracy for different legal clause categories after quantization.
- Enhance the dashboard to include interactive elements for filtering and comparing quantization results.
- Analyze the specific types of errors introduced or reduced by quantization for different clause types.
