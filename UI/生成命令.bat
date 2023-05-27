@chcp 65001
@echo 以下命令运行前请保证在正确的python环境下运行
@pause
python -m PyQt5.uic.pyuic AnalysisWnd.ui -o AnalysisWnd.py
python -m PyQt5.uic.pyuic MainWnd.ui -o MainWnd.py
python -m PyQt5.uic.pyuic VideoLoginWnd.ui -o VideoLoginWnd.py
python -m PyQt5.uic.pyuic UserLoginWnd.ui -o UserLoginWnd.py
python -m PyQt5.uic.pyuic welcome.ui -o welcome.py