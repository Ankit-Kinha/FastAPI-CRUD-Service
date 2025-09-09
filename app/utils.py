def normalize_title(title: str) -> str:
    \"\"\"Lowercase, strip and collapse spaces into hyphens.\"\"\"
    return \"-\".join(title.lower().strip().split())
