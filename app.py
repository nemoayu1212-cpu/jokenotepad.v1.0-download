import os, sys, webview
def get_path(p): return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), p)
webview.create_window('無題 - メモ帳', get_path('index.html'), width=900, height=650)
webview.start()
