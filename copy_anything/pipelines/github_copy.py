from urllib.parse import urlparse

from copy_anything.models import DNA


def copy_github(source: str) -> DNA:
    """V0.1：先把 GitHub 输入标准化并生成分析任务骨架。

    下一阶段再接 GitHub API / LLM，真实读取 README、目录、依赖和关键代码。
    """
    parsed = urlparse(source)
    parts = [p for p in parsed.path.split("/") if p]
    repo = "/".join(parts[:2]) if len(parts) >= 2 else source

    return DNA(
        type="github",
        source=source,
        summary=f"待分析 GitHub 项目：{repo}",
        structure={
            "repository": repo,
            "analysis_targets": [
                "README 与项目目标",
                "目录结构",
                "核心依赖",
                "关键模块",
                "数据流与控制流",
                "可复用设计模式",
            ],
        },
        patterns=[
            "找出项目真正解决的问题",
            "区分值得复用的思想与不应照搬的实现",
            "提炼最小可重建版本",
        ],
        rebuild_plan=[
            "读取项目入口和 README",
            "生成架构地图",
            "定位核心代码",
            "抽取 Project DNA",
            "生成自己的重建计划",
            "实现并验证关键功能",
        ],
        verification=[
            "项目目标是否理解正确",
            "核心调用链是否有证据支持",
            "重建版本是否真正实现核心能力",
        ],
    )
