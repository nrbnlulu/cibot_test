from pathlib import Path
import re


def main():
    print("Hello from cibot-test!")
    SEMVER_REGEX = re.compile(r"(\d+)\.(\d+)\.(\d+)")
    pp_toml = (Path.cwd() / "pyproject.toml")
    content = pp_toml.read_text()
    if matched := SEMVER_REGEX.search(content):
        print(f"Found semver: {matched.group(0)}")
        # replace
        new_version = f"{matched.group(1)}.{matched.group(2)}.{int(matched.group(3)) + 1}"
        print(f"New version: {new_version}")
        new_content = SEMVER_REGEX.sub(new_version, content)
        pp_toml.write_text(new_content)

if __name__ == "__main__":
    main()
wow cool feat