from app import core


def test_milestone_1():
    result = core.milestone_1()
    assert result["records"] == 5
    assert len(result["labels"]) == 4


def test_milestone_2():
    result = core.milestone_2()
    assert result["base_model"] == "gpt2"
    assert result["status"] == "not_trained"


def test_milestone_3():
    result = core.milestone_3()
    assert result["accuracy"] == 0.4
    assert result["records"] == 5


def test_milestone_4():
    result = core.milestone_4()
    assert result["dynamic_quantization"] == "not_run"
    assert result["static_quantization"] == "not_run"


def test_milestone_5():
    result = core.milestone_5()
    assert result["dataset_records"] == 5
    assert result["loading_time_ms"] >= 0


def test_milestone_6(capsys):
    result = core.milestone_6()
    assert "baseline" in result
    assert "efficiency" in result
    assert "quantization" in result
    assert '"accuracy": 0.4' in capsys.readouterr().out
