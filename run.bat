@echo off
call venv/scripts/activate
pytest -s -v -m "regression" --html ./reports/report.html --browser edge
pause

