@echo off
cd /d "%~dp0"
python -m streamlit run "nightliner_guide.py" --server.address 0.0.0.0
pause