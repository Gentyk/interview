from aiohttp import web
import aiohttp


async def hello(request):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://services.drova.io/") as resp:
            return web.Response(text=str(resp.status))


app = web.Application()
app.add_routes([web.get("/", hello)])
web.run_app(app)
