from demistomock.CommonServerPython import *
from demistomock import demistomock as demisto


def main() -> None:
    args = demisto.args()
    dict_path = args.get('dict_path')
    set_key = args.get('set_key')
    set_value = args.get('set_value')
    output_key = args.get('output_key', 'UpdatedDict')

    if not isinstance(dict_path, dict):
        return_error(message=f"No dict was provided. Provided type {type(dict_path)}")

    dict_path[set_key] = set_value

    command_results = CommandResults(
        outputs_prefix=output_key,
        outputs=dict_path
    )
    return_results(command_results)


if __name__ in ("__main__", "__builtin__", "builtins"):
    main()
