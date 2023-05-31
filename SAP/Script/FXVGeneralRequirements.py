def set_configuration_details(sales_document_textbox, general_requirement_page, general_requirement_values):
  variant_config_frame = sales_document_textbox.frameC120
  variant_config_section = variant_config_frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  variant_config_section2 = variant_config_section.sectionSplitter0Content1
  if(NameMapping.Sys.browser.pageFlp.frameApplicationSalesdocumentCre.frameC102.WaitNamedChild("textnodeNone", 15000).Exists):
    variant_config_section2.FindElement("//div//span[contains(@class, 'sapMSltLabel')]").Click()
  general_requirement_page.WaitConfirm(1000)
  #---Region Specific:
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["region_specific"]+"']").Click()
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
  
  #---Number of Circuits required:
  variant_config_section2.FindElement("//*[contains(text(),'Number of Circuits Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["number_of_circuits_required"]+"']").Click()  
  general_requirement_page.WaitConfirm(1000)
  
  #---Select Fluid:
  variant_config_section2.FindElement("//*[contains(text(),'Fluid')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["fluid"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---Select Unit Flow UOM:
  variant_config_section2.FindElement("//*[contains(text(),'Unit Flow UOM')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["unit_flow_uom"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---Unit flow:
  unit_flow_field = variant_config_section2.FindElement("//input[@id=(//label[.='Unit flow:']/@for)]")
  unit_flow_field.Keys(general_requirement_values["unit_flow"])
  
  #---Entering Water Temperature:
  entering_water_temperature_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Entering Fluid Temp')]/@for)]")
  entering_water_temperature_field.Click()
  entering_water_temperature_field.Keys(general_requirement_values["entering_fluid_temperature"])
  
  #---Leaving Water Temperature:
  leaving_water_temperature_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Leaving Fluid Temp')]/@for)]")
  leaving_water_temperature_field.Click()
  leaving_water_temperature_field.Keys(general_requirement_values["leaving_fluid_temperature"])
  
  #---Entering Wet-Bulb Temp:
  entering_wet_bulb_temp_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Entering Wet-Bulb Temp')]/@for)]")
  entering_wet_bulb_temp_field.Click()
  entering_wet_bulb_temp_field.Keys(general_requirement_values["entering_wet_bulb_temp"])
  
  #---Coil Pressure Drop:
  coil_pressure_drop_field = variant_config_section2.FindElement("//input[@id=(//label[contains(@title,'Coil Pressure Drop')]/@for)]")
  coil_pressure_drop_field.Click()
  coil_pressure_drop_field.Keys(general_requirement_values["coil_pressure_drop"])
  general_requirement_page.WaitConfirm(3000)
  
  #---Fill Material:
  variant_config_section2.FindElement("//*[contains(text(),'Fill Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(2000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["fill_material"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---CTI Certification:
  if general_requirement_values["cti_certification"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'CTI Certification')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["cti_certification"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
  
  #---California OSHPD Project:
  variant_config_section2.FindElement("//*[contains(text(),'California OSHPD Project?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  general_requirement_page.WaitConfirm(1000)
  variant_config_section2.FindElement("//*[contains(text(),'California OSHPD Project?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["california_oshpd_proj"])
  variant_config_section2.FindElement("//*[contains(text(),'California OSHPD Project?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  general_requirement_page.WaitConfirm(2000)
  
  #---Special Seismic Cert Required:
  variant_config_section2.FindElement("//*[contains(text(),'Special Seismic Cert Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+general_requirement_values["special_seismic"]+"']").Click()
  general_requirement_page.WaitConfirm(1000)
  
  #---FM approval:
  variant_config_section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  general_requirement_page.WaitConfirm(1000)
  variant_config_section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["fm_approval"])
  variant_config_section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  general_requirement_page.WaitConfirm(4000)
  
  #---Cooling Tower Structure:
  isEnabled = variant_config_section2.FindElement("//*[contains(text(),'Cooling Tower Structure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']//preceding-sibling::input[@class='sapUiPseudoInvisibleText sapMSltHiddenSelect']").getAttribute("aria-readonly")
  if isEnabled == "false":
    variant_config_section2.FindElement("//*[contains(text(),'Cooling Tower Structure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["cooling_tower_structure"]+"']").Click()
    general_requirement_page.WaitConfirm(1000) 
  
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
  
  #---Base Seismic Rating:
  if general_requirement_values["base_seismic_rating"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Base Seismic Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["base_seismic_rating"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)

  #---Design Accel z=1 1.0 Rigid:
  if general_requirement_values["design_accel_rigid"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Design Accel z=1 1.0 Rigid')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["base_seismic_rating"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
  
  #---Design Accel z=1 1.0 Isolated:
  if general_requirement_values["design_accel_isolated"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Design Accel z=1 1.0 Isolated')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["design_accel_isolated"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
  
  #---Design Accel z=0 1.0 Rigid:
  if general_requirement_values["design_accel_0_rigid"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Design Accel z=0 1.0 Rigid')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["design_accel_0_rigid"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
  
  #---Base Wind Rating:
  if general_requirement_values["base_wind_rating"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Base Wind Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["base_wind_rating"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
    
  #---Horizontal Wind Rating:
  if general_requirement_values["horizontal_wind_rating"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Horizontal Wind Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["horizontal_wind_rating"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)
    
  #---Vertical Wind Rating:
  if general_requirement_values["vertical_wind_rating"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'Vertical Wind Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["vertical_wind_rating"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)  
    
  #---FM Wind Load Rating:
  if general_requirement_values["fm_wind_load_rating"] != "SAP Defined":
    variant_config_section2.FindElement("//*[contains(text(),'FM Wind Load Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    general_requirement_page.WaitConfirm(2000)
    variant_config_frame.FindElement("//li[.='"+general_requirement_values["fm_wind_load_rating"]+"']").Click()
    general_requirement_page.WaitConfirm(1000)