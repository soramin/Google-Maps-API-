#（Kivy + Android WebView）

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

if platform == 'android':
    from android import activity
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

class MapScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform == 'android':
            self.load_webview()

    @run_on_ui_thread
    def load_webview(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')

        activity = PythonActivity.mActivity
        layout = activity.getWindow().getDecorView().findViewById(0x1020002)

        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl("file:///sdcard/map.html")  # HTMLファイルパスを変更可

        layout.addView(webview)

class MapApp(App):
    def build(self):
        return MapScreen()

if __name__ == '__main__':
    MapApp().run()

"""
📦 Buildozer で Android アプリ化
bash

sudo apt install buildozer
buildozer init
buildozer -v android debug
buildozer android deploy run
"""
