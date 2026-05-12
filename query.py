import sys
import asyncio
import subprocess
import unicodedata
from spoolman import Spool, Spoolman

# argument = sys.argv[1]

SERVER_ADDRESS = "10.50.1.7"

class SpoolData:
    names = []
    materials = []
    extruderTemp = []
    bedTemp = []

def sanitize(toSanitize) -> str:
    sanitized = unicodedata.normalize("NFKD", toSanitize)
    return sanitized


async def getSpools() -> SpoolData:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host=SERVER_ADDRESS) as client:
        spoolData = SpoolData()
        # IMPORTANT: The index of the parameter matches the ID number of the spool!
        spools: list[Spool] = await client.get_spools()
        for spool in spools:
            spoolData.names.insert(spool.id, sanitize(spool.filament.name))
            spoolData.materials.insert(spool.id, spool.filament.material)
            spoolData.extruderTemp.insert(spool.id, str(spool.filament.extruder_temp))
            spoolData.bedTemp.insert(spool.id, str(spool.filament.bed_temp))
        return spoolData

def sendGCode(command):
    subprocess.run("echo '" + command + "' > ~/printer_data/comms/klippy.serial", shell=True)

def respond() -> None:
    spoolData = asyncio.run(getSpools())
    namesStr = ",".join(spoolData.names)
    materialsStr = ",".join(spoolData.materials)
    extruderStr = ",".join(spoolData.extruderTemp)
    bedStr = ",".join(spoolData.bedTemp)
    sendGCode('_SIFM_RECEIVE NAMES="' + namesStr + '" MATERIALS="' + materialsStr + '" EXTRUDERS="' + extruderStr + '" BEDS="' + bedStr + '"')

match sys.argv[1]:
    case "Spools":
        respond()
    case _:
        sendGCode('RESPOND TYPE=error MSG="An error has occurred."')
