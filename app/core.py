"""Lightweight legal clause monitoring pipeline.

The pipeline supports dataset preparation, baseline evaluation and
transparent model-efficiency measurements. GPT-2 training and
PyTorch quantization require the optional ML dependencies.
"""
import csv
import json
import time
from pathlib import Path

DATA = Path("data")
ARTIFACTS = Path("artifacts")


def milestone_1():
    """Prepare a small, reproducible LEDGAR-format CSV subset."""
    DATA.mkdir(exist_ok=True)
    source = DATA / "ledgar_sample.csv"
    if not source.exists():
        rows = [
            ("The agreement shall terminate upon written notice.", "Termination"),
            ("The parties agree to maintain confidentiality.", "Confidentiality"),
            ("Payment shall be made within thirty days.", "Payment"),
            ("This agreement is governed by applicable law.", "Governing Law"),
            ("Either party may terminate this agreement.", "Termination"),
        ]
        with source.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["text", "label"])
            writer.writerows(rows)
    with source.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {"dataset": str(source), "records": len(rows),
            "labels": sorted({r["label"] for r in rows})}


def milestone_2():
    """Record the GPT-2 fine-tuning configuration without fabricating training."""
    ARTIFACTS.mkdir(exist_ok=True)
    config = {
        "base_model": "gpt2",
        "method": "classification as generation",
        "status": "not_trained",
        "reason": "Install torch, transformers and datasets to run fine-tuning."
    }
    (ARTIFACTS / "training_status.json").write_text(
        json.dumps(config, indent=2), encoding="utf-8")
    return config


def milestone_3():
    """Evaluate a transparent majority-label baseline on the sample."""
    result = milestone_1()
    with (DATA / "ledgar_sample.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    counts = {}
    for row in rows:
        counts[row["label"]] = counts.get(row["label"], 0) + 1
    majority = max(counts, key=counts.get)
    accuracy = sum(r["label"] == majority for r in rows) / len(rows)
    report = {
        "evaluation": "majority-label baseline, not GPT-2",
        "records": len(rows),
        "majority_label": majority,
        "accuracy": round(accuracy, 4)
    }
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "baseline_evaluation.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8")
    return report


def milestone_4():
    """Report quantization prerequisites honestly."""
    report = {
        "dynamic_quantization": "not_run",
        "static_quantization": "not_run",
        "reason": "GPT-2 checkpoint and PyTorch are not installed."
    }
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "quantization_status.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8")
    return report


def milestone_5():
    """Measure sample pipeline latency; do not mislabel it model inference."""
    start = time.perf_counter()
    result = milestone_1()
    elapsed_ms = (time.perf_counter() - start) * 1000
    report = {
        "measurement": "dataset loading latency, not model inference",
        "dataset_records": result["records"],
        "loading_time_ms": round(elapsed_ms, 3),
        "model_size_comparison": "unavailable: no trained checkpoint",
        "inference_comparison": "unavailable: no trained checkpoint"
    }
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "efficiency_metrics.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8")
    return report


def milestone_6():
    """Print a dashboard from actual pipeline reports."""
    reports = {
        "dataset": milestone_1(),
        "baseline": milestone_3(),
        "training": milestone_2(),
        "quantization": milestone_4(),
        "efficiency": milestone_5()
    }
    print(json.dumps(reports, indent=2))
    return reports
