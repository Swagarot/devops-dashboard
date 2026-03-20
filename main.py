import sysinfo
import logcheck
while True: 
 print("- [1] System Info")
 print("- [2] Log Checker")
 print("- [3] Task List")
 print("- [0] Exit")
 choice = int(input("select menu option"))
 match choice:
 
  case 1: 
   sysinfo.show_sysinfo()
  case 2:
   logcheck.check_log()
  case 3:
   intput ("Coming soon")
  case 0:
   input ("press enter to exit")
   break

