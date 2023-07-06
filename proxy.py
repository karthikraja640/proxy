import asyncio
from proxybroker import Broker

def save_proxy(proxy):
    with open('proxies.txt', 'a') as f:
        if 'SOCKS4' in proxy.types:
            f.write(f'{proxy.host}:{proxy.port}\n')

async def main():
    broker = Broker(callback=save_proxy)
    await broker.find(types=['SOCKS4'])

    await broker.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
￼Enter
