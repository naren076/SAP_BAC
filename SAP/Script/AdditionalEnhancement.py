import ShippingConfigurationPage

def additional_configs(page, additional_frame, additional_page, additional_configs):
  
  #Side Air Intake Option
  additional_page.FindElement("//*[contains(text(),'Side Air Intake Option')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["side_air_taken_option"]+"']").Click()
  page.WaitConfirm(2000)
  
  #Air Discharge Configuration
  additional_page.FindElement("//*[contains(text(),'Air Discharge Configuration')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["air_discharge_configuration"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Upgrade Fan Guard Material?:
  additional_page.FindElement("//*[contains(text(),'Upgrade Fan Guard Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["upgrade_fan_guard_material"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Fan Deck Safety Rails:
  additional_page.FindElement("//*[contains(text(),'Fan Deck Safety Rails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["fan_deck_safety_rails"]+"']").Click()
  page.WaitConfirm(2000)
  
  #3Side SafetyRail to Exist Cell:
  additional_page.FindElement("//*[contains(text(),'3Side SafetyRail to Exist Cell')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(2000)
  additional_frame.FindElement("//li[.='"+additional_configs["3Side_safetyRail_to_exist_cell"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Ladder to Fan Deck:
  additional_page.FindElement("//*[contains(text(),'Ladder to Fan Deck')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["ladder_fan_deck"]+"']").Click()
  page.WaitConfirm(2000)
  
  #Add Safety Cages to Ladders
  additional_page.FindElement("//*[contains(text(),'Add Safety Cages to Ladders')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//bdi[text()='Add Safety Cages to Ladders?:']//preceding::div[@class='sapUiSimpleFixFlexFlexContent'][1]//li[text()='"+additional_configs["add_safety_cages_to_ladders"]+"']").Click()
  #additional_frame.FindElement("//ul[contains(@id,'list268')]//li[contains(text(),'"+additional_configs["add_safety_cages_to_ladders"]+"')]").Click()
  #additional_frame.FindElement("//li[.='"+additional_configs["add_safety_cages_to_ladders"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Safety Gates to All Ladder?
  additional_page.FindElement("//*[contains(text(),'Safety Gates to All Ladder?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//bdi[text()='Safety Gates to All Ladder?:']//preceding::div[@class='sapUiSimpleFixFlexFlexContent'][1]//li[text()='"+additional_configs["safety_gates_to_all_ladder"]+"']").Click()
  #additional_frame.FindElement("//ul[contains(@id,'list269')]//li[contains(text(),'"+additional_configs["safety_gates_to_all_ladder"]+"')]").Click()
  #additional_frame.FindElement("//li[.='"+additional_configs["safety_gates_to_all_ladder"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Ladder/Safety Cage Extensions:
  additional_page.FindElement("//*[contains(text(),'Ladder/Safety Cage Extensions')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.=\""+additional_configs["ladder_safety_cage_extensions"]+"\"]").Click()
  page.WaitConfirm(1000)
  
  #MOC - Platform Supports
  additional_page.FindElement("//*[contains(text(),'MOC - Platform Supports')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["moc_platform_supports"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Fan Deck Ext with Handrails
  additional_page.FindElement("//*[contains(text(),'Fan Deck Ext with Handrails')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["fan_deck_ext_with_handrils"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Louver Face Platform !!DATA MISSING/MisMatch!!!!
  #additional_page.FindElement("//*[contains(text(),'Louver Face Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  #page.WaitConfirm(1000)
  #additional_frame.FindElement("//li[.='"+additional_configs["louver_face_platform"]+"']").Click()
  #page.WaitConfirm(1000)
  
  #External Fan Motor Platform !!MISSING!!
  #additional_page.FindElement("//*[contains(text(),'External Fan Motor Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  #page.WaitConfirm(1000)
  #additional_frame.FindElement("//li[.='"+air_handling_values["system_frequency"]+"']").Click()
  #page.WaitConfirm(2000)
  
  #Access Door Platform
  additional_page.FindElement("//*[contains(text(),'Access Door Platform')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["access_door_platform"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Louver Face Ldr/Cage Extension!!DATA MISMATCH
  #additional_page.FindElement("//*[contains(text(),'Louver Face Ldr/Cage Extension')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  #page.WaitConfirm(1000)
  #additional_frame.FindElement("//li[.=\""+additional_configs["louver_face_cage_extension"]+"\"]").Click()
  #page.WaitConfirm(1000)
  
  #Fan Motor Pltf Ladder/Cage Ext !!MISSING!!
  #additional_page.FindElement("//*[contains(text(),'Fan Motor Pltf Ladder/Cage Ext')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  #page.WaitConfirm(1000)
  #additional_frame.FindElement("//li[.='"+additional_configs["louver_face_cage_extension"]+"']").Click()
  #page.WaitConfirm(2000)
  
  #Access Door Pltf Ladder Ext!!NON EDITABLE DATA MISMATCH
  #additional_page.FindElement("//*[contains(text(),'Access Door Pltf Ladder Ext')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  #page.WaitConfirm(1000)
  #additional_frame.FindElement("//li[.='"+additional_configs["access_door_pltf"]+"']").Click()
  #page.WaitConfirm(1000)
  
  #Internal Walkway @ Access Door
  additional_page.FindElement("//*[contains(text(),'Internal Walkway @ Access Door')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//bdi[text()='Internal Walkway @ Access Door:']//preceding::div[@class='sapUiSimpleFixFlexFlexContent'][1]//li[text()='"+additional_configs["internal_walkway_access_door"]+"']").Click()
  #additional_frame.FindElement("//ul[contains(@id,'list279')]//li[contains(text(),'"+additional_configs["internal_walkway_access_door"]+"')]").Click()
  #additional_frame.FindElement("//li[.='"+additional_configs["internal_walkway_access_door"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Internal Walkway MOC
  additional_page.FindElement("//*[contains(text(),'Internal Walkway MOC')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  additional_frame.FindElement("//li[.='"+additional_configs["internal_walkway_moc"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Internal Access: !!DATA MISSING!!
  #additional_page.FindElement("//*[contains(text(),'Internal Access:')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  #page.WaitConfirm(1000)
  #additional_frame.FindElement("//li[.='"+additional_configs["internal_access"]+"']").Click()
  #page.WaitConfirm(2000)
  
  additional_page.FindElement("//span[.='Shipping and Specials']").Click()