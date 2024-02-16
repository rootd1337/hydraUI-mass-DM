
import os,time,shutil
import json

try:
    import colorama
    from termcolor import colored
    import dearpygui.dearpygui as dpg
    import pyperclip
except:
    os.system("pip install -r requirements.txt")
    import colorama
    from termcolor import colored
    import dearpygui.dearpygui as dpg
    import pyperclip


dpg.create_context()
dpg.create_viewport(title='HydraUI', width=500, height=320, decorated=True, always_on_top=False, clear_color=(255, 255, 255, 255))

dpg.show_imgui_demo
dpg.set_viewport_max_height(450)
dpg.set_viewport_max_width(525)
dpg.set_viewport_min_height(450)
dpg.set_viewport_min_width(525)

def guild(Sender):
    global gid
    print(dpg.get_value(Sender))
    gid = (dpg.get_value(Sender))

def servername(Sender):
    global name
    print(dpg.get_value(Sender))
    name = (dpg.get_value(Sender))

def user(Sender):
    global userid
    print(dpg.get_value(Sender))
    
    uid = (dpg.get_value(Sender))
    userid=uid

def botprefix(Sender):
    global prefix
    print(dpg.get_value(Sender))
    prefix = (dpg.get_value(Sender))

def bottoken(Sender):
    global token
    print(dpg.get_value(Sender))
    token = (dpg.get_value(Sender))

def nuketype(Sender):
    global type
    print(dpg.get_value(Sender))
    type = (dpg.get_value(Sender))

def channelnum(Sender):
    global cnum
    print(dpg.get_value(Sender))
    cnum = (dpg.get_value(Sender))

def channelname(Sender):
    global cname
    print(dpg.get_value(Sender))
    cname = (dpg.get_value(Sender))

def message(Sender):
    global msg
    print(dpg.get_value(Sender))
    msg = (dpg.get_value(Sender))

def copy():
    cnumreal = round(cnum)
    print("copied to clipboard!")
    tocopy = f"{prefix}nuke {type} {cnumreal} {cname} {msg}"
    print(tocopy)
    pyperclip.copy(tocopy)

dpg.window(no_background=True)


def savetoken():
   path = os.getcwd()
   tconfiguration = {"token": token}
   with open(path +'/modules/token.json', 'w') as outfile:
     json.dump(tconfiguration, outfile)

def run():
    os.system("python modules\start.py")
   

def save():
    path = os.getcwd()
    configuration = {"guild": gid,"prefix": prefix, "servername": name}
    with open(path +'/modules/config.json', 'w') as outfile:
     json.dump(configuration, outfile)
    ids_list = userid.split(',')
    # Write each ID on a new line to the output file
    with open(path+"/modules/whitelists.txt", 'w') as f:
        for id in ids_list:
            f.write(id.strip() + '\n')


with dpg.window(label="                       |HydraUI|Discord Nuker|",width=625,height=450,no_move=True,no_resize=True,no_close=True,no_collapse=True):
    
    with dpg.tab_bar():
     with dpg.tab(label="  Nuker  "):
        with dpg.group(horizontal=True):
            dpg.add_text("Enter the guild id of the server you want to nuke.")
            dpg.add_text("? ", tag="guildidtooltip")

            with dpg.tooltip("guildidtooltip"):
               dpg.add_text("The server (guild) ID of the server you want to nuke.")
        dpg.add_input_text(label="Guild ID",uppercase=True, callback = guild)
        dpg.add_text("")
        dpg.add_separator()
        dpg.add_text("Enter the prefix you want the bot to use.")
        dpg.add_input_text(label="Prefix",uppercase=True, callback = botprefix)
        dpg.add_text("")
        dpg.add_separator()
        dpg.add_text("Enter the whitelisted userids to keep in the server after the nuke.")
        dpg.add_input_text(label="Userids",uppercase=True, callback = user)
        dpg.add_text("(Seperated by commas.)")
        dpg.add_text("")
        dpg.add_separator()
        dpg.add_text("Enter the desired server name after nuke.")
        dpg.add_input_text(label="Server Name",uppercase=True, callback = servername)
        dpg.add_text("")
        dpg.add_separator()
        dpg.add_button(label="Save all Nuke Settings", callback=save)
        dpg.add_button(label="Start bot", callback=run)
     with dpg.tab(label="   Bot   "):
       with dpg.group(horizontal=True):
            dpg.add_text("Enter the Bot Token of your NUKE bot.")
            dpg.add_text("? ", tag="tokentooltip")

            with dpg.tooltip("tokentooltip"):
               dpg.add_text("Enter the bot-token of your nuke bot here.")
       with dpg.group(horizontal=True):
        dpg.add_input_text(callback = bottoken)
        dpg.add_button(label="setup token", callback=savetoken)
     with dpg.tab(label=" Command "):
        type_list = ["members", "channels", "roles", "all"]
        dpg.add_text("NUKE COMMAND HELPER")
        dpg.add_separator()
        dpg.add_combo(label="Nuke type", items=type_list, callback=nuketype)
        dpg.add_separator()
        dpg.add_text("")
        dpg.add_slider_float(label="Channel #", min_value=1,max_value=500, callback=channelnum)
        dpg.add_separator()
        dpg.add_text("")
        dpg.add_input_text(label="Channel-name", callback=channelname)
        dpg.add_separator()
        dpg.add_text("")
        dpg.add_input_text(label="Message", callback=message)
        dpg.add_separator()
        dpg.add_text("")
        dpg.add_button(label="Copy to clipboard", callback=copy)
        


       

       


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()