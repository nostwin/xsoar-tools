from demistomock.CommonServerPython import *
from demistomock import demistomock as demisto

def main() -> None:
    ...

    command_results = CommandResults(
        outputs_prefix='test',
        outputs='test'
    )
    return_results(command_results)


if __name__ in ("__main__", "__builtin__", "builtins"):
    main()