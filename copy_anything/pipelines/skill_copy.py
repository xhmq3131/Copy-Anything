from pathlib import Path

from copy_anything.models import DNA


def copy_skill(source: str) -> DNA:
    path = Path(source)
    label = path.name if path.name else source

    return DNA(
        type="skill",
        source=source,
        summary=f"待分析 Skill：{label}",
        structure={
            "analysis_targets": [
                "触发条件",
                "输入",
                "执行步骤",
                "工具依赖",
                "并行/串行关系",
                "输出",
                "验证方式",
                "失败处理",
            ]
        },
        patterns=[
            "把自然语言 Skill 转换成显式工作流",
            "把工具依赖和验证步骤独立出来",
            "尽量保留能力，不照搬平台绑定语法",
        ],
        rebuild_plan=[
            "读取 SKILL.md",
            "提取触发和约束",
            "拆解工作流节点",
            "识别工具调用",
            "生成 Workflow DNA",
            "转换到目标 Agent/Codex 形式",
            "运行样例验证",
        ],
        verification=[
            "触发条件是否保持",
            "关键步骤是否遗漏",
            "工具依赖是否可替换",
            "输出是否符合原目标",
        ],
    )
