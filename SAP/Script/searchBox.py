def search_item(page, search_value):
  if(NameMapping.Sys.browser.pageFlp.WaitNamedChild("textnode", 10000).Exists):
    page.FindElement("//a[@id='sf']/span").Click()
  page.WaitConfirm(5000)
  if(NameMapping.Sys.browser.pageFlp.WaitNamedChild("searchboxSearchfieldinshellInput", 10000).Exists):
    searchBox = page.FindElement("//div[@id='searchFieldInShell-input-content']/input")
    searchBox.SetText(search_value)
    searchBox.Keys("[Enter]")