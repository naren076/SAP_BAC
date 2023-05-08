#import WaterManagementConfiguration

def set_configuration_details(textbox, page, general_requirement_values):
  frame = textbox.frameC120
  section = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  section2 = section.sectionSplitter0Content1
  if(NameMapping.Sys.browser.pageFlp.frameApplicationSalesdocumentCre.frameC102.WaitNamedChild("textnodeNone", 15000).Exists):
    section2.FindElement("//div//span[contains(@class, 'sapMSltLabel')]").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["region_specific"]+"']").Click()
  page.WaitConfirm(3000)
  model_number_field = section2.FindElement("//input[@id=(//label[.='Model Number:']/@for)]")
  model_number_field.SetText(general_requirement_values["model_number"])
  model_number_field.Keys("[Enter]")
  page.WaitConfirm(4000)
  section2.panelConfigurationcomponentValua.Click()
  page.WaitConfirm(4000)
  section2.FindElement("//*[contains(text(),'Unit of Measure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(3000)
  frame.FindElement("//li[.='"+general_requirement_values["unit_of_measure"]+"']").Click()
  page.WaitConfirm(2000)
  
  #----Number of Circuits required
  section2.FindElement("//*[contains(text(),'Number of Circuits Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  #frame.FindElement("//li[.='"+general_requirement_values["number_of_circuits_required"]+"']").Click()
  section2.FindElement("//*[contains(text(),'Number of Circuits Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["number_of_circuits_required"])
  section2.FindElement("//*[contains(text(),'Number of Circuits Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  
  page.WaitConfirm(1000)
  
  #----Select Fluid
  section2.FindElement("//*[contains(text(),'Fluid')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["fluid"]+"']").Click()
  page.WaitConfirm(1000)
  
 #---Select Unit Flow UOM:
  section2.FindElement("//*[contains(text(),'Unit Flow UOM')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["unit_flow_uom"]+"']").Click()
  page.WaitConfirm(1000)
  
  textbox = section2.FindElement("//input[@id=(//label[.='Unit flow:']/@for)]")
  textbox.Keys(general_requirement_values["unit_flow"])
  
  textbox = section2.FindElement("//input[@id=(//label[contains(@title,'Entering Fluid Temp')]/@for)]")
  textbox.Click()
  textbox.Keys(general_requirement_values["entering_water_temperature"])
  
  textbox = section2.FindElement("//input[@id=(//label[contains(@title,'Leaving Fluid Temp')]/@for)]")
  textbox.Click()
  textbox.Keys(general_requirement_values["leaving_water_temperature"])
  
  textbox = section2.FindElement("//input[@id=(//label[contains(@title,'Entering Wet-Bulb Temp')]/@for)]")
  textbox.Click()
  textbox.Keys(general_requirement_values["entering_wet_bulb_temp"])
  
  textbox = section2.FindElement("//input[@id=(//label[contains(@title,'Coil Pressure Drop')]/@for)]")
  textbox.Click()
  textbox.Keys(general_requirement_values["coil_pressure_drop"])
  page.WaitConfirm(3000)
  #--fill material--
  section2.FindElement("//*[contains(text(),'Fill Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(2000)
  frame.FindElement("//li[.='"+general_requirement_values["fill_material"]+"']").Click()
  page.WaitConfirm(1000)
  
  #CTI Certification
  if general_requirement_values["cti_certification"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'CTI Certification')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["cti_certification"]+"']").Click()
    page.WaitConfirm(1000)
  
  #California OSHPD Project
  section2.FindElement("//*[contains(text(),'California OSHPD Project?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  section2.FindElement("//*[contains(text(),'California OSHPD Project?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["california_oshpd_proj"])
  section2.FindElement("//*[contains(text(),'California OSHPD Project?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
   #--Special Seismic Cert Required--
  section2.FindElement("//*[contains(text(),'Special Seismic Cert Required')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["special_seismic"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--FM approval--
  section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(general_requirement_values["fm_approval"])
  section2.FindElement("//*[contains(text(),'FM Approval')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  #frame.FindElement("//li[.='"+general_requirement_values["fm_approval"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--Cooling Tower Structure
  section2.FindElement("//*[contains(text(),'Cooling Tower Structure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+general_requirement_values["cooling_tower_structure"]+"']").Click()
  page.WaitConfirm(1000) 
  
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
  
  #Base Seismic Rating
  if general_requirement_values["base_seismic_rating"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Base Seismic Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["base_seismic_rating"]+"']").Click()
    page.WaitConfirm(1000)

  #Design Accel z=1 1.0 Rigid
  if general_requirement_values["design_accel_rigid"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Design Accel z=1 1.0 Rigid')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["base_seismic_rating"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Design Accel z=1 1.0 Isolated
  if general_requirement_values["design_accel_isolated"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Design Accel z=1 1.0 Isolated')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["design_accel_isolated"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Design Accel z=0 1.0 Rigid
  if general_requirement_values["design_accel_0_rigid"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Design Accel z=0 1.0 Rigid')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["design_accel_0_rigid"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Base Wind Rating
  if general_requirement_values["base_wind_rating"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Base Wind Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["base_wind_rating"]+"']").Click()
    page.WaitConfirm(1000)
    
  #Horizontal Wind Rating
  if general_requirement_values["horizontal_wind_rating"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Horizontal Wind Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["horizontal_wind_rating"]+"']").Click()
    page.WaitConfirm(1000)
    
  #Vertical Wind Rating
  if general_requirement_values["vertical_wind_rating"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Vertical Wind Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["vertical_wind_rating"]+"']").Click()
    page.WaitConfirm(1000)  
    
  #FM Wind Load Rating
  if general_requirement_values["fm_wind_load_rating"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'FM Wind Load Rating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+general_requirement_values["fm_wind_load_rating"]+"']").Click()
    page.WaitConfirm(1000) 