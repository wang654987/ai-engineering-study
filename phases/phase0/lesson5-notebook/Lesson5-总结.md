# Phase 0 · Lesson 5 总结 — Jupyter Notebooks

> 完成日期：2026-06-08
> 环境：JupyterLab 4.5.8 + Python 3.12.13

---

## 学到的核心概念

### 1. Notebook vs Script

| | Notebook (.ipynb) | Script (.py) |
|---|---|---|
| 执行方式 | 逐个 cell，手动触发 | 从头到尾自动跑 |
| 状态 | Kernel 持续存活，变量跨 cell 保留 | 跑完进程死，变量消失 |
| 适合 | 探索、原型、可视化、教学 | 训练管线、可复用工具、生产代码 |

**规则：在 notebook 里探索，在脚本里交付。**

### 2. Kernel（内核）

- 一个独立的后台 Python 进程
- 所有 cell 共享**同一个** kernel
- 变量一直存在，直到你重启 kernel
- 重启：Kernel → Restart（清空所有变量）

### 3. Cell 类型

| 类型 | 用途 | 快捷键 |
|------|------|--------|
| Code | 跑 Python 代码 | Y |
| Markdown | 写格式化的说明文字 | M |

### 4. Magic 命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `%timeit` | 跑多次取平均（微基准） | `%timeit np.random.randn(10000)` |
| `%%time` | 整个 cell 跑一次计时 | `%%time` 独占一个 cell 首行 |
| `%matplotlib inline` | 图表直接显示在 cell 下方 | |
| `!command` | 执行 shell 命令 | `!pip install pandas` |
| `%env VAR` | 查看环境变量 | `%env CUDA_VISIBLE_DEVICES` |

### 5. 常见陷阱

| 陷阱 | 现象 | 修复 |
|------|------|------|
| 乱序执行 | 自己机器能跑，别人跑崩 | Kernel → Restart & Run All |
| 隐藏状态 | 删了 cell 但变量还在内存 | 定期重启 kernel |
| 内存泄漏 | 反复加载大数据集不释放 | `del x; gc.collect()` 或重启 kernel |

---

## 练习成绩

| 练习 | 结果 |
|------|------|
| 1. `%timeit` 对比 list vs NumPy | ✅ 17.9ms vs 350μs (50x) |
| 2. Markdown + DataFrame + 绘图 + Restart & Run All | ✅ 全部通过 |
| 3. Colab + T4 GPU 跑 notebook_tips.py | ✅ NumPy 17.7x |

## 测验成绩

| # | 知识点 | 结果 |
|---|--------|------|
| 1 | Jupyter notebook 是什么 | ✅ |
| 2 | Kernel 的作用 | ✅ |
| 3 | `%timeit` vs `%%time` | ✅ |
| 4 | 乱序执行陷阱 | ✅ |
| 5 | notebook → .py 的时机 | ✅ |

**5/5 全过。**

---

## 课后文件

- `notebook_tips.py` — Colab 练习脚本
- `lesson5-exercises.ipynb` — 练习 1+2 的 notebook（手动保存到本目录）
