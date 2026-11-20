"""Command-line interface for the legal tagger monitor."""
import argparse
from app import core


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Quantized Legal Tagger Monitor")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("hello")
    for i in range(1, 7):
        sub.add_parser(f"milestone{i}")

    args = parser.parse_args(argv)

    if args.command == "hello":
        print("Quantized Legal Tagger Monitor is ready.")
        return

    functions = {
        "milestone1": core.milestone_1,
        "milestone2": core.milestone_2,
        "milestone3": core.milestone_3,
        "milestone4": core.milestone_4,
        "milestone5": core.milestone_5,
        "milestone6": core.milestone_6,
    }
    result = functions[args.command]()
    if args.command != "milestone6":
        import json
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
