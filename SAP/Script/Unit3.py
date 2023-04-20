def filecompare():
  if not Files.Compare("C:\\Work\\OrdersList_Var1.txt", "C:\\Work\\OrdersList.txt"):
  Log.Warning("List of orders was changed")