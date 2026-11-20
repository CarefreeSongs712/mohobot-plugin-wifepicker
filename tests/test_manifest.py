from pathlib import Path

import yaml


def test_manifest() -> None:
    root = Path(__file__).parents[1]
    metadata = yaml.safe_load((root / 'metadata.yaml').read_text(encoding='utf-8'))
    assert metadata['name'] == 'wifepicker'
    assert metadata['api_version'] == 1
    assert (root / 'main.py').is_file()
