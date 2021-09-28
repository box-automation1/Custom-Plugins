#Author: Box In A Box [TG: @Box_Boi ]

from userge import userge, Message
from userge.utils import runcmd

@userge.on_cmd("pdump", about={
    'header': "Android Firmware Dumping Tool(To Github Private Repo)",
    'usage': "{tr}pdump (Firmware Link)",
    'examples': "{tr}pdump http://bigota.d.miui.com/V11.0.2.0.NCFCNXM/mido_images_V11.0.2.0.NCFCNXM_20191107.0000.00_7.0_cn_07679911aa.tgz"})
async def test_(message: Message):
    """ Initiate Private Dump Process """
    cmd = message.input_str
    if cmd is None:
        return
    await message.edit("**Trying To Dump Given Link(Privately) ...**")
    try:
        out, err, ret, pid = await runcmd("bash pdump.sh " + cmd)
    except Exception as t_e:
        await message.err(str(t_e))
        return
    out = out or "no output"
    out = "\n".join(out.split("\n"))
    output = f"**Dumps Will Be Pushed On Private Github Org Soon!**\n\n**Dump Status/Workflow Link:**\n\n``{out}`` "
    await message.edit_or_send_as_file(text=output,
                                       parse_mode='md',
                                       filename="exec.txt",
                                       caption=cmd)
