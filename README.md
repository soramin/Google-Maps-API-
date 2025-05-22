Google Maps API + 軍事補助マップ機能

✅ 推奨方法：Kivy + Plyer + Android/iOSビルド
Python だけでクロスプラットフォーム開発ができる環境です。

🔧 1. 使用するライブラリ・ツール
目的	ライブラリ/ツール
モバイルGUI	Kivy
モバイル機能（GPSなど）	Plyer
マップ表示	Google Static Maps API（地図画像）または Leaflet via WebView
ビルド（Android）	Buildozer（Linux）
ビルド（iOS）	Xcode（Mac） + Kivy-ios

🚧 注意点
Kivy自体はGoogle Maps のネイティブSDKに非対応。
なので、以下の2パターンのどちらかで回避：

📌 パターンA：Google Static Maps API を画像で表示（最もシンプル）
地図画像を取得してマーカー描画などはPython側で処理

📌 パターンB：Kivy + WebView（via Android WebKit）
→ HTML＋JavaScript版をそのまま埋め込める（これが最も現実的に“マップAPI”を動かせる）

📁 フォルダ構成例
arduino
military_map_mobile/
├── main.py
├── assets/
│   └── map.html
├── buildozer.spec

📱 iOS 対応について
Mac 環境が必要

kivy-ios を使用

Google Maps JavaScript API を WebView に埋め込むのが無難

✅ アーキテクチャ選択肢
方法・利点・欠点
Kivy + Static Maps	軽い・簡単	画像のみで制限あり
Kivy + WebView + JS	リッチ機能・Google Maps動作可	Android/iOS連携が少し手間
BeeWare, Flutter, React Native + Python連携	より洗練されたUIが可能	Python以外を併用
