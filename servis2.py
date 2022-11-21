import aiohttp
import asyncio
import time
import aiosqlite
from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterUser")
async def filterUser(request):
        req = await request.json()
        priv = req
    try:
        priv = priv.get("results")
        priv = priv[0].get("name")

        tasks.append({"ime": priv.get("first"),"prezime":priv.get("last")})
        priv = req.get("results")

        tasks.append({"city": priv[0].get("city"),"email":priv[0].get("email")})
        
        priv = []

        print(tasks)
        return web.json_response({"Status": "ok","message":request}, status=200)
    except Exception as e:
        return web.json_response({"Status": "error"}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)

        
