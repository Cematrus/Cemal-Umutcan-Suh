alt = float(input("Wie alt sind sie?"))
if 50 > alt > 20 :
  abschlussnote("Geben Sie deine Abschlussnote")
  if abschlussnote >= 80 :
    print("Einstellen")
  if abschlussnote < 80 :
    print("Ablehnen")
if alt > 50 or alt < 20 :
  print("Ablehnen weil Alt")
