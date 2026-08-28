# Copy Anything

> 把任何优秀对象，转换成可理解、可复用、可重新构建的 DNA。

## 核心理念

Copy Anything 不是简单复制文件，而是执行：

**Observe → Understand → Extract DNA → Rebuild → Verify**

第一版 V0.1 只做三条主线：

1. **Copy Website**：输入 URL，提取设计、页面结构、组件、交互等 DNA。
2. **Copy GitHub**：输入仓库地址，分析架构、核心模块、值得复用的思路，并输出重建计划。
3. **Copy Skill**：输入 Skill / SKILL.md，抽取触发条件、流程、工具、校验方式，转换为统一 Workflow DNA。

## 统一输出

所有对象都尽量转换成统一的 DNA：

```json
{
  "type": "github|website|skill",
  "source": "...",
  "summary": "...",
  "structure": {},
  "patterns": [],
  "rebuild_plan": [],
  "verification": []
}
```

## 快速开始

```bash
python -m copy_anything.cli github https://github.com/owner/repo
python -m copy_anything.cli website https://example.com
python -m copy_anything.cli skill ./SKILL.md
```

当前 V0.1 是可扩展骨架：先把输入标准化、DNA 结构和输出流程跑通，再逐步接入浏览器、LLM、截图对比、GitHub API 和 Agent。

## 项目结构

```text
copy-anything/
├── copy_anything/
│   ├── cli.py
│   ├── models.py
│   └── pipelines/
│       ├── github_copy.py
│       ├── website_copy.py
│       └── skill_copy.py
├── schemas/
│   └── dna.schema.json
├── AGENTS.md
├── ROADMAP.md
└── pyproject.toml
```

## V0.1 验收标准

- [x] 一个统一 CLI 入口
- [x] 三种 Copy 类型
- [x] 一个统一 DNA 数据结构
- [x] 每次运行都生成 JSON 结果
- [ ] GitHub 仓库真实分析
- [ ] 网站抓取与 DOM 分析
- [ ] Skill 语义分析
- [ ] LLM 提炼 DNA
- [ ] 自动生成 Rebuild Plan
- [ ] 自动 Verify

## 边界

项目用于学习、分析、互操作、迁移与重新实现。应尊重软件许可证、版权、网站条款、隐私与访问控制；默认提炼模式和结构，不默认复制受保护内容或绕过技术限制。
