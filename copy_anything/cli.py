import argparse
import json
from pathlib import Path

from copy_anything.pipelines.github_copy import copy_github
from copy_anything.pipelines.skill_copy import copy_skill
from copy_anything.pipelines.website_copy import copy_website


PIPELINES = {
    "github": copy_github,
    "website": copy_website,
    "skill": copy_skill,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="copy-anything",
        description="把参考对象转换成可理解、可复用、可重建的 DNA。",
    )
    parser.add_argument("kind", choices=PIPELINES.keys(), help="要 Copy 的对象类型")
    parser.add_argument("source", help="URL、GitHub 仓库地址或 Skill 文件路径")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="输出 JSON 文件路径；不填写时使用 output/<type>.dna.json",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    dna = PIPELINES[args.kind](args.source)

    output = Path(args.output or f"output/{args.kind}.dna.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(dna.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"完成：{output}")
    print(json.dumps(dna.to_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
