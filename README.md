# 🚀 SPACE DEFENDER - 太空防衛射擊遊戲

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

一款使用 Pygame 開發的經典太空射擊遊戲，具備炫麗的粒子特效與流暢的遊戲體驗。

[功能特色](#-功能特色) •
[安裝方式](#-安裝方式) •
[遊戲操作](#-遊戲操作) •
[技術架構](#-技術架構) •
[開發者](#-開發者)

</div>

---

## 📖 遊戲簡介

《SPACE DEFENDER》是一款結合經典街機與現代視覺特效的太空射擊遊戲。玩家需要操控太空戰機，擊毀不斷襲來的敵方單位，在血量耗盡前達成 **500 分**的勝利目標。

### 🎮 遊戲目標

- **主要目標**：累積得分達到 500 分即可獲勝
- **次要目標**：在血量歸零前盡可能擊毀更多敵人
- **挑戰要素**：敵人會以隨機速度與旋轉動畫出現，考驗玩家的反應與走位能力

---

## ✨ 功能特色

### 🎨 視覺效果

- **動態粒子系統**：敵人被擊毀時產生具備透明度衰減的粒子爆炸效果
- **旋轉動畫**：敵人會隨機旋轉墜落,增加視覺張力
- **漸層配色**：採用深色太空背景與霓虹色彩,營造科幻氛圍
- **流暢畫面**：固定 60 FPS 運行,確保遊戲體驗絲滑順暢

### 🕹️ 遊戲機制

- **自動連發系統**：按住空格鍵即可持續射擊,無需連點
- **難度漸進設計**：敵人生成速度與移動速度隨機,維持挑戰性
- **碰撞判定**：精確的像素級碰撞偵測
- **生命值系統**：玩家擁有 3 點生命值,每次碰撞扣除 1 點

### 🎯 遊戲狀態

1. **主選單 (MENU)**：顯示標題與開始按鈕
2. **遊戲進行 (PLAYING)**：核心遊戲迴圈
3. **遊戲結束 (GAMEOVER)**：死亡後可選擇重新開始
4. **勝利畫面 (WIN)**：達成目標分數後顯示勝利訊息

---

## 🛠️ 安裝方式

### 系統需求

- **Python 版本**：3.8 或以上
- **作業系統**：Windows / macOS / Linux
- **硬體需求**：
  - 記憶體：至少 2GB RAM
  - 顯示卡：支援基本 2D 渲染即可

### 安裝步驟

#### 1. 克隆專案

```bash
git clone https://github.com/your-username/dotball_test.git
cd dotball_test
```

#### 2. 建立虛擬環境（建議）

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. 安裝依賴套件

```bash
pip install pygame
```

#### 4. 執行遊戲

```bash
python game.py
```

---

## 🎮 遊戲操作

### 鍵盤控制

| 按鍵      | 功能                 |
| --------- | -------------------- |
| `A` / `←` | 向左移動             |
| `D` / `→` | 向右移動             |
| `空格`    | 射擊（支援長按連發） |

### 滑鼠操作

- **主選單**：點擊綠色「START」按鈕開始遊戲
- **結束畫面**：點擊紅色「RETRY」或藍色「PLAY AGAIN」按鈕重新開始

---

## 🏗️ 技術架構

### 核心模組

#### 1️⃣ **粒子系統 (Particle)**

```python
class Particle(pygame.sprite.Sprite)
```

- 實現敵人毀滅時的爆炸特效
- 具備 Alpha 透明度衰減動畫
- 隨機速度向量產生碎裂效果

#### 2️⃣ **子彈系統 (Bullet)**

```python
class Bullet(pygame.sprite.Sprite)
```

- 垂直向上飛行的彈道
- 離開螢幕範圍後自動銷毀
- 採用矩形碰撞箱判定

#### 3️⃣ **敵人系統 (Enemy)**

```python
class Enemy(pygame.sprite.Sprite)
```

- 隨機生成位置與大小
- 動態旋轉動畫（使用 `pygame.transform.rotate`）
- 隨機下墜速度增加不可預測性

#### 4️⃣ **玩家控制 (Player)**

```python
class Player(pygame.sprite.Sprite)
```

- 三角形戰機造型
- 內建射擊冷卻機制（200ms 連發間隔）
- 範圍限制於螢幕內移動

#### 5️⃣ **遊戲控制器 (Game)**

```python
class Game
```

- 管理遊戲狀態機（MENU → PLAYING → WIN/GAMEOVER）
- 處理碰撞判定與得分計算
- 使用 `asyncio` 實現非同步遊戲迴圈

### 設計模式

- **Sprite 群組管理**：使用 `pygame.sprite.Group()` 高效處理大量物件
- **狀態機模式**：透過 `self.state` 切換不同遊戲階段
- **事件驅動**：基於 Pygame 事件系統處理輸入與更新

### 配色方案

```python
COLORS = {
    "bg": (20, 20, 35),         # 深色太空背景
    "player": (0, 255, 255),    # 青色戰機
    "enemy": (255, 80, 80),     # 紅色敵人
    "bullet": (255, 255, 100),  # 黃色子彈
    "particle": (255, 150, 50), # 橘色粒子
}
```

---

## 📊 遊戲數據

| 參數         | 數值    | 說明                  |
| ------------ | ------- | --------------------- |
| 畫面解析度   | 800x600 | 經典 4:3 比例         |
| 更新頻率     | 60 FPS  | 確保流暢動畫          |
| 勝利分數     | 500 分  | 每擊毀一個敵人 +20 分 |
| 玩家初始血量 | 3 HP    | 碰撞敵人扣 1 HP       |
| 敵人生成間隔 | 25 幀   | 約 0.42 秒            |
| 射擊冷卻時間 | 200 ms  | 每秒最多 5 發         |

---

## 🎓 學習要點

這個專案適合作為 Pygame 入門教材，涵蓋以下技術點：

1. **Sprite 系統**：了解遊戲物件的面向物件設計
2. **碰撞偵測**：掌握 `pygame.sprite.groupcollide()` 的使用
3. **粒子特效**：學習 Alpha 透明度與動畫實現
4. **狀態管理**：理解遊戲狀態機的設計模式
5. **輸入處理**：結合鍵盤與滑鼠事件的整合應用
6. **非同步程式**：使用 `asyncio` 實現流暢的遊戲迴圈

---

## 🚀 未來擴充方向

- [ ] 新增音效與背景音樂
- [ ] 實作排行榜系統（本地/線上）
- [ ] 增加道具系統（護盾、雙倍火力等）
- [ ] 多種敵人類型與 Boss 戰
- [ ] 關卡系統與漸進式難度
- [ ] 支援手把控制器
- [ ] 多人對戰模式

---

## 🐛 問題回報

如果您在遊戲中遇到任何問題，請透過以下方式回報：

1. 前往 [Issues](https://github.com/your-username/dotball_test/issues) 頁面
2. 點擊「New Issue」
3. 詳細描述問題（包含錯誤訊息與重現步驟）
4. 附上您的系統環境資訊

---

## 📄 授權條款

本專案採用 **MIT License** 授權。

```
MIT License

Copyright (c) 2026 Brian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 致謝

- **Pygame 團隊**：提供強大的 Python 遊戲開發框架
- **進階程式專題班**：促成此專案的學習平台
- **所有玩家**:感謝您的試玩與回饋

---

## 👨‍💻 開發者

**Brian** - 進階程式專題班講師

- 📧 Email: your.email@example.com
- 🌐 GitHub: [@your-username](https://github.com/your-username)

---

<div align="center">

**⭐ 如果您喜歡這個專案，請給我們一個 Star！⭐**

Made with ❤️ and Python

</div>
