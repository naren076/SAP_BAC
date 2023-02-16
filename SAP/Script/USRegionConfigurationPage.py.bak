def set_configuration_details(config_form, page, general_requirement_values, water_management_values):
  page.WaitConfirm(3000)
  frame = config_form.frameC120
  section = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  section2 = section.sectionSplitter0Content1
  section2.FindElement("//div//span[contains(@class, 'sapMSltLabel')]").Click()
  frame.FindElement("//li[.='"+general_requirement_values["region_specific"]+"']").Click()
  page.WaitConfirm(3000)
  section2.textnodeShowValueHelp.Click()
  frame.FindElement("//bdi[.='"+general_requirement_values["model_number"]+"']").Click()
  page.WaitConfirm(5000)
  unit_of_measure = section2.FindElement("//div[4]//span[contains(@class, 'sapMSltLabel')]").Click()
  page.WaitConfirm(2000)
  frame.FindElement("//li[.='"+general_requirement_values["unit_of_measure"]+"']").Click()
  textbox = section2.FindElement("//input[@id=(//label[.='Water Flow Rate per Unit (GPM):']/@for)]")
  textbox.SetText(general_requirement_values["water_flow_rate"])
  textbox = section2.FindElement("//input[@id=(//label[.='Entering Water Temp (°F):']/@for)]")
  textbox.Click()
  textbox.SetText(general_requirement_values["entering_water_temperature"])
  textbox = section2.FindElement("//input[@id=(//label[.='Leaving Water Temperature (°F):']/@for)]")
  textbox.Click()
  textbox.SetText(general_requirement_values["leaving_water_temperature"])
  textbox = section2.FindElement("//input[@id=(//label[.='Entering Wet-Bulb Temp (°F):']/@for)]")
  textbox.Click()
  textbox.SetText(general_requirement_values["entering_wet_bulb_temp"])
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  frame = browser.pageFlp.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  textNode = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu.sectionSplitter0Content1
  #textNode.textnodePvc.Click()
  section2.FindElement("//span[.='PVC']").Click()
  frame.FindElement("//li[.='"+general_requirement_values["fill_material"]+"']").Click()
  
  ibc = section2.FindElement("//div[11]//span[contains(@class, 'sapMSltLabel')]").Click()
  frame.FindElement("//li[.='"+general_requirement_values["ibc"]+"']").Click()
  #frame.sectionShellSplitCanvas2.sectionTileGroups.textnodeList173.textnodeOption.Click()
  water_management(page, water_management_values)
  
def water_management(page, water_management_values):
  frame = page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  textNode = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  textNode2 = textNode.sectionSplitter0Content1
  textNode2.textnodeWaterManagement.Click()
  material_of_construciton = frame.FindElement("//span[.='Galvanized Steel']")
  material_of_construciton.Click()
  frame.FindElement("//li[.='"+water_management_values["material_of_construction"]+"']").Click()
  textNode2.FindElement("//span[text()='FRP Casing Panels & Louvers']").Click()
  frame.FindElement("//li[.='"+water_management_values["casing_lovuver_material"]+"']").Click()
  textNode2.FindElement("//span[text()='Top Inlet - End Outlet - Pump Suction']").Click()
  frame.FindElement("//li[.='"+water_management_values["inlet_outlet_connections"]+"']").Click()
  page.WaitConfirm(2000)
  textNode2.FindElement("//span[.='Mechanical Float Valve']").Click()
  frame.FindElement("//li[.='"+water_management_values["basin_water_level_control"]+"']").Click()
  page.WaitConfirm(2000)
  textNode2.FindElement("//div[9]//span[contains(@class, 'sapMSltLabel')]").Click() 
  frame.FindElement("//li[.='"+water_management_values["basin_heaters"]+"']").Click()
  page.WaitConfirm(2000)
  textNode2.FindElement("//div[15]//span[contains(@class, 'sapMSltLabel')]").Click()
  frame.FindElement("//li[.='"+water_management_values["bottom_equalizer"]+"']").Click()
  page.WaitConfirm(2000)
  textNode.FindElement("//div[21]//span[contains(@class, 'sapMSelectListItemText')]").Click()
  frame.FindElement("//li[.='"+water_management_values["outlet_connection_options"]+"']").Click()
  page.WaitConfirm(2000)
  
  #Done button
  frame.FindElement("//button[.='Done']").Click()
  page.WaitConfirm(6000)
  browser = Aliases.browser
  #browser.BrowserWindow.Maximize()
  frame = browser.pageFlp.sectionShellSplitCanvas.frameApplicationSalesdocumentCre
  frame2 = frame.formWebguiform0
  review_frame = frame2.FindElement("//div[@id='C104-r']/iframe")
  review_frame.FindElement("//button[.='Apply']").Click()
  frame2.FindElement("//div[@id='msgarea']//span[2]/div").Click()
  page.WaitConfirm(10000)
  frame2.FindElement("//div[.='Continue']").Click()
  page.WaitConfirm(3000)
