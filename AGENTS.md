# AGENTS.md

## 项目目标

构建 **Copy Anything**：输入一个参考对象，先理解它，再提炼 DNA，最后生成可重建方案并验证。

核心流程：

**Observe → Understand → Extract DNA → Rebuild → Verify**

## 当前优先级

只做 V0.1：

1. Copy GitHub
2. Copy Website
3. Copy Skill

不要提前扩到 App、视频、公众号、商业模式等方向，除非前三条已经跑通。

## 开发原则

- 中文文档优先，方便维护。
- 每增加一种输入类型，都必须输出统一 `DNA` 对象。
- 所有能力都应分成：采集、理解、提炼、重建、验证。
- 先做最小可运行版本，再接复杂 Agent。
- 不要只生成漂亮报告；必须能产出下一步可执行结果。
- 不默认复制版权内容、密钥、个人数据或绕过访问控制。

## V0.1 下一步任务

### P0：Copy GitHub 真正跑通

输入 GitHub URL 后：

1. 解析 owner/repo。
2. 获取 README。
3. 获取目录树。
4. 识别语言、依赖、入口文件。
5. 读取最关键的少量文件。
6. 输出：
   - 项目解决什么问题
   - 架构地图
   - 核心调用链
   - 值得复用的设计
   - 不建议照搬的部分
   - 最小重建方案
7. 写入 `output/github.dna.json` 和一份 Markdown 报告。

### P1：Copy Skill 真正跑通

读取 SKILL.md，输出：trigger / inputs / steps / tools / constraints / verification / failure handling。

### P2：Copy Website 真正跑通

获取页面 HTML / DOM / 样式信息，输出 layout / typography / colors / components / interactions。之后再加入截图对比。

## 验收方式

每个 Pipeline 至少提供一个真实样例。不能仅凭 Mock 数据宣布完成。

第一个真实验收对象建议使用一个结构清晰的小型公开 GitHub 仓库。
