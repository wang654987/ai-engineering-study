# Phase 0 · Lesson 4 总结 — APIs & Keys

> 完成日期：2026-06-08
> API：DeepSeek（OpenAI 兼容格式）

---

## 学到的核心概念

### 1. API vs API Key

| | API | API Key |
|---|---|---|
| 是什么 | 两个程序间通信的**规则/约定** | 证明身份的**钥匙** |
| 比喻 | 银行柜台窗口的格式要求 | 你的身份证 |
| 你在代码里 | 包在 SDK/HTTP 请求里 | 放在环境变量里 |

### 2. API Key 安全原则

- **永远不要写在代码里** → 一旦 push 到 GitHub，全世界都能看到
- 用 `.env` 文件存储 → 加到 `.gitignore`
- 程序通过 `os.environ` 或 `dotenv` 读取

### 3. SDK vs Raw HTTP

| | SDK | Raw HTTP |
|---|---|---|
| 代码量 | 少 | 多 |
| 看到什么 | 只有文本 | 完整 JSON（token 数、模型名、请求 ID） |
| 调试 | 不够透明 | 能看到底层全部信息 |

**底层完全相同**：拼 URL → 加 key 到 header → POST JSON → 收 JSON → 取 text

### 4. HTTP 状态码速查

| 状态码 | 含义 | 你遇到的 |
|--------|------|----------|
| 200 | 成功 | ✅ |
| 400 | 请求格式错 | |
| 401 | Key 错/没传 | ✅ |
| 403 | 没权限 | |
| 429 | 超频限 | |
| 500/502/503 | 服务器崩 | |

---

## 课后文件

- `test_deepseek.py` — SDK 版 API 调用（OpenAI SDK → DeepSeek）
- `test_raw_http.py` — 裸 HTTP 调用（`urllib` 手写）
- `prompt-api-troubleshooter.md` — API 错误诊断速查卡
