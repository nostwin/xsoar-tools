from demistomock.CommonServerPython import *
from demistomock import demistomock as demisto

from email.message import EmailMessage
from random import randint


def generate_msg(args: dict) -> EmailMessage:
    """ Generate the email message object"""
    msg = EmailMessage()

    msg['Subject'] = args.get("subject")
    msg['From'] = args.get("from_")
    msg['To'] = args.get("to")
    msg['Cc'] = args.get("cc")
    msg['Bcc'] = args.get("bcc")
    msg.set_content(args.get("body"))

    return msg


def create_msg_file(msg: EmailMessage, template_id: str | int) -> dict:
    """ Create .eml email template and return it to the war room """
    template_name = f"template_{template_id}.eml"
    demisto.setContext("generated_template", template_name)
    with open(template_name, "wb") as f:
        f.write(bytes(msg))

    with open(template_name, 'rb') as _file:
        return fileResult(template_name, _file.read())


def main() -> None:
    try:
        args = demisto.args()
        template_id = randint(1, 999)
        msg = generate_msg(args)
        demisto.results(create_msg_file(msg, args.get("template_id", template_id)))
    except Exception as e:
        return_error(repr(e))


if __name__ in ("__main__", "__builtin__", "builtins"):
    main()
