import aiosqlite
import sqlite3
import aiohttp
import asyncio
from aiohttp import web
import time

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def get_getJokes_db(request):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            taskKorisnici = []
            taskŠale = []
            for _ in range(6):
                for _ in range(10):
                    taskŠala.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
                    taskKorisnici.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
            resŠala = await asyncio.gather(*taskŠala)
            resKorisnici = await asyncio.gather(*taskKorisnici)
            json_data_Šala = [await x.json() for x in res]
            json_data_Korisnici = [await x.json() for x in res]

            taskŠala = asyncio.create_task(sendToParserŠala(json_data_Šala, session))
            taskPerson = asyncio.create_task(sendToParserPerson(json_data_Šala, session))
            service2_response = await taskŠala
            service3_response = await taskPerson

            return web.json_response({"status:":"ok"}, status=200)
    except Exception as e:
        return web.json_response({"status:":"fail","message:": str(e)})

async def sendToParserPerson(json_activities, session):
    for i in range(len(json_activities)):
        async with session.post("http://localhost:8081/filterUser", json=json_activities[i]) as resp:
            print("Sending to parser - ", i)
            service2_response = await resp.text()
    return service2_response

async def sendToParserŠala(json_activities, session):
    for i in range(len(json_activities)):
        async with session.post("http://localhost:8082/filterJoke", json=json_activities[i]) as resp:
            print("Sending to parser - ", i)
            service2_response = await resp.text()
    return service2_response

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8080)