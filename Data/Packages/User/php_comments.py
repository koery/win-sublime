import sublime, sublime_plugin,time

class PhpCommentsCommand(sublime_plugin.TextCommand):
 def run(self, edit):
  self.view.run_command("insert_snippet",{
   "contents":"<?php\n"+
   "/**\n"+
   "* @author ${2:coco}\n"+
   "* @date "+time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+
   "* @todo "+"\n"+
   "*/\n"
  })