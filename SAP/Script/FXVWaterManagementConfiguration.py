def water_management(water_management_page, water_management_values):
  variant_config_frame = water_management_page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  variant_config_textNode = variant_config_frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  variant_config_textNode2 = variant_config_textNode.sectionSplitter0Content1
  variant_config_textNode2.FindElement("//span[.='Water Management']").Click()
  #---Material of Construction:
  material_of_construciton_field = variant_config_frame.FindElement("//*[contains(text(),'Material of Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']")
  material_of_construciton_field.Click()
  water_management_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+water_management_values["material_of_construction"]+"']").Click()
  water_management_page.WaitConfirm(1000)
  
  #---Unit Orientation:
  variant_config_textNode2.FindElement("//*[contains(text(),'Unit Orientation')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+water_management_values["unit_orientation"]+"']").Click()
  water_management_page.WaitConfirm(1000)
  
  #---Spray Water Outlet:
  variant_config_textNode2.FindElement("//*[contains(text(),'Spray Water Outlet')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+water_management_values["spray_water_outlet"]+"']").Click()
  water_management_page.WaitConfirm(1000)
  
  #---Spray Distribution Piping:
  isEnabled = variant_config_textNode2.FindElement("//*[contains(text(),'Spray Distribution Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']//preceding-sibling::input[@class='sapUiPseudoInvisibleText sapMSltHiddenSelect']").getAttribute("aria-readonly")
  if isEnabled == "false":
    variant_config_textNode2.FindElement("//*[contains(text(),'Spray Distribution Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+water_management_values["spray_distribution_piping"]+"']").Click()
    water_management_page.WaitConfirm(1000)
  
  #---Spray Pump Motor Type:
  if water_management_values["spray_pump_motor_type"] != "SAP Defined":
    variant_config_textNode2.FindElement("//*[contains(text(),'Spray Pump Motor Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+water_management_values["spray_pump_motor_type"]+"']").Click()
    water_management_page.WaitConfirm(1000)
  
  #---Pump Motor Efficiency Class:
  if water_management_values["pump_motor_efficiency_class"] != "SAP Defined":
    variant_config_textNode2.FindElement("//*[contains(text(),'Pump Motor Efficiency Class')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+water_management_values["pump_motor_efficiency_class"]+"']").Click()
    water_management_page.WaitConfirm(4000)
  
  #---Basin Water Level Control:
  if water_management_values["basin_water_level_control"] != "SAP Defined":
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    if water_management_values["basin_water_level_control"] != "None":
      variant_config_frame.FindElement("//li[.='"+water_management_values["basin_water_level_control"]+"']").Click()
    else:
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_water_level_control"])
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    water_management_page.WaitConfirm(1000)
  
  #---Basin Heaters:
  if water_management_values["basin_heaters"] != "SAP Defined":
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    water_management_page.WaitConfirm(1000)
    if water_management_values["basin_heaters"] != "None":
      variant_config_frame.FindElement("//li[.='"+water_management_values["basin_heaters"]+"']").Click()
    else:
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_heaters"])
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    water_management_page.WaitConfirm(2000)
    
  #---Heater Element Material:
  if water_management_values["heater_element_material"] != "Not Visible":
    variant_config_textNode2.FindElement("//*[contains(text(),'Heater Element Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+water_management_values["heater_element_material"]+"']").Click()
    water_management_page.WaitConfirm(1000)
    
  #---Basin Heater Controls:
  if water_management_values["basin_heater_controls"] != "Not Visible":
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heater Controls')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+water_management_values["basin_heater_controls"]+"']").Click()
    water_management_page.WaitConfirm(1000)
  
  #---Basin Sweeper Piping:
  variant_config_textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  water_management_page.WaitConfirm(2000)
  if water_management_values["basin_sweeper_piping"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["basin_sweeper_piping"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_sweeper_piping"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---Float Switch:
  variant_config_textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  water_management_page.WaitConfirm(1000)
  if water_management_values["float_switch"] != "None": 
    variant_config_frame.FindElement("//li[.='"+water_management_values["float_switch"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["float_switch"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)