import asyncio
import datetime

import requests
from sqlalchemy import Result

from config import API_KEY, CLIENT_ID, PARK_ID
from bd_requests import get_drivers_data
headers = {'X-Client-ID': CLIENT_ID,
           'X-Api-Key': API_KEY}
URL = 'https://fleet-api.taxi.yandex.net/v1/parks/orders/list'

async def get_order_list(teleg_id: str):

  driver_data: Result = await get_drivers_data(teleg_id=teleg_id)
  driver_profile_id: int = driver_data[1]

  car_id: str = driver_data[6]
  car_category: list[str] = driver_data[7]

  current_time = datetime.datetime.now(datetime.timezone.utc)
  booking_time_from = (current_time - datetime.timedelta(minutes=2)).isoformat()

  request_body = {
    "cursor": "string",
    "limit": 100,
    "query": {
      "park": {
        "car": {
          "id": car_id
        },
        "driver_profile": {
          "id": driver_profile_id
        },
        "id": PARK_ID,
        "order": {
          "booked_at": {
            "from": booking_time_from,
            "to": current_time.isoformat()
          },
          "categories": car_category,
          "ended_at": {
            "from": booking_time_from,
            "to": current_time.isoformat()
          },
          "payment_methods": [
            "card",
            "cash"
          ],
          "providers": [
            "yandex"
          ],
          "statuses": [
            "searching"
          ],
          "type": {
            "ids": [
              "4964b852670045b196e526d59915b777"
            ]
          }
        }
      }
    }
  }
  response = requests.post(URL, headers=headers, json=request_body)
  return response.json()


print(asyncio.run(get_order_list()))
