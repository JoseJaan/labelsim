import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_measure_table_is_up_to_date():
    spec = importlib.util.spec_from_file_location("tabela_medidas",
                                                  ROOT / "tools" / "tabela_medidas.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    current = (ROOT / "docs" / "medidas.md").read_text(encoding="utf-8")
    assert current == module.render(), "rode python tools/tabela_medidas.py"
