def search_item(search_page, search_value):
  if(NameMapping.Sys.browser.pageFlp.WaitNamedChild("textnode", 10000).Exists):
    search_page.FindElement("//a[@id='sf']/span").Click()
  search_page.WaitConfirm(5000)
  if(NameMapping.Sys.browser.pageFlp.WaitNamedChild("searchboxSearchfieldinshellInput", 10000).Exists):
    searchBox = search_page.FindElement("//div[@id='searchFieldInShell-input-content']/input")
    searchBox.SetText(search_value)
    searchBox.Keys("[Enter]")