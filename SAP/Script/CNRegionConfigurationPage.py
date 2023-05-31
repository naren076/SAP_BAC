import WaterManagementConfiguration

def set_configuration_details(sales_document_textbox, general_requirement_page, general_requirement_values):
  variant_config_frame = sales_document_textbox.frameC120
  variant_config_section = variant_config_frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  variant_config_section2 = variant_config_section.sectionSplitter0Content1
  if(NameMapping.Sys.browser.pageFlp.frameApplicationSalesdocumentCre.frameC102.WaitNamedChild("textnodeNone", 15000).Exists):
    variant_config_section2.FindElement("//div//span[contains(@class, 'sapMSltLabel')]").Click()
  general_requirement_page.WaitConfirm(1000)
  #---Region Specific:
  variant_config_frame.FindElement("//li[.='CN']").Click()
  general_requirement_page.WaitConfirm(3000)
  
  #---Model Number:
  model_number_field = variant_config_section2.FindElement("//input[@id=(//label[.='Model Number:']/@for)]")
  model_number_field.SetText(general_requirement_values["model_number"])
  model_number_field.Keys("[Enter]")
  general_requirement_page.WaitConfirm(4000)
  variant_config_section2.panelConfigurationcomponentValua.Click()
  general_requirement_page.WaitConfirm(4000)
  
  #---Unit of Measure:
  variant_config_section2.FindElement("//*[contains(text(),'Unit of Measure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(3000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["unit_of_measure"]+"']").Click()
  general_requirement_page.WaitConfirm(2000)
 
  #---Select Unit Flow UOM:
  variant_config_section2.FindElement("//*[contains(text(),'Unit Flow UOM')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["unit_flow_uom"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---Unit Flow:
  unit_flow_field = variant_config_section2.FindElement("//input[@id=(//label[.='Unit flow:']/@for)]")
  unit_flow_field.Keys(general_requirement_values["unit_flow"])
  
  #---Entering Water Temperature:
  entering_water_temperature_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Entering Water Temp')]/@for)]")
  entering_water_temperature_field.Click()
  entering_water_temperature_field.Keys(general_requirement_values["entering_water_temperature"])
  
  #---Leaving Water Temperature:
  leaving_water_temperature_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Leaving Water Temp')]/@for)]")
  leaving_water_temperature_field.Click()
  leaving_water_temperature_field.Keys(general_requirement_values["leaving_water_temperature"])
  
  #---Entering Wet-Bulb Temp:
  entering_wet_bulb_temp_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Entering Wet-Bulb Temp')]/@for)]")
  entering_wet_bulb_temp_field.Click()
  entering_wet_bulb_temp_field.Keys(general_requirement_values["entering_wet_bulb_temp"])
  general_requirement_page.WaitConfirm(3000)

  #---fill material:
  variant_config_section2.FindElement("//*[contains(text(),'Fill Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(2000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["fill_material"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---Special Seismic Cert Required:
  variant_config_section2.FindElement("//*[contains(text(),'Special Seismic Cert Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["special_seismic"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---FM approval:
  variant_config_section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["fm_approval"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---Cooling Tower Structure:
  variant_config_section2.FindElement("//*[contains(text(),'Cooling Tower Structure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["cooling_tower_structure"]+"']").Click()
  general_requirement_page.WaitConfirm(1000) 
  
  #---Basinless: 
  variant_config_section2.FindElement("//*[contains(text(),'Basinless Unit')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["basinless_unit"]+"']").Click()
  general_requirement_page.WaitConfirm(3000)
  
  #---Anchorage:
  isEnabled = variant_config_section2.FindElement("//*[contains(text(),'Anchorage')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']//preceding-sibling::input[@class='sapUiPseudoInvisibleText sapMSltHiddenSelect']").getAttribute("aria-readonly")
  if isEnabled == "false":
    variant_config_section2.FindElement("//*[contains(text(),'Anchorage')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["anchorage"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
  
  #---Shipping/Production Plan:
  variant_config_section2.FindElement("//*[contains(text(),'Shipping/Production Plant')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["shipping_plant"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---Knockdown For Field Assembly:
  variant_config_section2.FindElement("//*[contains(text(),'Knockdown For Field Assembly')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  general_requirement_page.WaitConfirm(1000)
  variant_config_section2.FindElement("//*[contains(text(),'Knockdown For Field Assembly')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["field_assembly"])
  variant_config_section2.FindElement("//*[contains(text(),'Knockdown For Field Assembly')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  general_requirement_page.WaitConfirm(1000)