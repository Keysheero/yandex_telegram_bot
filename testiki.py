# # import requests
# # import pprint
# # headers = {
# #     'X-Client-ID': 'taxi/park/50f91784ec3d469187a664dc71829095',
# #     'X-Api-Key': 'pRvgEogHkEiPOlxgRlzaIMGpFvjosnOQ',
# # }
# #
# #
# # url = "https://fleet-api.taxi.yandex.net/v1/parks/driver-profiles/list"
# #
# #
# data = {
#     "query": {
#         "park": {
#             "id": "50f91784ec3d469187a664dc71829095"
#         }
#     }
# }
# #
# # response = requests.post(url, headers=headers, json=data)
# #
# # print(response.status_code)
# # # pprint.pprint(response.json()['driver_profiles'][0]['driver_profile']['first_name'])
# # pprint.pprint(response.json())
# from sqlalchemy import insert, select
# from sqlalchemy.orm import sessionmaker
# from database.models import Driver
# from database.db_config import get_async_engine, get_async_sessionmaker, DATABASE_URL
# import asyncio
#
#
# engine = get_async_engine(DATABASE_URL)
# async_session = get_async_sessionmaker(engine)
#
#
# async def get_driver():
#     async with async_session() as session:
#         result = await session.execute(insert(Driver.__table__).values(id=2,
#                                                                        first_name='Egor',
#                                                                        last_name='Mihailov',
#                                                                        phones=['0129192192']))
#         await session.commit()
#
#
# asyncio.run(get_driver())
import asyncio

import requests
from sqlalchemy import select, insert, Result

from config import API_KEY
from database.models import Driver
from utils.bd_requests import async_session


# total_list = []
# some_list = [[1], [2], [3,4]]
# for i in some_list:
#     total_list.append(*i)
# print(total_list)

# async def get_drivers_data(teleg_id: str) -> dict | None | str:
#     try:
#         async with async_session as session:
#             res = await session.execute(select(Driver.__table__).where(Driver.__table__.c.teleg_id == teleg_id))
#             print(type(res.fetchone))
#             return res.fetchone()
#     except:
#         return 'пизда'
#
#
# print(get_drivers_data())
# import` asyncio
# import datetime
#
# import requests
# from sqlalchemy import Result
#
# from config import API_KEY, CLIENT_ID, PARK_ID
# from utils.bd_requests import get_drivers_data
# headers = {'X-Client-ID': CLIENT_ID,
#            'X-Api-Key': API_KEY}
# URL = 'https://fleet-api.taxi.yandex.net/v1/parks/orders/list'
#
# async def get_order_list(teleg_id: str):
#   driver_profile_id: str = "562560b19a534711b76e42c29fe3889a"
#
#   car_id: str = "3a6b2b2d585d925cca4da83aed067741"
#   car_category: list[str] = ['comfort', 'econom']
#
#   current_time = datetime.datetime.now(datetime.timezone.utc)
#   booking_time_from = (current_time - datetime.timedelta(minutes=2)).isoformat()
#
#   request_body = {
#     "limit": 100,
#     "query": {
#       "park": {
#         "car": {
#           "id": car_id
#         },
#         "driver_profile": {
#           "id": driver_profile_id
#         },
#         "id": PARK_ID,
#         "order": {
#           "booked_at": {
#             "from": booking_time_from,
#             "to": current_time.isoformat()
#           },
#           "categories": car_category,
#
#           "payment_methods": [
#             "card",
#             "cash"
#           ],
#           "providers": [
#             "platform"
#           ],
#           "statuses": [
#             "waiting"
#           ],
#           "type": {
#             "ids": [
#               "4964b852670045b196e526d59915b777"
#             ]
#           }
#         }
#       }
#     }
#   }
#   response = requests.post(URL, headers=headers, json=request_body)
#   return response.json()
#
#
# print(asyncio.run(get_order_lis`t('120')))
headers = {'Authorization': 'akop.tufyan'}


response = requests.get('https://business.taxi.yandex.ru/api/auth', headers=headers)
print(response.json())