from bitrix24 import *
import datetime


def test():
    bx24 = Bitrix24("https://b24-ld7a10.bitrix24.com/rest/1/6821gke35v7km390/")
    res = bx24.callMethod(
        "crm.contact.add",
        **{
            "FIELDS": {
                "NAME": "Name",
                "LAST_NAME": "Surname",
                "PHONE": [{"VALUE": "+998950657313", "VALUE_TYPE": "WORK"}],
                "EMAIL": [
                    {"VALUE": "example@gmail.com", "VALUE_TYPE": "WORK"}
                ],
            }
        }
    )
    print(res)


test()
