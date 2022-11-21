import aiohttp
import asyncio
import time
import aiosqlite


from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterJoke")
async def filterJoke(request):
    req = await request.json()
    priv = []
    try:
        priv.append({"setup":req.get("setup")})
        priv.append({"punchline":req.get("punchline")})
        print(temp)
        return web.json_response({"Status": "ok","message":request}, status=200)
    except Exception as e:
        return web.json_response({"Status": "error"}, status=500)


app.router.add_routes(routes)

web.run_app(app, port=8082)

