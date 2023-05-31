import ShippingConfigurationPage

def additional_configs(additional_config_page, additional_frame, additional_page, additional_config_values):
  #---Side Air Intake Option:
  additional_page.FindElement("//*[contains(text(),'Side Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["side_air_taken_option"] != 'None':
    additional_frame.FindElement("//li[.='"+additional_config_values["side_air_taken_option"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Side Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["side_air_taken_option"])
    additional_page.FindElement("//*[contains(text(),'Side Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(2000)
  
  #---Air Discharge Configuration:
  additional_page.FindElement("//*[contains(text(),'Air Discharge Configuration')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["air_discharge_configuration"] != 'None':
    if aqString.GetListLength(additional_config_values["x_path"]) > 1:
      additional_frame.FindElement(additional_config_values["x_path"]).Click()
      additional_config_page.WaitConfirm(1000)
    else:
      additional_frame.FindElement("//li[.='"+additional_config_values["air_discharge_configuration"]+"']").Click()
      additional_config_page.WaitConfirm(1000)
  else:
    additional_page.FindElement("//*[contains(text(),'Air Discharge Configuration')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["air_discharge_configuration"])
    additional_config_page.WaitConfirm(1000)
    additional_page.FindElement("//*[contains(text(),'Air Discharge Configuration')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(2000)
  
  #---Upgrade Fan Guard Material:
  additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["upgrade_fan_guard_material"] != "No":
    additional_frame.FindElement("//li[.='"+additional_config_values["upgrade_fan_guard_material"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["upgrade_fan_guard_material"])
    additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---Fan Deck Safety Rails:
  additional_page.FindElement("//*[contains(text(),'Fan Deck Safety Rails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["fan_deck_safety_rails"] != "None":
    additional_frame.FindElement("//li[.='"+additional_config_values["fan_deck_safety_rails"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Fan Deck Safety Rails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["fan_deck_safety_rails"])
    additional_page.FindElement("//*[contains(text(),'Fan Deck Safety Rails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(2000)
  
  #---3Side SafetyRail to Exist Cell:
  additional_page.FindElement("//*[contains(text(),'3Side SafetyRail to Exist Cell')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(2000)
  if additional_config_values["3Side_safetyRail_to_exist_cell"] != "No":
    additional_frame.FindElement("//li[.='"+additional_config_values["3Side_safetyRail_to_exist_cell"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'3Side SafetyRail to Exist Cell')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["3Side_safetyRail_to_exist_cell"])
    additional_page.FindElement("//*[contains(text(),'3Side SafetyRail to Exist Cell')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---Ladder to Fan Deck:
  if additional_config_values["ladder_fan_deck"] != "SAP Defined":
    additional_page.FindElement("//*[contains(text(),'Ladder to Fan Deck')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    if additional_config_values["ladder_fan_deck"] != "None":
     additional_frame.FindElement("//li[.='"+additional_config_values["ladder_fan_deck"]+"']").Click()
    else:
      additional_page.FindElement("//*[contains(text(),'Ladder to Fan Deck')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["ladder_fan_deck"])
      additional_page.FindElement("//*[contains(text(),'Ladder to Fan Deck')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(2000)
  
  #---Add Safety Cages to Ladders:
  if additional_config_values["add_safety_cages_to_ladders"] != "SAP Defined":
    additional_page.FindElement("//*[contains(text(),'Add Safety Cages to Ladders')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    additional_page.FindElement("//*[contains(text(),'Add Safety Cages to Ladders')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["add_safety_cages_to_ladders"]) 
    additional_page.FindElement("//*[contains(text(),'Add Safety Cages to Ladders')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(1000)
  
  #---Safety Gates to All Ladder:
  if additional_config_values["safety_gates_to_all_ladder"] != "SAP Defined":
    additional_page.FindElement("//*[contains(text(),'Safety Gates to All Ladder?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    additional_page.FindElement("//*[contains(text(),'Safety Gates to All Ladder?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["safety_gates_to_all_ladder"]) 
    additional_page.FindElement("//*[contains(text(),'Safety Gates to All Ladder?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(1000)
  
  #---Ladder/Safety Cage Extensions:
  if additional_config_values["ladder_safety_cage_extensions"] != "SAP Defined":
    additional_page.FindElement("//*[contains(text(),'Ladder/Safety Cage Extensions')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    if additional_config_values["ladder_safety_cage_extensions"] != "None":
      additional_frame.FindElement("//li[.=\""+additional_config_values["ladder_safety_cage_extensions"]+"\"]").Click()
    else:
      additional_page.FindElement("//*[contains(text(),'Ladder/Safety Cage Extensions')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["ladder_safety_cage_extensions"])
      additional_page.FindElement("//*[contains(text(),'Ladder/Safety Cage Extensions')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(1000)
  
  #---MOC - Platform Supports:
  additional_page.FindElement("//*[contains(text(),'MOC - Platform Supports')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_config_values["moc_platform_supports"]+"']").Click()
  additional_config_page.WaitConfirm(1000)
  
  #---Fan Deck Ext with Handrails:
  if additional_config_values["fan_deck_ext_with_handrils"] != "SAP Defined":
    additional_page.FindElement("//*[contains(text(),'Fan Deck Ext with Handrails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    if additional_config_values["fan_deck_ext_with_handrils"] != "None":
      additional_frame.FindElement("//li[.='"+additional_config_values["fan_deck_ext_with_handrils"]+"']").Click()
    else:
      additional_page.FindElement("//*[contains(text(),'Fan Deck Ext with Handrails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["fan_deck_ext_with_handrils"])
      additional_page.FindElement("//*[contains(text(),'Fan Deck Ext with Handrails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(1000)
  
  #---Louver Face Platform:
  additional_page.FindElement("//*[contains(text(),'Louver Face Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["louver_face_platform"] != "None":
    additional_frame.FindElement("//li[.='"+additional_config_values["louver_face_platform"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Louver Face Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["louver_face_platform"])
    additional_page.FindElement("//*[contains(text(),'Louver Face Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---Access Door Platform:
  additional_page.FindElement("//*[contains(text(),'Access Door Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["access_door_platform"] != "None":
    additional_frame.FindElement("//li[.='"+additional_config_values["access_door_platform"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Access Door Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["access_door_platform"])
    additional_page.FindElement("//*[contains(text(),'Access Door Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---Louver Face Ldr/Cage Extension:
  additional_page.FindElement("//*[contains(text(),'Louver Face Ldr/Cage Extension')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["louver_face_cage_extension"] != "None":
    additional_frame.FindElement("//li[.=\""+additional_config_values["louver_face_cage_extension"]+"\"]").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Louver Face Ldr/Cage Extension')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["louver_face_cage_extension"])
    additional_page.FindElement("//*[contains(text(),'Louver Face Ldr/Cage Extension')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---Access Door Pltf Ladder Ext:
  if additional_config_values["access_door_pltf"] != "SAP Defined":
    additional_page.FindElement("//*[contains(text(),'Access Door Pltf Ladder Ext')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    if additional_config_values["access_door_pltf"] != 'None':
      additional_frame.FindElement("//li[.=\""+additional_config_values["access_door_pltf"]+"\"]").Click()
    else:
      additional_page.FindElement("//*[contains(text(),'Access Door Pltf Ladder Ext')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["access_door_pltf"])
      additional_page.FindElement("//*[contains(text(),'Access Door Pltf Ladder Ext')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    additional_config_page.WaitConfirm(1000)
  
  #---Internal Walkway @ Access Door:
  additional_page.FindElement("//*[contains(text(),'Internal Walkway @ Access Door')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  additional_frame.FindElement("//bdi[text()='Internal Walkway @ Access Door:']//preceding::div[@class='sapUiSimpleFixFlexFlexContent'][1]//li[text()='"+additional_config_values["internal_walkway_access_door"]+"']").Click()
  additional_page.FindElement("//*[contains(text(),'Internal Walkway @ Access Door')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["internal_walkway_access_door"]) 
  additional_page.FindElement("//*[contains(text(),'Internal Walkway @ Access Door')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---Internal Walkway MOC:
  isEnabled = additional_page.FindElement("//*[contains(text(),'Internal Walkway MOC')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']//preceding-sibling::input[@class='sapUiPseudoInvisibleText sapMSltHiddenSelect']").getAttribute("aria-readonly")
  if isEnabled == "false":
    additional_page.FindElement("//*[contains(text(),'Internal Walkway MOC')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    additional_config_page.WaitConfirm(1000)
    additional_frame.FindElement("//li[.='"+additional_config_values["internal_walkway_moc"]+"']").Click()
    additional_config_page.WaitConfirm(1000)
    
  #---Internal Access:
  additional_page.FindElement("//*[contains(text(),'Internal Access:')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["internal_access"] != "None":
    additional_frame.FindElement("//li[.='"+additional_config_values["internal_access"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Internal Access:')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["internal_access"])
    additional_page.FindElement("//*[contains(text(),'Internal Access:')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---go to Shipping and Specials:
  additional_page.FindElement("//span[.='Shipping and Specials']").Click()