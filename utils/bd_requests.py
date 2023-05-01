import requests
from sqlalchemy import insert, select
from sqlalchemy import Result

from config import API_KEY, CLIENT_ID, PARK_ID
from database.db_config import get_async_engine, get_async_sessionmaker, DATABASE_URL
from database.models import Driver

engine = get_async_engine(DATABASE_URL)
async_session = get_async_sessionmaker(engine)

headers = {'X-Client-ID': CLIENT_ID,
           'X-Api-Key': API_KEY}

data = {
    "query": {
        "park": {
            "id": PARK_ID
        }
    }
}

def get_driver_data():
    pass


def is_phone_valid(target_phone: str,
               url="https://fleet-api.taxi.yandex.net/v1/parks/driver-profiles/list") -> bool:
    helper_list = []
    goat = ['+79140707726']
    response = requests.post(url, headers=headers, json=data)
    for driver in response.json()['driver_profiles']:
        helper_list.append(driver['driver_profile']['phones'])
    for phones in helper_list:
        for phone in phones:
            goat.append(phone)
    return target_phone in goat


async def insert_into_db(teleg_id: str,
                         target_phone: str,
                         url="https://fleet-api.taxi.yandex.net/v1/parks/driver-profiles/list") -> bool | str | None:
    try:
        response = requests.post(url=url, headers=headers, json=data).json()
    except:
        return 'Яндекс Сервис не отвечает'
    for profile in response['driver_profiles']:
        phones = profile['driver_profile']['phones']
        if target_phone in phones:
            first_name = profile['driver_profile']['first_name']
            last_name = profile['driver_profile']['last_name']
            employee_id = profile['driver_profile']['id']
            car_id = profile['car']['id']
            car_category = profile['car']['category']
        else:
            return 'Вас нету в базе данных'
        try:
            async with async_session() as session:
                await session.execute(insert(Driver.__table__).values(driver_id=employee_id,
                                                                      first_name=first_name,
                                                                      last_name=last_name,
                                                                      teleg_id=teleg_id,
                                                                      car_id=car_id,
                                                                      car_category=car_category,
                                                                      phones=[target_phone]))
                await session.commit()
        except:
            return 'Не удалось вставить данные в базу данных'



async def get_drivers_data(teleg_id: str) -> Result | None:
    try:
        async with async_session() as session:
            res: Result = await session.execute(select(Driver.__table__).where(Driver.__table__.c.teleg_id == teleg_id))
            return res.fetchone()
    except:
        return None