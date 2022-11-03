def Hhook(target_process):
 try:
     session = frida.attach(target_process) //target_process is the process_id of "clipbrd.exe"
     script = session.create_script("""
         var clipbrd = Module.getExportByName("user32.dll", "GetClipboardData");
         Interceptor.attach(clipbrd, {
                 onEnter: function (args) {
                 },
                 onLeave: function (retval, state) {
                     retval.replace(ptr(NULL));
                 },
         });
         """)
     script.on('message', on_message)
     script.load()
     str="hook %s success!\n"%target_process
     print("hook %s success!"%target_process)
 except Exception as e: 
  print(f'hook {target_process} error:{e}')
 
