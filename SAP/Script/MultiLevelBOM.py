def multi_level_bom(sales_order_panel,sales_document_textbox,page,sap_values):
    sales_order_panel.FindElement("//span/span/span[contains(text(), 'Multi-')]").Click()
    #---Item:
    item_field = sales_document_textbox.FindElement("//input[@id=(//label[.='Item']/@for)]")
    item_field.SetText("100")
    
    #---Material:
    material_field = sales_document_textbox.FindElement("//input[@id=(//label[.='Material']/@for)]")
    material_field.SetText(sap_values["Material (BAC Model)"])
    
    #---BOM Application:
    bom_application = sales_document_textbox.FindElement("//input[@id=(//label[.='BOM Application']/@for)]")
    bom_application.SetText("PP01")
    
    sales_document_textbox.FindElement("//div[.='Execute']").Click()
    multi_level_bom_frame = sales_order_panel.frameApplicationBillofmaterialMu
    multi_level_bom_form = multi_level_bom_frame.formWebguiform0
    if(NameMapping.Sys.browser.pageFlp.frameApplicationBillofmaterialMu.WaitNamedChild("panelSpreadsheetCtrlShiftF7", 10000).Exists):
     multi_level_bom_form.FindElement("//div[@title='Spreadsheet... (Ctrl+Shift+F7)']").Click()
    if(NameMapping.Sys.browser.pageFlp.frameApplicationBillofmaterialMu.WaitNamedChild("panelUpdowndialogchoose", 10000).Exists):
      multi_level_bom_frame.FindElement("//div[.='OK']").Click()