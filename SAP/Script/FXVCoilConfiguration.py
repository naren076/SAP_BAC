#import AirHandlingConfiguration

def coil_configuration(page, coil_configuration_values):
  frame = page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  textNode = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  textNode2 = textNode.sectionSplitter0Content1
  textNode2.FindElement("//span[.='Coil Configuration']").Click()
  
  #--Coil Style
  if coil_configuration_values["coil_style"] != "SAP Defined":
    frame.FindElement("//*[contains(text(),'Coil Style')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+coil_configuration_values["coil_style"]+"']").Click()
    page.WaitConfirm(1000)
  
  #--Coil Material of Construction
  frame.FindElement("//*[contains(text(),'Coil Material of Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+coil_configuration_values["coil_material_of_construction"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--Coil Finning
  frame.FindElement("//*[contains(text(),'Coil Finning')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+coil_configuration_values["coil_finning"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--Coil Gauge
  frame.FindElement("//*[contains(text(),'Coil Gauge')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+coil_configuration_values["coil_gauge"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--ASME Coil
  frame.FindElement("//*[contains(text(),'ASME Coil')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//*[contains(text(),'ASME Coil')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(coil_configuration_values["asme_coil"])
  frame.FindElement("//*[contains(text(),'ASME Coil')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
  #--CanadianRegistrationNumber-CRN
  frame.FindElement("//*[contains(text(),'CanadianRegistrationNumber-CRN')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//*[contains(text(),'CanadianRegistrationNumber-CRN')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(coil_configuration_values["canadianregistrationnumber_crn"])
  frame.FindElement("//*[contains(text(),'CanadianRegistrationNumber-CRN')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
  #--Coil Connection Pairs
  if coil_configuration_values["coil_connection_pairs"] != "SAP Defined":
    frame.FindElement("//*[contains(text(),'Coil Connection Pairs')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+coil_configuration_values["coil_connection_pairs"]+"']").Click()
    page.WaitConfirm(1000)
  
  #--Coil Connection Std Size
  if coil_configuration_values["coil_connection_std_size"] != "SAP Defined":
    frame.FindElement("//*[contains(text(),'Coil Connection Std Size')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+coil_configuration_values["coil_connection_std_size"]+"']").Click()
    page.WaitConfirm(1000)
  
  #--Coil Connection Type
  frame.FindElement("//*[contains(text(),'Coil Connection Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+coil_configuration_values["coil_connection_type"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--go to Air Handling System
  textNode2.FindElement("//span[.='Air Handling System']").Click()