PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> & "C:\Program Files\Python313\python.exe" "c:/Users/GOLD COMPUTERS/Desktop/Project/afrilang/app.py"
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.95:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Mar/2026 11:40:56] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:41:00] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:41:10] "POST /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:41:20] "POST /quiz HTTP/1.1" 200 -
PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> & "C:\Program Files\Python313\python.exe" "c:/Users/GOLD COMPUTERS/Desktop/Project/afrilang/app.py"
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.95:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Mar/2026 11:44:02] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:44:06] "GET /quiz HTTP/1.1" 200 -
[2026-03-08 11:44:11,891] ERROR in app: Exception on /quiz [POST]
Traceback (most recent call last):
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 1511, in wsgi_app       
    response = self.full_dispatch_request()
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "c:\Users\GOLD COMPUTERS\Desktop\Project\afrilang\app.py", line 39, in quiz
    return render_template("quiz.html", question=question, english=english, message=message)
                                                 ^^^^^^^^
UnboundLocalError: cannot access local variable 'question' where it is not associated with a value
127.0.0.1 - - [08/Mar/2026 11:44:11] "POST /quiz HTTP/1.1" 500 -
PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> & "C:\Program Files\Python313\python.exe" "c:/Users/GOLD COMPUTERS/Desktop/Project/afrilang/app.py"
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.95:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Mar/2026 11:45:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:45:27] "GET /quiz HTTP/1.1" 200 -
PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> & "C:\Program Files\Python313\python.exe" "c:/Users/GOLD COMPUTERS/Desktop/Project/afrilang/app.py"
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.95:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Mar/2026 11:47:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:47:05] "GET /quiz HTTP/1.1" 200 -
[2026-03-08 11:47:12,180] ERROR in app: Exception on /quiz [POST]
Traceback (most recent call last):
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 1511, in wsgi_app       
    response = self.full_dispatch_request()
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "c:\Users\GOLD COMPUTERS\Desktop\Project\afrilang\app.py", line 39, in quiz
    return render_template("quiz.html", question=question, english=english, message=message)
                                                 ^^^^^^^^
UnboundLocalError: cannot access local variable 'question' where it is not associated with a value
127.0.0.1 - - [08/Mar/2026 11:47:12] "POST /quiz HTTP/1.1" 500 -
PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> & "C:\Program Files\Python313\python.exe" "c:/Users/GOLD COMPUTERS/Desktop/Project/afrilang/app.py"
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.95:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Mar/2026 11:48:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:48:42] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:48:47] "POST /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:48:50] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:48:55] "POST /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:48:56] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:01] "POST /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:07] "POST /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:09] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:14] "POST /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:16] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:54] "GET /quiz HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 11:49:59] "POST /quiz HTTP/1.1" 200 -
PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> pip install gTTS
Defaulting to user installation because normal site-packages is not writeable
Collecting gTTS
  Downloading gTTS-2.5.4-py3-none-any.whl.metadata (4.1 kB)
Collecting requests<3,>=2.27 (from gTTS)
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting click<8.2,>=7.1 (from gTTS)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Requirement already satisfied: colorama in C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages (from click<8.2,>=7.1->gTTS) (0.4.6)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->gTTS)
  Downloading charset_normalizer-3.4.5-cp313-cp313-win_amd64.whl.metadata (39 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.27->gTTS)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.27->gTTS)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests<3,>=2.27->gTTS)
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Downloading gTTS-2.5.4-py3-none-any.whl (29 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.5-cp313-cp313-win_amd64.whl (142 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Installing collected packages: urllib3, idna, click, charset_normalizer, certifi, requests, gTTS
  Attempting uninstall: click
    Found existing installation: click 8.3.1
    Uninstalling click-8.3.1:
      Successfully uninstalled click-8.3.1
   ━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━ 3/7 [charset_normalizer]  WARNING: The script normalizer.exe is installed in 'C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.        
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━ 6/7 [gTTS]  WARNING: The script gtts-cli.exe is installed in 'C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.        
Successfully installed certifi-2026.2.25 charset_normalizer-3.4.5 click-8.1.8 gTTS-2.5.4 idna-3.11 requests-2.32.5 urllib3-2.6.3
PS C:\Users\GOLD COMPUTERS\Desktop\Project\afrilang> & "C:\Program Files\Python313\python.exe" "c:/Users/GOLD COMPUTERS/Desktop/Project/afrilang/app.py"
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.95:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Mar/2026 12:00:18] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Mar/2026 12:00:26] "POST /translate HTTP/1.1" 200 -
[2026-03-08 12:00:26,090] ERROR in app: Exception on /pronounce/Agoo [GET]
Traceback (most recent call last):
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 1511, in wsgi_app       
    response = self.full_dispatch_request()
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "c:\Users\GOLD COMPUTERS\Desktop\Project\afrilang\app.py", line 17, in pronounce
    tts = gTTS(text=word, lang="tw")
  File "C:\Users\GOLD COMPUTERS\AppData\Roaming\Python\Python313\site-packages\gtts\tts.py", line 150, in __init__
    raise ValueError("Language not supported: %s" % lang)
ValueError: Language not supported: tw
127.0.0.1 - - [08/Mar/2026 12:00:26] "GET /pronounce/Agoo HTTP/1.1" 500 -
