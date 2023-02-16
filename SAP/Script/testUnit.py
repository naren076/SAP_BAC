import loginForm
import searchBox
import createSalesPage
import createStandardOrder

def Test3():
  Browsers.Item[btChrome].Navigate("https://s4qas.baltimoreaircoil.com/sap/bc/ui2/flp")
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  page = browser.pageFlp
  page.linkLogonButton.textnodeContinue.Click()
  page.Wait()
  #--Login form
  loginForm.login_form(page, "NGANESAN")
  page.Wait()
  #--Search va01 ----
  searchBox.search_item(page, "va01")
  panel = page.sectionShellSplitCanvas
  panel.sectionSearchpageCont.linkCreateSalesOrders.Click()
  textbox = panel.frameApplicationSalesdocumentCre.formWebguiform0
  #--Enter order Type--
  createSalesPage.create_sales_order(textbox)
  #--Enter Order Details---
  createStandardOrder.create_standard_order(browser, textbox)
  
  page.headerShellBar.linkHome.imageShellHeaderIcon.Click()
  page.sectionShellSplitCanvas.sectionTileGroups.Click()
  #----Search vao1 ------
  searchBox.search_item(page, "va01")
  
  panel = page.sectionShellSplitCanvas
  panel.sectionSearchpageCont.linkCreateSalesOrders.Click()
  textbox = panel.frameApplicationSalesdocumentCre.formWebguiform0
  
  #--Enter order type------
  createSalesPage.create_sales_order(textbox)
  #--Enter order details---
  createStandardOrder.create_standard_order(browser, textbox)
  
  frame = textbox.frameC120
  section = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  section2 = section.sectionSplitter0Content1
  section2.textnodeNone.Click()
  frame.sectionShellSplitCanvas2.sectionTileGroups.textnodeList6.textnodeCn.Click()
  section2.textnodeShowValueHelp.Click()
  frame.sectionDialog2ValuehelpdialogDia.textnodeDialog2ValuehelpdialogLi.textnodeLabel9Clone98Bdi.Click()
  textbox = section2.textboxWaterFlowRatePerUnitLS
  textbox.SetText("50")
  textbox = section2.textboxEnteringWaterTemperatureC
  textbox.Click()
  textbox.SetText("30")
  textbox = section2.textboxLeavingWaterTemperatureC
  textbox.Click()
  textbox.SetText("24")
  textbox = section2.textbox
  textbox.Click()
  textbox.SetText("23")
  section2.panelConfigurationcomponentValua.Click()
  page.wait()
  frame = page.sectionShellSplitCanvas
  frame2 = frame.frameApplicationSalesdocumentCre
  frame3 = frame2.formWebguiform0
  #Done button
  section.footerConfigurationcomponentConf.buttonEmphasized.ClickButton()
  page.WaitConfirm(10000)
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  frame = browser.pageFlp.sectionShellSplitCanvas.frameApplicationSalesdocumentCre
  frame2 = frame.formWebguiform0
  #frame2.frameC102.sectionShellSplitCanvas.sectionApplicationVariantconfigu.footerConfigurationcomponentConf.buttonEmphasized.ClickButton()
  frame2.frameC104.sectionShellSplitCanvas.sectionTileGroups.footerPage0PageFooterwrapper.buttonEmphasized.ClickButton()
  frame2.panelSave.Click()
  page.WaitConfirm(40000)
  frame.panelContinue.Click()

  #browser.BrowserWindow.Maximize()
  #page = browser.pageFlp