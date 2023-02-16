def create_standard_order(browser, textbox, page, field_values):
  textbox2 = textbox.FindElement("//input[@title='Sold-to Party']")
  textbox2.SetText(field_values["sold_to_party"])
  textbox2 = textbox.FindElement("//input[@title='Customer Reference']")
  textbox2.SetText(field_values["customer_reference"])
  #frame = browser.pageFlp.sectionShellSplitCanvas.frameApplicationSalesdocumentCre
  #check_textbox = frame.formWebguiform0
  #panel = page.sectionShellSplitCanvas
  #test_frame = panel.frameApplicationSalesdocumentCre.formWebguiform0
  
  textbox2 = textbox.FindElement("//input[@id=(//label[.='Delivery Block']/@for)]")
  textbox2.Click()
  mrpoption = textbox.FindElement("//div[.='"+field_values["delivery_block"]+"']")  
  mrpoption.Click()
  textbox2.Keys("[Enter]")
  textbox.FindElement("//span/input[@name='InputField']").SetText(field_values["material"])
  textbox.Keys("[Tab]")
  textbox2 = textbox.FindElement("//td[2]//tr/td//input")
  textbox2.Click()
  textbox2.SetText(field_values["order_quantity"])
  textbox2.Keys("[Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab]")
  #textbox2.Keys("[Tab]")
  #textbox.textnodeInputfield2.Click()
  plnt_field = textbox.FindElement("//tr/td[11]/div")
  plnt_field.Click()
  plnt_field.Keys(field_values["plant"])
  plnt_field.Keys("[Enter]")