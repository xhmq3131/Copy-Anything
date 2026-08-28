from urllib.parse import urlparse

from copy_anything.models import DNA


def copy_website(source: str) -> DNA:
    parsed = urlparse(source)
    host = parsed.netloc or source

    return DNA(
        type="website",
        source=source,
        summary=f"待分析网站：{host}",
        structure={
            "host": host,
            "analysis_targets": [
                "页面结构",
                "设计 Token",
                "字体与层级",
                "组件",
                "交互",
                "响应式规则",
                "资源与内容类型",
            ],
        },
        patterns=[
            "先提取设计语言，再决定是否重建页面",
            "优先复用布局与组件模式，不默认复制受保护内容",
        ],
        rebuild_plan=[
            "抓取页面结构与样式信息",
            "生成 Website DNA",
            "输出组件清单",
            "生成目标技术栈页面",
            "截图比较",
            "根据差异迭代",
        ],
        verification=[
            "主要布局是否一致",
            "组件层级是否完整",
            "响应式表现是否合理",
            "视觉差异是否在可接受范围内",
        ],
    )
