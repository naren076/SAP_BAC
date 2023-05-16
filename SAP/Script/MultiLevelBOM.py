def multi_level_bom(panel,textbox,page,sap_values):
    panel.FindElement("//span/span/span[contains(text(), 'Multi-')]").Click()
    item_field = textbox.FindElement("//input[@id=(//label[.='Item']/@for)]")
    item_field.SetText("100")
    material_field = textbox.FindElement("//input[@id=(//label[.='Material']/@for)]")
    material_field.SetText(sap_values["Material (BAC Model)"])
    textbox2 = textbox.FindElement("//input[@id=(//label[.='BOM Application']/@for)]")
    textbox2.SetText("PP01")
    textbox.FindElement("//div[.='Execute']").Click()
    frame = panel.frameApplicationBillofmaterialMu
    form = frame.formWebguiform0
    if(NameMapping.Sys.browser.pageFlp.frameApplicationBillofmaterialMu.WaitNamedChild("panelSpreadsheetCtrlShiftF7", 10000).Exists):
     form.FindElement("//div[@title='Spreadsheet... (Ctrl+Shift+F7)']").Click()
    if(NameMapping.Sys.browser.pageFlp.frameApplicationBillofmaterialMu.WaitNamedChild("panelUpdowndialogchoose", 10000).Exists):
      frame.FindElement("//div[.='OK']").Click()
    