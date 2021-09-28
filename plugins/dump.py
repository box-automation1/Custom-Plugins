#Author: Box In A Box [TG: @Box_Boi ]

from userge import userge, Message
from userge.utils import runcmd

@userge.on_cmd("dump", about={
    'header': "Android Firmware Dumping Tool",
    'usage': "{tr}dump (Firmware Link)",
    'examples': "{tr}dump http://bigota.d.miui.com/V11.0.2.0.NCFCNXM/mido_images_V11.0.2.0.NCFCNXM_20191107.0000.00_7.0_cn_07679911aa.tgz"})
async def test_(message: Message):
    """ Initiate Dump Process """
    cmd = message.input_str
    if cmd is None:
        return
    await message.edit("**Trying To Dump Given Link ...**")
    try:
        out, err, ret, pid = await runcmd("bash dump.sh " + cmd)
    except Exception as t_e:
        await message.err(str(t_e))
        return
    out = out or "no output"
    out = "\n".join(out.split("\n"))
    output = f"**Dumps Will Be Pushed On @boxdumps**\n\n**Dump Status/Workflow Link:**\n\n``{out}`` "
    await message.edit_or_send_as_file(text=output,
                                       parse_mode='md',
                                       filename="exec.txt",
                                       caption=cmd)
