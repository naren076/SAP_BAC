def login_form(page, username):
  login_form = page.FindElement("//form")
  username_field = login_form.FindElement("//div[@id='USERNAME_BLOCK']/input")
  username_field.SetText(username)
  username_field.Keys("[Tab]")
  passwordBox = login_form.FindElement("//div[@id='PASSWORD_BLOCK']/input")
  #passwordBox.SetText(Project.Variables.Password1)
  passwordBox.SetText(Project.Variables.Password2)
  login_form.FindElement("//button[.='Log On']").Click()
  
  
  #https://www.youtube.com/watch?v=eci9iU_s6Ag&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=38