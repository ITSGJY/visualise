# Visualise · ChatGPT 可视化增强版

[简体中文](README.md) | [English](README.en.md)

[![下载最新 Skill](https://img.shields.io/badge/Release-%E4%B8%8B%E8%BD%BD%20Skill%20ZIP-157f65?logo=github)](https://github.com/ITSGJY/visualise/releases/latest) [![上游仓库](https://img.shields.io/badge/Upstream-bentossell%2Fvisualise-555?logo=github)](https://github.com/bentossell/visualise)

这是 [bentossell/visualise](https://github.com/bentossell/visualise) 的 Fork。**原作者的 Visualise Skill 完整保留在仓库根目录**；另在 `chatgpt-visualise/` 目录维护专为 ChatGPT 交互界面设计的独立版本。

它的目标是在对话中用图形**解释机制，而不只是展示代码**：网络与云架构图、工作流、数据流、SVG 示意图、数据图表、对比图、可调参数的交互式微演示。

> **重要：**原版 Visualise 假设客户端能识别 `visualizer` 代码块，并运行自定义 iframe 渲染器。ChatGPT 不保证具备该接口。增强版优先使用 ChatGPT 当前支持的原生可视化方式；需要完整网页交互时，再生成可独立打开的 HTML 文件。它不是原版渲染器的逐字节或功能级复现。

## 两个版本的区别

| | 原版 Visualise | ChatGPT 增强版 |
| --- | --- | --- |
| 文件位置 | 仓库根目录：`SKILL.md`、`references/` | `chatgpt-visualise/` |
| 主要用途 | 支持自定义 `visualizer` 渲染器的 Agent 客户端 | ChatGPT 对话内图解、图表与交互 |
| 输出方式 | HTML/SVG 代码片段交给 iframe | 优先原生组件；必要时交付独立 HTML/SVG 文件 |
| 点击发送消息 | 依赖客户端提供 `sendPrompt()` | 只使用 ChatGPT 已公开支持的交互接口 |
| 参考资料 | 原作者原始规范 | 保留原版全部 7 份文档，另有适配指南 |
| 是否相互覆盖 | 否 | 否 |

## 安装 ChatGPT 增强版（推荐）

1. 打开 **[Releases 最新版本](https://github.com/ITSGJY/visualise/releases/latest)**。
2. 在 **Assets** 中下载 **[`skill.zip`](https://github.com/ITSGJY/visualise/releases/latest/download/skill.zip)**，**不要下载 GitHub 自动生成的 Source code ZIP**。
3. 打开 ChatGPT 的 [Skills 管理页面](https://chatgpt.com/skills)，上传下载的 `skill.zip`。
4. 在对话中选择 **Visualise for ChatGPT**，或通过明确提及 Skill 进行调用。

示例提示：

- “使用 Visualise for ChatGPT，绘制用户 → Cloudflare → API → PostgreSQL 的数据流和信任边界。”
- “用交互式图解解释 Linux Page Cache 与 zram 的区别。”
- “把 NAS 的 RAID 0 / 1 / 5 / 6 / 10 容量及容错特性画成对比图。”
- “用滑块模拟缓存命中率变化，并实时更新命中和未命中次数。”

## 使用原作者版本

原版文件保持在根目录，可按 [原作者说明](https://github.com/bentossell/visualise) 安装，例如：

```bash
git clone https://github.com/bentossell/visualise.git ~/.agents/skills/visualise
```

如果使用不提供 `visualizer` 渲染器的客户端，原版输出的代码块可能只能作为代码阅读。

## 仓库结构

```text
visualise/
├── README.md                  # 中文首页
├── README.en.md               # English README
├── SKILL.md                   # 上游原版 Skill
├── references/                # 上游原版参考文档
├── chatgpt-visualise/
│   ├── SKILL.md               # ChatGPT 专用执行规则
│   ├── agents/openai.yaml     # ChatGPT Skills 展示元数据
│   ├── references/            # 适配指南 + 完整原版参考文档备份
│   ├── assets/                # 示例 SVG / 交互式 HTML
│   └── scripts/               # 静态检查脚本
```

## 致谢与授权

- 上游作者：[bentossell](https://github.com/bentossell/visualise)，原版由 [droid / Factory](https://factory.ai/) 构建。
- 上游项目采用 **MIT License**。本仓库保留原始来源说明；ChatGPT 增强功能为社区非官方适配，不代表原作者或 OpenAI 官方产品。
