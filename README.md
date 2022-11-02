# rdp-prohibits-file-copying-to-local
For security reasons, it is forbidden to copy files from the rdp server to the local
1.First, monitor all clipboard operations of the windows operating system through API Monitor software
![image](https://user-images.githubusercontent.com/35139449/199422164-6895f537-73b2-4e6c-a507-277c6de338f3.png)

2.It is not difficult to find that when copying files from rdp to local, "user32.dll", "GetClipboardData" api will be triggered

3.the frida 's hook code 
