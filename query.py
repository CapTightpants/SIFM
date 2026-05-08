import sys
import asyncio
import subprocess
from spoolman import Spool, Spoolman

# argument = sys.argv[1]

SERVER_ADDRESS = "10.50.1.7"

class SpoolData:
    names = []
    materials = []
    extruderTemp = []
    bedTemp = []


async def getSpools() -> SpoolData:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host=SERVER_ADDRESS) as client:
        spoolData = SpoolData()
        # print("All spools")
        # print("==========")
        spools: list[Spool] = await client.get_spools()
        for spool in spools:
            spoolData.names.append(spool.filament.name)
            spoolData.materials.append(spool.filament.material)
            spoolData.extruderTemp.append(spool.filament.extruder_temp)
            spoolData.bedTemp.append(spool.filament.bed_temp)
        return spoolData
            
        #
        # print()
        # print("Single spool")
        # print("============")

        # single_spool: Spool = await client.get_spool(spool_id=3)
        # print("Name: " + str(single_spool.filament.name))
        # print("Extruder Temp: " + str(single_spool.filament.extruder_temp))
        # print("Bed Temp: " + str(single_spool.filament.bed_temp))

def sendGCode(command):
    subprocess.run("echo '" + command + "' > ~/printer_data/comms/klippy.serial", shell=True)

def respond() -> None:
    spoolData = asyncio.run(getSpools())
    namesStr = ",".join(spoolData.names)
    print(len(spoolData.names))
    sendGCode('SIFM_PROMPT names=' + namesStr)

match sys.argv[1]:
    case "Spools":
        respond()
    case _:
        sendGCode('RESPOND TYPE=error MSG="An error has occurred."')
