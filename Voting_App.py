import wx

polls = {"0" : ["Sample Poll", "12345", {"Whats the weather like?" : {"Sunny" : 0, "Rainy" : 0, "Cold" : 0, "Warm" : 0},
                                             "Best Type of food?": {"Pizza": 0, "Ice Cream": 0, "Burger": 0, "Nachos": 0},
                                             "Most Enjoyable Sport?": {"Football": 0, "Basketball": 0, "Soccer": 0, "Baseball": 0}}]}

current_poll = "0"

def getPollName(code):
    return polls[code][0]

def getPollOwner(code):
    return polls[code][1]

def getQuestions(code):
    L = []
    for key in polls[code][2]:
        L.append(key)
    return L

def getQuestionAnswers(code, question):
    L = []
    for answer in polls[code][2][question]:
        L.append(answer)
    return L

def answerQuestion(code, question, answer):
    polls[code][2][question][answer] =  (polls[code][2][question][answer] +1)

def makePoll(name, owner):
    if len(sorted(polls.keys())) > 0:    
        code = sorted(polls.keys())[-1]
    else:
        code = 0
    code = str(int(code) + 1)
    polls[code] = [name, owner, {}]
    return code

def makeQuestion(code, question, answers):
    A = {}
    for a in answers:
        A[a] = 0
    polls[code][2][question] = A

def getResult(poll, question, answer):
    return polls[poll][2][question][answer]

def stringTOlist(code):
    return  list(map(str, code.split(',')))

def deleteQuestion(code, question):
    del(polls[code][2][question])

def renameQuestion(code, question, newname):
    polls[code][2][newname] = polls[code][2][question]
    del (polls[code][2][question])





class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        global current_poll
        Qs = getQuestions(current_poll)
        As =getQuestionAnswers(current_poll, Qs[0])


        Q1 = wx.StaticText(self, -1, Qs[0], (20,20))
        A1 = wx.StaticText(self, -1, As[0], (20,40))
        A2 = wx.StaticText(self, -1, As[1], (20,60))
        A3 = wx.StaticText(self, -1, As[2], (20, 80))
        A4 = wx.StaticText(self, -1, As[3], (20, 100))

        title = wx.StaticText(self, -1, "Total Vote", (250, 20))
        R1 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[0], As[0])), (260, 40))
        R2 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[0], As[1])), (260, 60))
        R3 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[0], As[2])), (260, 80))
        R4 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[0], As[3])), (260, 100))

class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        global current_poll
        Qs = getQuestions(current_poll)
        As =getQuestionAnswers(current_poll, Qs[1])


        Q1 = wx.StaticText(self, -1, Qs[1], (20,20))
        A1 = wx.StaticText(self, -1, As[0], (20,40))
        A2 = wx.StaticText(self, -1, As[1], (20,60))
        A3 = wx.StaticText(self, -1, As[2], (20, 80))
        A4 = wx.StaticText(self, -1, As[3], (20, 100))

        title = wx.StaticText(self, -1, "Total Vote", (250, 20))
        R1 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[1], As[0])), (260, 40))
        R2 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[1], As[1])), (260, 60))
        R3 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[1], As[2])), (260, 80))
        R4 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[1], As[3])), (260, 100))
        
 

class TabThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        global current_poll
        Qs = getQuestions(current_poll)
        As =getQuestionAnswers(current_poll, Qs[2])


        Q1 = wx.StaticText(self, -1, Qs[2], (20,20))
        A1 = wx.StaticText(self, -1, As[0], (20,40))
        A2 = wx.StaticText(self, -1, As[1], (20,60))
        A3 = wx.StaticText(self, -1, As[2], (20, 80))
        A4 = wx.StaticText(self, -1, As[3], (20, 100))

        title = wx.StaticText(self, -1, "Total Vote", (250, 20))
        R1 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[2], As[0])), (260, 40))
        R2 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[2], As[1])), (260, 60))
        R3 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[2], As[2])), (260, 80))
        R4 = wx.StaticText(self, -1, str(getResult(current_poll, Qs[2], As[3])), (260, 100))
        
 

class ResultFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Poll Results Menu")
 
        page = wx.Panel(self)
        noteb = wx.Notebook(page)
 
        tab1 = TabOne(noteb)
        tab2 = TabTwo(noteb)
        tab3 = TabThree(noteb)
       
        noteb.AddPage(tab1, "Q 1")
        noteb.AddPage(tab2, "Q 2")
        noteb.AddPage(tab3, "Q 3")
       
        sizer = wx.BoxSizer()
        sizer.Add(noteb, 1, wx.EXPAND)
        page.SetSizer(sizer)



class MyFrame(wx.Frame):
    def __init__(self):
       global current_poll
       wx.Frame.__init__(self, parent=None, title="Voting App", size = (400, 440))
       panel = wx.Panel(self)
       vote_button = wx.Button(panel, label="Vote", pos = (130, 10), size = (80, 60))
       self.Bind(wx.EVT_BUTTON, self.showQs, vote_button)
       
       view_button = wx.Button(panel, label="View Results", pos = (130, 90), size = (80, 60))
       self.Bind(wx.EVT_BUTTON, self.showResults, view_button)

       edit_button = wx.Button(panel, label="Edit Poll", pos = (130, 170), size = (80, 60))
       self.Bind(wx.EVT_BUTTON, self.editPoll, edit_button)

       create_button = wx.Button(panel, label="Create Poll", pos = (130, 250), size = (80, 60))
       self.Bind(wx.EVT_BUTTON, self.createPoll, create_button)

       exit_button = wx.Button(panel, label="Exit",pos = (130, 330),  size = (80, 60))
       self.Bind(wx.EVT_BUTTON, self.closeButton, exit_button)
       self.Bind(wx.EVT_CLOSE, self.closeWindow)
         
       self.Show()

    def closeButton(self, event):
        self.Close(True)

    def closeWindow(self, event):
        self.Destroy()

    def showQs(self, event):
        dlg = wx.TextEntryDialog(self, 'Enter the Poll Code','Poll Selection')
        if dlg.ShowModal() == wx.ID_OK:
           poll_code = dlg.GetValue()
        dlg.Destroy()

        current_poll = poll_code

        Qs = getQuestions(current_poll)
        for question in Qs:
           modal = wx.SingleChoiceDialog(None, question, '322 Poll', getQuestionAnswers(current_poll, question))

           if modal.ShowModal() == wx.ID_OK:
             answer = modal.GetStringSelection() 
             answerQuestion(current_poll, question, answer)

    def createPoll(self, event):
        global current_poll
        dlg = wx.TextEntryDialog(self, 'Enter a Name','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           name = dlg.GetValue()
        dlg.Destroy()

        dlg = wx.TextEntryDialog(self, 'Enter a owner','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           owner = dlg.GetValue()
        dlg.Destroy()

        current_poll = makePoll(name, owner)

        dlg = wx.TextEntryDialog(self, 'Enter Question 1','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           question = dlg.GetValue()
        dlg.Destroy()

        dlg = wx.TextEntryDialog(self, 'Enter the 4 answers for Question 1, seperated by commas','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           answers = dlg.GetValue()
        dlg.Destroy()

        answer_list = stringTOlist(answers)
        makeQuestion(current_poll, question, answer_list)

        dlg = wx.TextEntryDialog(self, 'Enter Question 2','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           question = dlg.GetValue()
        dlg.Destroy()

        dlg = wx.TextEntryDialog(self, 'Enter the 4 answers for Question 2, seperated by commas','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           answers = dlg.GetValue()
        dlg.Destroy()

        answer_list = stringTOlist(answers)
        makeQuestion(current_poll, question, answer_list)

        dlg = wx.TextEntryDialog(self, 'Enter Question 3','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           question = dlg.GetValue()
        dlg.Destroy()

        dlg = wx.TextEntryDialog(self, 'Enter the 4 answers for Question 3, seperated by commas','Poll Creation')
        if dlg.ShowModal() == wx.ID_OK:
           answers = dlg.GetValue()
        dlg.Destroy()

        answer_list = stringTOlist(answers)
        makeQuestion(current_poll, question, answer_list)

    def showResults(self, event):
       global current_poll
       dlg = wx.TextEntryDialog(self, 'Enter the Poll Code','Poll Selection')
       if dlg.ShowModal() == wx.ID_OK:
           poll_code = dlg.GetValue()
       dlg.Destroy()

       current_poll = poll_code
       app = wx.App()
       ResultFrame().Show()
       app.MainLoop()

    def editPoll(self, event):
       global current_poll
       dlg = wx.TextEntryDialog(self, 'Enter the Poll Code','Poll Selection')
       if dlg.ShowModal() == wx.ID_OK:
           poll_code = dlg.GetValue()
       dlg.Destroy()

       current_poll = poll_code
       Qs = getQuestions(current_poll)
		#----------#
       dlg = wx.MessageDialog(None, "Do you want to Change the Title of the current Poll?",'Edit Title',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
          dlg = wx.TextEntryDialog(self, 'Enter the new Title','Title Change')
          if dlg.ShowModal() == wx.ID_OK:
             new_title = dlg.GetValue()
          dlg.Destroy()
          polls[current_poll][0] = new_title

		#----------#
       dlg = wx.MessageDialog(None, "Do you want to Change the Owner of the current Poll?",'Edit Owner',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
          dlg = wx.TextEntryDialog(self, 'Enter the new Owner','Edit Owner')
          if dlg.ShowModal() == wx.ID_OK:
             new_owner = dlg.GetValue()
          dlg.Destroy()
          polls[current_poll][1] = new_owner
		#----------#
       dlg = wx.MessageDialog(None, "Do you want to Change Question 1 of the current Poll?",'Edit Q1',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
          dlg = wx.TextEntryDialog(self, 'Enter the corrected Question','Edit Q1')
          if dlg.ShowModal() == wx.ID_OK:
             Q1 = dlg.GetValue()
          dlg.Destroy()
          renameQuestion(current_poll, Qs[0], Q1)
		#----------#
       dlg = wx.MessageDialog(None, "Do you want to delete Question 1 from the current Poll?",'Delete Q1',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
         deleteQuestion(current_poll, Qs[0])

		 #----------#
       dlg = wx.MessageDialog(None, "Do you want to Change Question 2 of the current Poll?",'Edit Q2',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
          dlg = wx.TextEntryDialog(self, 'Enter the corrected Question','Edit Q2')
          if dlg.ShowModal() == wx.ID_OK:
             Q2 = dlg.GetValue()
          dlg.Destroy()
          renameQuestion(current_poll, Qs[1], Q2)
		#----------#
       dlg = wx.MessageDialog(None, "Do you want to delete Question 2 from the current Poll?",'Delete Q2',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
         deleteQuestion(current_poll, Qs[1])

		  #----------#
       dlg = wx.MessageDialog(None, "Do you want to Change Question 3 of the current Poll?",'Edit Q3',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
          dlg = wx.TextEntryDialog(self, 'Enter the corrected Question','Edit Q3')
          if dlg.ShowModal() == wx.ID_OK:
             Q2 = dlg.GetValue()
          dlg.Destroy()
          renameQuestion(current_poll, Qs[2], Q3)
		#----------#
       dlg = wx.MessageDialog(None, "Do you want to delete Question 3 from the current Poll?",'Delete Q3',wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
 
       if result == wx.ID_YES:
         deleteQuestion(current_poll, Qs[2])


if __name__ == "__main__":
   app = wx.App(False)
   frame = MyFrame()
   app.MainLoop()

