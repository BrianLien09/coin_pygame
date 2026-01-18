# 🚀 SPACE DEFENDER - 太空防衛射擊遊戲

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![HTML5](https://img.shields.io/badge/HTML5-Canvas-red.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

一款使用 Pygame / HTML5 開發的經典太空射擊遊戲，具備炫麗的粒子特效與流暢的遊戲體驗。

**🎮 [立即線上遊玩](https://your-username.github.io/dotball_test/) →**

[功能特色](#-功能特色) •
[遊玩方式](#-遊玩方式) •
[遊戲操作](#-遊戲操作) •
[部署到 GitHub Pages](#-部署到-github-pages) •
[技術架構](#-技術架構)

</div>

---

## 📖 遊戲簡介

《SPACE DEFENDER》是一款結合經典街機與現代視覺特效的太空射擊遊戲。玩家需要操控太空戰機，擊毀不斷襲來的敵方單位，在血量耗盡前達成 **500 分**的勝利目標。

### 🎮 遊戲目標

- **主要目標**:累積得分達到 500 分即可獲勝
- **次要目標**:在血量歸零前盡可能擊毀更多敵人
- **挑戰要素**:敵人會以隨機速度與旋轉動畫出現,考驗玩家的反應與走位能力

---

## ✨ 功能特色

### 🎨 視覺效果

- **動態粒子系統**:敵人被擊毀時產生具備透明度衰減的粒子爆炸效果
- **旋轉動畫**:敵人會隨機旋轉墜落,增加視覺張力
- **漸層配色**:採用深色太空背景與霓虹色彩,營造科幻氛圍
- **流暢畫面**:固定 60 FPS 運行,確保遊戲體驗絲滑順暢

### 🕹️ 遊戲機制

- **自動連發系統**:按住空格鍵即可持續射擊,無需連點
- **難度漸進設計**:敵人生成速度與移動速度隨機,維持挑戰性
- **碰撞判定**:精確的碰撞偵測
- **生命值系統**:玩家擁有 3 點生命值,每次碰撞扣除 1 點

### 🎯 遊戲狀態

1. **主選單 (MENU)**:顯示標題與開始按鈕
2. **遊戲進行 (PLAYING)**:核心遊戲迴圈
3. **遊戲結束 (GAMEOVER)**:死亡後可選擇重新開始
4. **勝利畫面 (WIN)**:達成目標分數後顯示勝利訊息

---

## 🎮 遊玩方式

本遊戲提供 **兩種版本**,您可以根據需求選擇:

### 🌐 方式一:線上遊玩 (推薦)

直接在瀏覽器中遊玩 HTML5 版本:

**👉 [點擊這裡開始遊戲](https://your-username.github.io/dotball_test/)**

**支援平台:**

- ✅ Chrome / Edge (建議)
- ✅ Firefox
- ✅ Safari
- ✅ 行動裝置瀏覽器

**優點:**

- 無需安裝任何軟體
- 跨平台支援
- 自動更新到最新版本

### 💻 方式二:本地執行 Pygame 版本

#### 系統需求

- **Python 版本**:3.8 或以上
- **作業系統**:Windows / macOS / Linux

#### 安裝步驟

```bash
# 1. 克隆專案
git clone https://github.com/your-username/dotball_test.git
cd dotball_test

# 2. 安裝 Pygame
pip install pygame

# 3. 執行遊戲
python game.py
```

### 🔧 本地測試 HTML5 版本

如果您想在本地測試 HTML5 版本:

```bash
# 使用 Python 內建伺服器
python -m http.server 8000

# 或使用 Node.js (需先安裝 http-server)
npx http-server

# 然後在瀏覽器開啟
# http://localhost:8000
```

---

## 🎮 遊戲操作

### 鍵盤控制

| 按鍵      | 功能                |
| --------- | ------------------- |
| `A` / `←` | 向左移動            |
| `D` / `→` | 向右移動            |
| `空格`    | 射擊 (支援長按連發) |

### 滑鼠操作

- **主選單**:點擊綠色「START」按鈕開始遊戲
- **結束畫面**:點擊「RETRY」或「PLAY AGAIN」重新開始

---

## 🚀 部署到 GitHub Pages

本專案已配置 GitHub Actions 自動部署流程,遵循以下步驟即可發佈您的遊戲:

### 1️⃣ 推送程式碼到 GitHub

```bash
# 初始化 Git (如果尚未初始化)
git init
git add .
git commit -m "初始化 SPACE DEFENDER 遊戲"

# 連結遠端倉庫
git remote add origin https://github.com/your-username/dotball_test.git
git branch -M main
git push -u origin main
```

### 2️⃣ 啟用 GitHub Pages

1. 前往您的 GitHub 倉庫
2. 點擊 **Settings** → **Pages**
3. 在 **Source** 下拉選單中選擇 **GitHub Actions**
4. 儲存設定

### 3️⃣ 自動部署

完成上述設定後:

- ✅ 每次 `push` 到 `main` 分支都會自動觸發部署
- ✅ 約 1-2 分鐘後即可在 `https://your-username.github.io/dotball_test/` 存取遊戲
- ✅ 可在 **Actions** 分頁查看部署狀態

### 4️⃣ 手動觸發部署 (選用)

前往倉庫的 **Actions** → **Deploy to GitHub Pages** → **Run workflow**

---

## 🏗️ 技術架構

### 🐍 Pygame 版本

#### 核心模組

**1️⃣ 粒子系統 (Particle)**

- 實現敵人毀滅時的爆炸特效
- 具備 Alpha 透明度衰減動畫
- 隨機速度向量產生碎裂效果

**2️⃣ 子彈系統 (Bullet)**

- 垂直向上飛行的彈道
- 離開螢幕範圍後自動銷毀
- 採用矩形碰撞箱判定

**3️⃣ 敵人系統 (Enemy)**

- 隨機生成位置與大小
- 動態旋轉動畫 (使用 `pygame.transform.rotate`)
- 隨機下墜速度增加不可預測性

**4️⃣ 玩家控制 (Player)**

- 三角形戰機造型
- 內建射擊冷卻機制 (200ms 連發間隔)
- 範圍限制於螢幕內移動

**5️⃣ 遊戲控制器 (Game)**

- 管理遊戲狀態機 (MENU → PLAYING → WIN/GAMEOVER)
- 處理碰撞判定與得分計算
- 使用 `asyncio` 實現非同步遊戲迴圈

#### 設計模式

- **Sprite 群組管理**:使用 `pygame.sprite.Group()` 高效處理大量物件
- **狀態機模式**:透過 `self.state` 切換不同遊戲階段
- **事件驅動**:基於 Pygame 事件系統處理輸入與更新

### 🌐 HTML5 版本

#### 技術堆疊

- **Canvas API**:純 JavaScript 實現 2D 遊戲渲染
- **requestAnimationFrame**:確保 60 FPS 流暢動畫
- **ES6 Class**:物件導向設計,與 Pygame 版本邏輯一致

#### 核心特性

- ✅ **零依賴**:無需任何外部函式庫
- ✅ **響應式設計**:適配不同螢幕尺寸
- ✅ **單一檔案**:所有程式碼整合在 `index.html`
- ✅ **即時載入**:無需編譯或建置步驟

### 配色方案

```javascript
COLORS = {
  bg: "rgb(20, 20, 35)", // 深色太空背景
  player: "rgb(0, 255, 255)", // 青色戰機
  enemy: "rgb(255, 80, 80)", // 紅色敵人
  bullet: "rgb(255, 255, 100)", // 黃色子彈
  particle: "rgb(255, 150, 50)", // 橘色粒子
};
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

這個專案適合作為遊戲開發入門教材,涵蓋以下技術點:

### Pygame 版本

1. **Sprite 系統**:了解遊戲物件的面向物件設計
2. **碰撞偵測**:掌握 `pygame.sprite.groupcollide()` 的使用
3. **粒子特效**:學習 Alpha 透明度與動畫實現
4. **狀態管理**:理解遊戲狀態機的設計模式
5. **非同步程式**:使用 `asyncio` 實現流暢的遊戲迴圈

### HTML5 版本

1. **Canvas 繪圖**:學習 2D 圖形渲染與變換
2. **遊戲迴圈**:理解 `requestAnimationFrame` 的運作機制
3. **碰撞檢測**:實作 AABB (軸對齊邊界框) 碰撞演算法
4. **事件處理**:整合鍵盤與滑鼠輸入
5. **效能優化**:管理物件生命週期避免記憶體洩漏

---

## 🚀 未來擴充方向

- [ ] 新增音效與背景音樂
- [ ] 實作排行榜系統 (本地/線上)
- [ ] 增加道具系統 (護盾、雙倍火力等)
- [ ] 多種敵人類型與 Boss 戰
- [ ] 關卡系統與漸進式難度
- [ ] 支援手把控制器
- [ ] 多人對戰模式
- [ ] PWA 支援 (可安裝為桌面應用)

---

## 🐛 問題回報

如果您在遊戲中遇到任何問題,請透過以下方式回報:

1. 前往 [Issues](https://github.com/your-username/dotball_test/issues) 頁面
2. 點擊「New Issue」
3. 詳細描述問題 (包含錯誤訊息與重現步驟)
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

- **Pygame 團隊**:提供強大的 Python 遊戲開發框架
- **MDN Web Docs**:完整的 Canvas API 參考文件
- **進階程式專題班**:促成此專案的學習平台
- **所有玩家**:感謝您的試玩與回饋

---

## 👨‍💻 開發者

**Brian** - 進階程式專題班講師

- 📧 Email: your.email@example.com
- 🌐 GitHub: [@your-username](https://github.com/your-username)

---

<div align="center">

**⭐ 如果您喜歡這個專案,請給我們一個 Star!⭐**

Made with ❤️ using Python & JavaScript

</div>
