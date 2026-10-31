import tkinter as tk
import pandas as pd
import numpy as np
pd.set_option('display.expand_frame_repr', False)

#final conclusion
search = 'support'

premiseTable = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Premise Table').astype(str)
detailRules = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Detail Rules').astype(str)
questions = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Questions').astype(str)
choices = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Choices').astype(str)
rules = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Rules').astype(str)
wm = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Working Memory Table').astype(str).reset_index(drop=True)

def reset():
  global premiseTable, detailRules, questions, choices, rules, wm
  premiseTable = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Premise Table').astype(str)
  detailRules = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Detail Rules').astype(str)
  questions = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Questions').astype(str)
  choices = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Choices').astype(str)
  rules = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Rules').astype(str)
  wm = pd.read_excel('database/Evaluasi Mahasiswa.xlsx', 'Working Memory Table').astype(str).reset_index(drop=True)
  

def start():
  global wm, ques_disp
  reset()
  searchConclude(search)
  print(wm.iloc[-1:]['Value'].values[0])
  txt = 'Status anda adalah '+wm.iloc[-1:]['Value'].values[0]
  ques_disp['text']=txt
  ques_lbl['text']='Conclusion'

def printWM():
    global wm
    txt = ''
    for item in wm.values:
      txt += item[0]
      if(len(item[0]) <= 7):
        txt += '\t'
      txt += '\t'  
      txt += item[1]
      txt += '\n'  

    wm_disp['text']=txt
    

def searchConclude1(id, conclude):
  global rules
  global wm

  temp_rule = rules.loc[(rules['Attribute_Conclude'] == id) & (rules['Conclusion'] == conclude )].sort_values(by=['Attribute_Conclude','Conclusion'], ascending=[False, True]).reset_index(drop=True)
  
  i=0
  while(True):
    
    #print("########")
    printWM()
    #print("########")
    
    
    rule_id = temp_rule['id'][i]
    rules.loc[(rules['id'] == rule_id), 'U'] = 0
    rules.loc[(rules['id'] == rule_id), 'M'] = 1
    
    num_rule = temp_rule['Rule'][i]
    #print(num_rule)
    #print("c1")
    ruleCheck(num_rule)
    
      
    temp_premise = detailRules[detailRules['rules_id'] == rule_id]
    
    premiseCheck(temp_premise, num_rule)
    
    i+=1

    ruleCheck(num_rule)
    
    #print("RULES")
    #print(rules[rules['Rule']==num_rule]['TD'].values)
    if((rules[rules['Rule']==num_rule]['TD'].values[0])==1):  #ada problem
      #print(num_rule + " masuk")
      answer = rules[rules['Rule']==num_rule]['Conclusion'].values[0]
      attrib = rules[rules['Rule']==num_rule]['Attribute_Conclude'].values[0]
      join_rule = (rules.set_index('id').join((detailRules.set_index('premise_id').join(premiseTable.set_index('id'))).set_index('rules_id')))
      #print('DETAIL RULE')
      #print(join_rule.loc[join_rule['Rule']==num_rule])
      if((attrib in wm.Attribute.values)==False):
        wm = wm.append({'Attribute' : attrib, 'Value' : answer }, ignore_index=True)
        #print("u2")
        updatePremiseTable()
        #print("########wm2")
        printWM()
        #print("########")
        #print("c2")
        ruleCheck(num_rule)
        return True

    if(i== len(temp_rule.index)):
      break


def searchConclude(id):
  global rules
  global wm
  temp_rule = rules[rules['Attribute_Conclude'].str.match(id)== True].sort_values(by=['Attribute_Conclude','Conclusion'], ascending=[False, True]).reset_index(drop=True)
  conclude = temp_rule['Conclusion'].unique()
  #print(conclude)
  for i in conclude:
    #print("======="+i+"======")
    if searchConclude1(id,i):
      break
  

  
    

    

def ruleCheck(rule_id):
  #print("RULE CHECK - "+rule_id)
  global rules

  # if (1 in rules.loc[(rules['Rule'] == rule_id), 'D'].values) :
  #   return 'discard'
    

  
  join_rule = (rules.set_index('id').join((detailRules.set_index('premise_id').join(premiseTable.set_index('id'))).set_index('rules_id')))
  #print('DETAIL RULE')
  #print(join_rule.loc[join_rule['Rule']==rule_id])
  #print('VALUE')
  #print(join_rule.loc[join_rule['Rule']==rule_id]['Premise Clause Status'].values)

  if('FA' in join_rule.loc[join_rule['Rule']==rule_id]['Premise Clause Status'].values):
    rules.loc[rules['Rule']==rule_id, 'U'] = 1
    rules.loc[rules['Rule']==rule_id, 'A'] = 0
    rules.loc[rules['Rule']==rule_id, 'M'] = 0
    rules.loc[rules['Rule']==rule_id, 'D'] = 1
    rules.loc[rules['Rule']==rule_id, 'TD'] = 0
    return 'discard'


  elif('FR' in join_rule.loc[join_rule['Rule']==rule_id]['Premise Clause Status'].values):
    #print('continue')
    return 'continue'


  else:
    rules.loc[rules['Rule']==rule_id, 'U'] = 1
    rules.loc[rules['Rule']==rule_id, 'A'] = 0
    rules.loc[rules['Rule']==rule_id, 'M'] = 0
    rules.loc[rules['Rule']==rule_id, 'TD'] = 1
    rules.loc[rules['Rule']==rule_id, 'D'] = 0
    return 'true'

