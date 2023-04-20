def search_item(page, search_value):
  if(page.headerShellBar.linkSearch.WaitAliasChild("textnode", 10000).Exists):
    page.FindElement("//a[@id='sf']/span").Click()
  page.WaitConfirm(5000)
  if(page.headerShellBar.WaitAliasChild("searchboxSearchfieldinshellInput", 10000).Exists):
    searchBox = page.FindElement("//div[@id='searchFieldInShell-input-content']/input")
    searchBox.SetText(search_value)
    searchBox.Keys("[Enter]")