from xml.dom.minidom import parse
import xml.dom.minidom
from xmlrpc.server import list_public_methods
import sys, os

# Open XML document using minidom parser
class XML_controller:
    def __init__(self, data):
          self.__url = data
          self.__DOMTree = xml.dom.minidom.parse(data)
          self.__collection = self.__DOMTree.documentElement

    def findRepereat(self):
          workflows = self.__collection.getElementsByTagName("Workflow")

          list_to_repeat = []
          for i in range(len(workflows)):
            aux = workflows[i]
            countR = 0
            j = i + 1
            for j in range(i+1,len(workflows)):
                   item_1 = aux.getAttribute('name')
                   item_2 = workflows[j].getAttribute('name')
                   if(item_1 == item_2):
                     countR += 1
                   #  agrego todos los elementos repetidos
                     list_to_repeat.append(workflows[j])
            if(countR > 0):
               list_to_repeat.append(workflows[i])
          return list_to_repeat
   
    def printWorkflows(self):
      results = self.findRepereat()
      new_name = str(self.__url).split("/")
      new_name = new_name[len(new_name)-1]
      new_name = new_name.split(".")[0]
      isdir = os.path.isdir("./results/")
      if (isdir == False):
        os.mkdir("./results/")
      with open(f"./results/{new_name}-result.xml", "w") as xml_file:
         for workflow in results:
            workflow.writexml(xml_file)
         # print("")
         # if workflow.hasAttribute("name") and workflow.hasAttribute("parameters"):
         #    print (f"<Name=\"{workflow.getAttribute('name')}\" parameters:=\"{workflow.getAttribute('parameters')}\">")
         # else:
         #    print (f"<Name=\"{workflow.getAttribute('name')}\">")
         # steps = workflow.getElementsByTagName('Step')
         # for step in steps:
         #    cmd=step.getAttribute('cmd')
         #    labelFalse = step.getAttribute('labelFalse')
         #    labelTrue = step.getAttribute('labelTrue')
         #    label = step.getAttribute('label')
         #    print (f"<Step cmd=\"{cmd}\" labelFalse=\"{labelFalse}\" labelTrue=\"{labelTrue}\" label=\"{label}\" >")
         #    cmd=""
         #    labelFalse = ""
         #    labelTrue = ""
         #    label = ""