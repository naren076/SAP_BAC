def coil_configuration(coil_configuration_page, coil_configuration_values):
  variant_config_frame = coil_configuration_page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  variant_config_textNode = variant_config_frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  variant_config_textNode2 = variant_config_textNode.sectionSplitter0Content1
  variant_config_textNode2.FindElement("//span[.='Coil Configuration']").Click()
  #---Coil Style:
  if coil_configuration_values["coil_style"] != "SAP Defined":
    variant_config_frame.FindElement("//*[contains(text(),'Coil Style')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    coil_configuration_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_style"]+"']").Click()
    coil_configuration_page.WaitConfirm(1000)
  
  #---Coil Material of Construction:
  variant_config_frame.FindElement("//*[contains(text(),'Coil Material of Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  coil_configuration_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_material_of_construction"]+"']").Click()
  coil_configuration_page.WaitConfirm(1000)
  
  #---Coil Finning:
  variant_config_frame.FindElement("//*[contains(text(),'Coil Finning')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  coil_configuration_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_finning"]+"']").Click()
  coil_configuration_page.WaitConfirm(1000)
  
  #---Coil Gauge:
  variant_config_frame.FindElement("//*[contains(text(),'Coil Gauge')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  coil_configuration_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_gauge"]+"']").Click()
  coil_configuration_page.WaitConfirm(1000)
  
  #---ASME Coil:
  variant_config_frame.FindElement("//*[contains(text(),'ASME Coil')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  coil_configuration_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//*[contains(text(),'ASME Coil')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(coil_configuration_values["asme_coil"])
  variant_config_frame.FindElement("//*[contains(text(),'ASME Coil')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  coil_configuration_page.WaitConfirm(1000)
  
  #---CanadianRegistrationNumber-CRN:
  variant_config_frame.FindElement("//*[contains(text(),'CanadianRegistrationNumber-CRN')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  coil_configuration_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//*[contains(text(),'CanadianRegistrationNumber-CRN')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(coil_configuration_values["canadianregistrationnumber_crn"])
  variant_config_frame.FindElement("//*[contains(text(),'CanadianRegistrationNumber-CRN')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  coil_configuration_page.WaitConfirm(1000)
  
  #---Coil Connection Pairs:
  if coil_configuration_values["coil_connection_pairs"] != "SAP Defined":
    variant_config_frame.FindElement("//*[contains(text(),'Coil Connection Pairs')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    coil_configuration_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_connection_pairs"]+"']").Click()
    coil_configuration_page.WaitConfirm(1000)
  
  #---Coil Connection Std Size:
  if coil_configuration_values["coil_connection_std_size"] != "SAP Defined":
    variant_config_frame.FindElement("//*[contains(text(),'Coil Connection Std Size')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    coil_configuration_page.WaitConfirm(1000)
    variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_connection_std_size"]+"']").Click()
    coil_configuration_page.WaitConfirm(1000)
  
  #---Coil Connection Type:
  variant_config_frame.FindElement("//*[contains(text(),'Coil Connection Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  coil_configuration_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+coil_configuration_values["coil_connection_type"]+"']").Click()
  coil_configuration_page.WaitConfirm(1000)
  
  #---go to Air Handling System:
  variant_config_textNode2.FindElement("//span[.='Air Handling System']").Click()