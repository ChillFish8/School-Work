import asyncio
import aiohttp
import bs4
import itertools

scp_number_iterator = itertools.count(1, 1)
scp_data = {}

MAX_CONCURRENCY = 5
SCP_COUNT = 6000
SCP_SPLIT = [x for x in range(SCP_COUNT)]
scp_chunks = []

scp_block = []
for index, scp in enumerate(SCP_SPLIT):
    if (index % 5) == 0 and index != 0:
        scp_chunks.append(scp_block)
        scp_block = []
        print(len(scp_chunks), "Chunks Completed")
    scp_block.append(scp)
print(f"Total chunks: {len(scp_chunks)}")


async def site_gatherer(number):
    print("Generating Task")
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                f"http://www.scp-wiki.net/{str(number) if number > 99 else '000'[:len(str(number))] + str(number)}",
                allow_redirects=True) as resp:
            if resp.status == 200:
                html = await resp.read()
                scp_data[f'{number}'] = html
            else:
                print(f"Ignoring SCP: {number}, invalid response from site, code@ {resp.status}")


async def generate_tasks():
    print(scp_chunks)
    for chunk in scp_chunks:
        await asyncio.gather(site_gatherer(chunk[0]),
                             site_gatherer(chunk[1]),
                             site_gatherer(chunk[2]),
                             site_gatherer(chunk[3]),
                             site_gatherer(chunk[4]),
                             loop=asyncio.get_event_loop())


async def main():
    await generate_tasks()


#if __name__ == "__main__":
asyncio.run(main())