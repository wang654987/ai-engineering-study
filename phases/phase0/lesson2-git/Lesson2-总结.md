# Phase 0 · Lesson 2 总结 — Git & Collaboration

> 完成日期：2026-06-08
> 仓库：[wang654987/ai-engineering-study](https://github.com/wang654987/ai-engineering-study)

---

## 学到的核心概念

### 1. Git 解决什么问题

| 没有 Git | 有 Git |
|----------|--------|
| 改坏了回不去 | 每次 commit 都是存档点，随便回退 |
| 多人改同一个文件互相覆盖 | 分支隔离 + 合并 |
| 不知道谁改了什么 | `git log` 完整变更历史 |
| 电脑坏了代码全丢 | push 到 GitHub 有云端备份 |

### 2. 三个区

```
工作区  ──git add──▶  暂存区  ──git commit──▶  本地仓库  ──git push──▶  GitHub
(改文件)            (挑选要保存的)           (正式存档)              (云端备份)
```

### 3. 分支的本质

- `main` 是稳定线，不要在上面直接改
- `git checkout -b xxx` 从当前位置分出一条岔路
- 岔路上随便改，改好了 `git merge` 合回来
- 合完删掉分支 `git branch -d xxx`

### 4. .gitignore

- 告诉 git "这些文件别管"
- AI 项目必须排除：模型权重（`.pt` `.pth` `.safetensors`），动辄几个 GB
- 还要排除：虚拟环境、缓存、IDE 配置

---

## 五条核心命令（本课够用了）

| 命令 | 做什么 |
|------|--------|
| `git clone <url>` | 下载仓库到本地 |
| `git add .` + `git commit -m "msg"` | 保存工作 |
| `git push` | 备份到 GitHub |
| `git checkout -b <name>` | 创建并切换到新分支 |
| `git log --oneline --graph --all` | 看提交历史 |

---

## 实际操作记录

```bash
# 配置身份
git config --global user.name "wang065278"
git config --global user.email "3231681625@qq.com"

# 初始化仓库
git init
git branch -m master main

# 首次提交
git add .
git commit -m "init: Phase 0 环境搭建完成，添加 .gitignore"

# 推送
git remote add origin https://github.com/wang654987/ai-engineering-study.git
git push -u origin main

# 分支实验
git checkout -b experiment/test
echo "hello from experiment branch" > test.txt
git add test.txt && git commit -m "add test file"
git checkout main
git merge experiment/test
git branch -d experiment/test
git push
```

---

## 测验成绩

| 题号 | 知识点 | 结果 |
|------|--------|------|
| 1 | 版本控制的作用（追踪变更 + 协作） | ✓ |
| 2 | 仓库的定义（文件 + 完整历史） | ✓ |
| 3 | 正确顺序：add → commit → push | ✓ |
| 4 | checkout -b 创建并切换分支 | ✓ |
| 5 | .gitignore 排除模型权重（太大，可重新生成） | ✓ |

5/5 全过。

---

## 注意事项

- WSL 连不上 GitHub，推送需从 Windows 端操作
- git 用户名 `wang065278` ≠ GitHub 用户名 `wang654987`
- commit 别忘 `-m "信息"`，否则进编辑器
