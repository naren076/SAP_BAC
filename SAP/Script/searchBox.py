def search_item(page, search_value):
  page.FindElement("//a[@id='sf']/span").Click()
  page.WaitConfirm(5000)
  searchBox = page.FindElement("//div[@id='searchFieldInShell-input-content']/input")
  searchBox.SetText(search_value)
  searchBox.Keys("[Enter]")