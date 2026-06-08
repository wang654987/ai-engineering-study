# Phase 0 · Lesson 6 总结 — Python Environments

> 完成日期：2026-06-08
> 工具：uv + venv

---

## 学到的核心概念

### 1. 依赖地狱 → 虚拟环境

| 问题 | 解法 |
|------|------|
| 项目 A 要 torch 2.6，项目 B 要 torch 2.1 | 各自一个 venv，互不干扰 |
| 全局 pip install 互相覆盖 | venv 隔离——装、删、炸，不影响别的项目 |

### 2. 三种方式对比

| 工具 | 速度 | 特点 |
|------|------|------|
| uv | 最快（Rust, 10-100x pip） | 一体化：venv + 包管理 + 锁文件 |
| venv | 内置，不需要安装 | 慢但到处能用 |
| conda | 中 | 管非 Python 依赖（CUDA toolkit），但别混 pip |

### 3. pyproject.toml

| 段落 | 作用 |
|------|------|
| `[project]` | 项目名、版本、Python 要求 |
| `dependencies` | 必装包 |
| `[project.optional-dependencies]` | 可选分组（`pip install -e ".[torch]"`） |
| lockfile | 精确锁定所有包版本，跨机器一致 |

### 4. PEP 668 保护

Ubuntu 系统 Python 不允许 `pip install --system`——强制你必须用 venv。

### 5. 常见错误

| 错误 | 原因 | 修复 |
|------|------|------|
| `ModuleNotFoundError` | 忘了激活 venv | `source .venv/bin/activate` |
| CUDA not available | torch CUDA 版本 > 驱动 CUDA 版本 | 装匹配的 torch 版本 |
| pip/conda 混用 | pip 绕过 conda 依赖追踪 | 一个环境只用一种包管理器 |
| `.venv/` 提交到 git | 几百 MB ~ 2GB | `.gitignore` 加 `.venv/`，提交 pyproject.toml 即可 |

---

## 练习

| # | 内容 | 结果 |
|---|------|------|
| 1 | 创建第二个 venv，装不同版 numpy 验证隔离 | ✅ `.venv-course`(2.4.4) vs `.venv-test`(1.26.4) |
| 2 | 写 pyproject.toml + optional-dependencies | ✅ torch/llm 分组 |
| 3 | 故意全局装包观察位置 | ✅ PEP 668 直接拦截，证明系统强制用 venv |

## 测验

| # | 知识点 | 结果 |
|---|--------|------|
| 1 | 虚拟环境解决什么 | ✅ |
| 2 | lockfile 是什么 | ✅ |
| 3 | `which python` 验证 venv | ✅ |
| 4 | pip/conda 混用问题 | ✅ |
| 5 | CUDA 版本不兼容 | ✅ |

**5/5 全过。**

---

## 课后文件

- `pyproject.toml` — 项目配置（含 torch/llm 可选依赖）
- `env_setup.sh` — 一键环境搭建脚本（课程提供，位于 `code/`）
