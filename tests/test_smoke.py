from dev import sh
from pathlib import Path


def test_smoke(tmp_dir):
    tests_dir = Path(__file__).parent
    in_file = tests_dir / 'EURUSD.csv'
    out_file = tmp_dir / 'EURUSD2.csv'
    sh.run(['shiftdata', '-c', '17:00', in_file, out_file])
    exp_out_file = tests_dir / 'EURUSD2.csv'
    assert out_file.read_text().strip() == exp_out_file.read_text().strip()
