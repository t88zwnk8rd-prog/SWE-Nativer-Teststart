"""Synthetische Anwendung für die manuelle Windows-Abnahme."""
from pathlib import Path
import time

if Path.cwd() != Path(__file__).resolve().parent:
    raise SystemExit('Unerwarteter Arbeitsordner')

print('SWE-TESTSTART PYTHON: Synthetische Testanwendung läuft.', flush=True)
print(f'Testordner: {Path.cwd()}', flush=True)
time.sleep(15)
