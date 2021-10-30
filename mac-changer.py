import subprocess
import optparse

def user_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC")
    (options, arguments) = parser.parse_args()
    #gg

def mac_change(interface, new_mac):
    print("- Changing MAC " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# take arguments option and new MAC address
options = user_arg() 
#invoking mac changer and passing above two arguments into the function
mac_change(options.interface, arguments.new_mac)
