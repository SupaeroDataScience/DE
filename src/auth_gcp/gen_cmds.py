import pandas as pd

base = "gcloud projects add-iam-policy-binding isae-sdd --member='user:{}' --role='roles/editor'\n"

df = pd.read_csv("gmails.csv")

with open("cmd.sh", "w") as f:
    for _, r in df.iterrows():
        email = str(r.get("mails")).replace(" ","")

        cmd = base.format(email)
        f.write(cmd)

