import sys
import asyncio
import subprocess
from spoolman import Spool, Spoolman

# argument = sys.argv[1]

SERVER_ADDRESS = "10.50.1.7"

async def getSpools() -> None:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host=SERVER_ADDRESS) as client:
        # print("All spools")
        # print("==========")
        # spools: list[Spool] = await client.get_spools()
        # for spool in spools:
        #     print(spool)
        #
        # print()
        # print("Single spool")
        # print("============")

        single_spool: Spool = await client.get_spool(spool_id=3)
        print("Name: " + str(single_spool.filament.name))
        print("Extruder Temp: " + str(single_spool.filament.extruder_temp))
        print("Bed Temp: " + str(single_spool.filament.bed_temp))



match sys.argv[1]:
    case Spools:
        asyncio.run(getSpools())
    case _:
        subprocess.run("echo """)
