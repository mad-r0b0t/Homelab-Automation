import mailbox
import os


def read_latest_emails(limit=5):

    path = os.path.expanduser(
        "~/.thunderbird"
    )

    profile = None

    for folder in os.listdir(path):
        if folder.endswith(".default-release"):
            profile = os.path.join(path, folder)

    if not profile:
        return "Thunderbird profile not found"

    inbox = os.path.join(
        profile,
        "Mail",
        "Local Folders",
        "Inbox"
    )

    if not os.path.exists(inbox):
        return "Inbox not found"

    mbox = mailbox.mbox(inbox)

    messages = list(mbox)[-limit:]

    result = []

    for msg in messages:

        subject = msg["subject"]
        sender = msg["from"]

        result.append(
            f"From: {sender}\nSubject: {subject}"
        )

    return "\n\n".join(result)
