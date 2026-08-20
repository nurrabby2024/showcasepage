"""Minimal example for ShowcasePage."""

from showcasepage import showcasepage


def main():
 runner = showcasepage({"name": "ShowcasePage", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()