# Phase 0 总结 — 环境布置

> 完成日期：2026-06-08
> 系统：WSL Ubuntu 26.04 LTS × RTX 4060 Laptop

---

## 学到的核心概念

### 1. 编程语言的三种运行方式

| 类型 | 语言 | 原理 |
|------|------|------|
| 解释型 | Python、JavaScript | 边跑边翻译，慢但灵活 |
| JIT 编译 | Julia | 第一次跑时编译，之后用编译版 |
| AOT 编译 | Rust | 提前全编译成二进制，独立运行 |

### 2. 包管理器演进

| 旧 | 新 | 快的原因 |
|------|------|------|
| pip | **uv** | Rust 重写 + 并行下载 + 全局缓存 |
| npm | **pnpm** | 全局存储 + 硬链接，省空间 |

### 3. 虚拟环境 + 全局缓存

- 虚拟环境：每个项目独立的包空间，互不冲突
- 全局缓存（uv）：包只存一份在 `~/.cache/uv/`，各虚拟环境通过硬链接指向它
- 删除虚拟环境 ≠ 删除缓存

### 4. CUDA

- 不是编程语言，是 NVIDIA 的计算平台
- 让 PyTorch 等库能把矩阵运算丢给 GPU 并行跑
- `torch.cuda.is_available()` 验证 PyTorch 能否调用 GPU

### 5. 四层环境栈

```
层 4: AI/ML 库（PyTorch）
层 3: 语言运行时（Python、Node.js、Julia）
层 2: 包管理器（uv、pnpm、cargo）
层 1: 系统基础（OS、GPU 驱动、Git）
```

安装顺序：**从下往上**。

---

## 安装清单

| 组件 | 版本 | 验证命令 |
|------|------|------|
| Python | 3.12.13 | `python3 --version` |
| NumPy | 2.4.6 | `python -c "import numpy"` |
| Matplotlib | 3.10.9 | `python -c "import matplotlib"` |
| Jupyter | 4.5.8 | `python -c "import jupyter"` |
| Node.js | 22.22.3 | `node --version` |
| pnpm | 11.5.2 | `pnpm --version` |
| Rust | 1.96.0 | `rustc --version` |
| Cargo | 1.96.0 | `cargo --version` |
| Julia | 1.12.6 | `julia --version` |
| PyTorch | 2.6.0+cu124 | `python -c "import torch; print(torch.__version__)"` |
| CUDA | True | `python -c "import torch; print(torch.cuda.is_available())"` |
| Git | ✓ | `git --version` |

---

## 常用命令速查

### 虚拟环境
```bash
uv venv .venv              # 创建
source .venv/bin/activate  # 激活（Linux）
deactivate                 # 退出
```

### 包安装
```bash
uv pip install numpy matplotlib jupyter
uv pip install torch --index-url https://download.pytorch.org/whl/cu124
```

### PATH 刷新
```bash
source "$HOME/.cargo/env"   # Rust
source "$HOME/.bashrc"      # Julia / 通用
```

### Hello World 四种语言
```bash
python -c "print('Hello, World!')"                                      # Python
node -e "console.log('Hello, World!')"                                  # Node.js
julia -e 'println("Hello, World!")'                                     # Julia
echo 'fn main(){println!("Hello, World!");}' > h.rs && rustc h.rs -o h && ./h  # Rust
```

---

## 验证脚本

```bash
python verify.py
```

期望：`7/7 core, 2/2 GPU — You're ready.`

---

## 测验成绩

| 题号 | 知识点 | 结果 |
|------|------|------|
| 1 | 虚拟环境隔离依赖 | ✓ |
| 2 | CUDA 并行计算 | ✓ |
| 3 | 四层环境栈顺序 | ✓ |
| 4 | uv 快速包管理器 | ✓ |
| 5 | `torch.cuda.is_available()` | ✓ |

5/5 全过。
