## Model Evaluation using [SuperGLUE Diagnostic Dataset](https://super.gluebenchmark.com/diagnostics/)

Here is an example of evaluating a model (fine-tuned either on MNLI or SNLI) using SuperGLUE diagnostic dataset [Wang et al., 2019](https://arxiv.org/abs/1905.00537).

This is an example of using run_diagnostics_mnli.py in Google Colab:

```bash
!git clone https://github.com/mhdr3a/transformers-diagnostics
!mv /content/transformers-diagnostics/* /content/
!rm transformers-diagnostics -r
!pip install -r requirements.txt

!python run_diagnostics_mnli.py \
        --task_name diagnostics \
        --do_eval \
        --data_dir ./ \
        --model_name_or_path mnli-6 \
        --max_seq_length 128 \
        --output_dir mnli-6
```
* Note that the mnli-6 model is fine-tuned on MNLI; so, use run_diagnostics_snli.py if your model is fine-tuned on SNLI.

This will create the diagnostics_predictions.txt file in ./mnli-6, which can then be evaluated using evaluate_predictions.py.

```bash
!python evaluate_predictions.py ./mnli-6/diagnostics_predictions.txt
```

The evaluation results for the [mnli-6 model](https://huggingface.co/mahdiyar/mnli-6) is as follows:

```bash
Heuristic entailed results:
entailment correct predictions: 0.7913043478260869

Heuristic non-entailed results:
not_entailment correct predictions: 0.6785714285714286

MCC = 0.46357845870027464

lexical-semantics results:
Morphological negation: 0.8461538461538461
Lexical entailment: 0.7214285714285714
Quantifiers: 0.8653846153846154
Redundancy: 0.8846153846153846
Symmetry/Collectivity: 0.7142857142857143
Named entities: 0.8055555555555556
Factivity: 0.7058823529411765

predicate-argument-structure results:
Anaphora/Coreference: 0.6896551724137931
Intersectivity: 0.6521739130434783
Nominalization: 0.8571428571428571
Active/Passive: 0.6176470588235294
Prepositional phrases: 0.8676470588235294
Genitives/Partitives: 0.9
Core args: 0.7115384615384616
Relative clauses: 0.65625
Coordination scope: 0.7
Restrictivity: 0.5
Datives: 0.85
Ellipsis/Implicits: 0.7058823529411765

logic results:
Negation: 0.8170731707317073
Conditionals: 0.6875
Double negation: 0.9642857142857143
Upward monotone: 0.9117647058823529
Downward monotone: 0.16666666666666666
Intervals/Numbers: 0.631578947368421
Conjunction: 0.875
Disjunction: 0.5
Universal: 0.8888888888888888
Existential: 0.7
Temporal: 0.375
Non-monotone: 0.6666666666666666

knowledge results:
World knowledge: 0.6567164179104478
Common sense: 0.7533333333333333
```

And here are the evaluation results for the [snli-6 model](https://huggingface.co/mahdiyar/snli-6):

```bash
Heuristic entailed results:
entailment correct predictions: 0.7043478260869566

Heuristic non-entailed results:
not_entailment correct predictions: 0.7127329192546584

MCC = 0.41250063027484707

lexical-semantics results:
Morphological negation: 0.7307692307692307
Lexical entailment: 0.7357142857142858
Quantifiers: 0.7884615384615384
Redundancy: 0.6923076923076923
Symmetry/Collectivity: 0.75
Named entities: 0.7222222222222222
Factivity: 0.6323529411764706

predicate-argument-structure results:
Anaphora/Coreference: 0.6724137931034483
Intersectivity: 0.6739130434782609
Nominalization: 0.8928571428571429
Active/Passive: 0.5882352941176471
Prepositional phrases: 0.8676470588235294
Genitives/Partitives: 0.95
Core args: 0.7115384615384616
Relative clauses: 0.65625
Coordination scope: 0.75
Restrictivity: 0.5
Datives: 0.85
Ellipsis/Implicits: 0.6470588235294118

logic results:
Negation: 0.7317073170731707
Conditionals: 0.625
Double negation: 0.5714285714285714
Upward monotone: 0.9411764705882353
Downward monotone: 0.2
Intervals/Numbers: 0.6578947368421053
Conjunction: 0.85
Disjunction: 0.42105263157894735
Universal: 0.8333333333333334
Existential: 0.75
Temporal: 0.5625
Non-monotone: 0.6333333333333333

knowledge results:
World knowledge: 0.6194029850746269
Common sense: 0.72
```
