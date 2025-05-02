import os
import re

# Input markdown file
filename = "docs-ja-manual.md"  # Replace this with your actual file path

# Output directory
output_dir = "split_md_sections"
os.makedirs(output_dir, exist_ok=True)

# Define custom reading order (titles exactly as they appear in the file)
reading_order = [
    "登録とアカウントアクセス", "CVATワークスペース", "ナビゲーションバーとメニュー", "タスクページ", "ジョブページ", "タスク詳細",
    "CVATアノテーションインターフェース", "オブジェクトサイドバー", "コントロールサイドバー", "ショートカット", "結合・分割ツール", 
    "フィルター", "検索", "アノテーター向け仕様書", "アノテーションタスクの作成", "マルチタスクの作成", 
    "属性アノテーションモード（基本）", "シェイプモード（基本）", "トラックモード（基本）", "長方形によるアノテーション", 
    "ポリラインによるアノテーション", "ポリゴンによるアノテーション", "楕円によるアノテーション", "タグによるアノテーション", 
    "ポイントによるアノテーション", "スケルトンによるアノテーション", "単一シェイプ", "シェイプモードでのポイント", 
    "シェイプのグループ化", "手動描画", "マスクの作成", "自動境界を使用した描画", "ブラシツールによるアノテーション", 
    "属性アノテーションモード（上級）", "トラックモード（上級編）", "シェイプモード（上級）", "3Dオブジェクトアノテーション", 
    "3Dタスクワークスペース", "標準3Dモード（基本）", "3Dオブジェクトアノテーション（上級）", "キュボイドによるアノテーション", 
    "直方体の作成", "直方体の編集", "ポリゴンによるトラックモード", "プロジェクトページ", "組織", "クラウドストレージの接続", 
    "クラウドストレージページ", "データセットのインポートおよびアノテーションのアップロード", "タスクおよびプロジェクトのバックアップ", 
    "オンザフライでのデータ準備", "自動アノテーション", "CVAT ユーザーロール", "コンテキスト画像", "手動QAとレビュー", 
    "品質管理", "CVATチームのパフォーマンスとモニタリング", "CVAT クラウドにおける分析と品質管理",  
    "フレームの削除", "削除フレームの表示とナビゲーションの設定", "削除フレームの復元", "1点による線形補間", 
    "CVAT for image", "LabelMe", "MOT", "MOTS", "LFW", "Wider Face", "CamVid", "ICDAR13/15", "VGGFace2", 
    "Ultralytics YOLO", "Ultralytics-YOLO-分類", "YOLO", "ImageNet", "Open Images", "Market-1501", 
    "Cityscapes（シティスケープス）", "Cityscapes エクスポート", "Cityscapes アノテーションのインポート", 
    "Cityscapesデータセットでタスクを作成", "Pascal VOC", "COCO", "COCO キーポイント", 
    "KITTI", "Datumaro", "CVATからアノテーションとデータをエクスポートする"
]

# Load content and split into sections
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by H1 headings
sections = re.split(r'^# (.+)$', content, flags=re.MULTILINE)

# Recombine into dict of {title: section_content}
section_map = {}
for i in range(1, len(sections), 2):
    title = sections[i].strip()
    body = sections[i + 1].strip()
    section_map[title] = f"{body}"

# Write sections in specified order
for idx, title in enumerate(reading_order, start=1):
    if title in section_map:
        safe_title = re.sub(r'[\\/:"*?<>|]+', '', title)  # Sanitize filename
        filename_out = f"{idx:02d}.{safe_title}.md"
        with open(os.path.join(output_dir, filename_out), 'w', encoding='utf-8') as f:
            f.write(f"\n# {idx}.{title}\n\n" + section_map[title])
    else:
        print(f"⚠️ Missing: {title}")
