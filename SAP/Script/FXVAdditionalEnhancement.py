﻿def additional_configs(additional_config_page, additional_frame, additional_page, additional_config_values):
  #---Coil Air Intake Option:
  additional_page.FindElement("//*[contains(text(),'Coil Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["coil_air_intake_option"] != 'None':
    additional_frame.FindElement("//li[.='"+additional_config_values["coil_air_intake_option"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Coil Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["coil_air_intake_option"])
    additional_page.FindElement("//*[contains(text(),'Coil Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(2000)
  
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
    
  #---Insulation:
  additional_page.FindElement("//*[contains(text(),'Insulation')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["insulation"] != 'None':
    additional_frame.FindElement("//li[.='"+additional_config_values["insulation"]+"']").Click()
  else:
    additional_page.FindElement("//*[contains(text(),'Insulation')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["insulation"])
    additional_page.FindElement("//*[contains(text(),'Insulation')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(2000)
       
  #---Upgrade Fan Guard Material:
  additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  additional_config_page.WaitConfirm(1000)
  if additional_config_values["upgrade_fan_guard_material"] != "No":
    additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(additional_config_values["upgrade_fan_guard_material"])
    additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  additional_config_page.WaitConfirm(1000)
  
  #---FM Fan Shrouds For Zone HM:
  if additional_config_values["fm_fan_shrouds_for_zone_hm"] != "SAP Defined":
      additional_page.FindElement("//*[contains(text(),'FM Fan Shrouds For Zone HM')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
      additional_frame.FindElement("//li[.='"+additional_config_values["fm_fan_shrouds_for_zone_hm"]+"']").Click()
      additional_config_page.WaitConfirm(1000)
      
  #---Air Intake Scr And Inlet Wings:
  if additional_config_values["air_intake_scr_and_inlet_wings"] != "SAP Defined":
      additional_page.FindElement("//*[contains(text(),'Air Intake Scr And Inlet Wings')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
      additional_frame.FindElement("//li[.='"+additional_config_values["air_intake_scr_and_inlet_wings"]+"']").Click()
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
  
  #---additional Enhancement Page:
  if(additional_frame.FindElement("//div[@class='sapMITHEndOverflow']//child::span[contains(text(), 'More')]")).VisibleOnScreen:
    additional_frame.FindElement("//div[@class='sapMITHEndOverflow']//child::span[contains(text(), 'More')]").Click() 
    additional_frame.FindElement("//div[@class='sapMPopoverScroll']//child::span[.='Shipping and Specials']").Click()