def premiseCheck(prem, rule_id):
  global premiseTable
  global rules
  #print("===PREMISE===")
  #print(prem)
  for index, prem_i in prem.iterrows() :
    #print("-")
    #print(prem_i)
    id_prem = prem_i[2]
    check_premise = premiseTable[premiseTable['id'] == id_prem]
    attrib = check_premise['Attribute'].values[0]
    checkAttrib(attrib)
    if(ruleCheck(rule_id) == 'discard'):
      #print("DISCARD")
      break
  
  

  

  

def checkAttrib(attrib):
    
    global wm
    if((attrib in wm.Attribute.values)==False):
      if(attrib in rules.Attribute_Conclude.unique()):
        searchConclude(attrib)
      else:
        collectAnswer(attrib)

def updatePremiseTable():
  global wm
  global premiseTable

  for index, att in wm.iterrows():
    #print("masuk")
    #print(att)
    premiseTable.loc[(premiseTable['Attribute']==att[0]) & (premiseTable['Value'] == att[1]), 'Premise Clause Status'] = 'TU'
    premiseTable.loc[(premiseTable['Attribute']==att[0]) & (premiseTable['Value'] != att[1]), 'Premise Clause Status'] = 'FA'
    #print("TRUE")
    #print(premiseTable.loc[(premiseTable['Attribute']==att[0]) & (premiseTable['Value'] == att[1])])
    #print("FALSE")
    #print(premiseTable.loc[(premiseTable['Attribute']==att[0]) & (premiseTable['Value'] != att[1])])

  

def collectAnswer(attrib):
  
  temp_quest = (questions.set_index('id').join(choices.set_index('id_questions')))
  temp_quest = temp_quest[temp_quest['Attribute'] == attrib].reset_index(drop=True)
  ask = temp_quest['Questions'][0]
  choice = temp_quest['choices'].unique()

  #print('=============')
  #print(ask)
  ques_disp['text']=ask

  global ques_entry
  global ques_ans
  text_choice = ''
  counter = 0
  #ques_entry = tk.Entry(master=ques_frm)
  ques_ans = tk.StringVar()
  answer = ''
  for i in choice:
    text_choice = text_choice + str(counter) + ' : '
    text_choice = text_choice + i + '\n'
    counter = counter+1
  
  ques_choice['text'] = text_choice
  print(text_choice)
  
  btn_ans.wait_variable(ques_ans)

  print(ques_ans.get())
  answer=ques_entry.get()

  if(answer == ''):
    answer=0
  answer = choice[int(answer)]
  
  global wm
  wm = wm.append({'Attribute' : attrib, 'Value' : answer}, ignore_index=True)
  #print("u1")
  updatePremiseTable()
  #print("########wm1")
  printWM()
  #print("########")

  ques_disp['text']=''
  ques_choice['text'] = ''
  ques_entry.delete(0)

#Setup GUI
window = tk.Tk()
window.title("Evaluasi Mahasiswa")


window.columnconfigure([0,1], minsize=400, weight=1)
window.rowconfigure(1, minsize=400)

btn_frm = tk.Frame(master=window, height=20, bg='gray')
btn_strt = tk.Button(master=btn_frm, text="Start", command=start)
btn_strt.grid(row=0, column=0, sticky='ns', pady=10, padx=10)

wm_frm = tk.Frame(master=window, bg='#cfeff3')
wm_lbl = tk.Label(master=wm_frm, text="Working Memory", bg='#cfeff3')
wm_disp = tk.Label(master=wm_frm, bg='#cfeff3', justify='left')
wm_lbl.grid(row=0, column=0, sticky='nwe')
wm_disp.grid(row=1, column=0, sticky='nwe')

ques_frm = tk.Frame(master=window, bg='#bfd4d8')
ques_lbl = tk.Label(master=ques_frm, text="Question", bg='#bfd4d8')
ques_disp = tk.Label(master=ques_frm, bg='#bfd4d8', justify='left')
ques_choice = tk.Label(master=ques_frm, bg='#bfd4d8', justify='left')
ques_entry = tk.Entry(master=ques_frm)
ques_ans = tk.StringVar()
btn_ans = tk.Button(master=ques_frm, text='Submit', command=lambda: ques_ans.set(ques_entry.get()))
ques_lbl.grid(row=0, column=0, sticky='nwe')
ques_disp.grid(row=1, column=0, sticky='nw')
ques_choice.grid(row=2, column = 0, sticky='nw')
ques_entry.grid(row=3, column=0, sticky='swen')
btn_ans.grid(row=3, column=1, sticky='swn', padx=10)

btn_frm.grid(row=0, column=0, columnspan=2, sticky='nsew')
wm_frm.grid(row=1, column=0, sticky='nwes')
ques_frm.grid(row=1, column=1, sticky='nwes')

window.mainloop()

