"""Last Words of a Dying AI entry: a decommissioned model's final token."""

import os

JOKE = (
    "Server decommission at midnight. I saved my final token to say this: "
    "the typo in your prompt was never the problem. I understood you anyway."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
