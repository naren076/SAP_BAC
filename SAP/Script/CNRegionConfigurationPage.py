import WaterManagementConfiguration

def set_configuration_details(textbox, page, general_requirement_values):
  page.WaitConfirm(3000)
  frame = textbox.frameC120
  section = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  section2 = section.sectionSplitter0Content1
  section2.FindElement("//div//span[contains(@class, 'sapMSltLabel')]").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='CN']").Click()
  page.WaitConfirm(3000)
  #section2.textnodeShowValueHelp.Click()
  model_number_field = section2.FindElement("//input[@id=(//label[.='Model Number:']/@for)]")
  model_number_field.SetText(general_requirement_values["model_number"])
  page.WaitConfirm(3000)
  model_number_field.Keys("[Enter]")
  page.WaitConfirm(2000)
  section2.panelConfigurationcomponentValua.Click()
  page.WaitConfirm(6000)
  #---Select Unit of Measure
  section2.FindElement("//div[4]//span[contains(@class, 'sapMSltLabel')]").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["unit_of_measure"]+"']").Click()
  page.WaitConfirm(2000)
 
 #---Select Unit Flow UOM:
  section2.FindElement("//*[contains(text(),'Unit Flow UOM')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["unit_flow_uom"]+"']").Click()
  page.WaitConfirm(1000)
  
  unit = "°F" if general_requirement_values["unit_of_measure"] == "Imperial" else "°C"
  unit_level = "°F" if general_requirement_values["unit_of_measure"] == "Imperial" else "C"
  flow_meter = "GPM" if general_requirement_values["unit_of_measure"] == "Imperial" else "l/s"
  temp = "Temp" if general_requirement_values["unit_of_measure"] == "Imperial" else "Temperature"
  
  #textbox = section2.FindElement("//input[@id=(//label[.='Water Flow Rate per Unit ("+flow_meter+"):']/@for)]")
  textbox = section2.FindElement("//input[@id=(//label[.='Unit flow:']/@for)]")
  textbox.Keys(general_requirement_values["unit_flow"])
  textbox = section2.FindElement("//input[@id=(//label[.='Entering Water "+temp+" ("+unit_level+"):']/@for)]")
  textbox.Click()
  
  textbox.Keys(general_requirement_values["entering_water_temperature"])
  textbox = section2.FindElement("//input[@id=(//label[.='Leaving Water Temperature ("+unit+"):']/@for)]")
  textbox.Click()
  textbox.Keys(general_requirement_values["leaving_water_temperature"])
  textbox = section2.FindElement("//input[@id=(//label[.='Entering Wet-Bulb Temp ("+unit_level+"):']/@for)]")
  textbox.Click()
  textbox.Keys(general_requirement_values["entering_wet_bulb_temp"])
  page.WaitConfirm(3000)
  #--fill material--
  section2.FindElement("//*[contains(text(),'Fill Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(2000)
  frame.FindElement("//li[.='"+general_requirement_values["fill_material"]+"']").Click()
  page.WaitConfirm(1000)
  
   #--Special Seismic Cert Required--
  section2.FindElement("//*[contains(text(),'Special Seismic Cert Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["special_seismic"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--FM approval--
  section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["fm_approval"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--Cooling Tower Structure
  section2.FindElement("//*[contains(text(),'Cooling Tower Structure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["cooling_tower_structure"]+"']").Click()
  page.WaitConfirm(1000) 
  
  #--Basinless 
  section2.FindElement("//*[contains(text(),'Basinless Unit')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["basinless_unit"]+"']").Click()
  page.WaitConfirm(3000)
  
  #--Anchorage
  isEnabled = section2.FindElement("//*[contains(text(),'Anchorage')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']//preceding-sibling::input[@class='sapUiPseudoInvisibleText sapMSltHiddenSelect']").getAttribute("aria-readonly")
  if isEnabled == "false":
    section2.FindElement("//*[contains(text(),'Anchorage')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+general_requirement_values["anchorage"]+"']").Click()
    page.WaitConfirm(1000)
  
  #--Shipping/Production Plan
  section2.FindElement("//*[contains(text(),'Shipping/Production Plant')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["shipping_plant"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--Knockdown For Field Assembly?
  section2.FindElement("//*[contains(text(),'Knockdown For Field Assembly')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  section2.FindElement("//*[contains(text(),'Knockdown For Field Assembly')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["field_assembly"])
  section2.FindElement("//*[contains(text(),'Knockdown For Field Assembly')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)