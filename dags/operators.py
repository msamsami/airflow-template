import os

import pandas as pd


def first_operator(**context):
    print("From the first_operator execution: Hello World!")
    app_secret = os.getenv("MY_APP_SECRET")
    context["ti"].xcom_push(key="app_secret", value=app_secret)


def second_operator(**context):
    app_secret = context.get("ti").xcom_pull(key="app_secret")

    data = [
        {
            "name": "Mehdi Samsami",
            "title": "Data Scientist",
        },
        {
            "name": "Hesam Sharifi",
            "title": "Product Manager",
        },
    ]

    df = pd.DataFrame(data=data)

    print("@" * 60)
    print(df.head())
    print("@" * 60)

    print("From the second_operator execution: Hey there!")
    print(f"This is the app secret received from the first_operator: {app_secret}")
