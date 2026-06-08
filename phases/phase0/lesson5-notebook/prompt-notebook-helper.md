# prompt-notebook-helper — Notebook 问题诊断速查卡

> Phase 0 · Lesson 5

---

## 常见问题与修复

| 症状 | 原因 | 修复 |
|------|------|------|
| `NameError: name 'x' is not defined` | 变量在别的 cell 定义但当前没跑，或 kernel 重启过了 | 从头 Run All |
| Notebook 自己跑正常，别人跑崩 | 乱序执行造成的隐藏状态 | Kernel → Restart & Run All |
| `ModuleNotFoundError` | 包没装在当前 kernel 的环境里 | `!pip install xxx` 或在终端装 |
| Cell 一直 `[*]` 不结束 | 代码卡死或无限循环 | Kernel → Interrupt |
| 内存越用越多 | 反复加载大数据集不释放 | Kernel → Restart |
| 图表不显示 | 没加 `%matplotlib inline` | 在第一个 cell 加上 |

---

## 诊断步骤

1. **Kernel 活着吗？** 看右下角圆点是实心（活着）还是空心（死了）

2. **环境对吗？**
   ```python
   import sys
   print(sys.executable)
   ```

3. **从头跑一遍：** Kernel → Restart Kernel and Run All Cells

4. **有隐藏状态吗？**
   ```python
   %who   # 列出所有当前变量
   ```
